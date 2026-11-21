# 3. 在 macOS（Apple Silicon）上装 LeRobot

```
1 备料 → 2 打印 → [3 装软件] → 4 烧 ID → 5 组装 → 6 标定 → 7 动起来 → 8 示教
                   ^ 你在这里
```

前提：Apple Silicon 的 Mac，macOS 14 或更新（PyTorch 的最低要求）。GPU 加速（MPS）要 macOS 15 以上，不过训练之前用不到 GPU，本教程暂时还不涉及训练。

按 `Command + 空格`，输入 Terminal，回车，打开终端。

## 第 1 步：装 conda（miniforge）

**这一步在干什么：** conda 用来创建互相隔离的 Python 环境。LeRobot 会装 PyTorch 和几十个别的包，把它们关在单独的环境里，就不会把 Mac 上其他东西搞乱。

先看看有没有装过：

```bash
conda --version
```

如果显示 `command not found`，就装 miniforge。官方文档用的是 `wget`，但 **macOS 自带没有 wget**，改用 `curl`：

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

许可协议输 `yes`，安装路径直接回车用默认，最后问要不要初始化也输 `yes`。然后**关掉终端重新打开**。

## 第 2 步：建环境

LeRobot 要求 **Python 3.12** 或更新（有些老教程写 3.10，已经过时了）。

```bash
conda create -y -n lerobot python=3.12
conda activate lerobot
```

命令行开头出现 `(lerobot)` 就对了。以后每次新开终端都要先敲 `conda activate lerobot`。我自己的环境叫 `lerobot-arm`，名字随便起，记住就行。

## 第 3 步：装 ffmpeg

**这一步在干什么：** ffmpeg 负责视频的压缩和解压。控制机械臂本身用不到它，但以后录数据集时，LeRobot 会把摄像头画面压成视频存。现在装好，比以后跑到一半报错再查省事。

```bash
conda install ffmpeg -c conda-forge
```

问 Proceed 时输 `y`。如果后面报 `libsvtav1` 缺失或者和 `torchcodec` 版本不匹配，就固定版本：`conda install ffmpeg=7.1.1 -c conda-forge`。

## 第 4 步：装 LeRobot

```bash
pip install 'lerobot[core_scripts,feetech]'
```

**方括号是什么意思：** LeRobot 本体很轻，其他功能拆成了可选模块（extras），按需加装：

- `core_scripts` 提供命令行工具：`lerobot-find-port`、`lerobot-setup-motors`、`lerobot-calibrate`、`lerobot-record` 等。
- `feetech` 是飞特 STS3215 舵机的驱动。不装的话 Mac 认不出舵机。

引号不能省，不然 zsh 会把方括号当成别的意思。这一步要下载 PyTorch，比较慢。

## 第 5 步：验证

```bash
lerobot-find-port
```

驱动板还没接，所以它会列出端口、让你拔线，这是正常的。按 `Ctrl + C` 退出。唯一不对的结果是 `command not found`，说明环境没激活。

## 第 6 步：下载本仓库

```bash
cd ~
git clone https://github.com/Boz322/so101-mac-single-arm.git
```

下一步：[4. 找端口、烧录舵机 ID](04-motor-ids.md)
