# 3. Install LeRobot on macOS (Apple Silicon)

```
1 Parts → 2 Print → [3 Install] → 4 Motor IDs → 5 Assemble → 6 Calibrate → 7 First motion → 8 Teach
                     ^ you are here
```

Requirements: an Apple Silicon Mac on macOS 14 or newer (PyTorch's minimum). GPU acceleration (MPS) needs macOS 15+, but you won't need the GPU until training, which this guide doesn't cover yet.

Open Terminal with `Cmd + Space`, type Terminal, Enter.

## Step 1: install conda (miniforge)

**What it does:** conda creates isolated Python environments. LeRobot pulls in PyTorch and dozens of other packages; keeping them in their own environment means they can't break anything else on your Mac.

Check whether you already have it:

```bash
conda --version
```

If you see `command not found`, install miniforge. The official docs use `wget`, which **macOS doesn't ship with**. Use `curl` instead:

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

Accept the license (`yes`), keep the default path, and answer `yes` to initialize. Then **close and reopen Terminal**.

## Step 2: create the environment

LeRobot requires **Python 3.12** or newer. (Older guides say 3.10. They are out of date.)

```bash
conda create -y -n lerobot python=3.12
conda activate lerobot
```

Your prompt should now start with `(lerobot)`. You need `conda activate lerobot` every time you open a new terminal. I named mine `lerobot-arm`; any name works as long as you remember it.

## Step 3: install ffmpeg

**What it does:** ffmpeg compresses and decompresses video. You don't need it to move the arm, but LeRobot stores camera recordings as video when you collect datasets later, and it's easier to install now than to debug later.

```bash
conda install ffmpeg -c conda-forge
```

Answer `y` when asked. If a later step complains about `libsvtav1` or a `torchcodec` mismatch, pin the version: `conda install ffmpeg=7.1.1 -c conda-forge`.

## Step 4: install LeRobot

```bash
pip install 'lerobot[core_scripts,feetech]'
```

**What the brackets mean:** LeRobot's base install is small. Optional features are "extras":

- `core_scripts` gives you the command-line tools: `lerobot-find-port`, `lerobot-setup-motors`, `lerobot-calibrate`, `lerobot-record`, and so on.
- `feetech` is the driver for your Feetech STS3215 servos. Without it, your Mac can't talk to them.

Keep the quotes; zsh would otherwise try to interpret the square brackets. This step downloads PyTorch and takes a while.

## Step 5: verify

```bash
lerobot-find-port
```

The board isn't connected yet, so it will list ports and ask you to unplug something. That's expected. Press `Ctrl + C` to quit. The only bad result is `command not found`, which means the environment isn't active.

## Step 6: get this repo

```bash
cd ~
git clone https://github.com/Boz322/so101-mac-single-arm.git
```

Next: [4. Find the port, set motor IDs](04-motor-ids.md)
