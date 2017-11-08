<!-- .slide: data-background="resources/textures/background-radial.jpeg" -->

<div class="captioned-image-row">
  <div>
    <img class="plain" data-src="resources/textures/arShadows-circ.png">
    <i>Tech:<br> WebAR</i>
  </div>
</div>
------
<!-- .slide: data-background="resources/textures/khronos-pic.jpg" -->
<blockquote style="background: rgba(32, 32, 32, 0.5);">

<h1>  WebAR Doesn't exist yet</h1>
But how close are we?
</blockquote>

------
<!-- .slide: data-background-video="resources/videos/shadow-movie4-720p.mov" -->

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<blockquote style="background: rgba(32, 32, 32, 0.5);">
    Mixing media with a <br>
    person's perception of the world<br>
    <span class="green">_registered in 3D_</span>
    <span class="green">, _in real-time_</span>
</blockquote>

------

<!-- .slide: data-background="resources/textures/background-radial.jpeg" -->

<div class="image-row">
  <div><img class="plain" data-src="resources/textures/ardisplay-hololens-circ.png"></div>
  <div><img class="plain" data-src="resources/textures/ardisplay-daqri-circ.png"></div>
  <div><img class="plain" data-src="resources/textures/ardisplay-odg-circ.png"></div>
  <div><img class="plain" data-src="resources/textures/ardisplay-meta-circ.png"></div>
</div>
<div class="image-row">
  <div><img class="plain" data-src="resources/textures/ardisplay-vuzix-circ.png"></div>
  <div><img class="plain" data-src="resources/textures/lenovo-phab2-lowes-circ.png"></div>
  <div><img class="plain" data-src="resources/textures/iphone7plus-circ.png"></div>
  <div><img class="plain" data-src="resources/textures/ardisplay-magicleap-circ.png"></div>

<!-- NOTES -->

------

<!-- .slide: data-background-video="resources/videos/ARhrrrr-short.mov" -->

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<blockquote style="background: rgba(32, 32, 32, 0.5);">
<h1>The Challenge of AR</h1>
<p>Must display in <span class="green">real time</span> (akin to VR)</p>
<p>Can only  <span class="green">display</span> based on what we <br>
already <span class="green">know</span> or can <span class="green">sense</span> 
about the world <br><span class="green"> relative to </SPAN> the display</p>
</blockquote>

------

<!-- .slide: data-background-video="resources/videos/arjs-hole.mp4" -->

<h2>Simple AR Has Been Possible for A While</h2>
<p>WebRTC <span class="green">getUserMedia</span> + JS tracking</p><br>
<br>
<br><br>
<br>

<br>
<br>
<br>
<br>
<br>
<br>
<small><a href="https://github.com/jeromeetienne/AR.js">https://github.com/jeromeetienne/AR.js</a><br>
<a href="https://twitter.com/jerome_etienne/status/836754117964017664">https://twitter.com/jerome_etienne/status/836754117964017664</a></small>

------

<!-- .slide: data-background="resources/textures/levelhead.png" -->

<br>
<br>
<br>
<br>
<br>
<h1>In the Long Run, This Simple Approach Will Not Be Enough</h1>
<blockquote style="background: rgba(32, 32, 32, 0.5);">
    <span><h3>Very Little World Knowledge,<br>
    Tightly Coupled to Specific Technology,<br>
    Doesn't Leverage Platform Capabilties</h3></span>
</blockquote>

<br>
<p><small>Julian Oliver "Levelhead" 2008</small></p>

    
------

<!-- .slide: data-background-video="resources/videos/tango-cat-trim.m4v" data-transition="slide-in none-out" -->

<h2>Platform-Specific Sensing is Diverse</h2>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<blockquote style="background: rgba(32, 32, 32, 0.5);">
    <span>SLAM capabilities in Google Tango, Microsoft Hololens, Facebook Camera, Wikitude, Kudan, etc.
    </span>
</blockquote>

------

<!-- .slide: data-background-video="resources/videos/ARKit BB-8 Test.mp4" data-transition="none-in slide-out" -->

<h2>Platform-Specific Sensing is Diverse</h2>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<blockquote style="background: rgba(32, 32, 32, 0.5);">
    <span>Visual-Intertial Odometry plus plane detection<br> (ARKit, ARCore) <br> <small>https://www.youtube.com/watch?v=Rq2NChZ3c4E</small>
    </span>
</blockquote>

------

<!-- .slide: data-background-video="resources/videos/hololens-trim-noaudio.mp4" -->

<h2>Display Tech Also Diverse: See-through vs Video-Mixed vs ...</h2>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

------

<!-- .slide: data-background="resources/textures/background-radial.jpeg" -->

<div style="background: rgba(32, 32, 32, 0.5);">
## Mimic / Extend WebVR? 
</div>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<!-- .slide: data-background="resources/textures/sketch-webvr-arch-orig.png" -->

------

<!-- .slide: data-background="resources/textures/background-radial.jpeg" -->

## Problem: 
### AR is more than "VR + video + spatial tracking"
_and more importantly_
### MR >= AR + VR

------

<!-- .slide: data-background="resources/textures/home-HoloLens-crop.jpg" -->

<div style="background: rgba(32, 32, 32, 0.5);">

<h1>Decouple Apps from "Reality"</h1>

<p>A "webby" approach to MR must</p>

<ul>
<li> Support platform independent AR/VR web apps</li>
<li> Leverage platform capabilities efficiently</li>
<li> Enable user privacy</li>
</ul>

<p>http://blairmacintyre.me/2017/05/20/its-not-webar-yet/</p>
<p>(Gheric Speiginer's PhD work on argon.js and Argon4)</p>

</div>
