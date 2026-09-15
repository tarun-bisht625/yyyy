/**
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
