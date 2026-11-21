# 1. Parts and tools

```
[1 Parts] → 2 Print → 3 Install → 4 Motor IDs → 5 Assemble → 6 Calibrate → 7 First motion → 8 Teach
 ^ you are here
```

## What you are buying

An SO-101 arm is three kinds of things:

- **Six servos.** Each joint is one Feetech STS3215 servo: a small motor, a gearbox, a position sensor and a controller in one black box. They are chained together on one cable (a "bus") and each one answers to its own ID number.
- **A driver board.** Your Mac speaks USB; the servos speak a serial protocol. The Waveshare board sits in between and translates. It also distributes power from the power supply to the servos.
- **The frame.** Printed plastic parts. You print these yourself (next chapter).

## Option A: a US kit (what I did)

Fun fact: nearly all of these parts are made in China anyway. If you're patient, ordering straight from overseas🚢 (Option B below) is noticeably cheaper, about $50 less. But someone on Amazon has already bundled every part into one kit in the US. I didn't want to wait for a slow boat, so I paid the convenience tax and bought the kit.🥲

| Item | Price (Oct 2026) | Link |
|---|---|---|
| ForgeMotion Labs SO-101 **Follower** Arm Electronics Kit: 6x STS3215 12 V servos, 12 V power supply, Waveshare driver board, cables, servo horns and screws | $154.99 | [Amazon](https://www.amazon.com/dp/B0GH35175P) · [ForgeMotion](https://forgemotionlabs.com/products/so-101-follower-arm-electronics) |
| Desk clamps, 2-pack | ~$5 | [Amazon](https://www.amazon.com/dp/B092L925J4) |
| Precision screwdriver set (you need **PH0 and PH1**) | ~$6 | [Amazon](https://www.amazon.com/dp/B0DB227RTH) |
| PLA+ (or Bambu PLA Tough) filament, 1 roll | ~$20 | any |
| USB-C cable | | a phone charging cable works |

Notes:

- The kit uses **12 V** servos (part number C018, 30 kg·cm). The official BOM lists 7.4 V servos (C001, 16.5 kg·cm). Both are the **same 1/345 gear ratio**, so they fit the same frame. The 12 V version just has more torque and needs the 12 V supply that comes with the kit.
- Ship dates on kits move around. Mine took about ten days.
- The kit has no clamps. The arm must be clamped to a table edge, or it tips over the first time it reaches out.

## Option B: source parts yourself

The official BOM in the [SO-ARM100 README](https://github.com/TheRobotStudio/SO-ARM100) lists every part with links for the US, EU, China and Japan. It's cheaper (about $122 for one follower in the US) but the servos usually ship from overseas.

If you buy servos separately, **all six follower servos must be 1/345**. The leader arm uses a mix of gear ratios, so don't buy a leader kit by mistake.

## You do not need

- A soldering iron. The SO-101 is solder-free.
- A screw assortment. The servos come with the screws you need.

Next: [2. 3D printing](02-printing.md)
