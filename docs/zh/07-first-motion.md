# 7. 第一次动起来、关节测试

```
1 备料 → 2 打印 → 3 装软件 → 4 烧 ID → 5 组装 → 6 标定 → [7 动起来] → 8 示教
                                                          ^ 你在这里
```

## 官方是怎么控制机械臂的？

单臂的话，官方没有给方法。官方设定的流程是 `lerobot-teleoperate` 配合 **leader 臂**：你用手掰那条小的 leader，它把自己的关节角度报给电脑，follower 跟着做一样的动作。`lerobot-teleoperate` 虽然有键盘选项，但那是给轮式底盘之类的机器人准备的，不是用来逐个关节控制机械臂的。

只有 follower 的时候，最直接的办法是用 Python 跟机械臂对话。遥操作和训练出来的模型，底层调用的也是同一套接口：

```python
from lerobot.robots.so_follower import SO101Follower, SO101FollowerConfig

robot = SO101Follower(SO101FollowerConfig(port="/dev/tty.usbmodem...", id="my_follower"))
robot.connect()
pose = robot.get_observation()      # {"shoulder_pan.pos": 3.2, ..., "gripper.pos": 41.0}
robot.send_action(pose)             # 发送目标位置（单位是度，夹爪是 0-100）
robot.disconnect()
```

> **我踩过的坑：** `lerobot.robots.so_follower` 里还有一个 `SOFollowerConfig`。它是基类，**没有 `id` 参数**，写 `SOFollowerConfig(port=..., id=...)` 会报 `unexpected keyword argument 'id'`。要用 `SO101FollowerConfig`。`id` 是 LeRobot 用来找标定文件的。

## 让底座转一下

```bash
cd ~/so101-mac-single-arm
python scripts/first_move.py
```

（前提是你 export 了 `SO101_PORT` 和 `SO101_ID`，否则加上 `--port ... --id ...`。）

底座往一边转 15 度、往另一边转 15 度、再回原位。转了就说明整条链路通了：Python → USB → 驱动板 → 总线 → 舵机 → 机械运动。

**为什么脚本要分小步走：** 如果一条指令直接发最终角度，舵机会全速冲过去。脚本把运动切成 50 小步，每步间隔 20 毫秒，动作就是平滑滑过去的。这个思路叫插值，也是下一章示教工具的核心。

## 六个关节都测一遍

```bash
python scripts/test_all_joints.py
```

每个关节来回转 ±10 度（夹爪 ±5），每个之前会暂停。测的时候注意：

- **方向。** 记下每个关节往 `+` 是转向哪边，后面会用到。
- **异响。** 咯吱声或顿挫感，一般是螺丝太紧或者支撑没清干净。
- **静止时抖动。** 轻微的没关系。
- **肩膀手感不一样。** `shoulder_lift` 扛着整条臂的重量，往下走可能稍微多坠一点，往上走更费力。这是重力，不是故障。

下一步：[8. 示教回放](08-teach-and-replay.md)
