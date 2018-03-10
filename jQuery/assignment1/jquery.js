
$(document).ready(function(){
    $('.click').click(function(){
        alert("This was the click function.")
    })

    $('.hide').click(function(){
        $('.remove').hide("slow");
    })

    $('.show').click(function(){
        $('.toShow').show();
    })

    $('.toggle').click(function(){
        $('.toToggle').toggle("slow");
    })

    $('.slideUp').click(function(){
        $('.toSlideDown').slideUp("slow");
    })

    $('.slideDown').click(function(){
        $('.toSlideDown').slideDown("slow");
    })

    $('.slideToggle').click(function(){
        $('.toSlideToggle').slideToggle("slow");
    })

    $('.fadeIn').click(function(){
        $('.tofadeIn').fadeIn("slow");
    })

    $('.fadeOut').click(function(){
        $('.tofadeIn').fadeOut("slow");
    })

    $('.addClass').click(function(){
        $('.toAddClass').addClass("redColor");
    })

    $('.before').click(function(){
        $('.toBefore').before(" <p>Adding text before whatever was here first.</p>");
    })

    $('.after').click(function(){
        $('.toBefore').before("<p>Adding text after whatever was here first.</p>");
    })

    $('.append').click(function(){
        $('.toAppend').append("Appending text to after original stuffs");
    })

    $('.html').click(function(){
        // var htmlString = $('.toHtml').html();
        $('.toHtml').text($('.toHtml').html());
    })

    // $('.attr').click(function(){
    //     // var title = $('img').attr('src');
    //     $('toAttr').text($('img').attr('src'));
    // })

    var title = $('em').attr('title');
    $('.toAttr').text(title);

    $('.val').keyup(function() {
        $('.toVal').text($('.val').val());
    })

    $('.text').click(function(){
        $('.toText').text($('span').text());
    })

    $('#dataDiv').data('testData', {first_name: "Jason", last_name: "Shin"});
    $('.toDataFirst').text($('#dataDiv').data('testData').first_name);
    $('.toDataLast').text($('#dataDiv').data('testData').last_name);

})