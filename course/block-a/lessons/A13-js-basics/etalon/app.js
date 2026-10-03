const MAX_LIVES = 3;
let score = 0;
let lives = MAX_LIVES;

function addScore(n) {
  score += n;
  console.log("score", score);
}

function takeHit() {
  lives -= 1;
  console.log("lives", lives);
}

addScore(10);
addScore(5);
takeHit();
