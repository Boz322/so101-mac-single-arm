# 6. Calibration

```
1 Parts → 2 Print → 3 Install → 4 Motor IDs → 5 Assemble → [6 Calibrate] → 7 First motion → 8 Teach
                                                            ^ you are here
```

## What calibration solves

Each servo has a position sensor that reads 0 to 4095 over one full turn. But where "0" sits depends on how the servo horn happened to be mounted. Two arms built from the same parts will read different raw numbers in the same pose.

Calibration measures, for each joint:

- where the **middle** of its range is (stored as `homing_offset`)
- how far it can physically travel each way (`range_min`, `range_max`)

After that, LeRobot can report joint positions in degrees that mean the same thing on every SO-101. That's what lets a policy trained on one arm run on another, and it stops software from driving a joint into its hard stop.

## Run it

Power and USB connected, arm clamped.

```bash
lerobot-calibrate \
    --robot.type=so101_follower \
    --robot.port=$SO101_PORT \
    --robot.id=my_follower
```

The script will:

1. Turn torque off so you can move the arm by hand.
2. Ask you to move **every joint to the middle of its range**, then press Enter. Watch the official video in the [SO-101 guide](https://huggingface.co/docs/lerobot/so101) for what "middle" looks like.
3. Ask you to move **each joint through its full range**, slowly, end to end. It records the min and max it sees.

`--robot.id` is a name you choose. **Remember it.** Every script in this repo needs the same id to find your calibration.

## Where it's saved

```
~/.cache/huggingface/lerobot/calibration/robots/so_follower/my_follower.json
```

Mine, as a reference ([examples/calibration_example.json](../../examples/calibration_example.json)):

```json
"shoulder_pan": { "id": 1, "drive_mode": 0, "homing_offset": -2044, "range_min": 811, "range_max": 3273 },
"wrist_roll":   { "id": 5, "drive_mode": 0, "homing_offset": -339,  "range_min": 0,   "range_max": 4095 },
```

How to read it:

- `id`: the servo ID you set in step 4.
- `homing_offset`: shift applied so the middle pose reads as zero.
- `range_min` / `range_max`: raw sensor limits you swept through. Most joints cover roughly 2000 to 2500 of the 4096 counts.
- `wrist_roll` going 0 to 4095 is normal: the wrist can spin a full turn.

**Don't copy someone else's file.** It only works for the arm it was measured on. Re-run calibration if you take a joint apart or re-mount a servo horn.

Next: [7. First motion](07-first-motion.md)
