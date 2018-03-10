$(document).ready(function() {
    for(var i = 1; i < 152; i++) {
        $('#images').append('<img id = "'+i+'" class = "pokeImages" src = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/'+i+'.png">')
    }

    $(document).on("click", ".pokeImages", function() {
        var pokeNum = $(this).attr("id");
        console.log(pokeNum);
        $.get('http://pokeapi.co/api/v2/pokemon/'+pokeNum+'', function(pokemon) {
            // console.log(pokemon);
            // console.log(pokemon.forms);
            // console.log(pokemon.forms[0].name); needed to see these to find out to use forms[0]
            $('#infos').html('<h1>'+pokemon.forms[0].name+'</h1><img class = "infoImage" src = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/'+pokeNum+'.png">')
            $('#infos').append('<h3>Types</h3>')
            $('#infos').append('<ul></ul>')
            for(var i = 0; i < pokemon.types.length; i++) {
                $('#infos').append('<li>'+pokemon.types[i].type.name+'</li>')
            }
            $('#infos').append('<h3>Height</h3>')
            $('#infos').append('<p>'+pokemon.height+'</p>')
            $('#infos').append('<h3>Weight</h3>')
            $('#infos').append('<p>'+pokemon.weight+'</p>')
        })
    })

})