# 在 Mac 上搭建 SO-101 单臂

[English](README.md) | **中文**

这是一份从零开始的 [SO-101](https://github.com/TheRobotStudio/SO-ARM100) 机械臂搭建记录和配套工具，软件用的是 [LeRobot](https://github.com/huggingface/lerobot)。写给用 Apple Silicon Mac、**只做一条 follower 臂、没有 leader 臂**的人。

<!-- 换成你自己的 teach.py 运行 GIF -->
<p align="center"><img src="media/demo.gif" width="480" alt="SO-101 回放示教动作"></p>

## 为什么做这个仓库

官方 SO-101 教程写得不错，但它默认了两件在我这里不成立的事：

- **默认你用 Linux。** Mac 用户只拿到一个端口名的例子。实际上在 Mac 上，`lerobot-find-port` 会把你的蓝牙耳机和机械臂列在一起，系统没有 `wget`，也用不着折腾 `dialout` 用户组。
- **默认你有 leader 臂。** 官方流程走到标定就结束了，下一步直接是双臂遥操作。只有一条 follower 的话，装好了却不知道拿它干什么。

我开始做的时候完全没有电子电路基础（我本科是土木，后来转做机器学习）。这个仓库就是我当时想要的那份教程：每一步先讲在干什么、为什么，再给命令。最后附一个**示教回放工具**，让单臂也能玩起来：用手掰姿势、存下来、按任意速度平滑回放。

## 我的配置

| | |
|---|---|
| 电脑 | MacBook，Apple M3，macOS，conda（miniforge） |
| 打印机 | 拓竹 Bambu Lab P1S，0.4 mm 喷嘴，PLA+ |
| 电子件 | ForgeMotion Labs SO-101 Follower 电子件套装（6 个 **12V** STS3215 舵机、Waveshare 驱动板、12V 电源） |
| 软件 | PyPI 安装的 LeRobot，Python 3.12 |

## 整体流程

```
[1 备料] → [2 打印] → [3 装软件] → [4 烧舵机 ID] → [5 组装] → [6 标定] → [7 第一次动起来] → [8 示教回放]
```

| 步骤 | 文档 | 我花的时间 |
|---|---|---|
| 1 | [零件和工具](docs/zh/01-parts.md) | 等快递约十天 |
| 2 | [用 P1S 打印零件](docs/zh/02-printing.md) | 打印一到两天 |
| 3 | [在 macOS 上装 LeRobot](docs/zh/03-install-mac.md) | 30 分钟 |
| 4 | [找端口、烧录舵机 ID](docs/zh/04-motor-ids.md) | 30 分钟 |
| 5 | [组装](docs/zh/05-assembly.md) | 一个晚上 |
| 6 | [标定](docs/zh/06-calibration.md) | 15 分钟 |
| 7 | [第一次动起来、关节测试](docs/zh/07-first-motion.md) | 15 分钟 |
| 8 | [没有 leader 臂的示教回放](docs/zh/08-teach-and-replay.md) | 想玩多久玩多久 |
| | [常见问题](docs/zh/troubleshooting.md) | |

## 快速开始（机械臂已经装好并标定过）

```bash
git clone https://github.com/Boz322/so101-mac-single-arm.git
cd so101-mac-single-arm
conda activate lerobot

export SO101_PORT=/dev/tty.usbmodemXXXXXXXX   # lerobot-find-port 找到的端口
export SO101_ID=my_follower                   # 标定时用的 id

python scripts/test_all_joints.py
python scripts/teach.py record wave
python scripts/teach.py play wave --speed 2
```

## 脚本

| 脚本 | 作用 |
|---|---|
| [`scripts/first_move.py`](scripts/first_move.py) | 底座左右各转 15 度，检查整条链路通不通 |
| [`scripts/test_all_joints.py`](scripts/test_all_joints.py) | 六个关节逐个小幅度测试，每个之间暂停 |
| [`scripts/teach.py`](scripts/teach.py) | 用手摆姿势录制、回放、串联多套动作、调速 |

所有脚本都接受 `--port` 和 `--id` 参数，也可以从环境变量 `SO101_PORT` / `SO101_ID` 读取。

## 后续计划

这一版只覆盖单条 follower 臂。接下来打算写：

- [ ] leader 臂（7.4V，混合减速比）的搭建和遥操作
- [ ] 腕部和俯视摄像头
- [ ] 在 Apple Silicon（MPS）上录数据集、训练模仿学习策略

## 致谢

- [TheRobotStudio/SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100)：机械臂设计
- [Hugging Face LeRobot](https://github.com/huggingface/lerobot)：软件和[官方 SO-101 教程](https://huggingface.co/docs/lerobot/so101)

这是社区教程，和 Hugging Face、TheRobotStudio 没有官方关系。LeRobot 更新很快，如果这里的命令失效了，请对照官方文档，也欢迎提 issue。

## 许可证

[Apache-2.0](LICENSE)
