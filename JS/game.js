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
  displayTexture('log_in_button', 'login_button.png' );
  displayTexture('new_game_button','new_game_button.png');
  displayTexture('leaderboard_button','leaderboard_button.png');

});


// Funktio joka piirtää näytölle kuvan, ja lisää niihin koon ja position.

function displayTexture(elementId, textureName){
    const texture = textureData.frames.find(texture => texture.filename === textureName);
    const style = document.getElementById(elementId).style;
    style.width = texture.frame.w + 'px';
    style.height = texture.frame.h + 'px';
    style.backgroundPosition = `-${texture.frame.x}px -${texture.frame.y}px`;
}


// Leaderboard data ja nappi.

$(document).ready(function(){
  $('#leaderboard_button').click(function(){
    $('#leaderboard').toggle();
    $('#leaderboard_close').toggle()
      fetch('http://127.0.0.1:3000/leaderboard_info')
      .then(response => response.json())
      .then(values => {
          const leaderboard = document.getElementById('leaderboard')
          leaderboard.innerHTML ='';
          values.forEach((value, index) =>{
              const placement = index + 1
              const p = document.createElement('p')
              p.innerHTML = `${placement}.${value[0]} || Score: ${value[1]}`
              leaderboard.appendChild(p)
          })
      })
  });

  $('#leaderboard_close').click(function(){
    $('#leaderboard').hide();
    $('#leaderboard_close').hide()
  });
});

document.getElementById('login-form').addEventListener('submit', function(event) {

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
            alert('Login successful');
            hideLoginElements();
            showMainMenu();
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

function hideLoginElements(){
    $('.login-container').css("display","none")

}

// Main menu

function showMainMenu(){
    $('.game-container').css("display","block")

}

function hideMainMenu(){
    $('.game-container').css("display","none")
}

// Pause menu

function showPauseMenu(){
    $('.pause-menu-container').css("display","block")

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

$(document).ready(function(){
  $('#menu_button').click(function(){
    hideMainMenu()
    showPauseMenu()
  });

  $('#pause_close').click(function(){
    showMainMenu()
  });
});