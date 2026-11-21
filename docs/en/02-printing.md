# 2. 3D printing on a Bambu Lab P1S

```
1 Parts → [2 Print] → 3 Install → 4 Motor IDs → 5 Assemble → 6 Calibrate → 7 First motion → 8 Teach
           ^ you are here
```

You can start this while the electronics are still shipping.

## Where the settings live

Layer height and infill are not set on the printer or in the Bambu Handy phone app. The phone app only prints models that someone already sliced. You need **Bambu Studio** on your Mac:

1. New project, printer P1S, filament PLA (or PLA+).
2. Drag in the STL.
3. Set the parameters below, slice, send to printer.

## Settings I used

| Setting | Value | Where in Bambu Studio |
|---|---|---|
| Nozzle | 0.4 mm (P1S default, no change) | |
| Layer height | 0.2 mm | Quality |
| Sparse infill density | 15% | Strength |
| X-Y hole compensation | 0.05 mm (after the gauge test, see below) | Quality |
| Supports | as set in the STL plate | |
| Material | PLA+ or Bambu PLA Tough | |

## ⭐️⭐️Print the gauges first

The SO-ARM100 repo has calibration gauges in [`STL/Gauges`](https://github.com/TheRobotStudio/SO-ARM100/tree/main/STL/Gauges). Print `Gauge_0` and `Gauge_tight_1` before anything else and test-fit a servo (or the LEGO version of the gauge if your servos haven't arrived).

This tells you whether your printer prints holes a little small or a little big. On my P1S, setting **X-Y hole compensation to 0.05 mm** made the fit right. Your printer may need a different value. Fixing it here is much cheaper than finding out after a full set of parts.

## Which STL

The P1S plate is 256 x 256 mm, so the all-in-one plate files fit. I used [`STL/SO101/Follower/Ender_Follower_SO101.stl`](https://github.com/TheRobotStudio/SO-ARM100/tree/main/STL/SO101/Follower) (sized for a 220 x 220 bed), which has every follower part on one plate with orientation already set.

**Don't rotate the parts.** They are oriented for strength and minimal support.

## After printing

Remove all support material. A small flat screwdriver works best. Leftover support inside a motor pocket is the most common reason a servo won't seat or a joint grinds later.

Next: [3. Install LeRobot on macOS](03-install-mac.md)
