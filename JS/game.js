'use strict';
let textureData
let mySession;

// lockpicking minigame
let randomNumber = 0
let x = 0
let y = 0
let z = 0
let lockpick = false
let userid;


// check if user already has a session, and redirect to game.
document.addEventListener('DOMContentLoaded', function() {
    if (sessionStorage.getItem('user_id')) {
        hideLoginElements();
        showMainMenu();
        player_info();
        current_missions();
    }
});


fetch('../Assets/login_textures.json')
    .then(response => response.json())
    .then(data => {
        textureData = data;

        // Tässä yhdistyy html id ja kuva json tiedostosta esim. <div id="header" class="texture"></div>
        // Nämä funktio kutsut on täällä juuri json datan hitaan lataamisen takia
        displayTexture('leaderboard_close', 'back_button.png');
        displayTexture('leaderboard', 'leaderboard_text_background.png');
        displayTexture('background', 'main_menu_background_corr.png');
        displayTexture('header', 'header_corr.png');
        displayTexture('log_in_button', 'login_button.png');
        displayTexture('new_game_button', 'new_game_button.png');
        displayTexture('leaderboard_button', 'leaderboard_button.png');
        displayTexture('pause_leaderboard_button', 'leaderboard_button.png');
        displayTexture('pause_leaderboard', 'leaderboard_text_background.png');
        displayTexture('pause_leaderboard_close', 'back_button.png');
    });


fetch('../Assets/main_menu_textures.json')
    .then(response => response.json())
    .then(data => {
        textureData = data;

        // Tässä yhdistyy html id ja kuva json tiedostosta esim. <div id="header" class="texture"></div>
        // Nämä funktio kutsut on täällä juuri json datan hitaan lataamisen takia
        displayTexture('mission3', 'mission_select_box.png');
        displayTexture('mission2', 'mission_select_box.png');
        displayTexture('mission1', 'mission_select_box.png');
        displayTexture('deliver_button', 'deliver_button.png');
        displayTexture('store_button', 'store_button.png');
        displayTexture('menu_button', 'menu_button.png');
        displayTexture('active_mission', 'active_mission_box.png');
        displayTexture('player_location', 'money_co2_text_box.png');
        displayTexture('player_info', 'location_text_box.png');
        displayTexture('main_menu_background', 'main_menu.png');
        displayTexture('pause_background', 'pause_menu_background.png');
        displayTexture('resume_button', 'back_button.png');
        displayTexture('new_run', 'new_game_button_blue.png');
        displayTexture('exit_button', 'exit_game_button_blue.png');
    });

fetch('../Assets/lockpick_textures.json')
    .then(response => response.json())
    .then(data => {
        textureData = data;

        // Tässä yhdistyy html id ja kuva json tiedostosta esim. <div id="header" class="texture"></div>
        // Nämä funktio kutsut on täällä juuri json datan hitaan lataamisen takia
        displayTexture('lockpicking_background', 'lockpicking_background.png');
        displayTexture('lock', 'lock.png');
    });


fetch('../Assets/shop_menu_textures.json')
    .then(response => response.json())
    .then(data => {
        textureData = data;

        // Tässä yhdistyy html id ja kuva json tiedostosta esim. <div id="header" class="texture"></div>
        // Nämä funktio kutsut on täällä juuri json datan hitaan lataamisen takia
        displayTexture('store_background', 'shop_menu_background.png');
        displayTexture('store_exit', 'back_button.png');
        displayTexture('item1', 'hybrid_car_store.png');
        displayTexture('item2', 'plant_trees_store.png');
        displayTexture('item3', 'rahakone_store.png');
        displayTexture('item4', 'lockpick_store.png');
        displayTexture('buy_item1_button', 'buy_button.png');
        displayTexture('buy_item2_button', 'buy_button.png');
        displayTexture('buy_item3_button', 'buy_button.png');
        displayTexture('buy_item4_button', 'buy_button.png');
        displayTexture('item1_info', 'hybrid_car_buy_screen.png');
        displayTexture('item2_info', 'plant_trees_buy_screen.png');
        displayTexture('item3_info', 'rahakone_buy_screen.png');
        displayTexture('item4_info', 'lockpick_buy_screen.png');
        displayTexture('close-info', 'close_info_button.png');
        displayTexture('buy-item-1', 'buy_button_var1.png');
        displayTexture('buy-item-2', 'buy_button_var1.png');
        displayTexture('buy-item-3', 'buy_button_var1.png');
        displayTexture('buy-item-4', 'buy_button_var1.png');
    });


