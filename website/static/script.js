const scrollThreshold = 32;

function checkScrolled() {
    if (window.scrollY > scrollThreshold) {
        $("header nav").addClass("scrolled");
    } else {
        $("header nav").removeClass("scrolled");
    }
}

$(document).ready(function(){
    checkScrolled()
    $(window).scroll(checkScrolled);
});