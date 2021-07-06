"use strict";

window.onload = function () {
    console.log("DOM ready");
    $('.delete-application-to-team-from-team').on('click', 'input[type=number]', function (event) {
       let qty = event.target.value
       let pk = event.target.name
       $.ajax({
            url:"/basket/update_book/" + pk + "/" + qty + "/",
            success: function (answer) {
                document.querySelector('.basket_list').innerHTML = answer.basket_list;
            }
       });
    })
}

