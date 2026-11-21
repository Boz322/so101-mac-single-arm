# Troubleshooting

Problems I actually hit, plus the obvious ones around them.

## Install

**`wget: command not found`** when installing miniforge
macOS doesn't include `wget`. Use the `curl -L -O ...` command in [chapter 3](03-install-mac.md).

**`lerobot-find-port: command not found`** (or any `lerobot-*` command)
The conda environment isn't active. Run `conda activate lerobot` (or whatever you named it). Check that your prompt starts with `(lerobot)`.

**`zsh: no matches found: lerobot[core_scripts,feetech]`**
You dropped the quotes. Use `pip install 'lerobot[core_scripts,feetech]'`.

**Python version errors**
LeRobot needs Python 3.12+. Older guides say 3.10. Recreate the environment with `python=3.12`.

## Port and motors

**`lerobot-find-port` asks me to unplug a cable but nothing is plugged in**
It has to run with the board connected. `Ctrl + C`, plug in power and USB, run it again.

**The port list is full of Bluetooth devices**
Normal on a Mac. Ignore the list and let the unplug-and-compare step find the board.

**Servos don't respond / setup-motors can't find a motor**
- Is the power supply plugged into the board? USB alone doesn't power servos.
- Is exactly one servo connected during ID setup?
- Re-seat the 3-pin cable on both ends.
- Waveshare board with jumpers: both on **B**.

**The port name changed**
It can change if you use a different USB socket or hub. Re-run `lerobot-find-port` and update `SO101_PORT`.

## Python

**`TypeError: SOFollowerConfig.__init__() got an unexpected keyword argument 'id'`**
Use `SO101FollowerConfig`, not `SOFollowerConfig`. The base class has no `id`. See [chapter 7](07-first-motion.md).

**Old tutorials import `lerobot.robots.so101_follower`**
LeRobot merged SO-100 and SO-101 into `lerobot.robots.so_follower`. LeRobot changes fast; when an example doesn't match your version, ask Python what exists:

```bash
python -c "import lerobot.robots.so_follower as m; print(dir(m))"
```

**Calibration not found / arm moves strangely after connecting**
The `--id` you pass must match the id you calibrated with. Check `~/.cache/huggingface/lerobot/calibration/robots/so_follower/`.

## Teleoperation

**`lerobot-teleoperate` with `--teleop.type=keyboard` doesn't drive the arm**
The keyboard teleoperator isn't meant for joint-by-joint control of an arm. Teleoperating an SO-101 expects a leader arm (`--teleop.type=so101_leader`). With one arm, use the scripts in this repo.

## Motion

**Torque won't turn off in `teach.py record`**
The script prints a warning. Make sure nothing else (another script, a terminal you forgot) holds the port, then retry.

**Playback is jerky at high speed**
`--speed` reduces the number of interpolation steps. Lower the speed, or raise `BASE_STEPS` in `teach.py`.

**The arm slams down when I unplug it**
Move it to a low pose first, then unplug power. See the shutdown section in [chapter 8](08-teach-and-replay.md).
