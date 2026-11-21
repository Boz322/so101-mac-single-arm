# 常见问题

我实际遇到过的问题，加上相关的常见情况。

## 安装

**装 miniforge 时报 `wget: command not found`**
macOS 没有 `wget`。用[第 3 章](03-install-mac.md)里的 `curl -L -O ...` 命令。

**`lerobot-find-port: command not found`**（或任何 `lerobot-*` 命令）
conda 环境没激活。运行 `conda activate lerobot`（或者你起的名字），确认命令行开头是 `(lerobot)`。

**`zsh: no matches found: lerobot[core_scripts,feetech]`**
引号漏了。用 `pip install 'lerobot[core_scripts,feetech]'`。

**Python 版本报错**
LeRobot 要 Python 3.12 以上。老教程写的 3.10 已经不行了，用 `python=3.12` 重建环境。

## 端口和舵机

**`lerobot-find-port` 让我拔线，但我什么都没插**
要插着板子运行。`Ctrl + C` 退出，插上电源和 USB 再跑。

**端口列表里全是蓝牙设备**
Mac 上很正常。不用看列表，让它通过拔线对比找出板子。

**舵机没反应 / setup-motors 找不到舵机**
- 电源插到驱动板上了吗？光插 USB 舵机不工作。
- 烧 ID 时总线上是不是只有一个舵机？
- 3-pin 线两头重新插一遍。
- 带跳线帽的 Waveshare 板：两个都在 **B**。

**端口名变了**
换了 USB 口或者集线器，端口名可能会变。重新跑 `lerobot-find-port`，更新 `SO101_PORT`。

## Python

**`TypeError: SOFollowerConfig.__init__() got an unexpected keyword argument 'id'`**
用 `SO101FollowerConfig`，别用 `SOFollowerConfig`，基类没有 `id`。见[第 7 章](07-first-motion.md)。

**老教程里写的是 `lerobot.robots.so101_follower`**
LeRobot 已经把 SO-100 和 SO-101 合并成了 `lerobot.robots.so_follower`。LeRobot 更新很快，示例和你的版本对不上时，直接问 Python 当前有什么：

```bash
python -c "import lerobot.robots.so_follower as m; print(dir(m))"
```

**找不到标定 / 连接后动作很怪**
脚本用的 `--id` 必须和标定时的一样。看一下 `~/.cache/huggingface/lerobot/calibration/robots/so_follower/` 里的文件名。

## 遥操作

**`lerobot-teleoperate` 用 `--teleop.type=keyboard` 控制不了机械臂**
键盘遥操作不是用来逐个关节控制机械臂的。SO-101 的遥操作默认要 leader 臂（`--teleop.type=so101_leader`）。只有一条臂的话，用这个仓库里的脚本。

## 运动

**`teach.py record` 时扭矩关不掉**
脚本会打印提示。确认没有别的脚本或者忘关的终端占着这个端口，然后重试。

**高速回放时一顿一顿的**
`--speed` 会减少插值步数。把速度调低，或者把 `teach.py` 里的 `BASE_STEPS` 调大。

**一拔电臂就砸下来**
先摆到低位再拔电源。见[第 8 章](08-teach-and-replay.md)的安全关机部分。
