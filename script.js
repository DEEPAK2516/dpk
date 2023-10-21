document.addEventListener('DOMContentLoaded', function() {
    const yesBtn = document.getElementById('yesBtn');
    const noBtn = document.getElementById('noBtn');
    const message = document.getElementById('message');
    let noButtonClicked = false;

    yesBtn.addEventListener('click', function() {
        message.innerHTML = "Let's live our lives together! 😍";
        hideButtons();
    });

    noBtn.addEventListener('click', function() {
        if (!noButtonClicked) {
            noButtonClicked = true;
            noBtn.style.animation = 'moveNoButton 0.5s linear infinite';
        } else {
            noBtn.innerHTML = "No (Unavailable) 😂";
            message.innerHTML = "Don't try hard, you will be mine! 😂";
            hideButtons();
        }
    });

    function hideButtons() {
        yesBtn.style.display = 'none';
        noBtn.style.display = 'none';
    }
});
