
function quote_api() {
    return fetch('http://api.quotable.io/random')
        .then(response => response.json())
        .then(data => data)
}

let data = ''
async function renderQuote() {

    const text = document.querySelector('#text')
    const text_input = document.querySelector('#text_input')

    data = await quote_api()

    const quote = data.content
    console.log(quote, data.author)
    text.innerHTML = ''
    const len = quote.length
    text_input.maxLength = len
    quote.split('').forEach(character => {
        const characterSpan = document.createElement('span')
        characterSpan.className = 'characterSpan'
        characterSpan.innerHTML = character
        text.appendChild(characterSpan)
    })
    text_input.value = null;
}



let time = 0
function startTimer() {
    if(document.querySelector('#text_input').disabled === false){
        time++
        document.querySelector('#time').innerHTML = `Time: ${time}s`
        document.querySelector('#try_again').className = 'btn btn-info'

    } else {
        document.querySelector('#time').innerHTML = 'Time: 0s'
    }
}
function stopTimer() {
    return time
}


document.addEventListener('DOMContentLoaded', function () {
    
    const try_again = document.querySelector('#try_again')
    const next = document.querySelector('#next')
    const accuracy = document.querySelector('#accuracy')
    const progress = document.querySelector('#progress')
    const total_time = document.querySelector('#total_time')
    const wpm = document.querySelector('#wpm')
    const hwpm = document.querySelector('#h_wpm')
    const alert = document.querySelector('#alert')
    const score = document.querySelector('#score')
    const hscore = document.querySelector('#h_score')

    let wpm_val = 0
    let accuracy_val = 0
    let h_wpm = 0
    let score_val = 0
    let h_score = 0


    let last_accuracy = 0
    let last_time = 0
    let last_score = 0
    let last_wpm = 0


    try_again.className = 'btn btn-info disabled'

    alert.className = 'alert alert-primary'
    alert.innerHTML = 'Click below to start the game!'

    renderQuote();

    //hwpm.innerHTML = `Highest WPM: ${h_wpm}` 
    //hscore.innerHTML = `Highest Score: ${h_score.toFixed(0)}`

    // Event for starttimer
    text_input.addEventListener('focus', () => {
        setInterval(startTimer, 1000)
    })


    // For accuracy
    let b_count = 0
    text_input.addEventListener('keydown', () => {

        if (event.keyCode === 8 || event.keyCode === 46) {
            b_count ++
            console.log("Backspace or del pressed")
        }
    })


    // Main input eventlistener
    text_input.addEventListener('input', () => {

        let correct = true
        const arrayQuote = text.querySelectorAll('span')
        const arrayValue = text_input.value.split('')
        const len = arrayQuote.length
        
        alert.innerHTML = null
        alert.className = null

        arrayQuote.forEach((characterSpan, index) => {
            const character = arrayValue[index]
            if (character == null) {
                characterSpan.style.color = 'black'
                correct = false
            }
            else if (character === characterSpan.innerHTML) {
                characterSpan.style.color = 'springgreen'
                
                percent = ((index + 1)/len ) * 100
                round_percent = Math.round(percent)
                progress.innerHTML = round_percent + '%'
                progress.style.width = percent + '%'
                

            } else {
                characterSpan.style.color = 'red'
                correct = false
            }
        })

        if (correct) {
            time = stopTimer()
            if(last_time !== 0){
                total_time.innerHTML = `Total time: ${time}s (Last try: ${last_time}s)`
            } else {
                total_time.innerHTML = `Total time: ${time}s`
            }

            text_input.value = null
            text_input.disabled = true
            text_input.focus = false       

            try_again.className = 'btn btn-info'

            arrayQuote.forEach((characterSpan, index) => {
                characterSpan.style.color = 'black'
            })

            // Author of the quote
            author = data.author
            alert.className = 'alert alert-success'
            alert.innerHTML = `You just typed a quote of ${author}!`


            //Calculation for accuracy
            accuracy_val = ((len - b_count) / len) * 100
            if (last_accuracy !== 0) {
                accuracy.innerHTML = `Accuracy: ${accuracy_val.toFixed(1)}% (Last try: ${last_accuracy.toFixed(1)}%)` 
            } else {
                accuracy.innerHTML = `Accuracy: ${accuracy_val.toFixed(1)}%`
            }

            //Calculation for wpm
            wpm_val = (len / 5)/(time/60)

            if(h_wpm < wpm_val){
                h_wpm = wpm_val
                hwpm.innerHTML = `Highest WPM: ${h_wpm.toFixed(0)}`
            }
            if (last_wpm !== 0) {
                wpm.innerHTML = `WPM: ${wpm_val.toFixed(0)} (Last try: ${last_wpm.toFixed(0)})`
            } else {
                wpm.innerHTML = `WPM: ${wpm_val.toFixed(0)}`
            }


            //Calculation for score
            score_val = wpm_val * (accuracy_val / 100)

            if (h_score < score_val) {
                h_score = score_val
                hscore.innerHTML = `Highest Score: ${h_score.toFixed(0)}`
            }
            if (last_score !== 0) {
                score.innerHTML = `Score: ${score_val.toFixed(0)} (Last try: ${last_score.toFixed(0)})`
            } else {
                score.innerHTML = `Score: ${score_val.toFixed(0)}`
            }
            
        }
    })


    // Event for next button
    next.onclick = () => {

        time = 0
        last_time = 0
        total_time.innerHTML = 'Total time: 0s'

        wpm_val = 0
        last_wpm = 0
        wpm.innerHTML = 'WPM: 0'

        percent = 0
        progress.innerHTML = percent
        progress.style.width = percent + '%'

        accuracy_val = 0
        last_accuracy = 0
        accuracy.innerHTML = `Accuracy: ${accuracy_val.toFixed(1)}%`

        score_val = 0
        last_score = 0
        score.innerHTML = `Score: ${score_val.toFixed(0)}`

        alert.className = 'alert alert-danger'
        alert.innerHTML = `Get ready`

        text_input.value = null
        text_input.disabled = false

        text_input.focus = false
        renderQuote()
    }


    // Event for try again button
    try_again.onclick = () => {

        last_time = time
        total_time.innerHTML = `Total time: 0s (Last try: ${time}s)`
        time = 0

        last_wpm = wpm_val
        wpm.innerHTML = `WPM: 0 (Last try: ${wpm_val.toFixed(0)})`

        last_score = score_val
        score.innerHTML = `Score: 0 (Last try: ${score_val.toFixed(0)})`


        const arrayQuote = text.querySelectorAll('span')
        arrayQuote.forEach((characterSpan, index) => {
            characterSpan.style.color = 'black'
        })

        progress.innerHTML = '0%'
        progress.style.width = '0%'

        last_accuracy = accuracy_val
        accuracy.innerHTML = `Accuracy: 0.0% (Last try: ${accuracy_val.toFixed(1)}%)` 

        text_input.value = null
        text_input.disabled = false

        text_input.focus = false
    }
})
