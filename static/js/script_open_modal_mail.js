"use strict";

let datamap = new Map([
    [document.getElementById("messages"), document.getElementById("messagesMyModal")]
]);

let dialogs = document.getElementById("messages");
let link = dialogs.getAttribute("data-link");

let panel = document.getElementsByClassName("panel-body");

let accountChat = document.getElementById("tab_column");
let blockTwo = document.getElementById("accountOpenChat");

async function gotoBottom(id) {
    var element = document.getElementById(id);
    console.log("gotobottom");
    element.scrollTop = element.scrollHeight - element.clientHeight;
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

dialogs.addEventListener("click", async function () {

    getButtons()
});

async function getButtons() {
    let token = readCookie('csrftoken');
    let mesAuthorName = document.getElementById("mesAuthorName").value;
    let mesAuthorId = document.getElementById("mesAuthorId").value;

    let btnOne = await getButton(link);

    if (!btnOne) {
        panel[0].innerHTML = 'Нет ни одного начатого диалога';
    } else {
        btnOne = JSON.parse(btnOne);

        let dialogCount = [];

        btnOne.filter(function (item) {
            let i = dialogCount.findIndex(x => (x.dialog == item.dialog));
            if (i <= -1) {

                dialogCount.push(item.dialog);

            }
            return null;
        });

        dialogCount = [...new Set(dialogCount)];
        console.log(dialogCount);
        let getUsers = once(function () {

            for (let i = 0; i < dialogCount.length; i++) {
                let tab = createNewElement("div", "tab", dialogCount[i]);
                let tablinks = createNewElement("button", "tablinks");
                let avatar = createNewElement("img", "avatar-messages account__avatar__messages");
                let tabcontent = createNewElement("div", "tabcontent account__reply_body", dialogCount[i] + 'dialog');
                let inputBlock = createNewElement("input", "id_message", dialogCount[i] + 'input', "text");
                inputBlock.placeholder = "Сообщение";
                let inputImageBlock = document.createElement("span");
                let inputImage = createNewElement("img", "account__img_sent", dialogCount[i] + "registration__send");
                inputImage.src = "/static/img/send_24px.png";

                inputImageBlock.appendChild(inputImage);

                if (dialogCount[0]) {
                    (new Promise((resolve, reject) => {
                        resolve(tablinks.id = "defaultOpen")
                    }))
                        .then(() => {
                            document.getElementById("defaultOpen").click();
                        })
                }

                tablinks.setAttribute('data-id', dialogCount[i]);

                accountChat.insertBefore(tab, accountChat.firstChild);

                tab.appendChild(tablinks);

                blockTwo.appendChild(tabcontent);

                for (let j = 0; j < btnOne.length; j++) {
                    if (btnOne[j].dialog == dialogCount[i]) {
                        tablinks.innerHTML = btnOne[j].user_name;
                        avatar.src = btnOne[j].user_avatar;

                        let mesBlock = createNewElement("div", "account_mes_block");
                        let messageText = createNewElement("div", "account__message_inline");
                        let mesDate = createNewElement("p", "account__message_date");
                        let mesAuthor = createNewElement("p", "account__message_author");
                        messageText.innerHTML = btnOne[j].message;
                        mesDate.innerHTML = btnOne[j].pub_date;
                        mesAuthor.innerHTML = btnOne[j].user_name;
                        tabcontent.insertBefore(mesBlock, tabcontent.firstChild);

                        mesBlock.appendChild(mesAuthor);
                        mesBlock.appendChild(messageText);
                        mesBlock.appendChild(mesDate);

                        tabcontent.appendChild(inputImageBlock);

                        (new Promise((resolve, reject) => {
                            resolve(
                                tabcontent.appendChild(inputBlock)

                            )
                        }))
                            .then(() => {
                                gotoBottom('accountOpenChat');
                            })

                    }
                }
                tablinks.appendChild(avatar);
                once = function () { };

            }
        });
        getUsers();
        let tabcontentFirst = document.getElementsByClassName("tabcontent");
        tabcontentFirst[0].style.display = "block";
        let users = document.getElementsByClassName("tablinks");

        for (const dialog of users) {
            let dialogId = dialog.getAttribute("data-id");
            dialogId += 'dialog';

            dialog.addEventListener("click", function () {
                openDialog(event, dialogId);
                gotoBottom('accountOpenChat');
            })
        }

    };

    let inputs = document.getElementsByClassName('id_message');
    
    let newMessageBlock = document.createElement("ul");

    let inputImgs = document.getElementsByClassName("account__img_sent");

    for (let h = 0; h < inputs.length; h++) {

        let newMessageId = inputs[h].id;
        newMessageId = newMessageId.slice(0, -5);

        inputs[h].addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {

                let newMessage = inputs[h].value;
                // dialod_id, author_id, message, url = /message/api/dialogs/{id}/
                let urlPost = '/message/api/dialogs/' + newMessageId + '/';

                let data = JSON.stringify({
                    'dialog': newMessageId,
                    'author': mesAuthorId,
                    'user_name': mesAuthorName,
                    'message': newMessage
                });
                postData(urlPost, data, token);

                inputs[h].parentNode.insertBefore(newMessageBlock, inputs[h]);
                newMesShow(mesAuthorName, newMessage, newMessageBlock);
                inputs[h].value = '';
                gotoBottom('accountOpenChat');
            }
        });

        inputImgs[h].addEventListener("click", function (e) {
            let newMessage = inputs[h].value;
            // dialod_id, author_id, message, url = /message/api/dialogs/{id}/
            let urlPost = '/message/api/dialogs/' + newMessageId + '/';

            let data = JSON.stringify({
                'dialog': newMessageId,
                'author': mesAuthorId,
                'user_name': mesAuthorName,
                'message': newMessage
            });
            postData(urlPost, data, token);

            inputs[h].parentNode.insertBefore(newMessageBlock, inputs[h]);
            newMesShow(mesAuthorName, newMessage, newMessageBlock);
            inputs[h].value = '';
            gotoBottom('accountOpenChat');
        });
    }
}

function createNewElement(block, cssClass, id = null, type = null) {
    let element = document.createElement(block);
    element.className = cssClass;
    if (id !== null) {
        element.id = id;
    }
    if (type !== null) {
        element.type = type;
    }
    return element;
}

async function postData(url = '', data = {}, token) {

    const response = await fetch(url, {
        method: 'POST',
        // credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': token
        },
        body: data
    });
    return response;
}

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

    let dialogBlock = document.getElementById(dialogName);
    console.log(dialogBlock);
    dialogBlock.style.display = "flex";
    evt.currentTarget.className += " active";
}

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

function once(fn, context) {

    var result;

    return function () {
        if (fn) {
            result = fn.apply(context || this, arguments);
            fn = null;
        }

        return result;
    };
}

function newMesShow(author, message, block) {
    let mes = createNewElement("li", "account__message_li");
    let mesNewAuthor = createNewElement("p", "account__message_author");
    let messageNewText = createNewElement("div", "account__message_inline");
    let mesNewDate = createNewElement("p", "account__message_date");
    let currentDate = new Date;
    currentDate = currentDate.getDate() + "-" + (currentDate.getMonth() + 1) + "-" + currentDate.getFullYear() + " " +
        currentDate.getHours() + ":" + currentDate.getMinutes();

    mesNewAuthor.innerHTML = author;
    messageNewText.innerHTML = message;
    mesNewDate.innerHTML = currentDate;

    mes.appendChild(mesNewAuthor);
    mes.appendChild(messageNewText);
    mes.appendChild(mesNewDate);
    block.appendChild(mes);
}
