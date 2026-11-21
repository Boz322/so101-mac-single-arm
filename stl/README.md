# STL files

**English** | [中文](#中文)

These are the 3D models I printed for the follower arm. They are **unmodified copies** from [TheRobotStudio/SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100) (commit `141aea7`, 2026-11-20), which is where the arm design comes from. I put them here so you don't have to dig through their repo to find the right ones.

| File | What it is |
|---|---|
| [`gauges/Gauge_0.STL`](gauges/Gauge_0.STL) | Fit test piece. Print this first. |
| [`gauges/Gauge_tight_1.STL`](gauges/Gauge_tight_1.STL) | A tighter fit test piece. Print it next to the first one. |
| [`Ender_Follower_SO101.stl`](Ender_Follower_SO101.stl) | Every follower part on one plate, already oriented. 220 x 220 mm, so it fits on a P1S. **Don't rotate the parts.** |

How to use them is in [docs/en/02-printing.md](../docs/en/02-printing.md).

The upstream repo has more: plates for other beds (Prusa, Bambu A1 mini), every part as a separate file, and the leader arm. The design gets updated from time to time, so if you are about to print, take a quick look at the [upstream STL folder](https://github.com/TheRobotStudio/SO-ARM100/tree/main/STL) for newer versions.

**License.** These files belong to TheRobotStudio and are released under the Apache License 2.0. Their license text is in [`LICENSE-SO-ARM100`](LICENSE-SO-ARM100). The rest of this repo is my own work, also under Apache-2.0.

---

## 中文

这几个是我给 follower 臂打印用的 3D 模型文件，是从 [TheRobotStudio/SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100) **原样复制**过来的（提交 `141aea7`，2026-11-20）。机械臂的设计出自他们，我放在这里只是让你不用自己去他们仓库里翻。

| 文件 | 是什么 |
|---|---|
| [`gauges/Gauge_0.STL`](gauges/Gauge_0.STL) | 配合度测试件，先打这个 |
| [`gauges/Gauge_tight_1.STL`](gauges/Gauge_tight_1.STL) | 更紧一档的测试件，和上一个一起打 |
| [`Ender_Follower_SO101.stl`](Ender_Follower_SO101.stl) | follower 的所有零件排在一个盘上，方向已经摆好。盘面 220 x 220 mm，P1S 放得下。**不要旋转零件** |

具体怎么用见 [docs/zh/02-printing.md](../docs/zh/02-printing.md)。

官方仓库里还有更多：适配其他打印盘（Prusa、拓竹 A1 mini）的版本、每个零件的单独文件，还有 leader 臂。设计会不定期更新，打印之前可以去[官方 STL 文件夹](https://github.com/TheRobotStudio/SO-ARM100/tree/main/STL)看看有没有新版本。

**许可证。** 这些文件的版权属于 TheRobotStudio，采用 Apache License 2.0，许可证原文在 [`LICENSE-SO-ARM100`](LICENSE-SO-ARM100)。仓库里其余内容是我自己写的，同样是 Apache-2.0。
