import os

DEST_DIR = r"C:\Users\pathr\.gemini\antigravity\scratch\engineers-day-blueprint\js"
os.makedirs(DEST_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. audio.js
# -------------------------------------------------------------
audio_js = """/**
 * Procedural Web Audio API Synthesizer
 * Zero external audio files, pure mathematical sound synthesis.
 */

class SoundEngine {
  constructor() {
    this.ctx = null;
    this.enabled = localStorage.getItem('blueprint_sound') !== 'false';
    this.initialized = false;
  }

  init() {
    if (this.initialized && this.ctx) return;
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioCtx();
      this.initialized = true;
    } catch (e) {
      console.warn('Web Audio API not supported', e);
    }
  }

  ensureContext() {
    if (!this.initialized) this.init();
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  toggle() {
    this.enabled = !this.enabled;
    localStorage.setItem('blueprint_sound', this.enabled ? 'true' : 'false');
    if (this.enabled) {
      this.ensureContext();
      this.playClick();
    }
    return this.enabled;
  }

  playClick() {
    if (!this.enabled) return;
    this.ensureContext();
    if (!this.ctx) return;

    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = 'sine';
      const now = this.ctx.currentTime;
      osc.frequency.setValueAtTime(1400, now);
      osc.frequency.exponentialRampToValueAtTime(700, now + 0.04);

      gain.gain.setValueAtTime(0.12, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now);
      osc.stop(now + 0.04);
    } catch (e) {}
  }

  playType() {
    if (!this.enabled) return;
    this.ensureContext();
    if (!this.ctx) return;

    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = 'triangle';
      const now = this.ctx.currentTime;
      const freq = 600 + Math.random() * 400;
      osc.frequency.setValueAtTime(freq, now);

      gain.gain.setValueAtTime(0.04, now);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.025);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now);
      osc.stop(now + 0.025);
    } catch (e) {}
  }

  playGlitch() {
    if (!this.enabled) return;
    this.ensureContext();
    if (!this.ctx) return;

    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = 'sawtooth';
      const now = this.ctx.currentTime;
      osc.frequency.setValueAtTime(300, now);
      osc.frequency.setValueAtTime(800, now + 0.02);
      osc.frequency.setValueAtTime(250, now + 0.04);
      osc.frequency.setValueAtTime(950, now + 0.06);

      gain.gain.setValueAtTime(0.08, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now);
      osc.stop(now + 0.08);
    } catch (e) {}
  }

  playLaser() {
    if (!this.enabled) return;
    this.ensureContext();
    if (!this.ctx) return;

    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = 'sawtooth';
      const now = this.ctx.currentTime;
      osc.frequency.setValueAtTime(920, now);
      osc.frequency.exponentialRampToValueAtTime(140, now + 0.09);

      gain.gain.setValueAtTime(0.18, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.09);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now);
      osc.stop(now + 0.09);
    } catch (e) {}
  }

  playExplosion() {
    if (!this.enabled) return;
    this.ensureContext();
    if (!this.ctx) return;

    try {
      const bufferSize = Math.floor(this.ctx.sampleRate * 0.15);
      const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
      const data = buffer.getChannelData(0);
      for (let i = 0; i < bufferSize; i++) {
        data[i] = Math.random() * 2 - 1;
      }

      const noise = this.ctx.createBufferSource();
      noise.buffer = buffer;

      const filter = this.ctx.createBiquadFilter();
      filter.type = 'lowpass';
      const now = this.ctx.currentTime;
      filter.frequency.setValueAtTime(800, now);
      filter.frequency.exponentialRampToValueAtTime(80, now + 0.14);

      const gain = this.ctx.createGain();
      gain.gain.setValueAtTime(0.22, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);

      noise.connect(filter);
      filter.connect(gain);
      gain.connect(this.ctx.destination);

      noise.start(now);
    } catch (e) {}
  }

  playDamage() {
    if (!this.enabled) return;
    this.ensureContext();
    if (!this.ctx) return;

    try {
      const osc1 = this.ctx.createOscillator();
      const osc2 = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc1.type = 'square';
      osc2.type = 'sawtooth';

      const now = this.ctx.currentTime;
      osc1.frequency.setValueAtTime(110, now);
      osc2.frequency.setValueAtTime(116, now);

      gain.gain.setValueAtTime(0.25, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.2);

      osc1.connect(gain);
      osc2.connect(gain);
      gain.connect(this.ctx.destination);

      osc1.start(now);
      osc2.start(now);
      osc1.stop(now + 0.2);
      osc2.stop(now + 0.2);
    } catch (e) {}
  }

  playWaveStart() {
    if (!this.enabled) return;
    this.ensureContext();
    if (!this.ctx) return;

    try {
      const now = this.ctx.currentTime;
      const notes = [220, 330, 440, 660];
      notes.forEach((freq, idx) => {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, now + idx * 0.06);

        gain.gain.setValueAtTime(0.12, now + idx * 0.06);
        gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.06 + 0.12);

        osc.connect(gain);
        gain.connect(this.ctx.destination);

        osc.start(now + idx * 0.06);
        osc.stop(now + idx * 0.06 + 0.12);
      });
    } catch (e) {}
  }

  playVictory() {
    if (!this.enabled) return;
    this.ensureContext();
    if (!this.ctx) return;

    try {
      const now = this.ctx.currentTime;
      const notes = [523.25, 659.25, 783.99, 1046.5];
      notes.forEach((freq, idx) => {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();

        osc.type = idx === notes.length - 1 ? 'triangle' : 'sine';
        osc.frequency.setValueAtTime(freq, now + idx * 0.12);

        const duration = idx === notes.length - 1 ? 0.6 : 0.2;
        gain.gain.setValueAtTime(0.15, now + idx * 0.12);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + idx * 0.12 + duration);

        osc.connect(gain);
        gain.connect(this.ctx.destination);

        osc.start(now + idx * 0.12);
        osc.stop(now + idx * 0.12 + duration);
      });
    } catch (e) {}
  }
}

window.soundEngine = new SoundEngine();
"""

with open(os.path.join(DEST_DIR, "audio.js"), "w", encoding="utf-8") as f:
    f.write(audio_js)

# -------------------------------------------------------------
# 2. three-scene.js
# -------------------------------------------------------------
three_js = """/**
 * Three.js Hero Scene - Interactive 3D Architectural Blueprint Engine
 */

class Blueprint3DScene {
  constructor() {
    this.container = document.getElementById('hero-three-canvas');
    if (!this.container) return;

    this.scene = null;
    this.camera = null;
    this.renderer = null;
    this.modelsGroup = null;
    this.particles = null;

    this.currentMode = 0;
    this.modes = [];

    this.mouse = { x: 0, y: 0, targetX: 0, targetY: 0 };
    this.windowHalfX = window.innerWidth / 2;
    this.windowHalfY = window.innerHeight / 2;

    this.clock = new THREE.Clock();
    this.lastFrameTime = performance.now();
    this.frameCount = 0;
    this.fps = 60;
    this.isVisible = true;

    this.init();
  }

  init() {
    this.scene = new THREE.Scene();
    this.scene.fog = new THREE.FogExp2(0x0a192f, 0.035);

    const width = this.container.clientWidth || window.innerWidth;
    const height = this.container.clientHeight || window.innerHeight;
    const aspect = width / height;
    this.camera = new THREE.PerspectiveCamera(45, aspect, 0.1, 1000);
    this.camera.position.set(0, 0, 18);

    this.renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true,
      powerPreference: 'high-performance'
    });
    this.renderer.setSize(width, height);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    this.container.appendChild(this.renderer.domElement);

    const ambientLight = new THREE.AmbientLight(0x0a2540, 1.5);
    this.scene.add(ambientLight);

    const cyanLight = new THREE.PointLight(0x64ffda, 2, 50);
    cyanLight.position.set(10, 12, 10);
    this.scene.add(cyanLight);

    const blueLight = new THREE.PointLight(0x00d2ff, 1.8, 50);
    blueLight.position.set(-10, -10, 8);
    this.scene.add(blueLight);

    this.modelsGroup = new THREE.Group();
    this.scene.add(this.modelsGroup);

    this.createGeodesicMode();
    this.createHypercubeMode();
    this.createTrussMode();
    this.createBackgroundParticles();
    this.createBlueprintFloorGrid();

    this.switchMode(0);

    window.addEventListener('resize', () => this.onWindowResize());
    window.addEventListener('mousemove', (e) => this.onMouseMove(e));
    window.addEventListener('touchmove', (e) => this.onTouchMove(e), { passive: true });

    this.setupHUDControls();

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        this.isVisible = entry.isIntersecting;
      });
    }, { threshold: 0.05 });
    observer.observe(this.container);

    this.animate();
  }

  createGeodesicMode() {
    const group = new THREE.Group();

    const icoGeo = new THREE.IcosahedronGeometry(4.5, 1);
    const icoEdges = new THREE.EdgesGeometry(icoGeo);
    const icoMat = new THREE.LineBasicMaterial({
      color: 0x64ffda,
      transparent: true,
      opacity: 0.85,
      linewidth: 1.5
    });
    const icoWire = new THREE.LineSegments(icoEdges, icoMat);
    group.add(icoWire);

    const pointsMat = new THREE.PointsMaterial({
      color: 0x64ffda,
      size: 0.25,
      transparent: true,
      opacity: 0.95
    });
    const icoPoints = new THREE.Points(icoGeo, pointsMat);
    group.add(icoPoints);

    const octGeo = new THREE.OctahedronGeometry(2.6, 0);
    const octEdges = new THREE.EdgesGeometry(octGeo);
    const octMat = new THREE.LineBasicMaterial({
      color: 0x00d2ff,
      transparent: true,
      opacity: 0.75
    });
    const octWire = new THREE.LineSegments(octEdges, octMat);
    group.add(octWire);

    const sphereGeo = new THREE.SphereGeometry(1.2, 16, 16);
    const sphereMat = new THREE.MeshBasicMaterial({
      color: 0x112240,
      wireframe: true,
      transparent: true,
      opacity: 0.4
    });
    const sphereMesh = new THREE.Mesh(sphereGeo, sphereMat);
    group.add(sphereMesh);

    const ringMat1 = new THREE.LineBasicMaterial({ color: 0x64ffda, transparent: true, opacity: 0.35 });
    const ringGeo1 = new THREE.RingGeometry(6.2, 6.22, 64);
    const ring1 = new THREE.LineLoop(ringGeo1, ringMat1);
    ring1.rotation.x = Math.PI / 3;
    group.add(ring1);

    const ringMat2 = new THREE.LineBasicMaterial({ color: 0x00d2ff, transparent: true, opacity: 0.25 });
    const ringGeo2 = new THREE.RingGeometry(7.5, 7.52, 64);
    const ring2 = new THREE.LineLoop(ringGeo2, ringMat2);
    ring2.rotation.y = Math.PI / 4;
    group.add(ring2);

    group.name = 'mode_geodesic';
    this.modelsGroup.add(group);
    this.modes[0] = { group, vertexCount: 142, name: 'GEODESIC_CORE_V1' };
  }

  createHypercubeMode() {
    const group = new THREE.Group();

    const outerSize = 4.2;
    const innerSize = 2.2;

    const outerGeo = new THREE.BoxGeometry(outerSize, outerSize, outerSize);
    const outerEdges = new THREE.EdgesGeometry(outerGeo);
    const outerMat = new THREE.LineBasicMaterial({ color: 0x64ffda, transparent: true, opacity: 0.9 });
    const outerCube = new THREE.LineSegments(outerEdges, outerMat);
    group.add(outerCube);

    const innerGeo = new THREE.BoxGeometry(innerSize, innerSize, innerSize);
    const innerEdges = new THREE.EdgesGeometry(innerGeo);
    const innerMat = new THREE.LineBasicMaterial({ color: 0x00d2ff, transparent: true, opacity: 0.8 });
    const innerCube = new THREE.LineSegments(innerEdges, innerMat);
    group.add(innerCube);

    const strutsGeo = new THREE.BufferGeometry();
    const positions = [];
    const signs = [-1, 1];

    signs.forEach(x => {
      signs.forEach(y => {
        signs.forEach(z => {
          positions.push((x * outerSize) / 2, (y * outerSize) / 2, (z * outerSize) / 2);
          positions.push((x * innerSize) / 2, (y * innerSize) / 2, (z * innerSize) / 2);
        });
      });
    });

    strutsGeo.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
    const strutsMat = new THREE.LineBasicMaterial({ color: 0x64ffda, transparent: true, opacity: 0.6 });
    const struts = new THREE.LineSegments(strutsGeo, strutsMat);
    group.add(struts);

    const vertexMat = new THREE.PointsMaterial({ color: 0x64ffda, size: 0.3, transparent: true, opacity: 0.95 });
    const outerPoints = new THREE.Points(outerGeo, vertexMat);
    const innerPoints = new THREE.Points(innerGeo, vertexMat);
    group.add(outerPoints);
    group.add(innerPoints);

    const arcMat = new THREE.LineBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.3 });
    const arcGeo = new THREE.RingGeometry(5.8, 5.82, 48);
    const arc = new THREE.LineLoop(arcGeo, arcMat);
    arc.rotation.x = Math.PI / 2;
    group.add(arc);

    group.name = 'mode_hypercube';
    this.modelsGroup.add(group);
    this.modes[1] = { group, vertexCount: 96, name: 'TESSERACT_HYPERCUBE' };
  }

  createTrussMode() {
    const group = new THREE.Group();

    const length = 8;
    const width = 3.5;
    const height = 3.5;
    const divisions = 4;
    const step = length / divisions;

    const positions = [];
    const nodePositions = [];

    for (let i = 0; i <= divisions; i++) {
      const x = -length / 2 + i * step;

      const c1 = [x, -height / 2, -width / 2];
      const c2 = [x, -height / 2, width / 2];
      const c3 = [x, height / 2, width / 2];
      const c4 = [x, height / 2, -width / 2];

      nodePositions.push(...c1, ...c2, ...c3, ...c4);

      positions.push(...c1, ...c2);
      positions.push(...c2, ...c3);
      positions.push(...c3, ...c4);
      positions.push(...c4, ...c1);

      if (i < divisions) {
        const nextX = x + step;
        const nc1 = [nextX, -height / 2, -width / 2];
        const nc2 = [nextX, -height / 2, width / 2];
        const nc3 = [nextX, height / 2, width / 2];
        const nc4 = [nextX, height / 2, -width / 2];

        positions.push(...c1, ...nc1);
        positions.push(...c2, ...nc2);
        positions.push(...c3, ...nc3);
        positions.push(...c4, ...nc4);

        positions.push(...c1, ...nc4);
        positions.push(...c2, ...nc3);
        positions.push(...c1, ...nc2);
        positions.push(...c4, ...nc3);
      }
    }

    const trussGeo = new THREE.BufferGeometry();
    trussGeo.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
    const trussMat = new THREE.LineBasicMaterial({ color: 0x64ffda, transparent: true, opacity: 0.85 });
    const truss = new THREE.LineSegments(trussGeo, trussMat);
    group.add(truss);

    const nodesGeo = new THREE.BufferGeometry();
    nodesGeo.setAttribute('position', new THREE.Float32BufferAttribute(nodePositions, 3));
    const nodesMat = new THREE.PointsMaterial({ color: 0x00d2ff, size: 0.35, transparent: true, opacity: 0.95 });
    const nodes = new THREE.Points(nodesGeo, nodesMat);
    group.add(nodes);

    group.name = 'mode_truss';
    group.rotation.y = Math.PI / 4;
    group.rotation.x = Math.PI / 8;
    this.modelsGroup.add(group);
    this.modes[2] = { group, vertexCount: 168, name: 'SPACE_FRAME_TRUSS' };
  }

  createBackgroundParticles() {
    const count = 220;
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(count * 3);
    const scales = new Float32Array(count);

    for (let i = 0; i < count; i++) {
      positions[i * 3] = (Math.random() - 0.5) * 45;
      positions[i * 3 + 1] = (Math.random() - 0.5) * 35;
      positions[i * 3 + 2] = (Math.random() - 0.5) * 35;
      scales[i] = Math.random() * 0.15 + 0.05;
    }

    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('scale', new THREE.BufferAttribute(scales, 1));

    const material = new THREE.PointsMaterial({
      color: 0x64ffda,
      size: 0.18,
      transparent: true,
      opacity: 0.45,
      blending: THREE.AdditiveBlending
    });

    this.particles = new THREE.Points(geometry, material);
    this.scene.add(this.particles);
  }

  createBlueprintFloorGrid() {
    const gridHelper = new THREE.GridHelper(50, 50, 0x64ffda, 0x112240);
    gridHelper.position.y = -6;
    gridHelper.material.opacity = 0.22;
    gridHelper.material.transparent = true;
    this.scene.add(gridHelper);
  }

  switchMode(index) {
    this.currentMode = index;
    this.modes.forEach((mode, idx) => {
      if (mode && mode.group) {
        mode.group.visible = (idx === index);
        mode.group.scale.set(1, 1, 1);
      }
    });

    const modelTag = document.getElementById('hud-model-name');
    const nodesTag = document.getElementById('hud-node-count');
    if (modelTag && this.modes[index]) {
      modelTag.textContent = this.modes[index].name;
    }
    if (nodesTag && this.modes[index]) {
      nodesTag.textContent = this.modes[index].vertexCount + ' NODES';
    }

    if (window.soundEngine) {
      window.soundEngine.playClick();
    }
  }

  setupHUDControls() {
    const buttons = document.querySelectorAll('.hud-model-btn');
    buttons.forEach((btn, idx) => {
      btn.addEventListener('click', () => {
        buttons.forEach(b => b.classList.remove('active', 'border-cyan-400', 'text-cyan-300', 'bg-cyan-950/50', 'bg-cyan-950/40'));
        btn.classList.add('active', 'border-cyan-400', 'text-cyan-300', 'bg-cyan-950/50');
        this.switchMode(idx);
      });
    });
  }

  onMouseMove(e) {
    this.mouse.targetX = (e.clientX - this.windowHalfX) * 0.0012;
    this.mouse.targetY = (e.clientY - this.windowHalfY) * 0.0012;

    const coordDisplay = document.getElementById('hud-mouse-coords');
    if (coordDisplay) {
      coordDisplay.textContent = 'X: ' + e.clientX.toString().padStart(4, '0') + ' | Y: ' + e.clientY.toString().padStart(4, '0');
    }
  }

  onTouchMove(e) {
    if (e.touches.length > 0) {
      const touch = e.touches[0];
      this.mouse.targetX = (touch.clientX - this.windowHalfX) * 0.0015;
      this.mouse.targetY = (touch.clientY - this.windowHalfY) * 0.0015;
    }
  }

  onWindowResize() {
    if (!this.container || !this.camera || !this.renderer) return;
    this.windowHalfX = window.innerWidth / 2;
    this.windowHalfY = window.innerHeight / 2;

    const width = this.container.clientWidth || window.innerWidth;
    const height = this.container.clientHeight || window.innerHeight;

    this.camera.aspect = width / height;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(width, height);
  }

  animate() {
    requestAnimationFrame(() => this.animate());

    if (!this.isVisible) return;

    const delta = this.clock.getDelta();
    const time = this.clock.getElapsedTime();

    this.frameCount++;
    const now = performance.now();
    if (now - this.lastFrameTime >= 1000) {
      this.fps = this.frameCount;
      this.frameCount = 0;
      this.lastFrameTime = now;
      const fpsTag = document.getElementById('hud-fps');
      if (fpsTag) fpsTag.textContent = this.fps + ' FPS';
    }

    this.mouse.x += (this.mouse.targetX - this.mouse.x) * 0.05;
    this.mouse.y += (this.mouse.targetY - this.mouse.y) * 0.05;

    if (this.modelsGroup) {
      this.modelsGroup.rotation.y = time * 0.18 + this.mouse.x * 2.5;
      this.modelsGroup.rotation.x = Math.sin(time * 0.1) * 0.15 + this.mouse.y * 1.5;

      if (this.currentMode === 0 && this.modes[0] && this.modes[0].group) {
        if (this.modes[0].group.children[2]) this.modes[0].group.children[2].rotation.y = -time * 0.35;
        if (this.modes[0].group.children[4]) this.modes[0].group.children[4].rotation.z = time * 0.1;
        if (this.modes[0].group.children[5]) this.modes[0].group.children[5].rotation.x = -time * 0.15;
      } else if (this.currentMode === 1 && this.modes[1] && this.modes[1].group) {
        if (this.modes[1].group.children[1]) {
          this.modes[1].group.children[1].rotation.x = time * 0.25;
          this.modes[1].group.children[1].rotation.y = -time * 0.3;
        }
      } else if (this.currentMode === 2 && this.modes[2] && this.modes[2].group) {
        this.modes[2].group.position.y = Math.sin(time * 0.8) * 0.2;
      }
    }

    if (this.particles) {
      this.particles.rotation.y = time * 0.03;
      this.particles.rotation.x = time * 0.015;
    }

    this.renderer.render(this.scene, this.camera);
  }
}

function init3D() {
  if (!window.blueprint3D) {
    window.blueprint3D = new Blueprint3DScene();
  }
}
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init3D);
} else {
  init3D();
}
"""

with open(os.path.join(DEST_DIR, "three-scene.js"), "w", encoding="utf-8") as f:
    f.write(three_js)

# -------------------------------------------------------------
# 3. facts.js
# -------------------------------------------------------------
facts_js = """/**
 * Engineering Facts Database & Terminal Cipher Decoder Engine
 */

const ENGINEERING_FACTS = [
  {
    category: 'HISTORICAL PIONEER',
    discipline: 'Civil & Hydraulic',
    title: 'Automatic Sluice Floodgates (1903)',
    text: 'Sir M. Visvesvaraya patented automatic weir water floodgates in 1903 at Khadakwasla Dam. The counterweight design increased reservoir storage without compromising dam integrity during severe floods, later implemented across India.',
    metric: 'PATENT: NO. 1903-IND'
  },
  {
    category: 'DEEP SPACE',
    discipline: 'Aerospace & Telemetry',
    title: 'Voyager 1 - 70 Kilobytes at 24 Billion KM',
    text: 'Voyager 1 was launched in 1977 with only 69.63 kilobytes of memory across three dual-redundant computer systems. It still communicates across interstellar space 24+ billion kilometers away, powered by a 23-watt radio transmitter.',
    metric: 'DISTANCE: 24.3B KM'
  },
  {
    category: 'SOFTWARE ARCHITECTURE',
    discipline: 'Digital & Computing',
    title: 'Apollo 11 & Margaret Hamilton\\'s Priority Inversion',
    text: 'Three minutes before Apollo 11 touched down on the Moon, the radar overloaded the computer. Margaret Hamilton\\'s asynchronous executive software preempted low-priority tasks to keep thrusters and guidance active, preventing an abort.',
    metric: 'UPTIME: 100% MISSION CRITICAL'
  },
  {
    category: 'CIVIL & STRUCTURAL',
    discipline: 'Structural Engineering',
    title: 'Burj Khalifa Vortex Shedding Architecture',
    text: 'The Burj Khalifa\\'s Y-shaped stepping design was engineered to "confuse the wind." As wind spirals around the 828m tower, different elevations encounter different building shapes, preventing resonant wind vortices from snapping the tower.',
    metric: 'HEIGHT: 828 METERS'
  },
  {
    category: 'SEISMIC ENGINEERING',
    discipline: 'Earthquake Dynamics',
    title: 'Taipei 101 Tuned Mass Damper',
    text: 'Suspended between the 87th and 92nd floors of Taipei 101 hangs a 660-tonne golden steel pendulum. During typhoons and 7.0+ magnitude earthquakes, it sways opposite to the tower, absorbing up to 40% of seismic kinetic shock.',
    metric: 'PENDULUM WEIGHT: 660 TONNES'
  },
  {
    category: 'ALGORITHMIC FOUNDATIONS',
    discipline: 'Computer Science',
    title: 'The Fast Fourier Transform (FFT)',
    text: 'The Cooley-Tukey FFT algorithm reduced discrete Fourier transform complexity from O(N^2) to O(N log N). Without this single mathematical optimization, modern MRI scans, 5G wireless networks, JPEG compression, and digital audio would be computationally infeasible.',
    metric: 'COMPLEXITY: O(N log N)'
  },
  {
    category: 'HYDRAULIC FEATS',
    discipline: 'Civil & Hydro',
    title: 'The Panama Canal Gravity Lift',
    text: 'The Panama Canal lifts 100,000-ton cargo ships 26 meters above sea level across continental mountains. It uses ZERO water pumps—the entire system operates purely on gravitational hydrostatic head from Lake Gatun.',
    metric: 'ELEVATION LIFT: 26 METERS'
  },
  {
    category: 'OPTICAL & AEROSPACE',
    discipline: 'Deep Space Instrumentation',
    title: 'James Webb Nanometer Gold Mirrors',
    text: 'The James Webb Space Telescope folded 18 hexagonal beryllium mirrors plated with a microscopic 100-nanometer layer of vaporized 24k gold. Deployed at the L2 Lagrange point, each mirror actuator adjusts at 1/10,000th the width of a human hair.',
    metric: 'MIRROR ACCURACY: 10 NANOMETERS'
  },
  {
    category: 'MATERIALS SCIENCE',
    discipline: 'Mechanical Engineering',
    title: 'Jet Engine Single-Crystal Turbine Blades',
    text: 'Modern turbofan jet turbine blades operate at temperatures higher than the melting point of nickel alloy (1,400°C+). They are cast as a single continuous crystal with internal labyrinth air cooling channels to prevent boundary grain stress ruptures.',
    metric: 'THERMAL TOLERANCE: 1,600°C'
  },
  {
    category: 'INFRASTRUCTURE RESILIENCE',
    discipline: 'Structural Engineering',
    title: 'Akashi Kaikyō Bridge Mid-Construction Earthquake',
    text: 'During the 1995 Great Hanshin Earthquake (7.2 magnitude), the epicentre lay directly beneath the unfinished Akashi Kaikyō bridge. The seabed fault shifted the two support towers apart by 1.1 meters. Engineers simply recalculated cable catenary geometry and completed the bridge.',
    metric: 'CENTRAL SPAN: 1,991 METERS'
  },
  {
    category: 'BIOMEDICAL ENGINEERING',
    discipline: 'Neural & Bio-Cybernetics',
    title: 'Targeted Muscle Reinnervation (TMR)',
    text: 'Biomedical engineers can reroute severed motor nerves from amputated limbs into remaining chest or shoulder muscles. Sensors placed on the surface translate residual neural signals into bionic finger movements with sub-100ms latency.',
    metric: 'NEURAL LATENCY: < 100MS'
  },
  {
    category: 'SEMICONDUCTOR REVOLUTION',
    discipline: 'Electrical & Nano-Engineering',
    title: 'Extreme Ultraviolet Lithography (EUV)',
    text: 'Modern 3nm chips are etched using 13.5nm EUV lasers created by firing molten tin droplets at 50,000 times per second and vaporizing them with high-powered CO2 lasers. The mirror precision required is comparable to hitting a coin on the Moon with a laser pointer.',
    metric: 'PROCESS SCALE: 3 NANOMETERS'
  },
  {
    category: 'HISTORICAL PIONEER',
    discipline: 'Civil & Urban Planning',
    title: 'Krishna Raja Sagara Dam & Mysore Modernization',
    text: 'Sir M. Visvesvaraya designed and executed the Krishna Raja Sagara Dam on the Cauvery River, which transformed the arid Mandya district into a fertile agricultural engine and powered the historic Kolar Gold Fields hydroelectric grid.',
    metric: 'PROJECT: KRS DAM (1924)'
  }
];

class FactGenerator {
  constructor() {
    this.currentIndex = 0;
    this.isDecoding = false;
    this.factCard = document.getElementById('fact-display-card');
    this.factTitle = document.getElementById('fact-title');
    this.factText = document.getElementById('fact-text');
    this.factCategory = document.getElementById('fact-category');
    this.factDiscipline = document.getElementById('fact-discipline');
    this.factMetric = document.getElementById('fact-metric');
    this.generateBtn = document.getElementById('btn-generate-fact');
    this.copyBtn = document.getElementById('btn-copy-fact');
    this.toast = document.getElementById('fact-toast');

    this.glyphs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_#@%&<>[]{}/=*+-';

    this.init();
  }

  init() {
    if (this.generateBtn) {
      this.generateBtn.addEventListener('click', () => this.generateNewFact());
    }
    if (this.copyBtn) {
      this.copyBtn.addEventListener('click', () => this.copyCurrentFact());
    }

    this.displayFact(0, false);
  }

  generateNewFact() {
    if (this.isDecoding) return;

    let nextIndex;
    do {
      nextIndex = Math.floor(Math.random() * ENGINEERING_FACTS.length);
    } while (nextIndex === this.currentIndex && ENGINEERING_FACTS.length > 1);

    this.currentIndex = nextIndex;
    this.displayFact(this.currentIndex, true);
  }

  displayFact(index, animate) {
    const fact = ENGINEERING_FACTS[index];
    if (!fact) return;

    if (this.factCategory) this.factCategory.textContent = fact.category;
    if (this.factDiscipline) this.factDiscipline.textContent = '// ' + fact.discipline;
    if (this.factMetric) this.factMetric.textContent = fact.metric;

    if (!animate) {
      if (this.factTitle) this.factTitle.textContent = fact.title;
      if (this.factText) this.factText.textContent = fact.text;
      return;
    }

    this.isDecoding = true;
    if (window.soundEngine) window.soundEngine.playGlitch();

    this.decodeString(this.factTitle, fact.title, 350, () => {
      this.decodeString(this.factText, fact.text, 650, () => {
        this.isDecoding = false;
      });
    });
  }

  decodeString(element, targetText, duration, onComplete) {
    if (!element) {
      if (onComplete) onComplete();
      return;
    }

    const length = targetText.length;
    const startTime = performance.now();
    const interval = 30;

    const timer = setInterval(() => {
      const elapsed = performance.now() - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const charsRevealed = Math.floor(progress * length);

      let output = '';
      for (let i = 0; i < length; i++) {
        if (i < charsRevealed) {
          output += targetText[i];
        } else if (targetText[i] === ' ' || targetText[i] === '\\n') {
          output += targetText[i];
        } else {
          output += this.glyphs[Math.floor(Math.random() * this.glyphs.length)];
        }
      }

      element.textContent = output;

      if (progress >= 1) {
        clearInterval(timer);
        element.textContent = targetText;
        if (onComplete) onComplete();
      }
    }, interval);
  }

  copyCurrentFact() {
    const fact = ENGINEERING_FACTS[this.currentIndex];
    if (!fact) return;

    const copyText = "Engineers' Day Blueprint [" + fact.discipline + "]:\\n\\"" + fact.title + "\\" - " + fact.text + " (" + fact.metric + ")";

    navigator.clipboard.writeText(copyText).then(() => {
      if (window.soundEngine) window.soundEngine.playClick();
      this.showToast('COPIED SCHEMATIC FACT TO CLIPBOARD');
    }).catch(err => {
      console.warn('Clipboard write failed', err);
    });
  }

  showToast(message) {
    if (!this.toast) return;
    this.toast.textContent = message;
    this.toast.classList.remove('opacity-0', 'translate-y-2');
    this.toast.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
      this.toast.classList.add('opacity-0', 'translate-y-2');
      this.toast.classList.remove('opacity-100', 'translate-y-0');
    }, 2400);
  }
}

function initFacts() {
  if (!window.factGenerator) {
    window.factGenerator = new FactGenerator();
  }
}
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initFacts);
} else {
  initFacts();
}
"""

with open(os.path.join(DEST_DIR, "facts.js"), "w", encoding="utf-8") as f:
    f.write(facts_js)

# -------------------------------------------------------------
# 4. game.js
# -------------------------------------------------------------
game_js = """/**
 * Mini-Game: 'Debug & Destroy: The Production Patch'
 * 2D Canvas Cyberpunk Bug Squasher & CI/CD Deployment Defense
 */

class DebugGame {
  constructor() {
    this.canvas = document.getElementById('game-canvas');
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');

    this.scoreDisplay = document.getElementById('game-score');
    this.waveDisplay = document.getElementById('game-wave');
    this.healthDisplay = document.getElementById('game-health');
    this.bugsRemainingDisplay = document.getElementById('game-bugs-left');
    this.overlay = document.getElementById('game-overlay');
    this.overlayTitle = document.getElementById('game-overlay-title');
    this.overlaySubtitle = document.getElementById('game-overlay-subtitle');
    this.overlayStats = document.getElementById('game-overlay-stats');
    this.btnStart = document.getElementById('game-btn-start');
    this.btnPause = document.getElementById('game-btn-pause');
    this.btnRestart = document.getElementById('game-btn-restart');

    this.isRunning = false;
    this.isPaused = false;
    this.score = 0;
    this.serverHealth = 100;
    this.currentWave = 1;
    this.maxWaves = 3;
    this.bugsSpawnedThisWave = 0;
    this.bugsToSpawnTotal = 14;
    this.bugsKilledThisWave = 0;
    this.shotsFired = 0;
    this.shotsHit = 0;
    this.comboStreak = 0;
    this.maxCombo = 0;

    this.bugs = [];
    this.particles = [];
    this.floatingTexts = [];
    this.lasers = [];
    this.confetti = [];

    this.lastSpawnTime = 0;
    this.spawnInterval = 1400;
    this.animationFrameId = null;

    this.dpr = Math.min(window.devicePixelRatio || 1, 2);
    this.width = 800;
    this.height = 480;

    this.mouse = { x: this.width / 2, y: this.height / 2, down: false };

    this.init();
  }

  init() {
    this.setupCanvasSize();
    window.addEventListener('resize', () => this.setupCanvasSize());

    this.canvas.addEventListener('mousemove', (e) => this.handleMouseMove(e));
    this.canvas.addEventListener('mousedown', (e) => this.handleMouseDown(e));
    this.canvas.addEventListener('touchstart', (e) => this.handleTouch(e), { passive: false });

    if (this.btnStart) {
      this.btnStart.addEventListener('click', (e) => {
        if (e) e.stopPropagation();
        this.startGame();
      });
    }
    if (this.btnPause) {
      this.btnPause.addEventListener('click', (e) => {
        if (e) e.stopPropagation();
        this.togglePause();
      });
    }
    if (this.btnRestart) {
      this.btnRestart.addEventListener('click', (e) => {
        if (e) e.stopPropagation();
        this.resetGame();
      });
    }

    this.drawStandbyScreen();
  }

  setupCanvasSize() {
    const rect = this.canvas.getBoundingClientRect();
    this.width = rect.width || 800;
    this.height = rect.height || 480;
    if (this.height < 400) this.height = 480;

    this.dpr = Math.min(window.devicePixelRatio || 1, 2);
    this.canvas.width = Math.floor(this.width * this.dpr);
    this.canvas.height = Math.floor(this.height * this.dpr);

    if (!this.isRunning) {
      this.drawStandbyScreen();
    }
  }

  handleMouseMove(e) {
    const rect = this.canvas.getBoundingClientRect();
    this.mouse.x = e.clientX - rect.left;
    this.mouse.y = e.clientY - rect.top;
  }

  handleMouseDown(e) {
    if (!this.isRunning || this.isPaused) return;
    const rect = this.canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    this.mouse.x = x;
    this.mouse.y = y;
    this.shootHotfix(x, y);
  }

  handleTouch(e) {
    if (!this.isRunning || this.isPaused) return;
    if (e.cancelable) e.preventDefault();
    const rect = this.canvas.getBoundingClientRect();
    const touch = e.touches[0];
    if (!touch) return;
    const x = touch.clientX - rect.left;
    const y = touch.clientY - rect.top;
    this.mouse.x = x;
    this.mouse.y = y;
    this.shootHotfix(x, y);
  }

  startGame() {
    if (this.overlay) {
      this.overlay.classList.add('hidden');
      this.overlay.classList.remove('flex');
      this.overlay.style.display = 'none';
      this.overlay.style.pointerEvents = 'none';
    }

    this.isRunning = true;
    this.isPaused = false;
    this.score = 0;
    this.serverHealth = 100;
    this.currentWave = 1;
    this.shotsFired = 0;
    this.shotsHit = 0;
    this.comboStreak = 0;
    this.maxCombo = 0;
    this.bugs = [];
    this.particles = [];
    this.floatingTexts = [];
    this.lasers = [];
    this.confetti = [];
    this.lastSpawnTime = performance.now();

    this.startWave(1);

    if (window.soundEngine) {
      window.soundEngine.ensureContext();
      window.soundEngine.playWaveStart();
    }

    if (this.animationFrameId) cancelAnimationFrame(this.animationFrameId);
    this.lastFrameTime = performance.now();
    this.gameLoop(performance.now());
  }

  startWave(waveNum) {
    this.currentWave = waveNum;
    this.bugsSpawnedThisWave = 0;
    this.bugsKilledThisWave = 0;

    if (waveNum === 1) {
      this.bugsToSpawnTotal = 14;
      this.spawnInterval = 1300;
    } else if (waveNum === 2) {
      this.bugsToSpawnTotal = 22;
      this.spawnInterval = 1000;
    } else {
      this.bugsToSpawnTotal = 32;
      this.spawnInterval = 750;
    }

    this.updateHUD();

    const waveNames = ['', 'DEV_STAGING', 'CANARY_CLUSTER', 'PRODUCTION_PUSH'];
    this.addFloatingText(
      this.width / 2,
      this.height / 2 - 20,
      '--- WAVE ' + waveNum + ': ' + waveNames[waveNum] + ' ---',
      '#64ffda',
      22,
      110
    );

    if (window.soundEngine) window.soundEngine.playWaveStart();
  }

  togglePause() {
    if (!this.isRunning) return;
    this.isPaused = !this.isPaused;
    if (this.btnPause) {
      this.btnPause.textContent = this.isPaused ? 'RESUME [▶]' : 'PAUSE [⏸]';
    }
    if (!this.isPaused) {
      this.lastFrameTime = performance.now();
      this.gameLoop(performance.now());
    }
  }

  resetGame() {
    this.isRunning = false;
    this.isPaused = false;
    if (this.animationFrameId) cancelAnimationFrame(this.animationFrameId);
    if (this.btnPause) this.btnPause.textContent = 'PAUSE [⏸]';
    this.startGame();
  }

  shootHotfix(targetX, targetY) {
    this.shotsFired++;
    if (window.soundEngine) window.soundEngine.playLaser();

    const originX = 140;
    const originY = this.height - 30;

    this.lasers.push({
      x1: originX,
      y1: originY,
      x2: targetX,
      y2: targetY,
      opacity: 1,
      color: '#64ffda'
    });

    this.particles.push({
      x: targetX,
      y: targetY,
      radius: 4,
      maxRadius: 28,
      color: '#64ffda',
      alpha: 1,
      decay: 0.08,
      isShockwave: true
    });

    let hit = false;
    for (let i = this.bugs.length - 1; i >= 0; i--) {
      const bug = this.bugs[i];
      const dist = Math.hypot(targetX - bug.x, targetY - bug.y);

      if (dist <= bug.radius + 22) {
        hit = true;
        this.shotsHit++;
        this.comboStreak++;
        if (this.comboStreak > this.maxCombo) this.maxCombo = this.comboStreak;

        bug.hp--;
        this.createHitParticles(bug.x, bug.y, bug.color, 10);

        if (bug.hp <= 0) {
          this.destroyBug(bug, i);
        } else {
          this.addFloatingText(bug.x, bug.y - 12, 'PATCHED! -1 HP', '#00d2ff', 12, 40);
        }
        break;
      }
    }

    if (!hit) {
      this.comboStreak = 0;
      this.createHitParticles(targetX, targetY, 'rgba(100, 255, 218, 0.4)', 4);
    }

    this.updateHUD();
  }

  destroyBug(bug, index) {
    this.bugs.splice(index, 1);
    this.bugsKilledThisWave++;

    const multiplier = Math.min(Math.floor(this.comboStreak / 3) + 1, 5);
    const earned = bug.points * multiplier;
    this.score += earned;

    if (window.soundEngine) window.soundEngine.playExplosion();

    const bonusText = multiplier > 1 ? ' (' + multiplier + 'x COMBO!)' : '';
    this.addFloatingText(bug.x, bug.y, '+' + earned + bonusText, '#64ffda', 15, 60);

    this.createBugDebris(bug.x, bug.y, bug.type, bug.color);

    if (this.bugsSpawnedThisWave >= this.bugsToSpawnTotal && this.bugs.length === 0) {
      this.onWaveComplete();
    }
  }

  onWaveComplete() {
    if (this.currentWave < this.maxWaves) {
      this.addFloatingText(this.width / 2, this.height / 2, 'WAVE ' + this.currentWave + ' RESOLVED!', '#00d2ff', 22, 90);
      setTimeout(() => {
        if (this.isRunning) {
          this.startWave(this.currentWave + 1);
        }
      }, 1500);
    } else {
      this.triggerVictory();
    }
  }

  triggerVictory() {
    this.isRunning = false;
    if (window.soundEngine) window.soundEngine.playVictory();

    for (let i = 0; i < 120; i++) {
      this.confetti.push({
        x: Math.random() * this.width,
        y: Math.random() * -100,
        vx: (Math.random() - 0.5) * 4,
        vy: Math.random() * 3 + 2,
        color: ['#64ffda', '#00d2ff', '#38bdf8', '#ffffff'][Math.floor(Math.random() * 4)],
        size: Math.random() * 6 + 4,
        char: ['0', '1', ';', '{', '}', '✓'][Math.floor(Math.random() * 6)]
      });
    }

    const accuracy = this.shotsFired > 0 ? Math.round((this.shotsHit / this.shotsFired) * 100) : 100;

    if (this.overlay) {
      this.overlayTitle.textContent = 'DEPLOYMENT SUCCESSFUL! 0 ERRORS';
      this.overlayTitle.className = 'text-2xl md:text-3xl font-bold font-mono text-cyan-300 text-glow-cyan mb-2';
      this.overlaySubtitle.textContent = 'Production cluster stable. Zero downtime achieved across all waves.';
      this.overlayStats.innerHTML = 
        '<div class="grid grid-cols-2 gap-3 text-left font-mono text-sm">' +
          '<div class="p-2 bg-navy-900/80 border border-cyan-500/20 rounded">FINAL SCORE: <span class="text-cyan-300 font-bold">' + this.score + '</span></div>' +
          '<div class="p-2 bg-navy-900/80 border border-cyan-500/20 rounded">SERVER SLA: <span class="text-emerald-400 font-bold">' + this.serverHealth + '%</span></div>' +
          '<div class="p-2 bg-navy-900/80 border border-cyan-500/20 rounded">ACCURACY: <span class="text-cyan-300 font-bold">' + accuracy + '%</span></div>' +
          '<div class="p-2 bg-navy-900/80 border border-cyan-500/20 rounded">MAX COMBO: <span class="text-amber-400 font-bold">' + this.maxCombo + 'x</span></div>' +
        '</div>';
      this.btnStart.textContent = 'DEPLOY AGAIN [↺]';
      this.overlay.classList.remove('hidden');
      this.overlay.classList.add('flex');
      this.overlay.style.display = 'flex';
      this.overlay.style.pointerEvents = 'auto';
    }
  }

  triggerDefeat() {
    this.isRunning = false;
    if (window.soundEngine) window.soundEngine.playDamage();

    const canvasContainer = this.canvas.parentElement;
    if (canvasContainer) {
      canvasContainer.classList.add('screen-shake');
      setTimeout(() => canvasContainer.classList.remove('screen-shake'), 400);
    }

    if (this.overlay) {
      this.overlayTitle.textContent = 'SLA BREACH! 500 INTERNAL SERVER ERROR';
      this.overlayTitle.className = 'text-2xl md:text-3xl font-bold font-mono text-rose-500 mb-2';
      this.overlaySubtitle.textContent = 'Rogue bugs overwhelmed production servers. Automated rollback initiated.';
      this.overlayStats.innerHTML = 
        '<div class="text-sm font-mono text-slate-300">' +
          'Reached Wave ' + this.currentWave + ' of ' + this.maxWaves + ' | Score: ' + this.score +
        '</div>';
      this.btnStart.textContent = 'RE-DEPLOY HOTFIX [↻]';
      this.overlay.classList.remove('hidden');
      this.overlay.classList.add('flex');
      this.overlay.style.display = 'flex';
      this.overlay.style.pointerEvents = 'auto';
    }
  }

  spawnBug() {
    this.bugsSpawnedThisWave++;

    const types = [
      { name: 'NullPointerException', label: 'NULL_PTR', color: '#00d2ff', hp: 1, speed: 1.8, radius: 16, points: 100 },
      { name: 'SyntaxError', label: 'SYNTAX_ERR', color: '#ff3366', hp: 1, speed: 2.2, radius: 14, points: 120 },
      { name: 'MemoryLeak: OOM', label: 'MEM_LEAK', color: '#c084fc', hp: 3, speed: 0.9, radius: 24, points: 250 },
      { name: 'RaceCondition', label: 'RACE_COND', color: '#facc15', hp: 1, speed: 1.6, radius: 16, points: 150 },
      { name: 'OffByOne', label: 'OFF_BY_1', color: '#4ade80', hp: 1, speed: 2.4, radius: 13, points: 140 }
    ];

    let availableTypes = [types[0], types[1]];
    if (this.currentWave >= 2) availableTypes.push(types[2], types[4]);
    if (this.currentWave >= 3) availableTypes.push(types[3]);

    const chosen = availableTypes[Math.floor(Math.random() * availableTypes.length)];

    const spawnX = this.width - 40 + (Math.random() * 30);
    const spawnY = 60 + Math.random() * (this.height - 180);

    const targetX = 100 + Math.random() * 40;
    const targetY = this.height - 70;

    const angle = Math.atan2(targetY - spawnY, targetX - spawnX);
    const speedMult = 1 + (this.currentWave - 1) * 0.2;

    this.bugs.push({
      type: chosen.name,
      label: chosen.label,
      color: chosen.color,
      maxHp: chosen.hp,
      hp: chosen.hp,
      radius: chosen.radius,
      points: chosen.points,
      x: spawnX,
      y: spawnY,
      vx: Math.cos(angle) * chosen.speed * speedMult,
      vy: Math.sin(angle) * chosen.speed * speedMult,
      targetX: targetX,
      targetY: targetY,
      wiggleOffset: Math.random() * Math.PI * 2,
      glitchTimer: 0,
      legsPhase: 0
    });
  }

  createHitParticles(x, y, color, count) {
    const num = count || 8;
    for (let i = 0; i < num; i++) {
      const angle = Math.random() * Math.PI * 2;
      const speed = Math.random() * 3 + 1;
      this.particles.push({
        x: x,
        y: y,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed,
        color: color,
        radius: Math.random() * 2.5 + 1,
        alpha: 1,
        decay: Math.random() * 0.03 + 0.02
      });
    }
  }

  createBugDebris(x, y, type, color) {
    const chars = ['0', '1', ';', '{', '}', '<', '>', 'ERR', 'NULL', '404'];
    for (let i = 0; i < 8; i++) {
      const angle = Math.random() * Math.PI * 2;
      const speed = Math.random() * 2.5 + 1.5;
      this.particles.push({
        x: x,
        y: y,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed - 1,
        color: color,
        char: chars[Math.floor(Math.random() * chars.length)],
        alpha: 1,
        decay: 0.02,
        isText: true
      });
    }
  }

  addFloatingText(x, y, text, color, size, life) {
    this.floatingTexts.push({
      x: x,
      y: y,
      text: text,
      color: color || '#64ffda',
      size: size || 14,
      alpha: 1,
      life: life || 50,
      maxLife: life || 50
    });
  }

  updateHUD() {
    if (this.scoreDisplay) this.scoreDisplay.textContent = this.score.toString().padStart(5, '0');
    if (this.waveDisplay) this.waveDisplay.textContent = 'WAVE ' + this.currentWave + '/' + this.maxWaves;
    if (this.healthDisplay) {
      this.healthDisplay.textContent = this.serverHealth + '%';
      this.healthDisplay.className = this.serverHealth > 50 ? 'text-emerald-400 font-bold' : this.serverHealth > 25 ? 'text-amber-400 font-bold' : 'text-rose-500 font-bold animate-pulse';
    }
    if (this.bugsRemainingDisplay) {
      const remaining = Math.max(0, (this.bugsToSpawnTotal - this.bugsSpawnedThisWave) + this.bugs.length);
      this.bugsRemainingDisplay.textContent = remaining + ' ACTIVE';
    }
  }

  gameLoop(currentTime) {
    if (!this.isRunning || this.isPaused) return;

    const dt = Math.min((currentTime - this.lastFrameTime) / 1000, 0.1);
    this.lastFrameTime = currentTime;

    if (this.bugsSpawnedThisWave < this.bugsToSpawnTotal) {
      if (currentTime - this.lastSpawnTime >= this.spawnInterval) {
        this.spawnBug();
        this.lastSpawnTime = currentTime;
        this.updateHUD();
      }
    }

    this.updateBugs(dt);
    this.updateParticles(dt);
    this.updateLasers();
    this.updateFloatingTexts();

    this.render();

    this.animationFrameId = requestAnimationFrame((t) => this.gameLoop(t));
  }

  updateBugs(dt) {
    for (let i = this.bugs.length - 1; i >= 0; i--) {
      const bug = this.bugs[i];

      bug.legsPhase += 0.2;
      bug.wiggleOffset += 0.08;

      if (bug.type === 'RaceCondition') {
        bug.glitchTimer += dt;
        if (bug.glitchTimer > 1.8) {
          bug.x += bug.vx * 30;
          bug.y += bug.vy * 30;
          bug.glitchTimer = 0;
          this.createHitParticles(bug.x, bug.y, '#facc15', 5);
        }
      }

      const perpX = -bug.vy;
      const perpY = bug.vx;
      const wiggle = Math.sin(bug.wiggleOffset) * 0.8;

      bug.x += bug.vx + perpX * wiggle * 0.4;
      bug.y += bug.vy + perpY * wiggle * 0.4;

      const distToServer = Math.hypot(bug.x - bug.targetX, bug.y - bug.targetY);
      if (distToServer <= 35) {
        this.bugs.splice(i, 1);
        const damage = bug.type === 'MemoryLeak: OOM' ? 25 : 10;
        this.serverHealth = Math.max(0, this.serverHealth - damage);

        if (window.soundEngine) window.soundEngine.playDamage();
        this.addFloatingText(bug.targetX, bug.targetY - 15, '-' + damage + '% SLA DAMAGE!', '#ff3366', 16, 50);

        const canvasContainer = this.canvas.parentElement;
        if (canvasContainer) {
          canvasContainer.classList.add('screen-shake');
          setTimeout(() => canvasContainer.classList.remove('screen-shake'), 300);
        }

        this.updateHUD();

        if (this.serverHealth <= 0) {
          this.triggerDefeat();
          return;
        }

        if (this.bugsSpawnedThisWave >= this.bugsToSpawnTotal && this.bugs.length === 0) {
          this.onWaveComplete();
        }
      }
    }
  }

  updateParticles(dt) {
    for (let i = this.particles.length - 1; i >= 0; i--) {
      const p = this.particles[i];
      if (p.isShockwave) {
        p.radius += 2.5;
        p.alpha -= p.decay;
        if (p.alpha <= 0 || p.radius >= p.maxRadius) {
          this.particles.splice(i, 1);
        }
      } else {
        p.x += p.vx;
        p.y += p.vy;
        p.alpha -= p.decay;
        if (p.alpha <= 0) {
          this.particles.splice(i, 1);
        }
      }
    }

    for (let i = this.confetti.length - 1; i >= 0; i--) {
      const c = this.confetti[i];
      c.x += c.vx;
      c.y += c.vy;
      if (c.y > this.height) {
        c.y = -10;
        c.x = Math.random() * this.width;
      }
    }
  }

  updateLasers() {
    for (let i = this.lasers.length - 1; i >= 0; i--) {
      const l = this.lasers[i];
      l.opacity -= 0.12;
      if (l.opacity <= 0) {
        this.lasers.splice(i, 1);
      }
    }
  }

  updateFloatingTexts() {
    for (let i = this.floatingTexts.length - 1; i >= 0; i--) {
      const t = this.floatingTexts[i];
      t.y -= 0.8;
      t.life--;
      t.alpha = t.life / t.maxLife;

      if (t.life <= 0) {
        this.floatingTexts.splice(i, 1);
      }
    }
  }

  render() {
    const ctx = this.ctx;
    ctx.save();
    ctx.setTransform(this.dpr, 0, 0, this.dpr, 0, 0);
    ctx.clearRect(0, 0, this.width, this.height);

    this.drawBackgroundGrid(ctx);
    this.drawInfrastructure(ctx);
    this.drawLasers(ctx);

    this.bugs.forEach(bug => this.drawBug(ctx, bug));

    this.particles.forEach(p => {
      ctx.save();
      ctx.globalAlpha = Math.max(0, p.alpha);
      if (p.isShockwave) {
        ctx.strokeStyle = p.color;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(p.x, p.y, Math.max(0.1, p.radius), 0, Math.PI * 2);
        ctx.stroke();
      } else if (p.isText) {
        ctx.font = '11px monospace';
        ctx.fillStyle = p.color;
        ctx.fillText(p.char, p.x, p.y);
      } else {
        ctx.fillStyle = p.color;
        ctx.beginPath();
        ctx.arc(p.x, p.y, Math.max(0.1, p.radius), 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.restore();
    });

    if (this.confetti.length > 0) {
      this.confetti.forEach(c => {
        ctx.save();
        ctx.font = (c.size * 2) + 'px monospace';
        ctx.fillStyle = c.color;
        ctx.fillText(c.char, c.x, c.y);
        ctx.restore();
      });
    }

    this.floatingTexts.forEach(t => {
      ctx.save();
      ctx.globalAlpha = Math.max(0, t.alpha);
      ctx.font = 'bold ' + t.size + 'px monospace';
      ctx.fillStyle = t.color;
      ctx.textAlign = 'center';
      ctx.shadowColor = t.color;
      ctx.shadowBlur = 8;
      ctx.fillText(t.text, t.x, t.y);
      ctx.restore();
    });

    this.drawReticle(ctx);

    ctx.restore();
  }

  drawBackgroundGrid(ctx) {
    ctx.strokeStyle = 'rgba(100, 255, 218, 0.05)';
    ctx.lineWidth = 1;

    const gridSize = 25;
    for (let x = 0; x < this.width; x += gridSize) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, this.height);
      ctx.stroke();
    }
    for (let y = 0; y < this.height; y += gridSize) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(this.width, y);
      ctx.stroke();
    }
  }

  drawInfrastructure(ctx) {
    ctx.save();
    ctx.strokeStyle = 'rgba(100, 255, 218, 0.4)';
    ctx.fillStyle = 'rgba(15, 35, 71, 0.6)';
    ctx.lineWidth = 1.5;
    ctx.strokeRect(this.width - 150, 10, 140, 45);
    ctx.fillRect(this.width - 150, 10, 140, 45);

    ctx.font = '10px monospace';
    ctx.fillStyle = '#64ffda';
    ctx.fillText('CI/CD PIPELINE :: STAGING', this.width - 142, 28);
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('STATUS: DEPLOYING...', this.width - 142, 44);

    ctx.beginPath();
    ctx.arc(this.width - 18, 24, 4, 0, Math.PI * 2);
    ctx.fillStyle = (Math.floor(Date.now() / 400) % 2 === 0) ? '#64ffda' : '#00d2ff';
    ctx.fill();
    ctx.restore();

    ctx.save();
    ctx.strokeStyle = 'rgba(0, 210, 255, 0.4)';
    ctx.fillStyle = 'rgba(10, 25, 47, 0.85)';
    ctx.lineWidth = 2;
    ctx.strokeRect(20, this.height - 85, 160, 75);
    ctx.fillRect(20, this.height - 85, 160, 75);

    ctx.font = 'bold 11px monospace';
    ctx.fillStyle = '#00d2ff';
    ctx.fillText('PROD SERVER CLUSTER', 30, this.height - 66);

    const barWidth = 140;
    const hpWidth = (this.serverHealth / 100) * barWidth;
    ctx.fillStyle = 'rgba(255,255,255,0.1)';
    ctx.fillRect(30, this.height - 56, barWidth, 10);

    ctx.fillStyle = this.serverHealth > 50 ? '#10b981' : this.serverHealth > 25 ? '#f59e0b' : '#ef4444';
    ctx.fillRect(30, this.height - 56, hpWidth, 10);

    ctx.font = '9px monospace';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('UPTIME: 99.999% | SLA: ' + this.serverHealth + '%', 30, this.height - 28);

    for (let i = 0; i < 5; i++) {
      ctx.beginPath();
      ctx.arc(35 + i * 14, this.height - 18, 2.5, 0, Math.PI * 2);
      ctx.fillStyle = (i === 4 && this.serverHealth < 30) ? '#ef4444' : (Math.floor(Date.now() / 300) % 2 === i % 2) ? '#64ffda' : '#00d2ff';
      ctx.fill();
    }
    ctx.restore();
  }

  drawLasers(ctx) {
    this.lasers.forEach(l => {
      ctx.save();
      ctx.strokeStyle = l.color;
      ctx.globalAlpha = Math.max(0, l.opacity);
      ctx.lineWidth = 2.5;
      ctx.shadowColor = '#64ffda';
      ctx.shadowBlur = 12;

      ctx.beginPath();
      ctx.moveTo(l.x1, l.y1);
      ctx.lineTo(l.x2, l.y2);
      ctx.stroke();

      const flareRadius = Math.max(0, 10 * l.opacity);
      if (flareRadius > 0) {
        ctx.beginPath();
        ctx.arc(l.x2, l.y2, flareRadius, 0, Math.PI * 2);
        ctx.fillStyle = '#ffffff';
        ctx.fill();
      }
      ctx.restore();
    });
  }

  drawBug(ctx, bug) {
    ctx.save();
    ctx.translate(bug.x, bug.y);

    const angle = Math.atan2(bug.vy, bug.vx);
    ctx.rotate(angle);

    ctx.strokeStyle = bug.color;
    ctx.lineWidth = 1.5;
    for (let side = -1; side <= 1; side += 2) {
      for (let leg = -1; leg <= 1; leg++) {
        const legOffset = Math.sin(bug.legsPhase + leg) * 5;
        ctx.beginPath();
        ctx.moveTo(leg * 5, side * (bug.radius * 0.6));
        ctx.lineTo(leg * 7 + legOffset, side * (bug.radius * 1.3));
        ctx.stroke();
      }
    }

    ctx.beginPath();
    ctx.ellipse(0, 0, Math.max(2, bug.radius), Math.max(2, bug.radius * 0.7), 0, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(10, 25, 47, 0.9)';
    ctx.fill();
    ctx.strokeStyle = bug.color;
    ctx.lineWidth = 2;
    ctx.shadowColor = bug.color;
    ctx.shadowBlur = 8;
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(bug.radius * 0.8, -3);
    ctx.lineTo(bug.radius * 1.4, -8);
    ctx.moveTo(bug.radius * 0.8, 3);
    ctx.lineTo(bug.radius * 1.4, 8);
    ctx.stroke();

    if (bug.maxHp > 1) {
      ctx.rotate(-angle);
      const barW = bug.radius * 2;
      const hpW = (bug.hp / bug.maxHp) * barW;
      ctx.fillStyle = 'rgba(0,0,0,0.6)';
      ctx.fillRect(-barW / 2, -bug.radius - 12, barW, 4);
      ctx.fillStyle = bug.color;
      ctx.fillRect(-barW / 2, -bug.radius - 12, hpW, 4);
      ctx.rotate(angle);
    }

    ctx.restore();

    ctx.save();
    ctx.font = 'bold 10px monospace';
    ctx.fillStyle = bug.color;
    ctx.textAlign = 'center';
    ctx.shadowColor = bug.color;
    ctx.shadowBlur = 4;
    ctx.fillText(bug.label, bug.x, bug.y - bug.radius - 6);
    ctx.restore();
  }

  drawReticle(ctx) {
    ctx.save();
    ctx.translate(this.mouse.x, this.mouse.y);
    ctx.strokeStyle = 'rgba(100, 255, 218, 0.85)';
    ctx.lineWidth = 1.5;

    ctx.beginPath();
    ctx.arc(0, 0, 14, 0, Math.PI * 2);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(-20, 0); ctx.lineTo(-10, 0);
    ctx.moveTo(10, 0);  ctx.lineTo(20, 0);
    ctx.moveTo(0, -20); ctx.lineTo(0, -10);
    ctx.moveTo(0, 10);  ctx.lineTo(0, 20);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(0, 0, 2, 0, Math.PI * 2);
    ctx.fillStyle = '#64ffda';
    ctx.fill();

    ctx.font = '8px monospace';
    ctx.fillStyle = 'rgba(100, 255, 218, 0.7)';
    ctx.fillText('LOC: ' + Math.round(this.mouse.x) + ',' + Math.round(this.mouse.y), 16, -10);

    ctx.restore();
  }

  drawStandbyScreen() {
    const ctx = this.ctx;
    ctx.save();
    ctx.setTransform(this.dpr, 0, 0, this.dpr, 0, 0);
    ctx.clearRect(0, 0, this.width, this.height);
    this.drawBackgroundGrid(ctx);
    this.drawInfrastructure(ctx);

    ctx.textAlign = 'center';
    ctx.font = '14px monospace';
    ctx.fillStyle = '#64ffda';
    ctx.fillText('[ CI/CD PIPELINE STANDBY // AWAITING DEPLOYMENT COMMAND ]', this.width / 2, this.height / 2);
    ctx.font = '11px monospace';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('Click [INITIATE DEPLOYMENT] to start debugging incoming production bugs.', this.width / 2, this.height / 2 + 25);
    ctx.restore();
  }
}

function initGame() {
  if (!window.debugGame) {
    window.debugGame = new DebugGame();
  }
}
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initGame);
} else {
  initGame();
}
"""

with open(os.path.join(DEST_DIR, "game.js"), "w", encoding="utf-8") as f:
    f.write(game_js)

# -------------------------------------------------------------
# 5. main.js
# -------------------------------------------------------------
main_js = """/**
 * Main Application Logic
 * Typewriter, 3D Card Tilt, Blueprint Controls, HUD
 */

function initTypewriter() {
  const subtitleElem = document.getElementById('hero-typewriter-text');
  if (!subtitleElem) return;

  const messages = [
    'Architecting the physical and digital foundations of humanity.',
    'Turning theoretical impossibilities into resilient production realities.',
    'Transforming chaos into elegant, fault-tolerant infrastructure.',
    'Bridging human ambition with physics, silicon, and steel.',
    'Honoring the visionary minds that shape our tomorrow.'
  ];

  let msgIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  let typingSpeed = 55;

  function typeStep() {
    const currentMsg = messages[msgIndex];

    if (isDeleting) {
      charIndex--;
      subtitleElem.textContent = currentMsg.substring(0, charIndex);
      typingSpeed = 25;
    } else {
      charIndex++;
      subtitleElem.textContent = currentMsg.substring(0, charIndex);
      typingSpeed = 50;

      if (charIndex % 3 === 0 && window.soundEngine) {
        window.soundEngine.playType();
      }
    }

    if (!isDeleting && charIndex === currentMsg.length) {
      typingSpeed = 2200;
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      msgIndex = (msgIndex + 1) % messages.length;
      typingSpeed = 500;
    }

    setTimeout(typeStep, typingSpeed);
  }

  typeStep();
}

function initCardTilt() {
  const cards = document.querySelectorAll('.glass-card-tilt');

  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = ((y - centerY) / centerY) * -10;
      const rotateY = ((x - centerX) / centerX) * 10;

      card.style.transform = 'perspective(1000px) rotateX(' + rotateX.toFixed(2) + 'deg) rotateY(' + rotateY.toFixed(2) + 'deg) translateY(-4px)';

      const sheen = card.querySelector('.sheen-overlay');
      if (sheen) {
        sheen.style.setProperty('--mouse-x', ((x / rect.width) * 100) + '%');
        sheen.style.setProperty('--mouse-y', ((y / rect.height) * 100) + '%');
      }
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0px)';
    });

    card.addEventListener('mouseenter', () => {
      if (window.soundEngine) window.soundEngine.playClick();
    });
  });
}

function initGlobalControls() {
  const soundBtn = document.getElementById('toggle-sound');
  const soundLabel = document.getElementById('sound-status-text');

  function updateSoundUI() {
    const isEnabled = window.soundEngine ? window.soundEngine.enabled : true;
    if (soundLabel) {
      soundLabel.textContent = isEnabled ? 'AUDIO: ON' : 'AUDIO: OFF';
    }
    if (soundBtn) {
      soundBtn.classList.toggle('text-cyan-300', isEnabled);
      soundBtn.classList.toggle('text-slate-400', !isEnabled);
      soundBtn.classList.toggle('border-cyan-400', isEnabled);
    }
  }

  if (soundBtn) {
    soundBtn.addEventListener('click', () => {
      if (window.soundEngine) {
        window.soundEngine.toggle();
        updateSoundUI();
      }
    });
    updateSoundUI();
  }

  const gridBtn = document.getElementById('toggle-grid');
  const gridLabel = document.getElementById('grid-status-text');

  let gridEnabled = true;
  if (gridBtn) {
    gridBtn.addEventListener('click', () => {
      gridEnabled = !gridEnabled;
      const gridElements = document.querySelectorAll('.blueprint-grid-bg');
      gridElements.forEach(el => el.classList.toggle('grid-disabled', !gridEnabled));

      if (gridLabel) {
        gridLabel.textContent = gridEnabled ? 'GRID: ON' : 'GRID: OFF';
      }
      gridBtn.classList.toggle('text-cyan-300', gridEnabled);
      gridBtn.classList.toggle('text-slate-400', !gridEnabled);

      if (window.soundEngine) window.soundEngine.playClick();
    });
  }

  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
      if (window.soundEngine) window.soundEngine.playClick();
    });

    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => mobileMenu.classList.add('hidden'));
    });
  }
}

function initNavigation() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;

      const targetElem = document.querySelector(targetId);
      if (targetElem) {
        e.preventDefault();
        targetElem.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });

        if (window.soundEngine) window.soundEngine.playClick();
      }
    });
  });
}

function initCoordinateTracker() {
  const tracker = document.getElementById('global-coord-hud');
  if (!tracker) return;

  window.addEventListener('mousemove', (e) => {
    tracker.textContent = 'CRD: ' + e.clientX.toString().padStart(4, '0') + 'x, ' + e.clientY.toString().padStart(4, '0') + 'y | SYS.T: ' + Math.round(performance.now() / 1000) + 's';
  });
}

const DISCIPLINE_DATA = {
  infrastructure: {
    title: 'CIVIL & INFRASTRUCTURE SCHEMATICS',
    specId: 'SPEC-CIV-8849-B',
    stats: [
      { label: 'SEISMIC RESISTANCE', val: 'MAGNITUDE 9.0+' },
      { label: 'CONCRETE COMPRESSION', val: '120 MPa ULTRA-HIGH' },
      { label: 'SUSPENSION CATENARY', val: 'T = H / cos(θ)' },
      { label: 'HYDRAULIC DISCHARGE', val: 'Q = C_d A √(2gh)' }
    ],
    desc: 'From subterranean subway bore tunnels to tension-braced hyper-structures, civil engineering harmonizes raw planetary geology with architectural resilience.',
    breakdown: 'Core focus areas: Automated water reservoir weirs, seismic isolator tuned mass pendulums, ultra-low carbon geopolymers, and sensor-monitored smart highways.'
  },
  software: {
    title: 'DIGITAL & COMPUTING SYSTEMS ARCHITECTURE',
    specId: 'SPEC-CS-9901-X',
    stats: [
      { label: 'CONSENSUS PROTOCOL', val: 'RAFT / PAXOS FAULT-TOL' },
      { label: 'SEARCH COMPLEXITY', val: 'O(log N) BALANCED TREE' },
      { label: 'LATENCY BUDGET', val: '< 5ms P99 GLOBALLY' },
      { label: 'PARALLEL TFLOPS', val: '1,979 TFLOPS FP16' }
    ],
    desc: 'The invisible circulatory system of global civilization. Micro-architectures executing billions of instructions per millisecond without losing a single financial transaction or medical telemetry packet.',
    breakdown: 'Core focus areas: Zero-trust cryptographic protocols, self-healing distributed Kubernetes meshes, real-time deterministic OS kernels, and multi-tenant tensor parallel computing.'
  },
  aerospace: {
    title: 'AEROSPACE & PROPULSION TELEMETRY',
    specId: 'SPEC-AERO-0421-Z',
    stats: [
      { label: 'DELTA-V ORBITAL', val: 'Δv = Isp · g₀ · ln(m₀/mf)' },
      { label: 'SPECIFIC IMPULSE', val: '380s VACUUM METHOX' },
      { label: 'RE-ENTRY ABLATION', val: '3,000°C PICA-X' },
      { label: 'DEEP SPACE RANGE', val: '24,300,000,000 KM' }
    ],
    desc: 'Defying terrestrial gravitational wells through thermodynamic combustion and celestial orbital mechanics. Every gram shaved represents millions of Joules preserved.',
    breakdown: 'Core focus areas: Autonomous aerocapture, cryogenic stage separation, active laser retro-reflectors, and multi-spectral infrared exoplanet spectroscopy.'
  },
  biomedical: {
    title: 'BIOMEDICAL & NEURAL CYBERNETICS',
    specId: 'SPEC-BIO-7723-M',
    stats: [
      { label: 'SIGNAL EXTRACTION', val: 'SUB-10µV MYOELECTRIC' },
      { label: 'BIO-COMPATIBILITY', val: 'TITANIUM GRADE 5 / SILICONE' },
      { label: 'NEURAL FEEDBACK', val: 'HAPTIC FREQUENCY 250Hz' },
      { label: 'PUMP ACCURACY', val: '±0.01 µL/hr CONTINUOUS' }
    ],
    desc: 'Synthesizing biology and micro-robotics. Converting residual neuronal synaptic firing into articulated prosthetic movement and autonomous biochemical regulation.',
    breakdown: 'Core focus areas: Targeted muscle reinnervation, microfluidic lab-on-a-chip diagnostic arrays, deep-brain stimulation feedback loops, and bio-printed vascular scaffolds.'
  }
};

function initDisciplineModal() {
  const modal = document.getElementById('schematic-modal');
  const modalClose = document.getElementById('modal-close-btn');
  const modalTitle = document.getElementById('modal-title');
  const modalSpecId = document.getElementById('modal-spec-id');
  const modalDesc = document.getElementById('modal-desc');
  const modalBreakdown = document.getElementById('modal-breakdown');
  const modalStatsGrid = document.getElementById('modal-stats-grid');

  if (!modal) return;

  document.querySelectorAll('[data-schematic]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const key = btn.getAttribute('data-schematic');
      const data = DISCIPLINE_DATA[key];
      if (!data) return;

      modalTitle.textContent = data.title;
      modalSpecId.textContent = '[ ' + data.specId + ' ]';
      modalDesc.textContent = data.desc;
      modalBreakdown.textContent = data.breakdown;

      modalStatsGrid.innerHTML = data.stats.map(s => 
        '<div class="p-3 bg-navy-950/70 border border-cyan-500/20 rounded">' +
          '<div class="text-xs font-mono text-slate-400">' + s.label + '</div>' +
          '<div class="text-sm font-mono font-bold text-cyan-300">' + s.val + '</div>' +
        '</div>'
      ).join('');

      modal.classList.remove('hidden');
      modal.classList.add('flex');

      if (window.soundEngine) window.soundEngine.playClick();
    });
  });

  if (modalClose) {
    modalClose.addEventListener('click', () => {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
      if (window.soundEngine) window.soundEngine.playClick();
    });
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
      if (window.soundEngine) window.soundEngine.playClick();
    }
  });
}

function initMain() {
  initTypewriter();
  initCardTilt();
  initGlobalControls();
  initNavigation();
  initCoordinateTracker();
  initDisciplineModal();
}
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initMain);
} else {
  initMain();
}
"""

with open(os.path.join(DEST_DIR, "main.js"), "w", encoding="utf-8") as f:
    f.write(main_js)

print("All 5 JS files regenerated successfully!")
