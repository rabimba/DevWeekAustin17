<!-- .slide: data-background="resources/textures/background-radial.jpeg" -->

<h2>webxr.js and three.js are just libraries</h2>
<p class="green">Used webxr.js and three.js to add AR to this reveal.js presentation</p>
<p>Add argon and aframe scripts up top</p>
<pre><code class="HTML" data-trim contenteditable>
&lt;script src="resources/js/webxr.js"&gt; &lt;/script&gt; 
&lt;script src="resources/js/three.js"&gt; &lt;/script&gt;
&lt;script src="resources/js/reveal.js"&gt; &lt;/script&gt; 
</code></pre>
<p>Add a some code to create a three.js scene down below</p>
<pre><code class="javascript" data-trim contenteditable>
let box = new THREE.Mesh(
    new THREE.BoxBufferGeometry(0.1, 0.1, 0.1),
    new THREE.MeshPhongMaterial({ color: '#DDFFDD' })
)
</code></pre>
<p>Adjust the CSS a bit, add some more Javascript and we're off...</p>

------
<!-- .slide: data-background="resources/textures/iss-ar.png" -->
<blockquote style="background: rgba(32, 32, 32, 0.5);">
<h2>Web Ecosystem is Rich and Diverse</h2>
<p>Many tools, from the simple to the elaborate</p>
<p>Mashups may suggest new ways of creating 3D!</p>
</blockquote>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<blockquote style="background: rgba(32, 32, 32, 0.5);">
    <span><em>ISS Maintenance using PRIDE w/ Traclabs</em></span>
</blockquote>

---
<!-- .slide: data-background="resources/textures/argon-glitch.png" -->
<div style="background: rgba(32, 32, 32, 0.5);">
    <h2>glitch.com</h2>
</div>
<br>
<br>
<br>
<br>
<br>
<br>
<br><br>

<br>
<br>
<br>
<blockquote style="background: rgba(32, 32, 32, 0.5);">
    <span>https://argon-example.glitch.me</span>
</blockquote>
	

