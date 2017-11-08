
## Problem: WebGL (and libraries like three.js) still low level 

<!-- .slide: data-background-video="media/video/boilerplate.mp4" data-state="state--bg-dark" -->

<div class="slide__boilerplate">
  <p>Import WebVR polyfill</p>
  <p>Set up camera</p>
  <p>Set up lights</p>
  <p>Initialize scene</p>
  <p>Declare and pass canvas</p>
  <p>Listen to window resize</p>
  <p>Install VREffect</p>
  <p>Instantiate renderer</p>
  <p>Create render loop</p>
  <p>Preload assets</p>
  <p>Figure out responsiveness</p>
  <p>Deal with metatags and mobile</p>
</div>

<!-- NOTES -->
- It's still too difficult to create WebVR experiences
- Huge obstacle if doing small prototypes and experiments
- Boilerplate needs updating with new versions of WebVR, three.js, and browser quirks
- Encapsulate all of that into one line...
------
<!-- .slide: data-background="resources/textures/background-radial.jpeg" -->

<div class="captioned-image-row">
  <div>
    <img class="plain" data-src="media/img/aframe-logo-rendered.png">
    <i>Frameworks:<br> AFrame</i>
  </div>
</div>
------

## Hello World

<!-- .slide: data-background="media/img/aframe.jpg" data-transition="slide-in none" -->

```html
<html>
  <script src="https://aframe.io/releases/0.5.0/aframe.min.js"></script>
  <a-scene>





  </a-scene>
</html>
```
<!-- .element: class="stretch" style="background: rgba(32, 32, 32, 0.5);"-->

<!-- NOTES -->
- Just HTML
- Drop a script tag, no build steps
- Using Custom HTML Elements
- One line of HTML `<a-scene>` handles
  - canvas, camera, renderer, lights, controls, render loop, WebVR polyfill, VREffect
- Put stuff inside our scene...

------

## Hello World

<!-- .slide: data-background="media/img/aframe.jpg" data-transition="fade-in slide-out" -->

```html
<html>
  <script src="https://aframe.io/releases/0.5.0/aframe.min.js"></script>
  <a-scene>
    <a-box color="#4CC3D9" position="-1 0.5 -3" rotation="0 45 0"></a-box>
    <a-cylinder color="#FFC65D" position="1 0.75 -3" radius="0.5" height="1.5"></a-cylinder>
    <a-sphere color="#EF2D5E" position="0 1.25 -5" radius="1.25"></a-sphere>
    <a-plane color="#7BC8A4" position="0 0 -4" rotation="-90 0 0" width="4" height="4"></a-plane>
    <a-sky color="#ECECEC"></a-sky>
  </a-scene>
</html>
```
<!-- .element: class="stretch" style="background: rgba(32, 32, 32, 0.5);" -->

<!-- NOTES -->
- Basic 3D primitives with Custom Elements
- Readable: HTML arguably most accessible language in computing
- Encapsulated: copy-and-paste HTML anywhere else and still work, no state or variables
- Quickly look at a live example...

------

<!-- .slide: data-background="media/img/aframe.jpg" -->
<div style="background: rgba(32, 32, 32, 0.5);">
    <h2>Works With Everything</h1>

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

<!-- NOTES -->

- Based on HTML, compatible with all existing libraries/frameworks
- Good reason to have HTML as an intermediary layer between WebGL/three.js
- All tools were on top of the notion of HTML
- Under the hood, A-Frame is an extensible, declarative framework for three.js...

------

<div style="background: rgba(32, 32, 32, 0.5);">
    <h1> Entity-Component-System</h1>
</div>

<!-- .slide: data-background="media/img/minecraft-blocks.png" -->

<!-- NOTES -->
- Is an entity-component framework
- Popular in game development, used by Unity
- All objects in scene are **entities** that inherently empty objects. Plug in
  **components** to attach appearance / behavior / functionality
- 2D web where every element was fixed
- 3D/VR is different, objects of infinite types and complexities, need an easy way to build up different kinds of objects

---

<!-- .slide: data-background="media/img/minecraft-blocks.png" data-transition="slide-in none" -->

## Composing an Entity

```html
<a-entity>
```
<!-- .element: class="stretch" style="font-size: 24px; background: rgba(32, 32, 32, 0.5);"-->

<!-- NOTES -->
- Start with an `<a-entity>`
- By itself, has no appearance, behavior, functionality
- Plug in components to add appearance, behavior, functionality

---

## Composing an Entity

<!-- .slide: data-background="media/img/minecraft-blocks.png" data-transition="none" -->

```html
<a-entity
  geometry="primitive: sphere; radius: 1.5"
  material="color: #343434; roughness: 0.4; sphericalEnvMap: #texture">
```
<!-- .element: class="stretch" style="font-size: 24px;  background: rgba(32, 32, 32, 0.5);"-->

<!-- NOTES -->
- Syntax similar to CSS styles
- Component names as HTML attributes
- Component properties and values as HTML attribute value

---

## Composing an Entity

<!-- .slide: data-background="media/img/minecraft-blocks.png" data-transition="none" -->

```html
<a-entity
  geometry="primitive: sphere; radius: 1.5"
  material="color: #343434; roughness: 0.4; sphericalEnvMap: #texture"
  position="-1 2 4" rotation="45 0 90" scale="2 2 2">
```
<!-- .element: class="stretch" style="font-size: 24px;  background: rgba(32, 32, 32, 0.5);"-->

