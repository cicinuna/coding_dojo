$(document).ready(function() {
        for(var i = 1; i < 7; i++) {
            var htmlstr = '';
            $.get('http://pokeapi.co/api/v2/pokemon/'+i+'', function(pokemons) {
                htmlstr += '<img class = ".images" src = "';
                htmlstr += pokemons.sprites.front_shiny;
                console.log(htmlstr);
                htmlstr += '">';
                $('#wrapper').append(htmlstr);
            })

            // taking simpler approach than using .get()

            // $('#wrapper').append('<img class = ".images" src = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/'+i+'.png">');
        }
    })