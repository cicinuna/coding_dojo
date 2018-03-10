$(document).ready(function() {
    $("button").click(function() {
        var city = $("input:text[name = 'city']").val();
        // var country = $("input:text[name = 'country']").val();

        $.get("http://api.openweathermap.org/data/2.5/find?q="+city+"&units=metric&appid=559bcf2569a3c26aaf986eacac7dca04", function(weather) {
            // console.log(weather);
            // console.log(weather.list.name);

            var dateTime = new Date(weather.list[0].dt * 1000);
            var year = dateTime.getFullYear();
            var months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
            var month = months[dateTime.getMonth()];    
            var date = dateTime.getDate();

            
            var t_f = weather.list[0].main.temp * 1.8 + 32;
            t_f = Math.round(t_f);
            // console.log(t_f);

            $("#data").html("<h1>"+weather.list[0].name+"</h1>")
            $("#data").append("<p>The temperature in "+city+" for </p>")
            $("#data").append("<p>"+month+" "+date+", "+year+" is: "+t_f+"</p>")
            // $("#data").append("")
        })
    })
})