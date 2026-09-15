/**
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

  setMode(index) {
    this.switchMode(index);
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
