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

## ⭐️⭐️⭐️Print the gauges first

The gauges are in [`stl/gauges`](../../stl/gauges) in this repo (copied from the [SO-ARM100 repo](https://github.com/TheRobotStudio/SO-ARM100/tree/main/STL/Gauges)). Print `Gauge_0` and `Gauge_tight_1` before anything else and test-fit a servo. If your servos haven't arrived yet, the SO-ARM100 repo also has a LEGO version of the gauge.

This tells you whether your printer prints holes a little small or a little big. On my P1S, setting **X-Y hole compensation to 0.05 mm** made the fit right. Your printer may need a different value. Fixing it here is much cheaper than finding out after a full set of parts.

✅ How to tell if the size is right: push the servo in. If it goes in without you having to push really hard, the size is just right. If you have to force it, your holes are too small, then try turn 'X-Y hole compensation' up 0.05 mm.

## Which STL

The P1S plate is 256 x 256 mm, so the all-in-one plate files fit. I used [`stl/Ender_Follower_SO101.stl`](../../stl/Ender_Follower_SO101.stl) (sized for a 220 x 220 bed), which has every follower part on one plate with orientation already set. It's an unmodified copy of the [original file](https://github.com/TheRobotStudio/SO-ARM100/tree/main/STL/SO101/Follower); see [`stl/README.md`](../../stl/README.md) for the source and license.

**Don't rotate the parts.** They are oriented for strength and minimal support.

## After printing

Remove all support material. A small flat screwdriver works best. Leftover support inside a motor pocket is the most common reason a servo won't seat or a joint grinds later.

Next: [3. Install LeRobot on macOS](03-install-mac.md)
