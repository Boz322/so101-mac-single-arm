"""
Teach-and-replay for a single SO-101 follower arm (no leader arm needed).

How it works:
  record  turns torque OFF so you can move the arm by hand. Each time you press
          Enter, the current pose of all six joints is saved as a waypoint.
  play    turns torque ON and glides through the saved waypoints in order,
          interpolating between them so the motion is smooth.

Moves are saved as JSON files in moves/ next to this script.

Usage:
    python scripts/teach.py record <name>           record a move
    python scripts/teach.py play   <name> [loops]   play it once, or N times
    python scripts/teach.py chain  <name> <name>... play several moves back to back
    python scripts/teach.py list                    list saved moves

Speed (play / chain only):
    --speed 2      twice as fast      --speed 0.5   half speed
    Around 3 to 4 is the practical limit with the default settings.

Examples:
    python scripts/teach.py record pickup
    python scripts/teach.py play pickup 3
    python scripts/teach.py play pickup --speed 2.5
    python scripts/teach.py chain home pickup wave home --speed 2
"""

import argparse
import json
import time
from pathlib import Path

from so101_common import add_robot_args, connect, format_pose, read_pose, set_torque

MOVES_DIR = Path(__file__).resolve().parent / "moves"

# Motion tuning. Time per segment at speed 1.0 = BASE_STEPS * STEP_DELAY = 1.2 s
BASE_STEPS = 60  # how many small steps between two waypoints
STEP_DELAY = 0.02  # seconds between steps
PAUSE = 0.4  # seconds to rest at each waypoint
MIN_STEPS = 8  # never fewer steps than this, or motion gets jerky


def path_for(name: str) -> Path:
    return MOVES_DIR / f"{name}.json"


def glide(robot, start, target, speed):
    """Linear interpolation from `start` to `target`.

    Faster speed means fewer steps at the same delay. The servo's own controller
    smooths each small step, so we don't need to feed it very fine increments.
    """
    steps = max(MIN_STEPS, int(BASE_STEPS / speed))
    action = dict(start)
    for i in range(1, steps + 1):
        ratio = i / steps
        for key in target:
            action[key] = start[key] + (target[key] - start[key]) * ratio
        robot.send_action(dict(action))
        time.sleep(STEP_DELAY)
    return dict(target)


def cmd_list():
    MOVES_DIR.mkdir(exist_ok=True)
    files = sorted(MOVES_DIR.glob("*.json"))
    if not files:
        print("No moves yet. Try: python scripts/teach.py record <name>")
        return
    print("Saved moves:\n")
    for f in files:
        n = len(json.loads(f.read_text()))
        print(f"  {f.stem:20s} {n} waypoints")


def cmd_record(name, port, robot_id):
    MOVES_DIR.mkdir(exist_ok=True)
    target = path_for(name)
    if target.exists():
        old = len(json.loads(target.read_text()))
        ans = input(f'Move "{name}" exists ({old} waypoints). Overwrite? (y/N): ').strip().lower()
        if ans != "y":
            print("Cancelled")
            return

    robot = connect(port, robot_id)
    print("Connected\n")
    print("Hold the arm: with torque off it may sag under its own weight.")
    if set_torque(robot, False):
        print("Torque OFF, you can move the arm by hand.\n")
    else:
        print("Torque could not be turned off; the arm may be stiff.\n")

    points = []
    print(f'Recording "{name}". Pose the arm, press Enter to save a waypoint, type q + Enter to finish.\n')
    try:
        while True:
            cmd = input(f"[{len(points)} waypoints] Enter = save / q = finish: ").strip().lower()
            if cmd == "q":
                break
            pose = read_pose(robot)
            points.append(pose)
            print("   ", format_pose(pose), "\n")
    except KeyboardInterrupt:
        print("\nInterrupted")

    if points:
        target.write_text(json.dumps(points, indent=2))
        print(f'\nSaved "{name}" with {len(points)} waypoints -> {target}')
    else:
        print("\nNothing recorded, nothing saved")

    robot.disconnect()
    print("Disconnected")


def cmd_play(names, loops, speed, port, robot_id):
    seqs = []
    for name in names:
        p = path_for(name)
        if not p.exists():
            print(f'Move "{name}" not found. Run: python scripts/teach.py list')
            return
        seqs.append((name, json.loads(p.read_text())))

    total = sum(len(s) for _, s in seqs)
    print(f"Playing {len(seqs)} move(s), {total} waypoints, speed x{speed}\n")

    robot = connect(port, robot_id)
    print("Connected")
    set_torque(robot, True)
    current = read_pose(robot)

    print("\nThe arm will first travel to the first waypoint. Keep clear.")
    input("Press Enter to start ...")

    try:
        for loop in range(loops):
            if loops > 1:
                print(f"\n--- loop {loop + 1} / {loops} ---")
            for name, points in seqs:
                for i, target in enumerate(points, 1):
                    print(f"  {name} -> waypoint {i}")
                    current = glide(robot, current, target, speed)
                    time.sleep(PAUSE / speed)
        print("\nDone")
    except KeyboardInterrupt:
        print("\nInterrupted")
    finally:
        robot.disconnect()
        print("Disconnected")


def main():
    # Shared options live on every subcommand, so they go after it:
    #   python scripts/teach.py play wave --speed 2 --port /dev/tty.usbmodemXXXX
    common = argparse.ArgumentParser(add_help=False)
    add_robot_args(common)
    common.add_argument("--speed", type=float, default=1.0, help="playback speed multiplier (default 1.0)")

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="mode", required=True)

    p_rec = sub.add_parser("record", parents=[common], help="record a move")
    p_rec.add_argument("name")

    p_play = sub.add_parser("play", parents=[common], help="play a move")
    p_play.add_argument("name")
    p_play.add_argument("loops", nargs="?", type=int, default=1)

    p_chain = sub.add_parser("chain", parents=[common], help="play several moves back to back")
    p_chain.add_argument("names", nargs="+")

    sub.add_parser("list", help="list saved moves")

    args = parser.parse_args()

    if args.mode == "list":
        cmd_list()
        return
    if args.speed <= 0:
        parser.error("--speed must be positive")
    if args.mode == "record":
        cmd_record(args.name, args.port, args.robot_id)
    elif args.mode == "play":
        cmd_play([args.name], args.loops, args.speed, args.port, args.robot_id)
    elif args.mode == "chain":
        cmd_play(args.names, 1, args.speed, args.port, args.robot_id)


if __name__ == "__main__":
    main()
