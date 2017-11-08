
<!-- .slide: data-state="title" data-background="resources/textures/background-radial.jpeg"  -->

<div class="talk-title">
	<h1>Web-based AR/VR for Industrial Systems</h1>
    <p class="talk-info">
		<b><a href="http://blairmacintyre.me">Blair MacIntyre</a></b>
		<br>
		Principal Research Scientist, Mozilla <br>
		Professor, School of Interactive Computing, Georgia Tech<br>
		@blairmacintyre / bmacintyre@mozilla.com<br>
    </p>
</div>

<!-- NOTES -->
------
<!-- .slide: data-background="resources/textures/iss-ar.png" -->
<blockquote style="background: rgba(32, 32, 32, 0.5);">
<h2>Many 2D Systems built with browser-based UIs</h2>
ISS Maintenance using PRIDE w/ Traclabs
</blockquote>
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
    <span><em></em></span>
</blockquote>

------

<!-- .slide: data-background="resources/textures/background-radial.jpeg" -->

# WebVR 1.1 is shipping

An open virtual reality platform with the advantages of **the Web**

<div class="captioned-image-row">
  <div>
    <img class="plain" data-src="media/img/web-is-open.png">
    <i>Open</i>
  </div>
  <div>
    <img class="plain" data-src="media/img/web-is-connected.png">
    <i>Connected</i>
  </div>
  <div>
    <img class="plain" data-src="media/img/web-is-instant.png">
    <i>Instant</i>
  </div>
</div>

------

<!-- .slide: data-background="media/img/aframe.jpg" -->
<div style="background: rgba(32, 32, 32, 0.5);">
    <h2>Frameworks like AFrame Integrate VR with Everything</h1>

  <div class="captioned-image-row">
    <div>
      <img class="plain" data-src="media/img/d3.png">
      <i>d3.js</i>
    </div>
    <div>
      <img class="plain" data-src="media/img/vue.png">
      <i>Vue.js</i>
    </div>
    <div>
      <img class="plain" data-src="media/img/react.png">
      <i>React</i>
    </div>
    <div>
      <img class="plain" data-src="media/img/redux.png">
      <i>Redux</i>
    </div>
    <div>
      <img class="plain" data-src="media/img/jquery.png">
      <i>jQuery</i>
    </div>
    <div>
      <img class="plain" data-src="media/img/angular.png">
      <i>Angular</i>
    </div>
  </div>
</div>

------

<!-- .slide: data-background-video="resources/videos/arjs-hole.mp4" -->

<h2>Simple AR Has Been Possible, but Terrible</h2>
<p>WebRTC <span class="green">getUserMedia</span> + JS tracking</p><br>
<br>
<br><br>
<br>

<br>
<br>
<br>
<br>
<small><a href="https://github.com/jeromeetienne/AR.js">https://github.com/jeromeetienne/AR.js</a><br>
<a href="https://twitter.com/jerome_etienne/status/836754117964017664">https://twitter.com/jerome_etienne/status/836754117964017664</a></small>

------

<!-- .slide: data-background="resources/textures/background-radial.jpeg" -->

<h2>WebXR: Expanding WebVR to Support MR</h2>
<p>Web Platform: WebVR, Browsers (Custom, Servo, FF, ...), WebAssembly</p>
<p>Native AR Platforms: ARKit, ARCore, Vision SDKs, ...</p>
<p>MR Requirements: Augmented and Virtual Realities, Anchors, <br>Geospatial References, Custom Computer Vision.</p>
<br>
<br>
<p>https://github.com/mozilla/webxr-api<br>https://github.com/mozilla/webxr-polyfill <br>(_and more soon_)</p>

------

<!-- .slide: data-state="xrslide vrslide" -->

## This Presentation is Running in our WebXR Viewer</h2>
<p><em>on an iPhone</em></p>
<p>Using webxr.js + reveal.js + three.js</p>

------
<!-- .slide: data-state="xrslide vrslide boombox" style="text-align: left; top: 0px;" -->

<h2>VR</h2>
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
<!-- .slide: data-state="xrslide arslide boombox" style="text-align: left;" -->

<h2>AR</h2>
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
<!-- .slide: data-state="xrslide arslide 3deffects boombox" style="text-align: left;" -->

<h2>Arbitrary 3D Effects (e.g., bloomv + film effect)</h2>
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

<h2>Research: Platforms, Computer Vision, Services</h2>
<p>Web Platform: WebVR, <span class="blue">Browsers (Custom, Servo, FF, ...)</span>, WebAssembly</p>
<p>Native AR Platforms: ARKit, ARCore, Vision SDKs, ...</p>
<p>MR Requirements: Augmented and Virtual Realities, Anchors, <br>Geospatial References, <span class="blue">Custom Computer Vision</span>.</p>
<p><span class="green">Services for Persistence, Search, Social Sharing, Cloud CV/ML,... </span></p>
<br>
<p>https://github.com/mozilla/webxr-api<br>https://github.com/mozilla/webxr-polyfill <br>(_and more soon_)</p>
------

<!-- .slide: data-background="resources/textures/background-radial.jpeg" style="text-align: left;" -->

<h2>Adding AR/VR to Industrial Systems is Possible!</h2>
<p>Contact me: <a href="mailto:bmacintyre@mozilla.com">bmacintyre@mozilla.com</a> and <a href="https://twitter.com/blairmacintyre">@blairmacintyre</a></p>
<br>
<p>Try it out yourself, help ensure it supports the capabilities you need:</p>
<ul>
    <li>WebXR spec at http://github.com/mozilla/webxr-api</li>
    <li>webxr.js + samples at http://github.com/mozilla/webxr-polyfill</li>
    <li>iOS app source at http://github.com/mozilla/webxr-ios</li>
</ul>

<p>This talk available at <a href="https://blairmacintyre.github.io/ismar-2017/industrial.html">https://blairmacintyre.github.io/ismar-2017/industrial.html</a></p>