// Funktio joka piirtää näytölle kuvan, ja lisää niihin koon ja position.
function displayTexture(elementId, textureName) {
    const texture = textureData.frames.find(texture => texture.filename === textureName);
    const style = document.getElementById(elementId).style;
    style.width = texture.frame.w + 'px';
    style.height = texture.frame.h + 'px';
    style.backgroundPosition = `-${texture.frame.x}px -${texture.frame.y}px`;
}


// Leaderboard data ja nappi.
$(document).ready(function () {
    $('#leaderboard_button').click(function () {
        $('#leaderboard').toggle();
        $('#leaderboard_close').toggle()
        fetch('http://127.0.0.1:3000/leaderboard_info')
            .then(response => response.json())
            .then(values => {
                const leaderboard = document.getElementById('leaderboard')
                leaderboard.innerHTML = '';
                values.forEach((value, index) => {
                    const placement = index + 1
                    const p = document.createElement('p')
                    p.innerHTML = `${placement}.${value[0]} || Score: ${value[1]}`
                    leaderboard.appendChild(p)
                })
            })
    });
    $('#leaderboard_close').click(function () {
        $('#leaderboard').hide();
        $('#leaderboard_close').hide()
    });
});


function selectMission(missionId, missionNumber) {
    var missionIndex = missionId.charAt(missionId.length - 1);

    $.ajax({
        url: 'http://127.0.0.1:3000/set_mission',
        type: 'GET',
        data: {mission_index: missionIndex},
        success: function (response) {
            active_mission(missionNumber);
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        }
    });
}

$('#mission1').on('click', function () {
    selectMission($(this).attr('id'), '1');
});

$('#mission2').on('click', function () {
    selectMission($(this).attr('id'), '2');
});

$('#mission3').on('click', function () {
    selectMission($(this).attr('id'), '3');
});


$('#deliver_button').on('click', function () {
        $.ajax({
        url: 'http://127.0.0.1:3000/complete_mission',
        type: 'GET',
        success: function (response) {
            player_info()
            current_missions()
            lockpickingStart()
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        }
    });
        $('#current_mission').empty()  // Tyhjentää aktiivisen missionin infon VE
})


function player_info() {
    fetch('http://127.0.0.1:3000/player_info')
        .then(response => response.json())
        .then(values => {
            const { location, country, co2_consumed, co2_budget, pisteet } = values;
            const points_info = $('#points');
            const co2_info = $('#co2_consumed');
            const location_info = $('#location');

            location_info.text(`${location}, ${country}`);
            co2_info.text(`${co2_consumed}/${co2_budget}`);
            points_info.text(`${pisteet}$`);

            if (parseInt(co2_consumed) >= parseInt(co2_budget)) {
                gameOverActions();
            }
        })
        .catch(error => {
            console.error('Error fetching player info:', error);
        });
}


function current_missions() {
    fetch('http://127.0.0.1:3000/get_missions_info')
        .then(response => response.json())
        .then(values => {
            let m1 = document.getElementById('m1')
            let m2 = document.getElementById('m2')
            let m3 = document.getElementById('m3')

            m1.innerHTML = `1. ${values['mission1'][1]} ${values['mission1'][2]}, ${values['mission1'][0]} Co2`;
            m2.innerHTML = `2. ${values['mission2'][1]} ${values['mission2'][2]}, ${values['mission2'][0]} Co2`;
            m3.innerHTML = `3. ${values['mission3'][1]} ${values['mission3'][2]}, ${values['mission3'][0]} Co2`;
        })
}


