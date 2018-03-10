var houseIndex = [];

function getIndex(i) {
    var res = $.get('https://www.anapioficeandfire.com/api/houses/'+i, function(houses) {
            var houseName = houses.name;
            // console.log(houseName)
            if(houseName.includes("Lannister")){
                houseIndex.push(i);
                // console.log(houseIndex)
            }
            // if(houseName.indexOf("Stark") != 1) {
            //     houseIndex.push(i);
                // console.log(houseIndex);
            // }else if(houseName.indexOf("Targaryen") != 1) {
            //     houseIndex.push(i);
            // }else if(houseName.indexOf("Lannister") != 1) {
            //     houseIndex.push(i);
            // }else if(houseName.indexOf("Baratheon") != 1) {
            //     houseIndex.push(i);
            // }else if(houseName.indexOf("Tully") != 1) {
            //     houseIndex.push(i);
            // }else if(houseName.indexOf("Arryn") != 1) {
            //     houseIndex.push(i);
            // }else if(houseName.indexOf("Tyrell") != 1) {
            //     houseIndex.push(i);
            // }else if(houseName.indexOf("Martell") != 1) {
            //     houseIndex.push(i);
            // }
            // console.log(houseIndex);
    });
}

$(document).ready(function() {
    // console.log(getIndex(1));
    // trying to grab house numbers of all houses that contain this specific name, but
    // running .get inside for loop gives trouble
    // var houseIndex = [];
    for(var i = 1; i < 445; i++) {
        getIndex(i);
    //     $.get('https://anapioficeandfire.com/api/houses/'+i+'', function(houses){
    //         var houseName = houses.name;
    //         // console.log(houseName)
    //         if(houseName.indexOf("Stark") !== 1) {
    //             houseIndex.push(i);
    //             // console.log(houseIndex);
    //         }else if(houseName.indexOf("Targaryen") !== 1) {
    //             houseIndex.push(i);
    //         }else if(houseName.indexOf("Lannister") !== 1) {
    //             houseIndex.push(i);
    //         }else if(houseName.indexOf("Baratheon") !== 1) {
    //             houseIndex.push(i);
    //         }else if(houseName.indexOf("Tully") !== 1) {
    //             houseIndex.push(i);
    //         }else if(houseName.indexOf("Arryn") !== 1) {
    //             houseIndex.push(i);
    //         }else if(houseName.indexOf("Tyrell") !== 1) {
    //             houseIndex.push(i);
    //         }else if(houseName.indexOf("Martell") !== 1) {
    //             houseIndex.push(i);
    //         }
    //     })
    }
    console.log(houseIndex);
    $('img').click(function() {
        var houseIndex = $(this).attr('class');

        $.get('https://www.anapioficeandfire.com/api/houses/'+houseIndex+'', function(houses) {
            // console.log(houses.name);
            $('.houseDetails').html('<h1><span>'+houses.name+'</span> of <span>'+houses.region+'</span></h1>');
            $('.houseDetails').append('<p>Words: <span>"'+houses.words+'"</span></p>');
            $('.houseDetails').append('<p>House Titles: <ul>');
            for(var i = 0; i < houses.titles.length; i++) {
                $('.houseDetails').append('<li>'+houses.titles[i]+'</li>');
            }
            $('.houseDetails').append('</ul></p>');

            if(houses.currentLord == "") {
                $('.houseDetails').append('<p>The house currently has no Lord. </p>');
            } else {
                $.get(houses.currentLord, function(lord) {
                    $('.houseDetails').append('<p>The current house Lord is: <span>'+lord.name+'</span></p>');
                    $('.houseDetails').append('<p>born <span>'+lord.born+'</span></p>');
                })
            }
            // wanted to add ancestral weapons
            // i am make new ul after house titles, but for some reason the weapons get added to house titles list.

            // $('houseDetails').append('<p>House Ancestral Weapons: <ol>');
            // for(var i = 0; i < houses.ancestralWeapons.length; i++) {
            //     $('.houseDetails').append('<li>'+houses.ancestralWeapons[i]+'</li>');
            // }
            // $('.houseDetails').append('</ol></p>');
        })
    })
})