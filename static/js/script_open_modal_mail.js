"use strict";

let datamap = new Map([
    [document.getElementById("accountMyMailBtn"), document.getElementById("accountMyModal")]
]);

let mailBtn = document.getElementById("accountMyMailBtn");
let link = mailBtn.getAttribute("data-link");
let insertMail = document.getElementById("accountInsertMail");

function gotoBottom(id) {
    var element = document.getElementById(id);
    element.scrollTop = element.scrollHeight - element.clientHeight;
}

function getForm(formId) {
    let jsForm = document.getElementById(formId);
    let actionForm = jsForm.getAttribute("data-action");

    return [jsForm, actionForm];
}

function getEventListener(input, form, id) {
    $(input).keypress(function (e) {
        if (e.which == 13) {
            $(form).submit();
            // $("textarea").val("");
            //   return false;    //<---- Add this line 
        }

    });

    $(id).click(function () {
        $(form).submit();
        // $("textarea").val("");
        //   return false;    //<---- Add this line 

    });
}

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

    let blockTwo = document.getElementById("accountOpenChat");

    // let btnsTwo = document.getElementsByClassName("attached-reply-body");
    let users = document.getElementsByClassName("tablinks");
    console.log(users);
    let tabcontentFirst = document.getElementsByClassName("tabcontent");
    tabcontentFirst[0].style.display = "block";

    for (const dialog of users) {
        let dialogId = dialog.getAttribute("data-id");
        console.log(dialogId + " = dialogId");

        dialog.addEventListener("click", function () {
            openDialog(event, dialogId);
        })
    }

    // let nameForm = "sendForm" + dialogId;
    let jsForm = document.forms;

    console.log(jsForm);
    for (let i = 0; i<jsForm.length; i++) {
        let actionForm = jsForm[i].getAttribute("data-action");

        let id = '#' + jsForm[i].id;
        getEventListener('#id_message', id, '#registration__send');
        jsForm[i].onsubmit = async (e) => {
            e.preventDefault();

            blockTwo.innerHTML = await submitForm(jsForm[i], actionForm);
            gotoBottom("accountOpenChat");
            getEventListener('#id_message', id, '#registration__send');
            // let jsForm = document.getElementById("messageFormJs");
            // let actionForm = jsForm.getAttribute("data-action");

        }
    }











    // blockTwo.innerHTML = submitForm(jsForm[0], jsForm[1]);


    // for (const message of btnsTwo) {
    //     let urlTwo = message.getAttribute("data-link");
    //     let btnTwo = await getButton(urlTwo);
    //     // console.log(btnTwo);
    //     let users = document.getElementsByClassName("tablinks");
    //     console.log(users);
    //     let tabcontentFirst = document.getElementsByClassName("tabcontent");
    //     tabcontentFirst[0].style.display = "block";

    //     for (const user of users) {
    //         let userName = user.getAttribute("data-id");
    //         user.addEventListener("click", function () {
    //             openCity(event, userName);
    //         })
    //     }

    //     function openCity(evt, cityName) {
    //         console.log('func work');
    //         // Declare all variables
    //         var tabcontent, tablinks;

    //         // Get all elements with class="tabcontent" and hide them
    //         tabcontent = document.getElementsByClassName("tabcontent");
    //         for (let i = 0; i < tabcontent.length; i++) {
    //             tabcontent[i].style.display = "none";
    //         }

    //         // Get all elements with class="tablinks" and remove the class "active"
    //         tablinks = document.getElementsByClassName("tablinks");
    //         for (let i = 0; i < tablinks.length; i++) {
    //             tablinks[i].className = tablinks[i].className.replace(" active", "");
    //         }

    //         // Show the current tab, and add an "active" class to the link that opened the tab
    //         document.getElementById(cityName).style.display = "block";
    //         evt.currentTarget.className += " active";
    //     }


    //     message.addEventListener("click", function () {
    //         blockTwo.innerHTML = btnTwo;
    //         gotoBottom("accountOpenChat");

    //         let jsForm = document.getElementById("messageFormJs");
    //         let actionForm = jsForm.getAttribute("data-action");

    //         getEventListener('#id_message', 'form#messageFormJs', '#registration__send');

    //         jsForm.onsubmit = async (e) => {
    //             e.preventDefault();

    //             blockTwo.innerHTML = await submitForm(jsForm, actionForm);
    //             gotoBottom("accountOpenChat");
    //             getEventListener('#id_message', 'form#messageFormJs', '#registration__send');
    //             // let jsForm = document.getElementById("messageFormJs");
    //             // let actionForm = jsForm.getAttribute("data-action");

    //         }

    //         // blockTwo.innerHTML = submitForm(jsForm[0], jsForm[1]);

    //     });

    // }
}

async function submitForm(form, action) {

    let response = await fetch(action, {
        method: 'POST',
        body: new FormData(form),
        enctype: "multipart/form-data"
    })
    console.log(response);
    return response.text();
};

mailBtn.addEventListener("click", async function () {

    getButtons()
});

function openDialog(evt, dialogName) {
    console.log('func work');
    // Declare all variables
    var tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (let i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (let i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    // cityName = "chat" + cityName;
    // console.log(cityName);
    // Show the current tab, and add an "active" class to the link that opened the tab
    let dialogBlock = document.getElementById(dialogName);
    console.log(dialogBlock);
    dialogBlock.style.display = "block";
    evt.currentTarget.className += " active";
}