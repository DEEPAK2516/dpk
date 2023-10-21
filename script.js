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
            noBtn.style.animation = 'moveNoButton 1s linear forwards'; // Stop the animation after the first click
            noBtn.style.pointerEvents = 'none';
            noBtn.innerHTML = "No (Unavailable) 😂";
            message.innerHTML = "Don't try hard, you will be mine! 😂";
        }
    });

    setTimeout(function() {
        message.innerHTML = "Don't try hard, you will be mine! 😂";
    }, 10000); // Show message after 10 seconds

    function hideButtons() {
        yesBtn.style.display = 'none';
        noBtn.style.display = 'none';
    }
});
