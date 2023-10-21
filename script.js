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
            noBtn.style.animation = 'moveNoButton 10s linear'; // Move for 10 seconds
            noBtn.style.pointerEvents = 'none';

            setTimeout(function() {
                noBtn.style.animation = 'none'; // Stop the animation
                noBtn.innerHTML = "No (Unavailable) 😂";
                message.innerHTML = "Don't try hard, you will be mine! 😂";
            }, 10000); // Show the message after 10 seconds
        }
    });

    function hideButtons() {
        yesBtn.style.display = 'none';
        noBtn.style.display = 'none';
    }
});
