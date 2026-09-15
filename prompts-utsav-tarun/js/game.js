/**
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

  pauseGame() {
    if (this.isRunning && !this.isPaused) {
      this.togglePause();
    }
  }

  resumeGame() {
    if (this.isRunning && this.isPaused) {
      this.togglePause();
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
