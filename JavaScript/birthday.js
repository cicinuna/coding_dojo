function countToBirthday(days) {
    for (var i = days; days >=0; i--) {
        if(i >= 30) {
            console.log(i+ " days until my birthday. Such a long time ... =(");
        }
        if(i >5 && i <30) {
            console.log(i+ " days until my birthday. I'm kind of hyped =]");
        }
        if(i <=5 && i >1) {
            console.log(i+ " DAYS UNTIL MY BIRTHDAY!!");
        }
        if(i == 1) {
            console.log(i+ " DAY UNTIL MY BIRTHDAY!!!!!");
        }
        if(i == 0) {
            console.log("HAPPY BIRTHDAY TO ME :D");
        }
    }
}

countToBirthday(50);