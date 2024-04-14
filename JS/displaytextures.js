let textureData;
const library ={
    background: "main_menu_background_corr.png",
}
fetch('../Assets/textures.json')
  .then(response => response.json())
  .then(data => {
    textureData = data;
    displayTexture('background', 'main_menu_background_corr.png');
    displayTexture('header', 'header_corr.png');
  });

function displayTexture(elementId, textureName){
    const texture = textureData.frames.find(texture => texture.filename === textureName);
    const style = document.getElementById(elementId).style;
    style.width = texture.frame.w + 'px';
    style.height = texture.frame.h + 'px';
    style.backgroundPosition = `-${texture.frame.x}px -${texture.frame.y}px`;
}

// library["background"]