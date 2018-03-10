// var num1 = Math.pow(2,9);
// console.log(num1);
// var num2 = Math.random();
// console.log(num2);
// var num3 = Math.sqrt(808080);
// console.log(num3);
// var num4 = Math.pow(2,15);
// console.log(num4);

// var string1 = "Hello World";
// console.log(string1);
// var string2 = "Angry Cows steal my potatoes";
// console.log(string2);
// var string3 = "I have pizza";
// console.log(string3);

// var isRaining = false;
// console.log(isRaining);
// var isWindy = false;
// console.log(isWindy);

// var temp = '';
// console.log(temp);

// function isPalindrome(str) {
//     var check = '';
//     for(var i = str.length-1; i >= 0 ; i--) {
//         check += str[i];
//     }
//     if(str == check) {
//         console.log("true")
//     } else {
//         console.log(str[0])
//     }
// }

// isPalindrome("racecar")

function longPali(str) {
    var pali = '';
    var checkStr = '';

    if (str.length < 3) {
        console.log("too short")
    }
    for (var i = 0; i < str.length; i++) {
        for(var x = i+3; x <= str.length; x++) {
            checkStr = str.substring(i,x);
            // console.log(checkStr)
            var reverse = '';
            for(var y = checkStr.length-1; y>=0; y--) {
                reverse += checkStr[y];
            }
            // console.log(reverse)
            if(checkStr == reverse && checkStr.length > pali) {
                pali = checkStr;
            }
        }
        // console.log(pali)
    }
    console.log(pali)
}

longPali("Yikes! my favorite racecar erupted!")
