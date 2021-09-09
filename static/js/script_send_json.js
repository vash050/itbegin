"use strict";
const urlApplications = 'http://127.0.0.1:8000/group/api/update_applications_to_team/';

let addButton = document.getElementsByClassName("add-one-to-team");
let delButton = document.getElementsByClassName("delete-application-to-team-from-team");

async function getData(url) {
    const res = await fetch(url);
    let jsonFile = await res.json();
    return jsonFile;
}

async function putData(url = '', data = {}) {
    let token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    const response = await fetch(url, {
        method: 'PUT',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': token
        },
        body: data
    });
    return response;
}


for (let item of addButton) {

    item.addEventListener("click", function () {
        let id = this.id;
        id = id.slice(3, id.length) + '/';
        getData(urlApplications + id)
            .then(data => {
                if (data.acceptation == 0) {
                data.acceptation = 1;

                data = JSON.stringify(data);
                putData(urlApplications + id, data)
                    .then(data => {

                    })
                }
                let btsId = "bts" + id.substring(0, id.length - 1);
                let buttons = document.getElementById(btsId);
                console.log(buttons);
                buttons.innerHTML = 'Заявка принята';
            })

        this.disabled = true;
        setTimeout(function () {
            this.disabled = false;
        }, 3000);
    })

}

for (let item of delButton) {
    item.addEventListener("click", function () {
        let id = this.id;
        id = id.slice(3, id.length) + '/';
        getData(urlApplications + id)
            .then(data => {
                if (data.acceptation == 0) {
                    data.acceptation = 2;
                    data = JSON.stringify(data);
                    putData(urlApplications + id, data)
                        .then(data => {
                            console.log(data);
                        })
                }
                let btsId = "bts" + id.substring(0, id.length - 1);
                let blcId = "blc" + id.substring(0, id.length - 1);
                let buttons = document.getElementById(btsId);
                let blockAppl = document.getElementById(blcId);
                console.log(buttons);
                buttons.innerHTML = 'Заявка отклонена';
                blockAppl.setAttribute('class', 'team__application__block_reject');
            })
        this.disabled = true;
        setTimeout(function () {
            this.disabled = false;
        }, 3000);
    })

}


