"use strict";

let datamap = new Map([
    [document.getElementById("accountMyMailBtn"), document.getElementById("accountMyModal")]
]);

let mailBtn = document.getElementById("accountMyMailBtn");
let link = mailBtn.getAttribute("data-link");
let insertMail = document.getElementById("accountInsertMail");

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

async function getAsyncData(url) {
    const res = await fetch(url);
    let text = await res.text();
    return text;
}

async function getButton(url) {
    const res = await getAsyncData(url);
    return res;
}

async function getButtons() {

    let btnOne = await getButton(link);
    insertMail.innerHTML = btnOne;

    let btnTwoId = document.getElementById("accountChat")
    let urlTwo = btnTwoId.getAttribute("data-link");
    let blockTwo = document.getElementById("accountOpenChat");

    let btnTwo = await getButton(urlTwo);

    btnTwoId.addEventListener("click", function () {
        blockTwo.innerHTML = btnTwo
        let jsForm = document.getElementById("messageFormJs");
        let actionForm = jsForm.getAttribute("data-action");

        jsForm.onsubmit = async (e) => {
            e.preventDefault();

            let response = await fetch(actionForm, {
                method: 'POST',
                body: new FormData(jsForm),
                enctype: "multipart/form-data"
            });

            let result = await response;
            console.log(result);
            getButtons();
        };
    });
}

mailBtn.addEventListener("click", async function () {
    getButtons()
});
