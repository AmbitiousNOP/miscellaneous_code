const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');

const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

/* Declaring the array of image filenames */
const filenames = ['pic1.jpg', 'pic2.jpg', 'pic3.jpg', 'pic4.jpg', 'pic5.jpg'];

/* Declaring the alternative text for each image file */
const altText = {'pic1.jpg': 'eyeball', 'pic2.jpg': 'not sure. Granite?', 
                'pic3.jpg': 'flowers', 'pic4.jpg': 'egyptian stuff',
                'pic5.jpg': 'butterfly'};

/* Looping through images */
for (const filename of filenames) {
    const newImage = document.createElement('img');
    newImage.setAttribute('src', 'images/' + filename);
    newImage.setAttribute('alt', altText[filename]);
    thumbBar.appendChild(newImage);
    newImage.addEventListener("click", e =>{
        displayedImage.src = e.target.src;
        displayedImage.alt = e.target.alt; 
    });
}


/* Wiring up the Darken/Lighten button */
btn.addEventListener("click", () =>{
    const btnClass = btn.getAttribute("class");
    if (btnClass === 'dark'){
        displayedImage.style.filter = "brightness(50%)";
        btn.setAttribute('class', 'light');
        btn.textContent = "Lighten";
    }else {
        displayedImage.style.filter = "brightness(100%)";
        btn.setAttribute('class', 'dark');
        btn.textContent = "Darken";
    }
});