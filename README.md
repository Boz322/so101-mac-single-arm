# SO-101 Single Arm on a Mac

**English** | [中文](README.zh-CN.md)

A from-scratch build log and toolkit for the [SO-101](https://github.com/TheRobotStudio/SO-ARM100) robot arm with [LeRobot](https://github.com/huggingface/lerobot), written for people on an **Apple Silicon Mac** who are building **one follower arm**, without a leader arm. 
This first release covers a single follower arm. A dual-arm version and more of the LeRobot workflow are coming.

<!-- Replace with a GIF of your arm running teach.py -->
<p align="center"><img src="media/demo.gif" width="480" alt="SO-101 replaying a taught move"></p>

## Why I build this repo

The official SO-101 guide is good, but it assumes two things that weren't true for me:

- **Linux.** Mac users get a port-name example and little else. On a Mac, `lerobot-find-port` lists your Bluetooth headphones next to the robot, `wget` doesn't exist, and there is no `dialout` group to worry about.
- **A leader arm.** The official flow ends at calibration and then moves on to teleoperation with a second arm. With only a follower, you finish the build and have nothing to do with it.

I came into this with no electronics background (my background is civil engineering and ML). This repo is the guide I wish I had: every step explains what it does and why, and it ends with a **teach-and-replay tool** that makes a single arm useful. You move the arm by hand, save poses, and play them back as smooth motions at any speed.

## What I built with

| | |
|---|---|
| Computer | MacBook Air(M3), macOS, conda (miniforge) |
| Printer | Bambu Lab P1S, 0.4 mm nozzle, PLA+ |
| Electronics | ForgeMotion Labs SO-101 Follower Electronics Kit (6x STS3215 **12 V**, Waveshare driver board, 12 V PSU) |
| Software | LeRobot from PyPI, Python 3.12 |

## The path

| Step | Guide | Time it took me |
|---|---|---|
| 1 | [Parts and tools](docs/en/01-parts.md) | ~14 days waiting for shipping |
| 2 | [3D printing on a P1S](docs/en/02-printing.md) | 2 days of printing |
| 3 | [Install LeRobot on macOS](docs/en/03-install-mac.md) | 90 min |
| 4 | [Find the port, set motor IDs](docs/en/04-motor-ids.md) | 50 min |
| 5 | [Assembly](docs/en/05-assembly.md) | an evening |
| 6 | [Calibration](docs/en/06-calibration.md) | 40 min |
| 7 | [First motion and joint test](docs/en/07-first-motion.md) | 30 min |
| 8 | [Teach and replay without a leader arm](docs/en/08-teach-and-replay.md) | as long as you like~ |
| | [Troubleshooting](docs/en/troubleshooting.md) | |

## Quick start (arm already built and calibrated)

```bash
git clone https://github.com/Boz322/so101-mac-single-arm.git
cd so101-mac-single-arm
conda activate lerobot

export SO101_PORT=/dev/tty.usbmodemXXXXXXXX   # from lerobot-find-port
export SO101_ID=my_follower                   # the id you calibrated with

python scripts/test_all_joints.py
python scripts/teach.py record wave
python scripts/teach.py play wave --speed 2
```

## Scripts

| Script | What it does |
|---|---|
| [`scripts/first_move.py`](scripts/first_move.py) | Rotates the base ±15°. The "is it alive" test. |
| [`scripts/test_all_joints.py`](scripts/test_all_joints.py) | Moves each joint a little, one at a time, pausing between joints. |
| [`scripts/teach.py`](scripts/teach.py) | Record poses by hand, replay them, chain moves together, adjust speed. |

All scripts take `--port` and `--id`, or read `SO101_PORT` / `SO101_ID` from the environment.

## Roadmap

This first version covers the single follower arm. Planned next chapters:

- [ ] Leader arm build (7.4 V, mixed gear ratios) and teleoperation
- [ ] Wrist and overhead cameras
- [ ] Recording a dataset and training an imitation-learning policy on Apple Silicon (MPS)

## Credits

- [TheRobotStudio/SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100) for the arm design
- [Hugging Face LeRobot](https://github.com/huggingface/lerobot) for the software and the [official SO-101 guide](https://huggingface.co/docs/lerobot/so101)

This is a community guide and is not affiliated with Hugging Face or TheRobotStudio. LeRobot changes quickly; if a command here stops working, check the official docs and open an issue.

## License

[Apache-2.0](LICENSE)
