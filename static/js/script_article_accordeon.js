"use strict";

let acc = document.getElementById("accordion");

acc.addEventListener("click", function () {
    console.log('clicked');
    this.classList.toggle("active");
    let panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
        
    } else {
        panel.style.maxHeight = panel.scrollHeight + "px";
        
    }
});

acc.click();
