//copy numberphone
function clipboard1() {
    /* Get the text field */
    var copyText = document.getElementById("clipboard-text");
    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /*For mobile devices*/
    /* Copy the text inside the text field */
    document.execCommand("copy");
    /* Alert the copied text */
    alert("Copied the text: " + copyText.value);
}
function clipboard2() {
    /* Get the text field */
    var copyText = document.getElementById("clipboard-text");
    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /*For mobile devices*/
    /* Copy the text inside the text field */
    document.execCommand("copy");
    /* Alert the copied text */
    alert("Copied the text: " + copyText.value);
}

//scroll to the top
//Get the button:
mybutton = document.getElementById("scrolltotopbtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
    } else {
    mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


// choice productes image page

function imageFuc1(){
    document.getElementById('asli-gallery').src = "img/mask.jpg";
    document.getElementById('img-1').style.opacity = "1";
    document.getElementById('img-2').style.opacity = ".5";
    document.getElementById('img-3').style.opacity = ".5";
    document.getElementById('img-4').style.opacity = ".5";
}
function imageFuc2(){
    document.getElementById('asli-gallery').src = "img/puzzlechubi.jpg";
    document.getElementById('img-1').style.opacity = ".5";
    document.getElementById('img-2').style.opacity = "1";
    document.getElementById('img-3').style.opacity = ".5";
    document.getElementById('img-4').style.opacity = ".5";
}
function imageFuc3(){
    document.getElementById('asli-gallery').src = "img/saat.jpg";
    document.getElementById('img-1').style.opacity = ".5";
    document.getElementById('img-2').style.opacity = ".5";
    document.getElementById('img-3').style.opacity = "1";
    document.getElementById('img-4').style.opacity = ".5";
}
function imageFuc4(){
    document.getElementById('asli-gallery').src = "img/sticker.jpg";
    document.getElementById('img-1').style.opacity = ".5";
    document.getElementById('img-2').style.opacity = ".5";
    document.getElementById('img-3').style.opacity = ".5";
    document.getElementById('img-4').style.opacity = "1";
}


