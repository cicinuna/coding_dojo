$(document).ready(function() {
    $("button").click(function() {

        // alert("You submitted");
        var first_name = $("input:text[name = 'first_name']").val();
        // for(var i = 0; i < 10000; i++) {
        //     console.log(first_name);
        // }
        var last_name = $("input:text[name = 'last_name']").val();
        var email = $("input:text[name = 'email']").val();
        var contact = $("input:text[name = 'contact']").val();

        $("tbody").append("<tr><td>"+first_name+"</td><td>"+last_name+"</td><td>"+email+"</td><td>"+contact+"</td></tr>")

        $("input:text[name = 'first_name']").val("");
        $("input:text[name = 'last_name']").val("");
        $("input:text[name = 'email']").val("");
        $("input:text[name = 'contact']").val("");
        return false;
    })


})