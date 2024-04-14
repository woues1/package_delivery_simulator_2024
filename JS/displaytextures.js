let textureData;
const library ={
    background: "main_menu_background_corr.png",
}

// Fetch noutaa json datan, functio struktuuri ja .then käyttö on sen takia koska json data lataa hitaamin kun itse niiden piirtäminen näytölle

fetch('../Assets/textures.json')
  .then(response => response.json())
  .then(data => {
  textureData = data;

  // Tässä yhdistyy html id ja kuva json tiedostosta esim. <div id="header" class="texture"></div>
  // Nämä funktio kutsut on täällä juuri json datan hitaan lataamisen takia

  displayTexture('background', 'main_menu_background_corr.png');
  displayTexture('header', 'header_corr.png');
});


// Funktio joka piirtää näytölle kuvan, ja lisää niihin koon ja position.

function displayTexture(elementId, textureName){
    const texture = textureData.frames.find(texture => texture.filename === textureName);
    const style = document.getElementById(elementId).style;
    style.width = texture.frame.w + 'px';
    style.height = texture.frame.h + 'px';
    style.backgroundPosition = `-${texture.frame.x}px -${texture.frame.y}px`;
}

// library["background"]
// Tällä hetkellä skripti on aika ei käyttäjäystävällinen, voidaan muokata käyttämällä arrayta.