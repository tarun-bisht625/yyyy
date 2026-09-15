/**
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
    title: 'Apollo 11 & Margaret Hamilton\'s Priority Inversion',
    text: 'Three minutes before Apollo 11 touched down on the Moon, the radar overloaded the computer. Margaret Hamilton\'s asynchronous executive software preempted low-priority tasks to keep thrusters and guidance active, preventing an abort.',
    metric: 'UPTIME: 100% MISSION CRITICAL'
  },
  {
    category: 'CIVIL & STRUCTURAL',
    discipline: 'Structural Engineering',
    title: 'Burj Khalifa Vortex Shedding Architecture',
    text: 'The Burj Khalifa\'s Y-shaped stepping design was engineered to "confuse the wind." As wind spirals around the 828m tower, different elevations encounter different building shapes, preventing resonant wind vortices from snapping the tower.',
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
        } else if (targetText[i] === ' ' || targetText[i] === '\n') {
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

    const copyText = "Engineers' Day Blueprint [" + fact.discipline + "]:\n\"" + fact.title + "\" - " + fact.text + " (" + fact.metric + ")";

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
