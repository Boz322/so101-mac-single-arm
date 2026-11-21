"""
Shared helpers for the SO-101 single-arm scripts.

Every script needs to know two things about your arm:
  - the serial port of the driver board  (find it with `lerobot-find-port`)
  - the robot id you used when you ran `lerobot-calibrate`

You can pass them on the command line:
    python scripts/first_move.py --port /dev/tty.usbmodemXXXX --id my_follower

or set them once per terminal session:
    export SO101_PORT=/dev/tty.usbmodemXXXX
    export SO101_ID=my_follower
"""

import argparse
import os
import sys

from lerobot.robots.so_follower import SO101Follower, SO101FollowerConfig

JOINT_KEYS = [
    "shoulder_pan.pos",
    "shoulder_lift.pos",
    "elbow_flex.pos",
    "wrist_flex.pos",
    "wrist_roll.pos",
    "gripper.pos",
]


def add_robot_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--port",
        default=os.environ.get("SO101_PORT"),
        help="Serial port of the driver board, e.g. /dev/tty.usbmodem5B901506081 "
        "(default: $SO101_PORT)",
    )
    parser.add_argument(
        "--id",
        dest="robot_id",
        default=os.environ.get("SO101_ID", "my_follower"),
        help="Robot id used during lerobot-calibrate (default: $SO101_ID or my_follower)",
    )


def connect(port: str | None, robot_id: str) -> SO101Follower:
    if not port:
        sys.exit(
            "No port given. Run `lerobot-find-port`, then pass --port /dev/tty.usbmodem... "
            "or `export SO101_PORT=...`."
        )
    # The id is how LeRobot finds your calibration file:
    # ~/.cache/huggingface/lerobot/calibration/robots/so_follower/<id>.json
    # Note: use SO101FollowerConfig, not the base SOFollowerConfig, which has no `id` field.
    robot = SO101Follower(SO101FollowerConfig(port=port, id=robot_id))
    robot.connect()
    return robot


def read_pose(robot: SO101Follower) -> dict[str, float]:
    """Current position of all six joints (degrees; gripper is 0-100)."""
    obs = robot.get_observation()
    return {k: float(v) for k, v in obs.items() if k.endswith(".pos")}


def set_torque(robot: SO101Follower, on: bool) -> bool:
    """Torque on: the motors hold position. Torque off: you can move the arm by hand."""
    try:
        if on:
            robot.bus.enable_torque()
        else:
            robot.bus.disable_torque()
        return True
    except Exception as e:  # noqa: BLE001
        print(f"  (could not switch torque: {e})")
        return False


def format_pose(pose: dict[str, float]) -> str:
    return "  ".join(f"{k.split('.')[0]}={v:.1f}" for k, v in pose.items())
