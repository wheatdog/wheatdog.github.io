Title: Devember Day 5 - Collision Movement Search
Date: 2015-12-05
Authors: Tim Liou

Today's code is on
[this tag](https://github.com/wheatdog/wastale/tree/devember_5). The complete
code can be found in [here](https://github.com/wheatdog/wastale).

Yesterday, I implement the GJK algorithm to determine whether two rectangles are
overlapped or not. With this property, we can figure out which entities will
collide in this frame. If they does collide, "Collision Movement Search" will help
us find the right place to put the entity. You can learn a lot from
[Geometric vs. Temporal Movement Search](https://hero.handmadedev.org/videos/game-architecture/day045.html).
In video, Casey mention two method - "Search in P" and "Search in T".

I choose "Search in T" with a bound number of iteration for now.

![](http://i.imgur.com/3TI4A8R.gif)

The way I clip the entity movement contain two steps:

1. Transform fixed rectangle to the Minkowski sum of it and the movable
   rectangle. And then transform the movable rectangle to a point.
2. Find the intersection point of the line segment, whose start point is the
   point we just created and the direction is as same as the motion's, and the
   sides of Minkowski sum rectangle.

There are some TODOs here,

1. Make the collision routine support different shapes. I will not deal with
   this issue until I make the real game engine.
2. Something strange when two movable entity collide. I will take a look tomorrow.

That's it!
