function tellTime(hour, minute, period) {
    if (minute < 30) {
        if (period == "AM") {
            console.log("It's just " +minute+ " after " +hour+ " in the morning");
        } else {
            console.log("It's just " +minute+ " after " +hour+ " in the evening");
        }
    } else {
        if (period == "AM") {
            console.log("It's almost "+(hour+1)+ " in the morning");
        } else {
            console.log("It's almost "+(hour+1)+ " in the evening");
        }
    }
}

tellTime(7,15,"AM")
tellTime(8,50,"PM")