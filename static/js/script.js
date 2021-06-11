let butt = document.getElementsByTagName('button');


for (let i = 0; i < butt.length; i++) {
    let buttonClass = butt[i].className.split(" ");
    let result = buttonClass.find(buttonClass => buttonClass.startsWith("click"));
    if (result) {
        butt[i].addEventListener('click', function () {
            switch (result) {
                case 'click_tasks':
                    location.href = 'tasks.html';
                    break;
                case 'click_teams':
                    location.href = 'teams.html';
                    break;
            }
        });
    };
};