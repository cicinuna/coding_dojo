function fancyArray(arr,reversed) {
    if(reversed == true) {
        for(var i = 0; i < arr.length;i++) {
            console.log(arr[i]+ " -> " +i);
        }
    } else {
        for(var i = 0; i < arr.length;i++) {
            console.log(i + " -> " +arr[i]);
        }
    }
}

var plainArr = ["James", "Jill", "Jane", "Jack"];
fancyArray(plainArr, false);
fancyArray(plainArr, true);

//still can't figure out how to work if parameter is empty, then do something