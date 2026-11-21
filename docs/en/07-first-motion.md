# 7. First motion and joint test

```
1 Parts → 2 Print → 3 Install → 4 Motor IDs → 5 Assemble → 6 Calibrate → [7 First motion] → 8 Teach
                                                                          ^ you are here
```

## How does the official guide move the arm?

It doesn't, not with one arm. The intended workflow is `lerobot-teleoperate` with a **leader arm**: you move the small leader by hand, it reports its joint angles, and the follower copies them. `lerobot-teleoperate` has a keyboard option, but that's meant for other robots such as wheeled bases, not for driving an arm joint by joint.

With only a follower, the simplest path is to talk to the arm directly from Python. That's the same interface teleoperation and trained policies use underneath:

```python
from lerobot.robots.so_follower import SO101Follower, SO101FollowerConfig

robot = SO101Follower(SO101FollowerConfig(port="/dev/tty.usbmodem...", id="my_follower"))
robot.connect()
pose = robot.get_observation()      # {"shoulder_pan.pos": 3.2, ..., "gripper.pos": 41.0}
robot.send_action(pose)             # send target positions (degrees; gripper 0-100)
robot.disconnect()
```

> **Gotcha I hit:** `lerobot.robots.so_follower` also exports `SOFollowerConfig`. That's the base class and has **no `id` field**, so `SOFollowerConfig(port=..., id=...)` fails with `unexpected keyword argument 'id'`. Use `SO101FollowerConfig`. The `id` is how LeRobot finds your calibration file.

## Make the base move

```bash
cd ~/so101-mac-single-arm
python scripts/first_move.py
```

(Assuming you exported `SO101_PORT` and `SO101_ID`. Otherwise add `--port ... --id ...`.)

The base turns 15° one way, 15° the other, and returns. If it does, the whole chain works: Python → USB → driver board → bus → servo → motion.

**Why the script moves in small steps:** if you send the final angle in one command, the servo jumps there at full speed. The script cuts the motion into 50 tiny steps 20 ms apart, so it glides. This idea (interpolation) is the core of the teach tool in the next chapter.

## Test every joint

```bash
python scripts/test_all_joints.py
```

Each joint moves ±10° (gripper ±5), with a pause before each one. Watch for:

- **Direction.** Note which way `+` goes for each joint.
- **Noise.** Clicking or grinding usually means a tight screw or leftover support material.
- **Jitter at rest.** A little is fine.
- **The shoulder feels different.** `shoulder_lift` carries the whole arm, so it may sag slightly going down and work harder going up. That's gravity, not a fault.

Next: [8. Teach and replay](08-teach-and-replay.md)
