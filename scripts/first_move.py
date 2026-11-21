"""
First motion test: rotate the base (shoulder_pan) 15 degrees left, 15 right, then back.

If this works, the whole chain is alive:
your Python -> USB -> driver board -> serial bus -> servo -> movement.

Usage:
    python scripts/first_move.py --port /dev/tty.usbmodemXXXX --id my_follower
"""

import argparse
import time

from so101_common import add_robot_args, connect, read_pose

JOINT = "shoulder_pan.pos"
AMPLITUDE = 15  # degrees


def glide(robot, action, joint, target, steps=50, dt=0.02):
    """Move one joint to `target` in small steps so the motion is smooth."""
    start = action[joint]
    for i in range(1, steps + 1):
        action[joint] = start + (target - start) * i / steps
        robot.send_action(dict(action))
        time.sleep(dt)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_robot_args(parser)
    args = parser.parse_args()

    robot = connect(args.port, args.robot_id)
    print("Connected\n")

    action = read_pose(robot)
    print("Current pose:")
    for k, v in action.items():
        print(f"  {k:22s} {v:8.2f}")

    home = action[JOINT]
    input(f"\nPress Enter to move {JOINT} by +/-{AMPLITUDE} degrees (keep hands clear) ...")

    try:
        glide(robot, action, JOINT, home + AMPLITUDE)
        time.sleep(0.5)
        glide(robot, action, JOINT, home - AMPLITUDE)
        time.sleep(0.5)
        glide(robot, action, JOINT, home)
        print("Done")
    except KeyboardInterrupt:
        print("\nInterrupted")
    finally:
        robot.disconnect()
        print("Disconnected")


if __name__ == "__main__":
    main()
