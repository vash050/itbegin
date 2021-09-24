"use strict";

var l, newDivOption;

/* Look for any elements with the class "custom-select": */
let block = document.getElementsByClassName("registration__form__block");
let selElmnt = block[0].getElementsByTagName("select")[0];


/* For each element, create a new DIV that will act as the selected item: */
let newDivSelected = document.createElement("DIV");
newDivSelected.setAttribute("class", "select-selected");
newDivSelected.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
block[0].appendChild(newDivSelected);

/* For each element, create a new DIV that will contain the option list: */
let newDivHide = document.createElement("DIV");
newDivHide.setAttribute("class", "select-items select-hide");

for (let j = 1; j < selElmnt.length; j++) {
    /* For each option in the original select element,
    create a new DIV that will act as an option item: */
    newDivOption = document.createElement("DIV");
    newDivOption.innerHTML = selElmnt.options[j].innerHTML;
    
    newDivOption.addEventListener("click", function (e) {
        /* When an item is clicked, update the original select box,
        and the selected item: */
        var y, s, h;
        s = this.parentNode.parentNode.getElementsByTagName("select")[0];

        h = this.parentNode.previousSibling;
        for (let i = 0; i < s.length; i++) {
            if (s.options[i].innerHTML == this.innerHTML) {
                s.selectedIndex = i;
                h.innerHTML = this.innerHTML;
                y = this.parentNode.getElementsByClassName("same-as-selected");

                for (let k = 0; k < y.length; k++) {
                    y[k].removeAttribute("class");
                }
                this.setAttribute("class", "same-as-selected");
                break;
            }
        }
        h.click();
    });
    newDivHide.appendChild(newDivOption);
}

block[0].appendChild(newDivHide);
newDivSelected.addEventListener("click", function (e) {
    /* When the select box is clicked, close any other select boxes,
    and open/close the current select box: */
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
});


function closeAllSelect(elmnt) {
    /* A function that will close all select boxes in the document,
    except the current select box: */
    var x, y, arrNo = [];
    x = document.getElementsByClassName("select-items");
    y = document.getElementsByClassName("select-selected");

    for (let i = 0; i < y.length; i++) {
        if (elmnt == y[i]) {
            arrNo.push(i)
        } else {
            y[i].classList.remove("select-arrow-active");
        }
    }
    for (let i = 0; i < x.length; i++) {
        if (arrNo.indexOf(i)) {
            x[i].classList.add("select-hide");
        }
    }
    console.log('close all clicked');
}

/* If the user clicks anywhere outside the select box,
then close all select boxes: */
document.body.addEventListener("click", function (event) {
    console.log('window clicked');
    if (event.target != block) {
        console.log("if clicked");
        closeAllSelect();
    }
});

