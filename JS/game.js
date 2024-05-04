'use strict';
let textureData


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


$('#mission1').on('click', function () {
    var missionId = $(this).attr('id');
    var missionIndex = missionId.charAt(missionId.length - 1);

    $.ajax({
        url: 'http://127.0.0.1:3000/set_mission',
        type: 'GET',
        data: {mission_index: missionIndex},
        success: function (response) {
            console.log('Mission Completed')
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        }
    });
});


$('#mission2').on('click', function () {
    var missionId = $(this).attr('id');
    var missionIndex = missionId.charAt(missionId.length - 1);

    $.ajax({
        url: 'http://127.0.0.1:3000/set_mission',
        type: 'GET',
        data: {mission_index: missionIndex},
        success: function (response) {
            console.log('Mission Completed')
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        }
    });
});


$('#mission3').on('click', function () {
    var missionId = $(this).attr('id');
    var missionIndex = missionId.charAt(missionId.length - 1);
    $.ajax({
        url: 'http://127.0.0.1:3000/set_mission',
        type: 'GET',
        data: {mission_index: missionIndex},
        success: function (response) {
            console.log('Mission Completed')
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        }
    });
});

$('#deliver_button').on('click', function () {
        $.ajax({
        url: 'http://127.0.0.1:3000/complete_mission',
        type: 'GET',
        success: function (response) {
            console.log('Mission Completed')
            player_info()
            current_missions()
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        }
    });
})

function player_info() {
    fetch('http://127.0.0.1:3000/player_info')
        .then(response => response.json())
        .then(values => {
            let points_info = document.getElementById('points')
            let co2_info = document.getElementById('co2_consumed')
            let location_info = document.getElementById('location')


            location_info.innerHTML = `${values['location']}, ${values['country']}`;

            co2_info.innerHTML = `${values['co2_consumed']}/${values['co2_budget']}`;

            points_info.innerHTML = `${values['pisteet']}$`;

        })
}
function current_missions() {
    fetch('http://127.0.0.1:3000/get_missions_info')
        .then(response => response.json())
        .then(values => {
            let m1 = document.getElementById('m1')
            let m2 = document.getElementById('m2')
            let m3 = document.getElementById('m3')

            m1.innerHTML = `1. ${values['mission1'][0]} ${values['mission1'][1]} ${values['mission1'][2]}`;
            m2.innerHTML = `2. ${values['mission2'][0]} ${values['mission2'][1]} ${values['mission2'][2]}`;
            m3.innerHTML = `3. ${values['mission3'][0]} ${values['mission3'][1]} ${values['mission3'][2]}`;
        })
}


document.getElementById('login-form').addEventListener('submit', function (event) {

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const loginData = {
        username: username,
        password: password
    };
    console.log(loginData)

    fetch('http://127.0.0.1:3000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(loginData)
    })
        .then(response => {
            if (response.ok) {
                hideLoginElements();
                showMainMenu();
                player_info()
                current_missions()
            } else {
                return response.json().then(data => {
                    alert(data.error);
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again later.');
        });
    event.preventDefault();
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

function showBuyButton() {
    $('#buy').toggle()
}

function hideBuyButton() {
    $('#buy').hide()
}

function showCloseInfo() {
    $('#close-info').toggle()
}

function hideCloseInfo() {
    $('#close-info').hide()

}


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


// Pause menu

$('#menu_button').click(function () {
    hideMainMenu()
    showPauseMenu()
});

$('#resume_button').click(function () {
    showMainMenu()
    hidePauseMenu()
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
        displayTexture('buy_item1_button', 'buy_button.png');
        displayTexture('buy_item2_button', 'buy_button.png');
        displayTexture('buy_item3_button', 'buy_button.png');
        displayTexture('item1_info', 'hybrid_car_buy_screen.png');
        displayTexture('item2_info', 'plant_trees_buy_screen.png');
        displayTexture('item3_info', 'rahakone_buy_screen.png');
        displayTexture('buy', 'buy_button_var1.png');
        displayTexture('close-info', 'close_info_button.png');
    });


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
    showBuyButton()
    showCloseInfo()
});

$('#buy_item2_button').click(function () {
    showItem2Info()
    showBuyButton()
    showCloseInfo()
});

$('#buy_item3_button').click(function () {
    showItem3Info()
    showBuyButton()
    showCloseInfo()
});

$('#close-info').click(function () {
    hideCloseInfo()
    hideBuyButton()
    hideItem1Info()
    hideItem2Info()
    hideItem3Info()
});