// Initialize character counter for the title's note
$(document).ready(function() {
    $('input#title-note').characterCounter();
});

const error = document.getElementById('error')
if (error) {
    setTimeout(() => {
        error.remove()
    }, 3000)
}