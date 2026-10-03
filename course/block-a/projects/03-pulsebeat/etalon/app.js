const PADS = ["A", "S", "D", "F"];
const MAX_LIVES = 3;
const ROUND_SEC = 30;

const padsEl = document.querySelector("#pads");
const scoreEl = document.querySelector("#score");
const livesEl = document.querySelector("#lives");
const timeEl = document.querySelector("#time");
const statusEl = document.querySelector("#status");

let score = 0;
let lives = MAX_LIVES;
let timeLeft = ROUND_SEC;
let running = false;
let activePad = null;
let beatTimer = null;
let clockTimer = null;
let intervalMs = 900;

function renderPads() {
  padsEl.replaceChildren();
  PADS.forEach((name) => {
    const btn = document.createElement("button");
    btn.className = "pad";
    btn.type = "button";
    btn.textContent = name;
    btn.dataset.key = name;
    btn.addEventListener("click", () => tryHit(name));
    padsEl.append(btn);
  });
}

function paint() {
  scoreEl.textContent = String(score);
  livesEl.textContent = String(lives);
  timeEl.textContent = String(timeLeft);
}

function clearActive() {
  padsEl.querySelectorAll(".pad").forEach((el) => el.classList.remove("is-active", "is-hit"));
}

function pickPad() {
  if (!running) return;
  clearActive();
  const name = PADS[Math.floor(Math.random() * PADS.length)];
  activePad = name;
  const btn = padsEl.querySelector(`[data-key="${name}"]`);
  btn?.classList.add("is-active");
}

function tryHit(name) {
  if (!running) return;
  if (name === activePad) {
    score += 1;
    const btn = padsEl.querySelector(`[data-key="${name}"]`);
    btn?.classList.add("is-hit");
    activePad = null;
    if (score % 10 === 0) intervalMs = Math.max(400, intervalMs - 80);
  } else {
    takeHit();
  }
  paint();
}

function takeHit() {
  lives -= 1;
  if (lives <= 0) endGame("Жизни кончились");
}

function onKey(event) {
  const key = event.key.toUpperCase();
  if (event.code === "Space") {
    event.preventDefault();
    if (running) endGame("Пауза / стоп");
    return;
  }
  if (PADS.includes(key)) tryHit(key);
}

function startGame() {
  stopTimers();
  score = 0;
  lives = MAX_LIVES;
  timeLeft = ROUND_SEC;
  intervalMs = 900;
  running = true;
  statusEl.textContent = "Поехали";
  paint();
  pickPad();
  beatTimer = setInterval(pickPad, intervalMs);
  clockTimer = setInterval(() => {
    timeLeft -= 1;
    paint();
    if (timeLeft <= 0) endGame("Время");
  }, 1000);
}

function stopTimers() {
  clearInterval(beatTimer);
  clearInterval(clockTimer);
  beatTimer = null;
  clockTimer = null;
}

function endGame(reason) {
  running = false;
  stopTimers();
  clearActive();
  statusEl.textContent = `${reason}. Счёт ${score}`;
}

document.querySelector("#start").addEventListener("click", startGame);
document.querySelector("#restart").addEventListener("click", startGame);
window.addEventListener("keydown", onKey);
renderPads();
paint();
