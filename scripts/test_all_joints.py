"""
Test all six joints one at a time.

Each joint moves a small amount forward, backward, and back home.
The script pauses before every joint; press Enter to continue, Ctrl+C to stop.

Things to watch while it runs:
  - direction: note which way "+" goes for each joint, you will need it later
  - noise: clicking or grinding usually means a screw is too tight or support
    material was left in a printed part
  - jitter at rest: mild jitter is fine, strong shaking means the PID gains are
    too aggressive for that pose

Usage:
    python scripts/test_all_joints.py --port /dev/tty.usbmodemXXXX --id my_follower
"""

import argparse
import time

from so101_common import add_robot_args, connect, read_pose

# joint key, description, test amplitude (degrees; gripper uses its 0-100 range)
JOINTS = [
    ("shoulder_pan.pos", "base rotation", 10),
    ("shoulder_lift.pos", "shoulder lift", 10),
    ("elbow_flex.pos", "elbow flex", 10),
    ("wrist_flex.pos", "wrist flex", 10),
    ("wrist_roll.pos", "wrist roll", 10),
    ("gripper.pos", "gripper", 5),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_robot_args(parser)
    args = parser.parse_args()

    robot = connect(args.port, args.robot_id)
    print("Connected\n")
    action = read_pose(robot)

    def glide(joint, target, steps=40, dt=0.02):
        start = action[joint]
        for i in range(1, steps + 1):
            action[joint] = start + (target - start) * i / steps
            robot.send_action(dict(action))
            time.sleep(dt)

    try:
        for joint, name, amp in JOINTS:
            if joint not in action:
                print(f"Skipping {name}: {joint} not found")
                continue
            input(f"Press Enter to test [{name}] ({joint}), +/-{amp} ...")
            home = action[joint]
            for label, target in (("+", home + amp), ("-", home - amp), ("home", home)):
                print(f"  {label}")
                glide(joint, target)
                time.sleep(0.3)
            print(f"  {name} OK\n")
        print("All six joints tested")
    except KeyboardInterrupt:
        print("\nInterrupted")
    finally:
        robot.disconnect()
        print("Disconnected")


if __name__ == "__main__":
    main()