function active_mission(num){
    fetch('http://127.0.0.1:3000/get_missions_info')
    .then(response => response.json())
    .then(values => {
        let curr_mission = document.getElementById('current_mission')
        curr_mission.innerHTML = `${values['mission'+num][1]} ${values['mission'+num][2]},${values['mission'+num][0]} Co2`;
        })
}


function buyItem(ItemId) {
    var ItemIndex = ItemId.charAt(ItemId.length - 1);

    $.ajax({
        url: 'http://127.0.0.1:3000/buy_item',
        type: 'GET',
        data: {item_id: ItemIndex},
        success: function (response) {
            console.log(response);
            player_info();
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        }
    });
}

$('#buy-item-1').on('click', function () {
    buyItem($(this).attr('id'));
});

$('#buy-item-2').on('click', function () {
    buyItem($(this).attr('id'));
});

$('#buy-item-3').on('click', function () {
    buyItem($(this).attr('id'));
});

$('#buy-item-4').on('click', function () {
    buyItem($(this).attr('id'));
});


$('#login-form').submit(function(event) {
    event.preventDefault();
    const username = $('#username').val();
    const password = $('#password').val();

    const loginData = {
        username: username,
        password: password
    };

    $.ajax({
        url: 'http://127.0.0.1:3000/login',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(loginData),
        success: function(response) {
            hideLoginElements();
            showMainMenu();
            player_info();
            current_missions();
            sessionStorage.setItem('user_id', response['user_id'])
            },
        error: function(xhr, status, error) {
            const errorMessage = xhr.responseJSON ? xhr.responseJSON.error : 'An error occurred. Please try again later.';
            alert(errorMessage);
        }
    });
});


$('#new_game_button').click(function(event) {
    event.preventDefault();
    const username = $('#username').val();
    const password = $('#password').val();

    const newGameData = {
        username: username,
        password: password
    };

    $.ajax({
        url: 'http://127.0.0.1:3000/new_game',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(newGameData),
        success: function(response) {
            hideLoginElements();
            showMainMenu();
            player_info();
            current_missions();
        },
        error: function(xhr, status, error) {
            const errorMessage = xhr.responseJSON ? xhr.responseJSON.error : 'An error occurred. Please try again later.';
            alert(errorMessage);
        }
    });
});


// Login menu

function hideLoginElements() {
    $('.login-container').css("display", "none")

}

// Main menu

function showMainMenu() {
    $('.game-container').css("display", "block")

}

function hideMainMenu() {
    $('.game-container').css("display", "none")
}

// Minigame menu

function showMinigameMenu() {
    $('.lockpicking-game-container').css("display", "block")
}

function hideMinigameMenu() {
    $('.lockpicking-game-container').css("display", "none")
}

// Pause menu

function showPauseMenu() {
    $('.pause-menu-container').css("display", "block")

}


function hidePauseMenu() {
    $('.pause-menu-container').css("display", "none")

}


// Store menu

function showStoreMenu() {
    $('.store-container').css("display", "block")
}


function hideStoreMenu() {
    $('.store-container').css("display", "none")

}

function showLoginElements() {
    $('.login-container').css("display", "block")

}


function showItem1Info() {
    $('#item1_info').toggle()
}


function hideItem1Info() {
    $('#item1_info').hide()
}


function showItem2Info() {
    $('#item2_info').toggle()
}


function hideItem2Info() {
    $('#item2_info').hide()
}


function showItem3Info() {
    $('#item3_info').toggle()
}


function hideItem3Info() {
    $('#item3_info').hide()
}

function showItem4Info() {
    $('#item4_info').toggle()
}

function hideItem4Info() {
    $('#item4_info').hide()
}


function showCloseInfo() {
    $('#close-info').toggle()
}


function hideCloseInfo() {
    $('#close-info').hide()

}


function showBuyButton1() {
    $('#buy-item-1').toggle()
}


function hideBuyButton1() {
    $('#buy-item-1').hide()
}


function showBuyButton2() {
    $('#buy-item-2').toggle()
}


