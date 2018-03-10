function printRange(start, end, increment) {
    if(increment == '') {
        for(var i = start; i <= end; i++) {
            console.log(i);
        }
    }
    if(end == '') {
        if(increment == '') {
            for(var i = 0; i <= start; i++) {
                console.log(i);
            }
        } else {
            for(var i = 0; i <= start; i+=increment) {
                console.log(i);
            }
        } // Bonus part no work
    } else {
        for(var i = start; i < end; i+=increment) {
            console.log(i);
        }
    }
}

printRange(2,10,2);
// printRange(4,8);
// printRange(4);
printRange(-4,22,3);