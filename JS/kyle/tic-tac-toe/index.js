const x_class = 'x'
const o_class = 'o'

const winning_comb = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

const cells = document.querySelectorAll('[data-cell]')
const board = document.getElementById('board')
const winningMsgText = document.querySelector('[data-winning-msg-text]')
const winningMsg = document.querySelector('.winning-msg')
let circleTurn
const restart = document.querySelector('#restartButton')

startGame()

restartButton.addEventListener('click', startGame)


function startGame() {
    circleTurn = false
    cells.forEach(cell => {
        cell.classList.remove(x_class)
        cell.classList.remove(o_class)
        cell.removeEventListener('click', handleClick)
        cell.addEventListener('click', handleClick, { once: true })
    })
    setboardHoverclass()
    winningMsg.classList.remove('show')    
}


function handleClick(e) {
    const cell = e.target
    const currentClass = circleTurn ? o_class : x_class
    placeMark(cell, currentClass)
    if (checkWin(currentClass)) {
        endGame(false)
    } else if (isDraw()) {
        endGame(true)
    } else {
        switchTurn()
        setboardHoverclass()
    }

}

function endGame(draw) {
    if (draw) {
        winningMsgText.innerHTML = 'Draw!!'
    } else {
        winningMsgText.innerHTML = `${ circleTurn ? "O" : "X" } Wins!!`
    }
    winningMsg.classList.add('show')
}

function isDraw() {
    return [...cells].every(cell => {
        return cell.classList.contains(x_class) || cell.classList.contains(o_class)
    })
}

function placeMark(cell, currentClass) {
    cell.classList.add(currentClass)

}

function switchTurn() {
    circleTurn = !circleTurn
}

function setboardHoverclass() {
    board.classList.remove(x_class)
    board.classList.remove(o_class)
    if (circleTurn) {
        board.classList.add(o_class)
    } else {
        board.classList.add(x_class)
    }
}

function checkWin(currentClass) {
    return winning_comb.some(combination => {
        return combination.every(index => {
            return cells[index].classList.contains(currentClass)
        })
    })
}