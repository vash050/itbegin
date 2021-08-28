"use strict";

let datamap = new Map([
    [document.getElementById("accountMyMailBtn"), document.getElementById("accountMyModal")]
]);

let mailBtn = document.getElementById("accountMyMailBtn");
let link = mailBtn.getAttribute("data-link");
let insertMail = document.getElementById("accountInsertMail");

console.log(link);

datamap.forEach((value, key) => {
    doModal(key, value);
});

function doModal(anchor, popupbox) {
    let span = popupbox.getElementsByClassName("account__close")[0];

    anchor.addEventListener("click", function (event) {
        popupbox.style.display = "block";
    });

    span.addEventListener("click", function (event) {
        popupbox.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target == popupbox) {
            popupbox.style.display = "none";
        }
    });
}

const getData = function () {
    console.log('getData clicked');
    const xhr = new XMLHttpRequest();
    xhr.open("GET", link);

    xhr.onload = function () {
        const data = xhr.response;
        insertMail.innerHTML = data;
    };
    xhr.send();

};

mailBtn.addEventListener("click", getData);