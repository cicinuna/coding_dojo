$(document).ready(function() {
    $("img").click(function() {
        // console.log($(this).attr("alt-src"));
        var src = $(this).attr("src");
        var altSrc = $(this).attr("alt-Src");
        
        $(this).attr("src",altSrc);
        $(this).attr("alt-src", src);
        // if(which == "cat0.png") {
        //     $(this).attr("src", "ninja0.png");
        // } else if (which == "ninja0.png") {
        //     $(this).attr("src", "cat0.png");
        // } else if (which == "ninja1.png") {
        //     $(this).attr("src", "cat1.png");
        // } else if (which == "cat1.png") {
        //     $(this).attr("src", "ninja1.png");
        // } else if (which == "ninja2.png") {
        //     $(this).attr("src", "cat2.png");
        // } else if (which == "cat2.png") {
        //     $(this).attr("src", "ninja2.png");
        // } else if (which == "cat3.png") {
        //     $(this).attr("src", "ninja3.png");
        // } else if (which == "ninja3.png") {
        //     $(this).attr("src", "cat3.png");
        // } else if (which == "ninja4.png") {
        //     $(this).attr("src", "cat4.png");
        // } else if (which == "cat4.png") {
        //     $(this).attr("src", "ninja4.png");
        // }


    })

    //could you set up a dictionary with img src names and loop through it
    //and condense code?

    //fixed 
})