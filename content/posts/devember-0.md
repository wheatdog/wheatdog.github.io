Title: Devember Day 1 - Basic Win32 Layer
Date: 2015-12-01
Authors: Tim Liou

Last week, I spent some time reviewing the construction of Win32 prototyping
layer mentioned in Handmade Hero weeks 1 through 5. In those weeks, Casey talk
about some basic stuff that a game need - Graphic, Sound, and Input. If you are
interested in detail, I would recommend you to watch
[Day 1 to 25 of Handmade Hero](https://hero.handmadedev.org/jace/guide/).

Most codes of `win32_wastale.*` are as same as the codes in `win32_handmade.*`.
The most different part is the sound. I will talk about in the rest of the
article. By the way, the source code of wastale is on
[Github](https://github.com/wheatdog/wastale) if you want to take a look.
Today's code is on
[this tag](https://github.com/wheatdog/wastale/tree/devember_1).

# XAudio2

Instead of using DirectSound, I choose XAudio2. There is only one ring buffer in
DirectSound. When we have reached the end of the buffer, we start from the
beginning. However, in XAudio2, we can submit several `XAUDIO2_BUFFER` through
`IXAudio2SourceVoice::SubmitSourceBuffer` method. Basicly, it is like a queue.
Each time we reach the end of a buffer, it will start playing the next buffer.

We can reduce the audio latency by keeping the same number of samples in the
queue. For example, Red line represent the frame boundary. Let's say that we run
in 30 frames per second and have 48000 samples per second. Therefore, there are
1600 samples per frame. Every time we write, we will make sure that the number
of samples in the audio queue are 2400, that is the number of samples in one and
a half frames.
[![](https://farm6.staticflickr.com/5697/23152009310_c431845d73_o.png)](https://flic.kr/p/BgS6Lj)
Brown arrow represent the time that we first write to the sound buffer, and the
brown rounded rectangle near the black line represent the samples we write. Next
time we update samples at the time green arrow point to. To keep the number of
samples in the queue, we will only need to write the number of samples that
green rounded rectangle stand for. If we can update samples in the audio buffer
just in the middle of the frame like arrows in the image above. We can generate
enough samples for next frame and those samples will be played right on the
frame boundary.

Unfortunately, first we cannot guarantee we always update samples at the same
time. Therefore, sound boundary may not line up with the frame boudary, which I
think is fine. Second, `IXAudio2SourceVoice::GetState` cannot return the exactly
samples we just played without using callback. Its granularity is 480 samples in
my machine. That means that we might fill less sample than what we really need
to. The worst case is that we will have the gap of 480 samples.

The easy way to solve this problem is to make the number we want to keep in the
queue larger. Another solution will be using callback which I am really not
familiar with. I think the latency right now is fine for a prototyping
layer. Therefore, I will move on to deal with other problem.

# Tomorrow

I will try to implement "Live Code Editing" feature Casey talked about in
Handmade Hero Week 5 tomorrow. Then, maybe start game engine code exploration
Thursday. Until then!
