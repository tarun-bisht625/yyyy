import os

readme_content = """# 📐 The Architect’s Blueprint: Celebrating the Minds That Build Tomorrow

> **Engineers' Day Special Edition Frontend Showcase**  
> A dark-mode cyberpunk & blueprint-hybrid 3D interactive web experience celebrating the visionaries who shape the physical and digital world.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Three.js](https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=three.js&logoColor=white)

---

## 🌟 Key Features

### 1. 🌐 Interactive 3D Hero Section
- **Three.js 3D Wireframe Scene**: Procedurally rendered rotating 3D architectural structures that react with smooth parallax to cursor coordinates.
- **3 Dynamic Architectural Modes**: Switch seamlessly between **Geodesic Core**, **Hypercube (Tesseract)**, and **Space Frame Truss**.
- **Dynamic Typewriter Subtitle**: Real-time tribute cycling with mechanical typewriter sound synthesis.
- **HUD Telemetry Bar**: Live FPS monitor, active vertex node counter, and coordinates tracker.

### 2. 🏛️ The Four Pillars of Engineering
- **Glassmorphic 3D Tilt Cards**: Custom perspective calculations with dynamic specular light reflection sheen.
- **Hover Blueprint Reveal**: Interactive hover triggers isometric vector schematics, dimensional tolerances, and engineering formulas ($T = H/\\cos\\theta$, $O(\\log N)$, $\\Delta v = I_{sp} g_0 \\ln(m_0/m_f)$).
- **Disciplines Covered**:
  - *Infrastructure & Structural* (Civil & Hydraulic)
  - *Digital & Distributed Systems* (Software & Cloud)
  - *Aerospace & Deep Space* (Propulsion & Telemetry)
  - *Healthcare & Bio-Cybernetics* (Bionic & Neural Interfaces)

### 3. 🎖️ Unsung Hero Spotlight: Sir M. Visvesvaraya
- Tribute dossier commemorating the Father of Indian Engineering on his birthday (September 15).
- Technical patent schematic of his **Automatic Sluice Floodgates (1903)** and the Krishna Raja Sagara Dam.
- **Terminal Fact Generator (`fact_engine.sh`)**: Interactive cyberpunk cipher unscrambling animation displaying 15+ curated engineering milestones with one-click clipboard copy.

### 4. 👾 Retro Mini-Game: "Debug & Destroy: The Production Patch"
- Friday 17:00 On-Call Deployment Defense on an HTML5 2D Canvas!
- Defend the production server cluster against crawling bugs:
  - `NullPointerException` (Swift, zig-zagging)
  - `SyntaxError` (Fast swarm)
  - `MemoryLeak: OOM` (Heavy armored crawler)
  - `RaceCondition` (Glitching phase-teleporter)
- Tactical targeting crosshair, laser hotfix blasts, binary code particle explosions, combo streak multipliers, and wave victory celebration!

### 5. 🔊 Procedural Web Audio Engine
- Synthesizes all sound effects mathematically in real-time via the browser's Web Audio API:
  - Laser zap sweeps
  - Low-pass filtered noise bursts
  - Cipher glitch chirps
  - Wave victory chord fanfare
- Fully controllable with the header **AUDIO: ON/OFF** toggle (zero external audio file dependencies).

---

## 🚀 Quick Start & How to Run Locally

### Option 1: Direct Browser Launch
Simply double-click `index.html` or open it with any web browser (Chrome, Edge, Firefox, Safari).

### Option 2: Using the One-Click Launcher
Double-click `run.bat` in the project folder to automatically start a local server and launch the site at `http://localhost:8080`.

### Option 3: Terminal / CLI
```bash
# Clone the repository
git clone https://github.com/tarun-bisht625/PROMPTUTSAV-TARUN-.git

# Navigate into directory
cd PROMPTUTSAV-TARUN-

# Start a local static server
python -m http.server 8080
```
Open **[http://localhost:8080](http://localhost:8080)** in your browser.

---

## 📂 Project Structure

```
PROMPTUTSAV-TARUN-/
├── index.html              # Main application with semantic layout & HUD
├── css/
│   └── styles.css          # Blueprint grids, scanlines, glow & glassmorphism
├── js/
│   ├── audio.js            # Procedural Web Audio API sound synthesizer
│   ├── three-scene.js      # Three.js 3D interactive hero background
│   ├── facts.js            # Engineering fact generator & cipher engine
│   ├── game.js             # "Debug & Destroy" canvas arcade mini-game
│   └── main.js             # Typewriter, 3D tilt, HUD coordinates & controls
├── run.bat                 # Windows one-click local server launcher
└── README.md               # Project documentation
```

---

## 📄 License & Attribution
Created for **Engineers' Day** — *"The Architect’s Blueprint: Celebrating the Minds That Build Tomorrow."*
"""

gitignore_content = """.DS_Store
Thumbs.db
*.log
"""

target_dir = r"C:\Users\pathr\OneDrive\Desktop\Engineers-Day-Blueprint"
with open(os.path.join(target_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)

with open(os.path.join(target_dir, ".gitignore"), "w", encoding="utf-8") as f:
    f.write(gitignore_content)

print("Created README.md and .gitignore in", target_dir)
