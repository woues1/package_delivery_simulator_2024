const right = document.getElementById('right')
const left = document.getElementById('left')
const yrita = document.getElementById('yrita')

let randomNumber = 0
let x = 0
let y = 0
let lockpick = false

function lockpickingStart() {
    fetch('http://127.0.0.1:3000/random_number')
        .then(response => response.json())
        .then(data => {
            randomNumber = data.value
            document.getElementById('test').innerText = randomNumber
        })
    document.getElementById('test').innerText = randomNumber
}

right.addEventListener('click', function()  {
    x += 5
    document.getElementById('number').innerText = x
})

left.addEventListener('click', function() {
    x -= 5
    document.getElementById('number').innerText = x
})

yrita.addEventListener('click', function() {
    fetch('http://127.0.0.1:3000/value')
        .then(response => response.json())
        .then(data => {
            lockpick = data.value
        })
    if (lockpick == true) {
        if (x <= randomNumber + 15 && x >= randomNumber - 15) {
            document.getElementById('result').innerText = 'Onnistuit'
            sendResult(true)
        } else {
            y++
            document.getElementById('result').innerText = x < randomNumber ? 'Epaonnistuit yrita uudelleen, "kaanna enemman oikealle"' : 'Epaonnistuit yrita uudelleen, "kaanna enemman vasemmalle"'
        }
        if (y >= 5) {
            document.getElementById('result').innerText = 'Tiirikka rikkoutui'
            sendResult(false)
        }
    } else {
        if (x <= randomNumber + 5 && x >= randomNumber - 5) {
            document.getElementById('result').innerText = 'Onnistuit'
            sendResult(true)
        } else {
            y++
            document.getElementById('result').innerText = x < randomNumber ? 'Epaonnistuit yrita uudelleen, "kaanna enemman oikealle"' : 'Epaonnistuit yrita uudelleen, "kaanna enemman vasemmalle"'
        }
        if (y >= 5) {
            document.getElementById('result').innerText = 'Tiirikka rikkoutui'
            sendResult(false)
        }
    }
})

function sendResult(success) {
    fetch('http://127.0.0.1:3000/result', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ success: success })
    })
}