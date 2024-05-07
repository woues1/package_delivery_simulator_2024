const right = document.getElementById('right')
const left = document.getElementById('left')
const yrita = document.getElementById('yrita')

let randomNumber = 0
let x = 0
let y = 0
let z = 0
let lockpick = false
let userid = 1

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
    if (x + 5 <= 90) {
        x = 90
    } else {
        x += 5
    }
    document.getElementById('number').innerText = x
})

left.addEventListener('click', function() {
    if (x - 5 <= -90) {
        x = -90
    } else {
        x -= 5
    }
    document.getElementById('number').innerText = x
})

yrita.addEventListener('click', function() {
    fetch('http://127.0.0.1:3000/value')
        .then(response => response.json())
        .then(data => {
            lockpick = data.value
        })
    if (lockpick == true) {
        z = 15
    } else {
        z = 5
    }
    if (x <= randomNumber + z && x >= randomNumber - z) {
        document.getElementById('result').innerText = 'Onnistuit'
        sendResult(true)
    } else if (x < randomNumber - z || x > randomNumber + z) {
        y++
        if (x < randomNumber) {
            document.getElementById('result').innerText = 'Epaonnistuit yrita uudelleen, "kaanna enemman oikealle"'
        } else if (x > randomNumber) {
            document.getElementById('result').innerText = 'Epaonnistuit yrita uudelleen, "kaanna enemman vasemmalle"'
        }
    }
    if (y >= 5) {
        document.getElementById('result').innerText = 'Tiirikka rikkoutui'
        sendResult(false)
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
    fetch(`http://127.0.0.1:3000/update_points/${userid}`, {
    method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ success: success })

    })
}