let used = []

function randNumbers() {    
    num = Math.floor(Math.random() * 25)
    if (num in used) {
        
    } else {
        used.push(num)
        return num
    }
}

for (let i=0; i <=25; i++) {
    console.log(randNumbers(used))
}




const bingo = [
    [0,1,2,3,4],
    [6,7,8,9,10],
    [12,13,14,15,16],
    [18,19,20,21,22],
    [24,25,26,27,28],

    [0,6,12,18,24],
    [1,7,13,19,25],
    [2,8,14,20,26],
    [3,9,15,21,27],
    [4,10,16,22,28],

    [0,7,14,21,28],
    [4,9,14,19,24]
]



const cells = document.querySelectorAll(".cell")
const cell_pts = document.querySelectorAll('.cell.pts')
let bingo_pt = 5

cells.forEach((cell) => {
    cell.onclick = () => {
        cell.classList.add('x')
        CheckBingo()
    }
})

function CheckBingo() {
    let val =  bingo.some((combination) => {
        return combination.every((index) => {
          return cells[index].classList.contains('x')
        })
    })

    if (val === true){
        cell_pts[bingo_pt].classList.add('x')
        bingo_pt += 6
    }
}
