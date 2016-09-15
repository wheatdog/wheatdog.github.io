Title: Devember Day 3 - Basic MultiPlayer Movement
Date: 2015-12-03
Authors: Tim Liou

Today's code is on
[this tag](https://github.com/wheatdog/wastale/tree/devember_3). The complete
code can be found in [here](https://github.com/wheatdog/wastale).

First, Let's draw some rectangle on the screen. You can check out `DrawRect`
function. Be careful that the coordinates of angles in the rectangle might sit
outside of the screen. This might cause to memory access violation.

![](http://i.imgur.com/Q2K2vRs.gif?1)

Then, it is about physic of motion.
![v = v_0 + at](https://latex.codecogs.com/gif.latex?v&space;=&space;v_0&space;&plus;&space;at)
![x = x_0 + v_0t + \frac{1}{2}at](https://latex.codecogs.com/gif.latex?x&space;=&space;x_0&space;&plus;&space;v_0t&space;&plus;&space;0.5at)
Also, change the unit from pixel to meter. You can feel that motion is much better.

![](http://i.imgur.com/mOQgHIO.gif)

Each entry of `player_info` struct array store the information of each player.
Now, we have multiplayer.

![](http://i.imgur.com/m7jKV9f.gif)


See you tomorrow!
