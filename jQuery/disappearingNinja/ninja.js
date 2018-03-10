$(document).ready(function() {
    $("img").click(function() {
        // $(this).hide();
        // $(this).css("opacity", "0");
        // $(this).fadeOut(); // use animate() to control specific css properties
        $(this).animate({'opacity':'0'}, 1000);
    })

    $("button").click(function() {
        // $("img").show();
        // $("img").css("opacity", "1");
        $("img").animate({'opacity':'1'}, 1000);
    })
})