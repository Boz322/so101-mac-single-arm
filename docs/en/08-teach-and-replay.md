# 8. Teach and replay without a leader arm

```
1 Parts → 2 Print → 3 Install → 4 Motor IDs → 5 Assemble → 6 Calibrate → 7 First motion → [8 Teach]
                                                                                           ^ you are here
```

## The idea

Industrial robots have been programmed this way for decades. Nobody types "elbow 37°". You physically move the robot into the pose you want, save it, move to the next pose, save again. Each saved pose is a **waypoint**. On playback, the controller glides from waypoint to waypoint.

`teach.py` does exactly that for the SO-101.

<!-- media/teach-demo.gif -->

## The key mechanism: torque

When powered, a servo has **torque on**: it holds its position hard and you can't move it by hand. To teach, the script turns torque **off**, so the arm goes limp and you can pose it. For playback it turns torque back **on**.

**When torque goes off, the arm sags under its own weight.** Hold it before you start recording.

## Record a move

```bash
python scripts/teach.py record pickup
```

Pose the arm, press Enter to save a waypoint. Repeat. Type `q` and Enter to finish. A good first move:

1. Start pose, arm folded, gripper open
2. Reach toward the table, gripper still open
3. Close the gripper by hand
4. Lift
5. Rotate to the other side, open the gripper
6. Back to the start pose

The move is saved as `scripts/moves/pickup.json`: a list of waypoints, each holding the six joint positions.

## Play, loop, chain

```bash
python scripts/teach.py list                      # what's saved
python scripts/teach.py play pickup               # once
python scripts/teach.py play pickup 5             # five times
python scripts/teach.py chain home pickup wave home
```

`chain` plays several moves back to back with smooth transitions. Keep a `home` move (arm folded, low) and start and end chains with it.

The arm first travels from wherever it is to the first waypoint, so keep clear when you press Enter.

## Speed

```bash
python scripts/teach.py play pickup --speed 2
```

How speed works: between two waypoints, `glide()` sends `BASE_STEPS` small position updates, `STEP_DELAY` seconds apart:

```
time per segment = BASE_STEPS × STEP_DELAY = 60 × 0.02 s = 1.2 s   (at speed 1)
```

plus `PAUSE` (0.4 s) at each waypoint. `--speed 2` halves the number of steps and the pause.

There are two ways to go faster, with different trade-offs:

- **Fewer steps** (what `--speed` does). The servo's internal controller smooths each step, so this stays fairly smooth until the step count gets low.
- **Shorter delay.** Keeps more steps, but commands can arrive faster than the servo can follow, and the arm lags behind the script.

Finding your limit: start at 2 and go up. Stop when the path turns visibly segmented, or when the terminal says "waypoint 4" while the arm is still heading to waypoint 3. For me, **3 to 4** was the practical ceiling. The STS3215's top speed is a hard limit no matter what you send.

## Tuning constants

At the top of `scripts/teach.py`:

```python
BASE_STEPS = 60    # steps between two waypoints
STEP_DELAY = 0.02  # seconds per step
PAUSE = 0.4        # rest at each waypoint
```

- Motion speed is fine but the pauses feel long: lower `PAUSE` to 0.1 or 0.
- Want silkier motion and don't mind slow: raise `BASE_STEPS` to 100+.

## Shutting down safely

1. Stop any running script (`Ctrl + C`). On disconnect, the script turns torque off.
2. **Move the arm into a low, folded pose by hand.** When power is cut the servos go limp instantly, and a raised arm drops.
3. Unplug the **power supply** first, then USB.

Power first, because USB carries no power: once the supply is out the servos are off, and no half-sent command is left on the bus.

Next time: plug in power and USB, `conda activate lerobot`, and run the scripts. IDs and calibration are stored permanently; you don't redo them.

## Where to go from here

Teach-and-replay is open loop: the arm repeats the same motion whether or not the object is there. Making it react to what it sees needs cameras and a learned policy, which in LeRobot's workflow starts with a leader arm for collecting demonstrations. That's the next chapter of this repo.
