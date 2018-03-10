function numbersOnly(arr) {
    var numArr = [];

    for(var i = 0; i < arr.length; i++) {
        if(typeof(arr[i]) === "number") {
            numArr.push(arr[i]);
        }
    }
    return numArr;
}
randomArray = ["Jane", true, 4, 10, false, "Hi", true, 1000];
console.log(numbersOnly(randomArray));

// function refineArray(arr) {
//     for(var i = 0; i < arr.length; i++) {
//         if(typeof(arr[0]) !== "number") {
//             arr.splice(0,1);
//         }
//     }
//     return arr;
// }

// randomArray.splie();
// console.log(refineArray(randomArray));

// Bonus part cannot get to work