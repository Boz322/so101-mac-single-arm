# 6. 标定

```
1 备料 → 2 打印 → 3 装软件 → 4 烧 ID → 5 组装 → [6 标定] → 7 动起来 → 8 示教
                                                 ^ 你在这里
```

## 标定在解决什么问题

每个舵机里有一个位置传感器（编码器），转一整圈读数是 0 到 4095。但"0"在哪个位置，取决于装舵机摇臂时恰好对在了哪。同样的零件装出来的两条臂，摆同一个姿势，原始读数也不一样。

标定就是给每个关节测出：

- 活动范围的**中点**在哪（存成 `homing_offset`）
- 两个方向分别能转到多远（`range_min`、`range_max`）

有了这些，LeRobot 报出来的关节角度在每台 SO-101 上含义都一样。这样在一台臂上训练的策略才能在另一台上跑，软件也不会把关节硬怼到物理限位上。

## 开始标定

电源和 USB 都插上，臂夹好。

```bash
lerobot-calibrate \
    --robot.type=so101_follower \
    --robot.port=$SO101_PORT \
    --robot.id=my_follower
```

脚本会：

1. 关掉扭矩，让你能用手掰。
2. 让你把**每个关节都摆到活动范围的中间**，然后按回车。"中间"长什么样，看[官方 SO-101 教程](https://huggingface.co/docs/lerobot/so101)里的视频。
3. 让你把**每个关节都从一头慢慢转到另一头**，它会记下看到的最小值和最大值。

`--robot.id` 是你自己起的名字。**一定要记住**，这个仓库里的每个脚本都要用同一个 id 去找你的标定文件。

## 存在哪

```
~/.cache/huggingface/lerobot/calibration/robots/so_follower/my_follower.json
```

我的标定文件可以参考（[examples/calibration_example.json](../../examples/calibration_example.json)）：

```json
"shoulder_pan": { "id": 1, "drive_mode": 0, "homing_offset": -2044, "range_min": 811, "range_max": 3273 },
"wrist_roll":   { "id": 5, "drive_mode": 0, "homing_offset": -339,  "range_min": 0,   "range_max": 4095 },
```

怎么看：

- `id`：第 4 步烧进去的舵机 ID。
- `homing_offset`：偏移量，让中间姿势读数为零。
- `range_min` / `range_max`：你转动时测到的原始读数上下限。大多数关节覆盖 4096 里的 2000 到 2500 左右。
- `wrist_roll` 是 0 到 4095 很正常，手腕可以转一整圈。

**不要拷贝别人的标定文件。** 它只对测量它的那条臂有效。拆过关节或者重装过舵机摇臂，要重新标定。

下一步：[7. 第一次动起来](07-first-motion.md)