function hideBuyButton2() {
    $('#buy-item-2').hide()
}


function showBuyButton3() {
    $('#buy-item-3').toggle()
}


function hideBuyButton3() {
    $('#buy-item-3').hide()
}

function showBuyButton4() {
    $('#buy-item-4').toggle()
}

function hideBuyButton4() {
    $('#buy-item-4').hide()
}


// Pause menu

$('#menu_button').click(function () {
    hideMainMenu()
    showPauseMenu()
});


$('#resume_button').click(function () {
    showMainMenu()
    hidePauseMenu()
});

$('#new_run').click(function () {
    showMainMenu()
    hidePauseMenu()
    restartGame()
});

$('#exit_button').click(function () {
    exitGame()
    hideMainMenu()
    hidePauseMenu()
    location.reload()
    showLoginElements()
});


$(document).ready(function () {
    $('#pause_leaderboard_button').click(function () {
        $('#pause_leaderboard').toggle();
        $('#pause_leaderboard_close').toggle()
        fetch('http://127.0.0.1:3000/leaderboard_info')
            .then(response => response.json())
            .then(values => {
                const leaderboard = document.getElementById('pause_leaderboard')
                leaderboard.innerHTML = '';
                values.forEach((value, index) => {
                    const placement = index + 1
                    const p = document.createElement('p')
                    p.innerHTML = `${placement}.${value[0]} || Score: ${value[1]}`
                    leaderboard.appendChild(p)
                })
            })
    });
    $('#pause_leaderboard_close').click(function () {
        $('#pause_leaderboard').hide();
        $('#pause_leaderboard_close').hide()
    });
});

function restartGame() {
    fetch('http://127.0.0.1:3000/reset_game')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            player_info()
            current_missions()
        })
}

function exitGame() {
    sessionStorage.clear()
    fetch('http://http://127.0.0.1:3000/reset_game')
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
}

function updateLeaderboard() {
    fetch('http://127.0.0.1:3000/update_leaderboard')
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
}

function gameOverActions() {
    alert('Game over');
    updateLeaderboard();
    restartGame();
    exitGame();
    hideMainMenu();
    hidePauseMenu();
    location.reload();
    showLoginElements();
}


// Store menu

$('#store_button').click(function () {
    hideMainMenu()
    showStoreMenu()
});


$('#store_exit').click(function () {
    showMainMenu()
    hideStoreMenu()
});


$('#buy_item1_button').click(function () {
    showItem1Info()
    showBuyButton1()
    showCloseInfo()
});


$('#buy_item2_button').click(function () {
    showItem2Info()
    showBuyButton2()
    showCloseInfo()
});


$('#buy_item3_button').click(function () {
    showItem3Info()
    showBuyButton3()
    showCloseInfo()
});

$('#buy_item4_button').click(function () {
    showItem4Info()
    showBuyButton4()
    showCloseInfo()

});


$('#close-info').click(function () {
    hideCloseInfo()
    hideBuyButton1()
    hideBuyButton2()
    hideBuyButton3()
    hideBuyButton4()
    hideItem1Info()
    hideItem2Info()
    hideItem3Info()
    hideItem4Info()
});

$('#test_button').click(function () {
    showMinigameMenu()
    hideMainMenu()
});


const right = document.getElementById('right')
const left = document.getElementById('left')
const yrita = document.getElementById('yrita')


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
    if (x + 5 >= 90) {
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
        document.getElementById('lockpick_result').innerText = 'Onnistuit'
        sendResult(true)
    } else if (x < randomNumber - z || x > randomNumber + z) {
        y++
        if (x < randomNumber) {
            document.getElementById('lockpick_result').innerText = 'Epaonnistuit yrita uudelleen, "kaanna enemman oikealle"'
        } else if (x > randomNumber) {
            document.getElementById('lockpick_result').innerText = 'Epaonnistuit yrita uudelleen, "kaanna enemman vasemmalle"'
        }
    }
    if (y >= 500000000000000000) {
        document.getElementById('lockpick_result').innerText = 'Tiirikka rikkoutui'
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