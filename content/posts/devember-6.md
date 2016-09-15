Title: Devember Day 6 - Input Playback
Date: 2015-12-08
Authors: Tim Liou

Today's code is on
[this tag](https://github.com/wheatdog/wastale/tree/devember_6). The complete
code can be found in [here](https://github.com/wheatdog/wastale).

I think it is about time to implement "Input Playback" feature. For now, the
maximum minutes of input I can record is about one hour, which I think is fine
now.

I figure out the stuck problem. If you are interested, you can check out
[this commit](https://github.com/wheatdog/wastale/commit/f3411f9170ce00ec7d8393b53594d0f10dedc4d1).

There is another problem I think is about floating point precision.

When one player is on the other player and the player beneath press the up botton
and release it, it will sunk into the ground.

![](http://i.imgur.com/VHhvWA2.gif)

I sort of know there is something wrong in `ClipDimToValide`, especially the
value of `Theta`, but I am not sure how I want to handle it. Maybe I should
watch Week 16 of Handmade Hero, or I could leave it until I wrote the engine
version of collision detection. Let me think about it...
