import {
  update as updateSnake,
  draw as drawSnake,
  SNAKE_SPEED,
  getSnakeHead,
  snakeIntersection,
} from "./snake.js";

import { update as updateFood, draw as drawFood } from "./food.js";
import { outsideGrid } from "./grid.js";

let lastRenderTime = 0;
let gameOver = false;
const gameBoard = document.getElementById("game-board");

function main(currentTime) {
  if (gameOver) {
    return alert("You lose!");
  }

  window.requestAnimationFrame(main);

  // divide by 1000 to convert millis to secs
  // this is the lag between each frame call in secs
  const secondsSinceLastRender = (currentTime - lastRenderTime) / 1000;

  // if the time between the last render
  if (secondsSinceLastRender < 1 / SNAKE_SPEED) return;

  lastRenderTime = currentTime;

  //for logic (eg for apple score, snake length edit etc)
  update();

  //for rendering (drawing on screen)
  draw();
}

window.requestAnimationFrame(main);

function update() {
  updateSnake(); //from snake.js
  updateFood(); //from food.js
  checkDeath();
}

function draw() {
  gameBoard.innerHTML = ""; //remove previous view of gameboard
  drawSnake(gameBoard); //from snake.js
  drawFood(gameBoard); //from food.js
}

function checkDeath() {
  gameOver = outsideGrid(getSnakeHead()) || snakeIntersection();
}
