# 5. Assembly

```
1 Parts → 2 Print → 3 Install → 4 Motor IDs → [5 Assemble] → 6 Calibrate → 7 First motion → 8 Teach
                                               ^ you are here
```

I won't duplicate the official assembly photos. Follow these, in this order of usefulness:

1. **[Official SO-101 guide, assembly section](https://huggingface.co/docs/lerobot/so101)**: photos and a short video for every joint, with the screw type for each step.
2. **[Hugging Face assembly video](https://www.youtube.com/watch?v=70GuJf2jbYk)**: about 20 minutes. Watch it once all the way through without touching anything, then follow along.
3. A slower beginner series if the official video moves too fast: [motor IDs](https://www.youtube.com/watch?v=A4AjOv9Kqos), [assembly](https://www.youtube.com/watch?v=FfNdKNZSm48).

<!-- Add your own assembly photos to media/ and reference them here -->

## What I wish I'd known

**Check the screw size at every step.** The guide uses mostly M2x6 and M3x6. They look similar. M3 in an M2 hole cracks the plastic; M2 in an M3 hole holds nothing.

**Use the right screwdriver.** PH0 and PH1. A larger bit strips the tiny servo horn screws.

**Watch out for SO-100 videos.** Many videos online are for the older SO-100. Its assembly is different (it requires removing servo gears, and the cable routing changed). Make sure the title says **101**.

**Servo position matters.** Each servo goes in a specific joint. If you labeled them in the last step, this is easy. If a joint later moves when you command a different one, two servos are swapped.

**Don't overtighten.** If a joint grinds or clicks when it moves, a screw is often pressing too hard on a moving part.

**Clamp it down** before you power it. The arm is top-heavy when extended.

Next: [6. Calibration](06-calibration.md)
