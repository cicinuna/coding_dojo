$(document).ready(function() {
    // var front = $("img").attr("src");
    // console.log(front);
    // var back = $("img").attr("alt-src");
    // console.log(back);
    // front and back takes src and alt-src of first img
    // if I declare variables here

    $("img").hover(function() {
        var front = $(this).attr("src");
        // console.log(front);
        var back = $(this).attr("alt-src");

        // var temp = front;
        // console.log(back);

    //     $(this).animate({opacity:0}, "slow"); 
    // }, function() {
    //     $(this).animate({opacity:1}, "Slow");
    
    
        // $(this).css("display", "none");
        $(this).attr("src", back);
        $(this).attr("alt-src", front);
        // console.log(front);
        // console.log(back);
        }, function() {
        // Did not know i needed to create new set of variables for the
        // Second part of the hover() function. 
        // Why???
        var front = $(this).attr("src");
        // console.log(front);
        var back = $(this).attr("alt-src");
        // $(this).css("display", "inline-block");
        // console.log(front);
        // console.log(back);
        $(this).attr("alt-src", front);
        $(this).attr("src", back);
    });
})