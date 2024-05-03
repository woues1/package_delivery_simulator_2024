fetch('../Assets/textures.json')
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
