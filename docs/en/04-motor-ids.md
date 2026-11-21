# 4. Find the port and set motor IDs

```
1 Parts → 2 Print → 3 Install → [4 Motor IDs] → 5 Assemble → 6 Calibrate → 7 First motion → 8 Teach
                                 ^ you are here
```

**Do this before assembly.** Once a servo is buried inside the frame, re-wiring it to fix an ID is a pain.

## Why servos need IDs

All six servos share one cable. When your Mac sends "go to 90°", every servo on the bus receives the message. Each message starts with an ID, and only the servo with that ID acts on it.

Every servo leaves the factory with **ID 1**. Plug in six of them and they all answer at once. So you connect them **one at a time** and give each its own ID (1 to 6). The ID is written to the servo's permanent memory (EEPROM), so you only do this once.

## Wiring

Three parts on the driver board matter:

- **USB-C port**: to your Mac
- **DC barrel jack** (round black socket): to the power supply
- **3-pin sockets**: to a servo (either socket works)

```
wall ── 12 V supply ──barrel plug──> board DC jack
Mac  ── USB-C cable ──────────────> board USB-C
                                    board 3-pin ──> one servo
```

**Plug in both power and USB.** USB carries data only. With USB alone the servos won't respond; with power alone your Mac can't see the board. A light on the board means it has power.

If you have a Waveshare board with jumpers, set both to the **B (USB)** channel.

## Find the port

```bash
lerobot-find-port
```

**What it does:** macOS represents every serial device as a file under `/dev/`. The list is long and full of things that aren't your robot: built-in virtual ports, and **Bluetooth devices** (my headphones and speaker showed up). Nothing in the list says "robot arm".

So the tool takes two snapshots. It lists the ports, asks you to unplug the board's USB cable, lists them again, and reports which one disappeared.

Run it **with the board plugged in**, and actually unplug the USB cable when it asks. You'll get something like:

```
/dev/tty.usbmodem5B901506081
```

Write it down. Every hardware command needs it. To save typing later:

```bash
export SO101_PORT=/dev/tty.usbmodem5B901506081
```

**Mac vs Linux:** on Linux the port is `/dev/ttyACM0` and you need `chmod` or the `dialout` group. On macOS you don't need either.

## Set the IDs

```bash
lerobot-setup-motors \
    --robot.type=so101_follower \
    --robot.port=$SO101_PORT
```

The script walks you through the servos one by one. Currently it starts with the gripper (ID 6) and ends with the base, shoulder_pan (ID 1). Follow its prompts rather than any fixed order you read online:

1. Connect **only** the servo it names. Nothing else on the bus.
2. Press Enter. It writes the ID.
3. Disconnect it, connect the next one.

Before each Enter, check that the power plug and 3-pin cable are still seated. Moving servos around easily loosens a plug, and then that servo silently fails.

**Tip from the official guide:** after a servo gets its ID, plug a 3-pin cable into it and set it aside. When you assemble, the cables are already there.

Label each servo with its joint name or ID (masking tape works). Six identical black boxes are easy to mix up.

Next: [5. Assembly](05-assembly.md)
