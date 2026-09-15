import os

html_content = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Architect's Blueprint: Celebrating the Minds That Build Tomorrow | Engineers' Day</title>
  
  <!-- Google Fonts: Inter & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@300;400;500;700&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS via CDN with custom color configuration -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            navy: {
              950: '#060d1a',
              900: '#0a192f',
              850: '#0d1f3d',
              800: '#0f2347',
              700: '#1e3a5f',
              600: '#2a4d7d'
            },
            cyan: {
              300: '#64ffda',
              400: '#38efc6',
              500: '#14b8a6'
            },
            laser: {
              400: '#00d2ff',
              500: '#0284c7'
            }
          },
          fontFamily: {
            mono: ['"JetBrains Mono"', 'monospace'],
            sans: ['"Inter"', 'sans-serif']
          }
        }
      }
    }
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Three.js CDN -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

  <!-- Custom Stylesheet -->
  <link rel="stylesheet" href="css/styles.css">
</head>
<body class="bg-navy-900 text-slate-100 font-sans blueprint-grid-bg relative overflow-x-hidden antialiased selection:bg-cyan-300/20 selection:text-cyan-300">

  <!-- ========================================================================
       TOP NAVIGATION BAR
       ======================================================================== -->
  <header class="fixed top-0 left-0 right-0 z-50 bg-navy-950/85 backdrop-blur-md border-b border-cyan-500/20 px-4 md:px-8 py-3 transition-all">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      
      <!-- Brand / Logo -->
      <a href="#" class="flex items-center gap-3 group">
        <div class="relative w-8 h-8 flex items-center justify-center border border-cyan-400/60 bg-navy-900 rounded-sm group-hover:border-cyan-300 transition-colors">
          <span class="font-mono text-cyan-300 text-xs font-bold">AB</span>
          <div class="absolute -top-1 -right-1 w-2 h-2 bg-cyan-400 rounded-full animate-ping"></div>
          <div class="absolute -top-1 -right-1 w-2 h-2 bg-cyan-400 rounded-full"></div>
        </div>
        <div>
          <div class="font-mono text-xs text-cyan-400/80 tracking-widest leading-none">SYS.DESIGN // 2026</div>
          <div class="font-mono text-sm md:text-base font-bold text-slate-100 tracking-wider group-hover:text-cyan-300 transition-colors">
            THE ARCHITECT'S BLUEPRINT
          </div>
        </div>
      </a>

      <!-- Desktop Nav Links -->
      <nav class="hidden lg:flex items-center gap-6 font-mono text-xs">
        <a href="#hero" class="text-slate-300 hover:text-cyan-300 transition-colors py-1 flex items-center gap-1.5">
          <span class="text-cyan-400/60">01.</span>OVERVIEW
        </a>
        <a href="#disciplines" class="text-slate-300 hover:text-cyan-300 transition-colors py-1 flex items-center gap-1.5">
          <span class="text-cyan-400/60">02.</span>DISCIPLINES
        </a>
        <a href="#unsung-hero" class="text-slate-300 hover:text-cyan-300 transition-colors py-1 flex items-center gap-1.5">
          <span class="text-cyan-400/60">03.</span>UNSUNG HERO
        </a>
        <a href="#game-section" class="text-slate-300 hover:text-cyan-300 transition-colors py-1 flex items-center gap-1.5">
          <span class="text-cyan-400/60">04.</span>DEBUG_GAME
        </a>
      </nav>

      <!-- System Controls (Audio, Grid, Mobile) -->
      <div class="flex items-center gap-2 md:gap-3 font-mono text-xs">
        
        <!-- Sound Toggle Button -->
        <button id="toggle-sound" class="px-2.5 py-1.5 rounded bg-navy-900/80 border border-cyan-500/30 text-cyan-300 hover:border-cyan-300 transition-all flex items-center gap-1.5" title="Toggle Synthesizer Audio">
          <i data-lucide="volume-2" class="w-3.5 h-3.5"></i>
          <span id="sound-status-text" class="hidden sm:inline">AUDIO: ON</span>
        </button>

        <!-- Blueprint Grid Toggle Button -->
        <button id="toggle-grid" class="px-2.5 py-1.5 rounded bg-navy-900/80 border border-cyan-500/30 text-cyan-300 hover:border-cyan-300 transition-all flex items-center gap-1.5" title="Toggle Blueprint Grid">
          <i data-lucide="grid" class="w-3.5 h-3.5"></i>
          <span id="grid-status-text" class="hidden sm:inline">GRID: ON</span>
        </button>

        <!-- Mobile Hamburger Button -->
        <button id="mobile-menu-btn" class="lg:hidden p-2 text-slate-300 hover:text-cyan-300">
          <i data-lucide="menu" class="w-5 h-5"></i>
        </button>
      </div>
    </div>

    <!-- Mobile Drawer -->
    <div id="mobile-menu" class="hidden lg:hidden border-t border-cyan-500/20 mt-3 pt-3 flex flex-col gap-3 font-mono text-xs">
      <a href="#hero" class="text-slate-300 hover:text-cyan-300 py-1">01. OVERVIEW</a>
      <a href="#disciplines" class="text-slate-300 hover:text-cyan-300 py-1">02. DISCIPLINES</a>
      <a href="#unsung-hero" class="text-slate-300 hover:text-cyan-300 py-1">03. UNSUNG HERO</a>
      <a href="#game-section" class="text-slate-300 hover:text-cyan-300 py-1">04. DEBUG_GAME</a>
    </div>
  </header>


  <!-- ========================================================================
       SECTION 1: HERO SECTION WITH THREE.JS 3D CANVAS
       ======================================================================== -->
  <section id="hero" class="relative min-h-screen flex items-center justify-center pt-20 pb-12 px-4 md:px-8 overflow-hidden">
    
    <!-- Three.js Canvas Container -->
    <div id="hero-three-canvas" class="absolute inset-0 z-0 pointer-events-auto"></div>

    <!-- Radial Vignette Overlay to enhance contrast for text -->
    <div class="absolute inset-0 bg-gradient-to-b from-navy-950/40 via-transparent to-navy-900/90 pointer-events-none z-10"></div>

    <!-- Technical Corner Calibration Marks -->
    <div class="absolute top-24 left-6 font-mono text-[10px] text-cyan-400/50 hidden md:block z-20 pointer-events-none">
      <div>REF: ARCH_001 // SEC.HERO</div>
      <div>DIM: 1920x1080xINF</div>
      <div class="mt-1 flex items-center gap-1">
        <span class="w-1.5 h-1.5 bg-cyan-400 rounded-full inline-block"></span>
        <span>SYS.OK</span>
      </div>
    </div>

    <!-- 3D Model HUD Switcher (Top-Right of Hero) -->
    <div class="absolute top-24 right-4 md:right-8 z-20 flex flex-col items-end gap-1.5 font-mono text-[11px]">
      <div class="text-[10px] text-slate-400 tracking-wider uppercase mb-1">3D Schematic Mode</div>
      <div class="flex items-center gap-1 bg-navy-950/80 p-1 border border-cyan-500/30 rounded backdrop-blur-md">
        <button class="hud-model-btn active px-2.5 py-1 rounded border border-cyan-400 text-cyan-300 bg-cyan-950/50 hover:border-cyan-300 transition-all" data-mode="0">
          CORE
        </button>
        <button class="hud-model-btn px-2.5 py-1 rounded border border-transparent text-slate-400 hover:text-cyan-300 hover:border-cyan-500/40 transition-all" data-mode="1">
          HYPERCUBE
        </button>
        <button class="hud-model-btn px-2.5 py-1 rounded border border-transparent text-slate-400 hover:text-cyan-300 hover:border-cyan-500/40 transition-all" data-mode="2">
          TRUSS
        </button>
      </div>
    </div>

    <!-- Hero Central Content -->
    <div class="relative z-20 max-w-5xl mx-auto text-center mt-6">
      
      <!-- Engineers' Day Protocol Badge -->
      <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full border border-cyan-400/40 bg-navy-950/75 backdrop-blur-md mb-6 blueprint-corner">
        <span class="relative flex h-2 w-2">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-cyan-400 opacity-75"></span>
          <span class="relative inline-flex rounded-full h-2 w-2 bg-cyan-400"></span>
        </span>
        <span class="font-mono text-xs text-cyan-300 font-semibold tracking-wider">
          ENGINEERS' DAY // 15_SEPTEMBER_EDITION
        </span>
      </div>

      <!-- Main Headline -->
      <h1 class="text-4xl sm:text-6xl md:text-7xl lg:text-8xl font-black tracking-tight leading-none mb-6">
        <span class="block text-slate-100 drop-shadow-lg">Code. Calculate.</span>
        <span class="block bg-gradient-to-r from-cyan-300 via-laser-400 to-teal-300 bg-clip-text text-transparent text-glow-cyan">
          Construct.
        </span>
      </h1>

      <!-- Dynamic Typewriter Subtitle -->
      <div class="min-h-[3rem] sm:min-h-[2.5rem] flex items-center justify-center mb-8 px-4">
        <p class="font-mono text-sm sm:text-base md:text-xl text-slate-300 max-w-2xl leading-relaxed">
          <span id="hero-typewriter-text" class="text-cyan-200"></span><span class="typing-cursor"></span>
        </p>
      </div>

      <!-- Terminal CTA Buttons -->
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4 font-mono text-sm">
        
        <!-- Primary CTA: Smooth Scroll to Blueprint Schematics -->
        <a href="#disciplines" class="w-full sm:w-auto px-7 py-3.5 rounded bg-cyan-400 text-navy-950 font-bold tracking-wide hover:bg-cyan-300 hover:shadow-[0_0_25px_rgba(100,255,218,0.5)] transition-all flex items-center justify-center gap-2 group">
          <span>&gt; ./initiate_blueprint.sh</span>
          <i data-lucide="arrow-down" class="w-4 h-4 group-hover:translate-y-0.5 transition-transform"></i>
        </a>

        <!-- Secondary CTA: Jump to Debug Mini-Game -->
        <a href="#game-section" class="w-full sm:w-auto px-6 py-3.5 rounded bg-navy-950/80 border border-cyan-400/40 text-cyan-300 hover:border-cyan-300 hover:bg-cyan-950/40 hover:shadow-[0_0_20px_rgba(100,255,218,0.2)] transition-all flex items-center justify-center gap-2">
          <span>&gt; ./launch_debug_game.exe</span>
          <i data-lucide="bug" class="w-4 h-4 text-cyan-400"></i>
        </a>
      </div>

      <!-- Live Hero Telemetry Bar -->
      <div class="mt-12 inline-flex flex-wrap items-center justify-center gap-4 sm:gap-8 px-5 py-2.5 rounded border border-cyan-500/20 bg-navy-950/70 backdrop-blur-md font-mono text-xs text-slate-400">
        <div class="flex items-center gap-1.5">
          <span class="text-cyan-400">FPS:</span>
          <span id="hud-fps" class="text-slate-200 font-semibold">60 FPS</span>
        </div>
        <div class="hidden sm:block text-slate-700">|</div>
        <div class="flex items-center gap-1.5">
          <span class="text-cyan-400">STRUCTURE:</span>
          <span id="hud-model-name" class="text-slate-200 font-semibold">GEODESIC_CORE_V1</span>
        </div>
        <div class="hidden sm:block text-slate-700">|</div>
        <div class="flex items-center gap-1.5">
          <span class="text-cyan-400">NODES:</span>
          <span id="hud-node-count" class="text-slate-200 font-semibold">142 NODES</span>
        </div>
        <div class="hidden md:block text-slate-700">|</div>
        <div class="hidden md:flex items-center gap-1.5">
          <span class="text-cyan-400">CURSOR:</span>
          <span id="hud-mouse-coords" class="text-slate-200 font-semibold">X: 0000 | Y: 0000</span>
        </div>
      </div>
    </div>

    <!-- Downward Scroll Indicator -->
    <a href="#disciplines" class="absolute bottom-6 left-1/2 -translate-x-1/2 z-20 text-cyan-400/70 hover:text-cyan-300 animate-bounce transition-colors" title="Scroll to blueprints">
      <i data-lucide="chevron-down" class="w-6 h-6"></i>
    </a>
  </section>


  <!-- ========================================================================
       SECTION 2: TRIBUTE SECTION ("WHY ENGINEERS MATTER")
       ======================================================================== -->
  <section id="disciplines" class="relative py-24 px-4 md:px-8 border-t border-cyan-500/20 bg-navy-900/60">
    <div class="max-w-7xl mx-auto">
      
      <!-- Section Header -->
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 pb-6 border-b border-cyan-500/20">
        <div>
          <div class="flex items-center gap-2 font-mono text-xs text-cyan-400 tracking-wider mb-2">
            <span>SEC_02 // SYSTEM_PILLARS</span>
            <span class="text-slate-600">•</span>
            <span class="px-1.5 py-0.5 border border-cyan-500/40 text-[10px]">TOLERANCE: 0.001mm</span>
          </div>
          <h2 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-100 tracking-tight">
            Why Engineers Matter: <span class="bg-gradient-to-r from-cyan-300 to-laser-400 bg-clip-text text-transparent">The Four Pillars</span>
          </h2>
        </div>
        <p class="font-mono text-xs text-slate-400 max-w-md mt-4 md:mt-0 leading-relaxed">
          Hover over schematics to reveal engineering blueprints, formulas, and structural tolerances.
        </p>
      </div>

      <!-- 4 Glassmorphic Cards Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        
        <!-- Card 1: Infrastructure & Civil -->
        <div class="glass-card glass-card-tilt rounded-lg p-6 sm:p-8 relative overflow-hidden group cursor-pointer" data-schematic="infrastructure">
          <div class="sheen-overlay"></div>

          <!-- Card Header & Badge -->
          <div class="flex items-start justify-between mb-6">
            <div class="w-12 h-12 rounded bg-navy-950 border border-cyan-500/40 flex items-center justify-center text-cyan-300 group-hover:border-cyan-300 group-hover:shadow-[0_0_15px_rgba(100,255,218,0.4)] transition-all">
              <i data-lucide="building-2" class="w-6 h-6"></i>
            </div>
            <span class="font-mono text-[11px] px-2 py-1 rounded bg-navy-950 border border-cyan-500/30 text-cyan-400">
              DISCIPLINE_01 // CIVIL
            </span>
          </div>

          <!-- Card Content -->
          <h3 class="text-xl sm:text-2xl font-bold text-slate-100 mb-2 group-hover:text-cyan-300 transition-colors">
            Infrastructure & Structural
          </h3>
          <p class="text-sm text-slate-300 leading-relaxed mb-6">
            Constructing earthquake-resistant skyscrapers, mega-dams, high-speed rail viaducts, and ocean-spanning bridges that physically connect civilisations.
          </p>

          <!-- Metric Tags -->
          <div class="grid grid-cols-2 gap-3 font-mono text-xs text-slate-400 mb-6">
            <div class="p-2 bg-navy-950/60 rounded border border-cyan-500/10">
              <span class="text-slate-500 block text-[10px]">SEISMIC RATING</span>
              <span class="text-cyan-300 font-semibold">9.0+ MAGNITUDE</span>
            </div>
            <div class="p-2 bg-navy-950/60 rounded border border-cyan-500/10">
              <span class="text-slate-500 block text-[10px]">HYDRO HARNESS</span>
              <span class="text-laser-400 font-semibold">Q = C_d·A·√(2gh)</span>
            </div>
          </div>

          <!-- Blueprint Schematic Hover Overlay -->
          <div class="schematic-layer p-6 rounded-lg flex flex-col justify-between border border-cyan-400/80">
            <div>
              <div class="flex items-center justify-between border-b border-cyan-500/40 pb-2 mb-4">
                <span class="font-mono text-xs text-cyan-300 font-bold">SCHEMATIC: SUSPENSION TRUSS</span>
                <span class="font-mono text-[10px] text-slate-400">REV: 2026.09</span>
              </div>
              
              <!-- Blueprint SVG Schematic Diagram -->
              <div class="py-2 flex items-center justify-center">
                <svg class="w-full h-28 text-cyan-300 stroke-current fill-none stroke-[1.5]" viewBox="0 0 300 80">
                  <line x1="10" y1="70" x2="290" y2="70" stroke-dasharray="4,4" />
                  <line x1="70" y1="70" x2="70" y2="10" />
                  <line x1="230" y1="70" x2="230" y2="10" />
                  <path d="M10,40 Q70,10 150,45 Q230,10 290,40" />
                  <line x1="100" y1="35" x2="100" y2="60" />
                  <line x1="130" y1="42" x2="130" y2="60" />
                  <line x1="150" y1="45" x2="150" y2="60" />
                  <line x1="170" y1="42" x2="170" y2="60" />
                  <line x1="200" y1="35" x2="200" y2="60" />
                  <rect x="20" y="60" width="260" height="8" fill="rgba(100,255,218,0.1)" />
                  <line x1="30" y1="60" x2="45" y2="68" />
                  <line x1="45" y1="60" x2="30" y2="68" />
                  <line x1="140" y1="60" x2="160" y2="68" />
                  <line x1="160" y1="60" x2="140" y2="68" />
                </svg>
              </div>

              <div class="font-mono text-[11px] text-slate-300 mt-2 space-y-1">
                <div>• Catenary Cable Tension: <span class="text-cyan-300">T = H / cos(θ)</span></div>
                <div>• Resonant Frequency Damped: <span class="text-cyan-300">0.14 Hz Wind Aero</span></div>
              </div>
            </div>

            <button class="mt-4 w-full py-2 bg-cyan-400 text-navy-950 font-mono text-xs font-bold rounded hover:bg-cyan-300 transition-colors flex items-center justify-center gap-1.5" data-schematic="infrastructure">
              <span>INSPECT COMPLETE SCHEMATIC</span>
              <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>

        <!-- Card 2: Digital & Software Systems -->
        <div class="glass-card glass-card-tilt rounded-lg p-6 sm:p-8 relative overflow-hidden group cursor-pointer" data-schematic="software">
          <div class="sheen-overlay"></div>

          <!-- Card Header & Badge -->
          <div class="flex items-start justify-between mb-6">
            <div class="w-12 h-12 rounded bg-navy-950 border border-cyan-500/40 flex items-center justify-center text-cyan-300 group-hover:border-cyan-300 group-hover:shadow-[0_0_15px_rgba(100,255,218,0.4)] transition-all">
              <i data-lucide="cpu" class="w-6 h-6"></i>
            </div>
            <span class="font-mono text-[11px] px-2 py-1 rounded bg-navy-950 border border-cyan-500/30 text-cyan-400">
              DISCIPLINE_02 // SOFTWARE
            </span>
          </div>

          <!-- Card Content -->
          <h3 class="text-xl sm:text-2xl font-bold text-slate-100 mb-2 group-hover:text-cyan-300 transition-colors">
            Digital & Distributed Systems
          </h3>
          <p class="text-sm text-slate-300 leading-relaxed mb-6">
            Designing distributed consensus algorithms, planetary-scale cloud networks, neural network compilers, and cryptographic protocols with zero downtime.
          </p>

          <!-- Metric Tags -->
          <div class="grid grid-cols-2 gap-3 font-mono text-xs text-slate-400 mb-6">
            <div class="p-2 bg-navy-950/60 rounded border border-cyan-500/10">
              <span class="text-slate-500 block text-[10px]">GLOBAL AVAILABILITY</span>
              <span class="text-cyan-300 font-semibold">99.999% SLA</span>
            </div>
            <div class="p-2 bg-navy-950/60 rounded border border-cyan-500/10">
              <span class="text-slate-500 block text-[10px]">TIME COMPLEXITY</span>
              <span class="text-laser-400 font-semibold">O(log N) SEARCH</span>
            </div>
          </div>

          <!-- Blueprint Schematic Hover Overlay -->
          <div class="schematic-layer p-6 rounded-lg flex flex-col justify-between border border-cyan-400/80">
            <div>
              <div class="flex items-center justify-between border-b border-cyan-500/40 pb-2 mb-4">
                <span class="font-mono text-xs text-cyan-300 font-bold">SCHEMATIC: DISTRIBUTED RAFT MESH</span>
                <span class="font-mono text-[10px] text-slate-400">REV: 2026.09</span>
              </div>
              
              <!-- Blueprint SVG Distributed Cluster -->
              <div class="py-2 flex items-center justify-center">
                <svg class="w-full h-28 text-cyan-300 stroke-current fill-none stroke-[1.5]" viewBox="0 0 300 80">
                  <circle cx="50" cy="40" r="16" fill="rgba(100,255,218,0.1)" />
                  <circle cx="150" cy="20" r="18" fill="rgba(0,210,255,0.15)" stroke="#00d2ff" />
                  <circle cx="150" cy="65" r="14" fill="rgba(100,255,218,0.1)" />
                  <circle cx="250" cy="40" r="16" fill="rgba(100,255,218,0.1)" />
                  <line x1="66" y1="40" x2="132" y2="22" stroke-dasharray="3,3" />
                  <line x1="66" y1="40" x2="136" y2="65" stroke-dasharray="3,3" />
                  <line x1="168" y1="22" x2="234" y2="40" />
                  <line x1="164" y1="65" x2="234" y2="40" stroke-dasharray="3,3" />
                  <text x="50" y="43" font-size="8" fill="#64ffda" font-family="monospace" text-anchor="middle" stroke="none">FOLLOWER</text>
                  <text x="150" y="23" font-size="8" fill="#00d2ff" font-family="monospace" text-anchor="middle" stroke="none">LEADER</text>
                  <text x="150" y="68" font-size="8" fill="#64ffda" font-family="monospace" text-anchor="middle" stroke="none">CANDIDATE</text>
                  <text x="250" y="43" font-size="8" fill="#64ffda" font-family="monospace" text-anchor="middle" stroke="none">FOLLOWER</text>
                </svg>
              </div>

              <div class="font-mono text-[11px] text-slate-300 mt-2 space-y-1">
                <div>• Consensus Quorum: <span class="text-cyan-300">Q = ⌊N/2⌋ + 1 Nodes</span></div>
                <div>• Replication Heartbeat: <span class="text-cyan-300">&lt; 15ms Roundtrip</span></div>
              </div>
            </div>

            <button class="mt-4 w-full py-2 bg-cyan-400 text-navy-950 font-mono text-xs font-bold rounded hover:bg-cyan-300 transition-colors flex items-center justify-center gap-1.5" data-schematic="software">
              <span>INSPECT COMPLETE SCHEMATIC</span>
              <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>

        <!-- Card 3: Aerospace & Space Exploration -->
        <div class="glass-card glass-card-tilt rounded-lg p-6 sm:p-8 relative overflow-hidden group cursor-pointer" data-schematic="aerospace">
          <div class="sheen-overlay"></div>

          <!-- Card Header & Badge -->
          <div class="flex items-start justify-between mb-6">
            <div class="w-12 h-12 rounded bg-navy-950 border border-cyan-500/40 flex items-center justify-center text-cyan-300 group-hover:border-cyan-300 group-hover:shadow-[0_0_15px_rgba(100,255,218,0.4)] transition-all">
              <i data-lucide="rocket" class="w-6 h-6"></i>
            </div>
            <span class="font-mono text-[11px] px-2 py-1 rounded bg-navy-950 border border-cyan-500/30 text-cyan-400">
              DISCIPLINE_03 // AEROSPACE
            </span>
          </div>

          <!-- Card Content -->
          <h3 class="text-xl sm:text-2xl font-bold text-slate-100 mb-2 group-hover:text-cyan-300 transition-colors">
            Aerospace & Deep Space
          </h3>
          <p class="text-sm text-slate-300 leading-relaxed mb-6">
            Pioneering autonomous orbital rendezvous, reusable methalox rocket propulsion, lunar habitats, and interstellar robotic probes navigating outer space.
          </p>

          <!-- Metric Tags -->
          <div class="grid grid-cols-2 gap-3 font-mono text-xs text-slate-400 mb-6">
            <div class="p-2 bg-navy-950/60 rounded border border-cyan-500/10">
              <span class="text-slate-500 block text-[10px]">ESCAPE VELOCITY</span>
              <span class="text-cyan-300 font-semibold">11.186 KM/S</span>
            </div>
            <div class="p-2 bg-navy-950/60 rounded border border-cyan-500/10">
              <span class="text-slate-500 block text-[10px]">TSIOLKOVSKY LAW</span>
              <span class="text-laser-400 font-semibold">Δv = Isp·g₀·ln(m₀/mf)</span>
            </div>
          </div>

          <!-- Blueprint Schematic Hover Overlay -->
          <div class="schematic-layer p-6 rounded-lg flex flex-col justify-between border border-cyan-400/80">
            <div>
              <div class="flex items-center justify-between border-b border-cyan-500/40 pb-2 mb-4">
                <span class="font-mono text-xs text-cyan-300 font-bold">SCHEMATIC: HOHMANN ORBITAL TRANSFER</span>
                <span class="font-mono text-[10px] text-slate-400">REV: 2026.09</span>
              </div>
              
              <!-- Blueprint SVG Orbital Trajectory -->
              <div class="py-2 flex items-center justify-center">
                <svg class="w-full h-28 text-cyan-300 stroke-current fill-none stroke-[1.5]" viewBox="0 0 300 80">
                  <circle cx="150" cy="40" r="10" fill="rgba(0,210,255,0.3)" stroke="#00d2ff" />
                  <ellipse cx="150" cy="40" rx="45" ry="25" stroke-dasharray="2,2" />
                  <ellipse cx="150" cy="40" rx="120" ry="36" stroke-dasharray="2,2" />
                  <path d="M105,40 A82,34 0 0,1 270,40" stroke="#64ffda" stroke-width="2" />
                  <circle cx="105" cy="40" r="3" fill="#64ffda" />
                  <line x1="105" y1="40" x2="105" y2="28" stroke="#ffaa00" />
                  <circle cx="270" cy="40" r="3" fill="#64ffda" />
                  <line x1="270" y1="40" x2="270" y2="26" stroke="#ffaa00" />
                  <text x="105" y="24" font-size="7" fill="#ffaa00" font-family="monospace" text-anchor="middle" stroke="none">Δv1 BURN</text>
                  <text x="270" y="22" font-size="7" fill="#ffaa00" font-family="monospace" text-anchor="middle" stroke="none">Δv2 INSERTION</text>
                </svg>
              </div>

              <div class="font-mono text-[11px] text-slate-300 mt-2 space-y-1">
                <div>• Semi-major axis: <span class="text-cyan-300">a = (r₁ + r₂) / 2</span></div>
                <div>• Transfer Time: <span class="text-cyan-300">t_H = π · √(a³ / μ)</span></div>
              </div>
            </div>

            <button class="mt-4 w-full py-2 bg-cyan-400 text-navy-950 font-mono text-xs font-bold rounded hover:bg-cyan-300 transition-colors flex items-center justify-center gap-1.5" data-schematic="aerospace">
              <span>INSPECT COMPLETE SCHEMATIC</span>
              <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>

        <!-- Card 4: Healthcare & Biomedical Engineering -->
        <div class="glass-card glass-card-tilt rounded-lg p-6 sm:p-8 relative overflow-hidden group cursor-pointer" data-schematic="biomedical">
          <div class="sheen-overlay"></div>

          <!-- Card Header & Badge -->
          <div class="flex items-start justify-between mb-6">
            <div class="w-12 h-12 rounded bg-navy-950 border border-cyan-500/40 flex items-center justify-center text-cyan-300 group-hover:border-cyan-300 group-hover:shadow-[0_0_15px_rgba(100,255,218,0.4)] transition-all">
              <i data-lucide="activity" class="w-6 h-6"></i>
            </div>
            <span class="font-mono text-[11px] px-2 py-1 rounded bg-navy-950 border border-cyan-500/30 text-cyan-400">
              DISCIPLINE_04 // BIOMEDICAL
            </span>
          </div>

          <!-- Card Content -->
          <h3 class="text-xl sm:text-2xl font-bold text-slate-100 mb-2 group-hover:text-cyan-300 transition-colors">
            Healthcare & Bio-Cybernetics
          </h3>
          <p class="text-sm text-slate-300 leading-relaxed mb-6">
            Synthesizing myoelectric neural prosthetics, ultra-sensitive MRI quantum sensors, automated microfluidic dialysis, and surgical robotic systems.
          </p>

          <!-- Metric Tags -->
          <div class="grid grid-cols-2 gap-3 font-mono text-xs text-slate-400 mb-6">
            <div class="p-2 bg-navy-950/60 rounded border border-cyan-500/10">
              <span class="text-slate-500 block text-[10px]">NEURAL LATENCY</span>
              <span class="text-cyan-300 font-semibold">&lt; 85 MS RESPONSE</span>
            </div>
            <div class="p-2 bg-navy-950/60 rounded border border-cyan-500/10">
              <span class="text-slate-500 block text-[10px]">PRECISION CONTROL</span>
              <span class="text-laser-400 font-semibold">10 MICROMETERS</span>
            </div>
          </div>

          <!-- Blueprint Schematic Hover Overlay -->
          <div class="schematic-layer p-6 rounded-lg flex flex-col justify-between border border-cyan-400/80">
            <div>
              <div class="flex items-center justify-between border-b border-cyan-500/40 pb-2 mb-4">
                <span class="font-mono text-xs text-cyan-300 font-bold">SCHEMATIC: MYOELECTRIC BIONIC LINK</span>
                <span class="font-mono text-[10px] text-slate-400">REV: 2026.09</span>
              </div>
              
              <!-- Blueprint SVG Bionic Neural Schematic -->
              <div class="py-2 flex items-center justify-center">
                <svg class="w-full h-28 text-cyan-300 stroke-current fill-none stroke-[1.5]" viewBox="0 0 300 80">
                  <path d="M10,40 L40,40 L50,15 L60,65 L70,40 L100,40" stroke="#00d2ff" />
                  <rect x="110" y="22" width="60" height="36" fill="rgba(100,255,218,0.1)" />
                  <text x="140" y="43" font-size="8" fill="#64ffda" font-family="monospace" text-anchor="middle" stroke="none">NEURAL DSP</text>
                  <line x1="170" y1="40" x2="200" y2="40" />
                  <circle cx="215" cy="40" r="7" />
                  <line x1="222" y1="40" x2="245" y2="30" stroke-width="2" />
                  <circle cx="250" cy="28" r="5" />
                  <line x1="255" y1="26" x2="275" y2="20" stroke-width="2" />
                  <circle cx="278" cy="19" r="3" fill="#64ffda" />
                </svg>
              </div>

              <div class="font-mono text-[11px] text-slate-300 mt-2 space-y-1">
                <div>• EMG Signal Bandpass: <span class="text-cyan-300">20 Hz - 500 Hz</span></div>
                <div>• Closed-Loop Haptic: <span class="text-cyan-300">Force Sensor Micro-Grid</span></div>
              </div>
            </div>

            <button class="mt-4 w-full py-2 bg-cyan-400 text-navy-950 font-mono text-xs font-bold rounded hover:bg-cyan-300 transition-colors flex items-center justify-center gap-1.5" data-schematic="biomedical">
              <span>INSPECT COMPLETE SCHEMATIC</span>
              <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>

      </div>
    </div>
  </section>


  <!-- ========================================================================
       SECTION 3: UNSUNG HERO SPOTLIGHT (SIR M. VISVESVARAYA) & FACT ENGINE
       ======================================================================== -->
  <section id="unsung-hero" class="relative py-24 px-4 md:px-8 border-t border-cyan-500/20 bg-navy-950/80">
    <div class="max-w-7xl mx-auto">
      
      <!-- Section Header -->
      <div class="mb-16 pb-6 border-b border-cyan-500/20">
        <div class="flex items-center gap-2 font-mono text-xs text-cyan-400 tracking-wider mb-2">
          <span>SEC_03 // TRIBUTE_DOSSIER</span>
          <span class="text-slate-600">•</span>
          <span class="px-1.5 py-0.5 border border-cyan-500/40 text-[10px]">15 SEPTEMBER 1861 - 1962</span>
        </div>
        <h2 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-100 tracking-tight">
          Unsung Hero Spotlight: <span class="bg-gradient-to-r from-cyan-300 to-teal-300 bg-clip-text text-transparent">Sir M. Visvesvaraya</span>
        </h2>
        <p class="text-sm sm:text-base text-slate-400 mt-2 max-w-2xl font-mono">
          The Father of Indian Engineering whose birthday is celebrated nationwide as Engineers' Day.
        </p>
      </div>

      <!-- Two-Column Tribute Layout -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
        
        <!-- Left Column: Sir M. Visvesvaraya Blueprint Dossier Card (7 Cols) -->
        <div class="lg:col-span-7 glass-card rounded-lg p-6 sm:p-8 relative border border-cyan-500/30 flex flex-col justify-between">
          <div class="sheen-overlay"></div>

          <div>
            <!-- Technical File Header -->
            <div class="flex items-center justify-between font-mono text-xs text-slate-400 border-b border-cyan-500/20 pb-3 mb-6">
              <span class="text-cyan-300 font-bold">DOSSIER_ID: BHARAT_RATNA_1955</span>
              <span class="text-slate-500">CLASS: HISTORICAL ARCHITECT</span>
            </div>

            <div class="flex flex-col sm:flex-row gap-6 items-start mb-6">
              
              <!-- Blueprint Stylized Portrait / Badge -->
              <div class="relative w-28 h-28 sm:w-32 sm:h-32 flex-shrink-0 mx-auto sm:mx-0 rounded border-2 border-cyan-400/60 bg-navy-900 p-2 flex flex-col items-center justify-center text-center shadow-[0_0_20px_rgba(100,255,218,0.15)]">
                <div class="w-16 h-16 rounded-full border border-dashed border-cyan-400/50 flex items-center justify-center mb-1">
                  <i data-lucide="award" class="w-8 h-8 text-cyan-300"></i>
                </div>
                <div class="font-mono text-[9px] text-cyan-300 font-bold uppercase tracking-wider">SIR M.V.</div>
                <div class="font-mono text-[8px] text-slate-400">1861 – 1962</div>
              </div>

              <!-- Biographical & Technical Summary -->
              <div class="flex-1">
                <h3 class="text-2xl font-bold text-slate-100 mb-1">
                  Mokshagundam Visvesvaraya
                </h3>
                <div class="font-mono text-xs text-cyan-400 mb-3">
                  // Chief Engineer of Mysore & Hydraulic Pioneer
                </div>
                <p class="text-sm text-slate-300 leading-relaxed mb-4">
                  A visionary civil engineer and statesman who invented the patented <span class="text-cyan-300 font-semibold">Automatic Sluice Floodgate</span> system in 1903. He designed the landmark <span class="text-cyan-300 font-semibold">Krishna Raja Sagara Dam</span>, transformed regional flood control at Hyderabad, and mechanized the Bhadravati Iron & Steel Works.
                </p>
              </div>
            </div>

            <!-- Patent Diagram: Automatic Sluice Gate SVG Schematic -->
            <div class="bg-navy-950/80 rounded border border-cyan-500/20 p-4 mb-6">
              <div class="flex items-center justify-between font-mono text-[10px] text-slate-400 mb-2">
                <span class="text-cyan-300">PATENT SCHEMATIC: AUTOMATIC FLOODGATE (1903)</span>
                <span>KHADAKWASLA & KRS RESERVOIRS</span>
              </div>
              <svg class="w-full h-24 text-cyan-300 stroke-current fill-none stroke-[1.5]" viewBox="0 0 320 70">
                <polygon points="10,65 10,15 80,15 110,65" fill="rgba(100,255,218,0.05)" stroke="#64ffda" />
                <text x="45" y="45" font-size="8" fill="#94a3b8" font-family="monospace" stroke="none">DAM WALL</text>
                <line x1="10" y1="25" x2="80" y2="25" stroke="#00d2ff" stroke-width="2" stroke-dasharray="4,2" />
                <text x="15" y="22" font-size="7" fill="#00d2ff" font-family="monospace" stroke="none">H.F.L. WATER</text>
                <rect x="130" y="15" width="16" height="40" fill="rgba(0,210,255,0.2)" stroke="#00d2ff" />
                <circle cx="138" cy="15" r="3" fill="#64ffda" />
                <circle cx="190" cy="10" r="6" />
                <line x1="138" y1="15" x2="190" y2="4" />
                <line x1="196" y1="10" x2="220" y2="35" />
                <rect x="215" y="35" width="12" height="18" fill="rgba(100,255,218,0.2)" />
                <text x="232" y="46" font-size="7" fill="#64ffda" font-family="monospace" stroke="none">COUNTERWEIGHT</text>
                <path d="M95,50 C120,50 140,65 180,65" stroke="#00d2ff" stroke-width="2" stroke-dasharray="2,2" />
                <text x="175" y="60" font-size="7" fill="#00d2ff" font-family="monospace" stroke="none">DISCHARGE -&gt;</text>
              </svg>
            </div>

            <!-- Key Milestones Specs Grid -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 font-mono text-xs text-slate-300 mb-6">
              <div class="p-2.5 bg-navy-950/70 border border-cyan-500/15 rounded">
                <span class="text-slate-500 text-[10px] block">BORN</span>
                <span class="text-slate-200">15-SEP-1861</span>
              </div>
              <div class="p-2.5 bg-navy-950/70 border border-cyan-500/15 rounded">
                <span class="text-slate-500 text-[10px] block">PATENT</span>
                <span class="text-cyan-300">SLUICE GATES</span>
              </div>
              <div class="p-2.5 bg-navy-950/70 border border-cyan-500/15 rounded">
                <span class="text-slate-500 text-[10px] block">CIVIL HONOR</span>
                <span class="text-laser-400">BHARAT RATNA</span>
              </div>
              <div class="p-2.5 bg-navy-950/70 border border-cyan-500/15 rounded">
                <span class="text-slate-500 text-[10px] block">LIFESPAN</span>
                <span class="text-slate-200">101 YEARS</span>
              </div>
            </div>
          </div>

          <!-- Legendary Quote -->
          <div class="border-l-2 border-cyan-400 pl-4 py-1 italic text-xs sm:text-sm text-slate-400 font-sans">
            "Remember, your work may be only to sweep a railway crossing, but it is your duty to keep it so clean that no other crossing in the world is in any way superior."
          </div>
        </div>

        <!-- Right Column: Interactive Random Engineering Fact Generator (5 Cols) -->
        <div class="lg:col-span-5 glass-card rounded-lg p-6 sm:p-8 relative border border-cyan-500/30 flex flex-col justify-between">
          <div class="sheen-overlay"></div>

          <div>
            <!-- Terminal Header -->
            <div class="flex items-center justify-between font-mono text-xs text-slate-400 border-b border-cyan-500/20 pb-3 mb-6">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-rose-500 inline-block"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-amber-500 inline-block"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block"></span>
                <span class="text-slate-300 ml-1">fact_engine.sh</span>
              </div>
              <span class="text-cyan-300 font-mono text-[10px]">VER: 4.2.0</span>
            </div>

            <!-- Terminal Output Box -->
            <div id="fact-display-card" class="bg-navy-950 rounded border border-cyan-500/30 p-5 mb-6 relative">
              
              <!-- Badges -->
              <div class="flex items-center justify-between mb-4">
                <span id="fact-category" class="font-mono text-[10px] px-2 py-0.5 rounded bg-cyan-950 border border-cyan-500/40 text-cyan-300 uppercase tracking-widest font-bold">
                  HISTORICAL PIONEER
                </span>
                <span id="fact-discipline" class="font-mono text-[10px] text-slate-400">
                  // Civil &amp; Hydraulic
                </span>
              </div>

              <!-- Fact Title (Unscrambles dynamically) -->
              <h4 id="fact-title" class="font-mono text-base sm:text-lg font-bold text-slate-100 mb-3 min-h-[2rem]">
                Automatic Sluice Floodgates (1903)
              </h4>

              <!-- Fact Text Body (Unscrambles dynamically) -->
              <p id="fact-text" class="font-mono text-xs sm:text-sm text-slate-300 leading-relaxed min-h-[5.5rem]">
                Sir M. Visvesvaraya patented automatic weir water floodgates in 1903 at Khadakwasla Dam. The counterweight design increased reservoir storage without compromising dam integrity during severe floods, later implemented across India.
              </p>

              <!-- Technical Spec Metric Tag -->
              <div class="mt-4 pt-3 border-t border-cyan-500/20 flex items-center justify-between font-mono text-[11px]">
                <span class="text-slate-500">SCHEMATIC LOG:</span>
                <span id="fact-metric" class="text-cyan-300 font-bold">PATENT: NO. 1903-IND</span>
              </div>
            </div>
          </div>

          <!-- Actions / Buttons -->
          <div>
            <div class="flex flex-col sm:flex-row gap-3">
              <!-- Generate Button -->
              <button id="btn-generate-fact" class="flex-1 py-3 px-4 rounded bg-cyan-400 text-navy-950 font-mono text-xs font-bold hover:bg-cyan-300 hover:shadow-[0_0_20px_rgba(100,255,218,0.4)] transition-all flex items-center justify-center gap-2">
                <i data-lucide="refresh-cw" class="w-4 h-4"></i>
                <span>GENERATE_ENGINEERING_FACT</span>
              </button>

              <!-- Copy Button -->
              <button id="btn-copy-fact" class="py-3 px-4 rounded bg-navy-950 border border-cyan-500/40 text-cyan-300 font-mono text-xs hover:border-cyan-300 hover:bg-cyan-950/40 transition-all flex items-center justify-center gap-2" title="Copy fact text">
                <i data-lucide="copy" class="w-4 h-4"></i>
                <span class="sm:hidden">COPY</span>
              </button>
            </div>

            <!-- Toast Notification -->
            <div id="fact-toast" class="opacity-0 translate-y-2 transition-all duration-300 font-mono text-[11px] text-cyan-300 text-center mt-3">
              COPIED SCHEMATIC FACT TO CLIPBOARD
            </div>
          </div>

        </div>
      </div>
    </div>
  </section>


  <!-- ========================================================================
       SECTION 4: INTERACTIVE MINI-GAME ("DEBUG & DESTROY: THE PRODUCTION PATCH")
       ======================================================================== -->
  <section id="game-section" class="relative py-24 px-4 md:px-8 border-t border-cyan-500/20 bg-navy-900/90">
    <div class="max-w-6xl mx-auto">
      
      <!-- Section Header -->
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 pb-4 border-b border-cyan-500/20">
        <div>
          <div class="flex items-center gap-2 font-mono text-xs text-cyan-400 tracking-wider mb-2">
            <span>SEC_04 // ARCADE_DEFENSE</span>
            <span class="text-slate-600">•</span>
            <span class="px-1.5 py-0.5 border border-cyan-500/40 text-[10px]">FRIDAY 17:00 DEPLOYMENT</span>
          </div>
          <h2 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-100 tracking-tight">
            Debug &amp; Destroy: <span class="bg-gradient-to-r from-rose-400 via-amber-300 to-cyan-300 bg-clip-text text-transparent">The Production Patch</span>
          </h2>
        </div>
        <p class="font-mono text-xs text-slate-400 max-w-md mt-4 md:mt-0 leading-relaxed">
          Click or tap to fire laser hotfixes at crawling bugs emerging from the CI/CD pipeline before they breach the production cluster!
        </p>
      </div>

      <!-- Retro Cyberpunk Arcade Cabinet Frame -->
      <div class="crt-frame rounded-lg border-2 border-cyan-500/40 bg-navy-950 overflow-hidden shadow-[0_0_40px_rgba(10,25,47,0.9)]">
        
        <!-- Game HUD Status Bar -->
        <div class="bg-navy-950/95 border-b border-cyan-500/30 px-4 py-3 flex flex-wrap items-center justify-between gap-3 font-mono text-xs">
          
          <!-- Wave & Server Health -->
          <div class="flex items-center gap-4">
            <div class="flex items-center gap-1.5">
              <span class="text-slate-500">STAGE:</span>
              <span id="game-wave" class="text-cyan-300 font-bold">WAVE 1/3</span>
            </div>
            <div class="flex items-center gap-1.5">
              <span class="text-slate-500">SERVER SLA:</span>
              <span id="game-health" class="text-emerald-400 font-bold">100%</span>
            </div>
          </div>

          <!-- Score & Remaining -->
          <div class="flex items-center gap-4">
            <div class="flex items-center gap-1.5">
              <span class="text-slate-500">SCORE:</span>
              <span id="game-score" class="text-laser-400 font-bold">00000</span>
            </div>
            <div class="flex items-center gap-1.5">
              <span class="text-slate-500">BUGS:</span>
              <span id="game-bugs-left" class="text-slate-300 font-semibold">14 ACTIVE</span>
            </div>
          </div>

          <!-- Control Buttons -->
          <div class="flex items-center gap-2">
            <button id="game-btn-pause" onclick="if (window.debugGame) window.debugGame.togglePause();" class="px-2.5 py-1 rounded bg-navy-900 border border-cyan-500/30 text-slate-300 hover:text-cyan-300 hover:border-cyan-400 transition-colors">
              PAUSE [⏸]
            </button>
            <button id="game-btn-restart" onclick="if (window.debugGame) window.debugGame.resetGame();" class="px-2.5 py-1 rounded bg-navy-900 border border-cyan-500/30 text-slate-300 hover:text-cyan-300 hover:border-cyan-400 transition-colors">
              RESTART [↺]
            </button>
          </div>
        </div>

        <!-- 2D Canvas Container -->
        <div class="relative w-full h-[460px] sm:h-[500px] overflow-hidden">
          
          <canvas id="game-canvas" class="w-full h-full block"></canvas>

          <!-- Scanline overlay -->
          <div class="absolute inset-0 scanlines opacity-40 pointer-events-none"></div>

          <!-- Overlay Modal (Start / Victory / Defeat) -->
          <div id="game-overlay" style="display: flex;" class="absolute inset-0 bg-navy-950/85 backdrop-blur-md flex flex-col items-center justify-center p-6 text-center z-30 transition-all">
            <div class="max-w-md">
              <div class="inline-block p-3 rounded-full bg-cyan-950 border border-cyan-400/50 text-cyan-300 mb-4 shadow-[0_0_20px_rgba(100,255,218,0.3)]">
                <i data-lucide="shield-alert" class="w-8 h-8"></i>
              </div>
              <h3 id="game-overlay-title" class="text-2xl sm:text-3xl font-black font-mono text-cyan-300 text-glow-cyan mb-2">
                HOTFIX ON-CALL: MISSION CRITICAL
              </h3>
              <p id="game-overlay-subtitle" class="text-sm text-slate-300 mb-6 font-mono leading-relaxed">
                Rogue bugs are crawling from the CI/CD pipeline toward the production cluster! Click or tap to deploy precision hotfix patches.
              </p>

              <!-- Dynamic Stats Container -->
              <div id="game-overlay-stats" class="mb-6"></div>

              <!-- Start / Deploy Button -->
              <button id="game-btn-start" onclick="if (window.debugGame) window.debugGame.startGame();" class="w-full py-3.5 px-6 rounded bg-cyan-400 text-navy-950 font-mono text-sm font-bold tracking-wider hover:bg-cyan-300 hover:shadow-[0_0_25px_rgba(100,255,218,0.6)] transition-all">
                INITIATE DEPLOYMENT [▶]
              </button>
            </div>
          </div>

        </div>

        <!-- Bug Legend Footer -->
        <div class="bg-navy-950/95 border-t border-cyan-500/20 px-4 py-2.5 flex flex-wrap items-center justify-center sm:justify-between gap-4 font-mono text-[11px] text-slate-400">
          <div class="flex items-center gap-1.5">
            <span class="w-2.5 h-2.5 rounded-full bg-[#00d2ff]"></span>
            <span>NullPointerException (Swift)</span>
          </div>
          <div class="flex items-center gap-1.5">
            <span class="w-2.5 h-2.5 rounded-full bg-[#ff3366]"></span>
            <span>SyntaxError (Fast Swarm)</span>
          </div>
          <div class="flex items-center gap-1.5">
            <span class="w-2.5 h-2.5 rounded-full bg-[#c084fc]"></span>
            <span>MemoryLeak: OOM (3 HP)</span>
          </div>
          <div class="flex items-center gap-1.5">
            <span class="w-2.5 h-2.5 rounded-full bg-[#facc15]"></span>
            <span>RaceCondition (Glitch)</span>
          </div>
        </div>

      </div>
    </div>
  </section>


  <!-- ========================================================================
       FOOTER & ARCHITECTURAL BLUEPRINT METADATA
       ======================================================================== -->
  <footer class="relative border-t border-cyan-500/30 bg-navy-950 py-12 px-4 md:px-8 font-mono text-xs text-slate-400">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6">
      
      <!-- Revision Stamp -->
      <div class="flex items-center gap-3">
        <div class="blueprint-stamp px-3 py-1.5 rounded text-cyan-300 border-cyan-400/50">
          REV: 2026.09.15 // ENG_DAY_STABLE
        </div>
        <div>
          <div class="text-slate-300 font-bold">THE ARCHITECT’S BLUEPRINT</div>
          <div class="text-slate-500 text-[10px]">ENGINEERS' DAY EDITION // OPEN TRIBUTE</div>
        </div>
      </div>

      <!-- Homage Message -->
      <div class="text-center md:text-right max-w-md text-[11px] text-slate-400 leading-relaxed">
        "Celebrating the architects, programmers, designers, and engineers whose calculations bridge the impossible with reality."
      </div>

      <!-- Real-time HUD Coordinates & Back to Top -->
      <div class="flex items-center gap-4">
        <div id="global-coord-hud" class="hidden sm:block text-[10px] text-cyan-400/70">
          CRD: 0000x, 0000y | SYS.T: 0s
        </div>
        <a href="#hero" class="p-2 rounded border border-cyan-500/30 text-cyan-300 hover:border-cyan-300 hover:bg-cyan-950/50 transition-colors" title="Back to top">
          <i data-lucide="chevron-up" class="w-4 h-4"></i>
        </a>
      </div>

    </div>
  </footer>


  <!-- ========================================================================
       MODAL: FULL SCHEMATIC DEEP-DIVE INSPECTION
       ======================================================================== -->
  <div id="schematic-modal" class="fixed inset-0 bg-navy-950/80 backdrop-blur-md z-50 hidden items-center justify-center p-4">
    <div class="glass-card max-w-2xl w-full rounded-lg border border-cyan-400/60 p-6 sm:p-8 relative shadow-[0_0_40px_rgba(100,255,218,0.2)]">
      
      <!-- Close Button -->
      <button id="modal-close-btn" class="absolute top-4 right-4 p-2 text-slate-400 hover:text-cyan-300 transition-colors">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <!-- Modal Header -->
      <div class="flex items-center gap-2 font-mono text-xs text-cyan-400 mb-2">
        <span id="modal-spec-id">[ SPEC-SYS-0001 ]</span>
        <span class="text-slate-600">•</span>
        <span>BLUEPRINT SCHEMATIC REVEAL</span>
      </div>
      <h3 id="modal-title" class="text-2xl font-bold font-mono text-slate-100 mb-4">
        SCHEMATIC TITLE
      </h3>

      <!-- Modal Content Description -->
      <p id="modal-desc" class="text-sm text-slate-300 mb-4 leading-relaxed"></p>
      
      <!-- Technical Breakdown -->
      <div class="p-3 bg-navy-950/70 rounded border border-cyan-500/20 mb-6 font-mono text-xs text-slate-300 leading-relaxed" id="modal-breakdown">
      </div>

      <!-- Stats Grid -->
      <div id="modal-stats-grid" class="grid grid-cols-2 gap-3 mb-6"></div>

      <!-- Dismiss Button -->
      <button onclick="document.getElementById('schematic-modal').classList.add('hidden'); document.getElementById('schematic-modal').classList.remove('flex');" class="w-full py-2.5 bg-cyan-400 text-navy-950 font-mono text-xs font-bold rounded hover:bg-cyan-300 transition-colors">
        CLOSE SCHEMATIC [ESC]
      </button>

    </div>
  </div>


  <!-- ========================================================================
       SCRIPTS
       ======================================================================== -->
  <!-- Audio Engine -->
  <script src="js/audio.js"></script>
  <!-- Three.js 3D Hero Scene -->
  <script src="js/three-scene.js"></script>
  <!-- Engineering Facts Generator -->
  <script src="js/facts.js"></script>
  <!-- Mini-Game Engine -->
  <script src="js/game.js"></script>
  <!-- Main UI Controller -->
  <script src="js/main.js"></script>

  <script>
    // Initialize Lucide icons on DOM ready
    document.addEventListener('DOMContentLoaded', () => {
      lucide.createIcons();
    });
  </script>
</body>
</html>
"""

target_path = r"C:\Users\pathr\.gemini\antigravity\scratch\engineers-day-blueprint\index.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Successfully written {len(html_content)} bytes to {target_path}")
