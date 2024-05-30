document.addEventListener('DOMContentLoaded', function () {
    const popup = document.getElementById('popup');
    const showPopupBtn = document.getElementById('show-popup');
    const closePopupBtn = document.getElementById('close-popup');
    const showPopupActions = document.getElementsByClassName('actions-update');

    showPopupBtn.addEventListener('click', function () {
        popup.style.display = 'flex';
    });

    Array.from(showPopupActions).forEach(function (action) {
        action.addEventListener('click', function () {
            popup.style.display = 'flex';
        });
    });

    closePopupBtn.addEventListener('click', function () {
        popup.style.display = 'none';
    });

    popup.addEventListener('click', function (event) {
        if (event.target === popup) {
            popup.style.display = 'none';
        }
    });
});
