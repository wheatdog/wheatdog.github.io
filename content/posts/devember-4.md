Title: Devember Day 4 - GJK Collision Detection
Date: 2015-12-04
Authors: Tim Liou

Today's code is on
[this tag](https://github.com/wheatdog/wastale/tree/devember_4). The complete
code can be found in [here](https://github.com/wheatdog/wastale).

Yesterday, I use `player_info` to deal with multiplayer problem. Today, I
spend a while thinking more harder. I realize that it may be a good time to
bring the concept of `entity` into the code.

~~~c
struct entity
{
    b32 Exist;
    entity_type Type;
    v2 ddP;
    v2 dP;
    v2 P;
    v2 WidthHeight;
    b32 Collide;
};
~~~

Following is about collision detection. I use well-known GJK algorithm. You can
learn how it work via [Casey's video](http://mollyrocket.com/849) and
[William Bittle's post](http://www.dyn4j.org/2010/04/gjk-gilbert-johnson-keerthi/).
I might write a separate post to explan GJK in chinese.

Anyway, here is what it looks like.

![](http://i.imgur.com/fJ4s7RO.gif)

Really cool, right?

Tomorrow, I will make entities truly collide with each others. Until then.
