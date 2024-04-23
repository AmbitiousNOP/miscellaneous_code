document.addEventListener('DOMContentLoaded', function (){
let randomnumber = Math.floor(Math.random() * 100) + 1;

const guesses = document.querySelector(".guesses");
const lastResult = document.querySelector(".lastResult");
const lowOrHi = document.querySelector(".lowOrHi");

const guessSubmit = document.querySelector(".guessSubmit");
const guessField = document.querySelector(".guessField");

let guessCount = 1;
let resetButton;

function checkGuess() {
    const userGuess = Number(guessField.value);
    if (userGuess === randomnumber) {
        guesses.textContent = "Congratulations! You got it right!";
        setGameOver();
    } else if (guessCount === 10){
        guesses.textContent = "!!!GAME OVER!!! You have used up all your guesses!";
        setGameOver();
    } else {
        lastResult.textContent = "Wrong!";
        lastResult.style.backgroundColor = "red";
        if (userGuess > randomnumber) {
            lowOrHi.textContent = "Last guess was too high!";
        } else if (userGuess < randomnumber) {
            lowOrHi.textContent = "Last guess was too low!";
        }
    }
    guessCount++;
    guessField.value = "";
    guessField.focus();
}

guessSubmit.addEventListener("click", checkGuess)


function setGameOver(){
    guessField.disabled = true;
    guessSubmit.disabled = true;
    resetButton = document.createElement("button");
    resetButton.textContent = "Start new game";
    document.body.appendChild(resetButton);
    resetButton.addEventListener("click", resetGame);
}

function resetGame() {
    guessCount = 1;

    const resetParas = document.querySelectorAll(".resultParas p");
    for (const resetParas of resetParas) {
        resetParas.textContent = "";
    }

    resetButton.parentNode.removeChild(resetButton);

    guessField.disabled = false;
    guessSubmit.disabled = false;
    guessField.value = "";
    guessField.focus();

    lastResult.style.backgroundColor = "white";

    randomnumber = Math.floor(Math.random() * 100) + 1;
}
});