---

## Composing an Entity

<!-- .slide: data-background="media/img/minecraft-blocks.png" data-transition="none" -->

```html
<a-entity
  geometry="primitive: sphere; radius: 1.5"
  material="color: #343434; roughness: 0.4; sphericalEnvMap: #texture"
  position="-1 2 4" rotation="45 0 90" scale="2 2 2"
  animation="property: rotation; loop: true; to: 0 360 0"
  movement-pattern="type: spline; speed: 4">
```
<!-- .element: class="stretch" style="font-size: 24px;  background: rgba(32, 32, 32, 0.5);"-->

---

## Composing an Entity

<!-- .slide: data-background="media/img/minecraft-blocks.png" data-transition="none" -->

```html
<a-entity
  json-model="src: #robot"
  position="-1 2 4" rotation="45 0 90" scale="2 2 2"
  animation="property: rotation; loop: true; to: 0 360 0"
  movement-pattern="type: spline; speed: 4">
```
<!-- .element: class="stretch" style="font-size: 24px;  background: rgba(32, 32, 32, 0.5);"-->

---

## Composing an Entity

<!-- .slide: data-background="media/img/minecraft-blocks.png" data-transition="none" -->

```html
<a-entity
  json-model="src: #robot"
  position="-1 2 4" rotation="45 0 90" scale="2 2 2"
  animation="property: rotation; loop: true; to: 0 360 0"
  movement-pattern="type: attack; target: #player"
  explode="on: hit">
```
<!-- .element: class="stretch" style="font-size: 24px;  background: rgba(32, 32, 32, 0.5);"-->


------

<!-- .slide: data-background="media/img/standard-components.png" data-background-size="contain" -->

<!-- NOTES -->
- These are some components that ship with A-Frame
- A-Frame is fully extensible at its core so...

------

<!-- .slide: data-background="media/img/community-components.png" data-background-size="contain" -->

<!-- NOTES -->
- Community has filled the ecosystem with tons of components
- Components can do whatever they want, have full access to three.js and Web APIs
- The component ecosystem the lifeblood of A-Frame
- Physics, leap motion, particle systems, audio visualizations, oceans
- Drop these components as script tags and use them straight from HTML
- Advanced developers empowering other developers
- Working on collecting these components...

------

<!-- .slide: data-background-video="media/video/registrypreview-sm.mov" data-transition="slide-in fade-out" data-state="state--bg-dark"  data-background-video-loop="true" -->

<div style="background: rgba(32, 32, 32, 0.5);">
    <h1>Registry</h1>
    Curated collection of A-Frame components.
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

<!-- NOTES -->
- Collecting them into the A-Frame registry
- Like a store of components that we make sure work well
- People can browse and search for components or install them....

------

<!-- .slide: data-background-video="media/video/leaphands.mp4" data-transition="fade-in slide-out"  data-state="state--bg-dark" data-background-video-loop="true" -->

<div style="background: rgba(32, 32, 32, 0.5);">
    <h1>Registry</h1>
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
<br>
<br>
<br>
<br>

------

# Inspector

<!-- .slide: data-background="media/img/inspector.jpg" data-state="state--bg-dark" -->

Visual tool for A-Frame. 

Just `<ctrl>+<alt>+i`.
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

<!-- .slide: data-background="media/img/header.png" -->

# Community

https://aframe.io/blog/
---

<!-- .slide: data-background="media/img/apainter.gif" -->

# Art - *A-Painter*

@mozillavr

---

<!-- .slide: data-background="media/img/syria.gif" -->

# Journalism - *Fear of the Sky*

Amnesty International UK

---

<!-- .slide: data-background="media/img/mars.jpg" -->

# Journalism - *Journey to Mars*

The Washington Post

---

<!-- .slide: data-background="media/img/adit.gif" -->

# Data Visualization - *Adit*

@datatitian

---

<!-- .slide: data-background="media/img/a-blast.gif" -->

# Gaming - *A-Blast*

@mozillavr

---

<!-- .slide: data-background="media/img/math.gif" -->

# Mathematics - *MathworldVR*

@sleighdogs

---

<!-- .slide: data-background="media/img/webvrstudio.png" -->

# Tools - *WebVR Studio*

@webvrstudio

---

<!-- .slide: data-background-video="media/video/livetour.mp4" data-background-video-loop="true" -->

# Real Estate - *Live Tour*

iStaging

---

<!-- .slide: data-background="media/img/cadavr.gif" -->

# Education - *CadaVR*

@drryanjames

------

<!-- .slide: data-background="media/img/stars.gif" -->
<div style="background: rgba(32, 32, 32, 0.5);">

# aframe.io

`aframe-5000.glitch.me / glitch.com/~aframe-5000`

<div class="captioned-image-row">
  <div>
    <img class="plain" data-src="media/img/github.png">
    <i>135 contributors 5000 Stargazers</i>
  </div>
  <div>
    <img class="plain" data-src="media/img/slack.png">
    <i>3200 members on Slack</i>
  </div>
  <div>
    <img class="plain" data-src="media/img/scene-collage-circle.png">
    <i>100s of featured projects</i>
  </div>
</div>
</div>
<!-- NOTES -->
- Open source and inclusive project
- Most work done on GitHub
- Active community on Slack to share projects, interact, hang out, seek help
- Featured projects on the `awesome-aframe` repository and *A Week of A-Frame* blog
