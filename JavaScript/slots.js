function slots(coins, leave) {
    var win = 5;
    while (coins >=0) {
        // console.log(didWin);
        if(coins >= leave) {
            console.log("You now have " +coins+ ", more than your goal. GoodBye!");
            break;
        }
        var didWin = Math.trunc(Math.random() * 100);
        console.log("We needed " +win+ " in order to win, and we got " +didWin+ " on this try.");
        if(didWin == win) {
            var winning = Math.trunc(Math.random() * 50) +50;
            coins = coins + winning;
            console.log("YOU'VE WON " + winning+ " COINS! CONGRATS!");
        } 
        coins--;
        console.log("You currently have " +coins+ " coins left.");
        if(coins == 0) {
            console.log("You have no coins left to continue playing. GoodBye!");
            break;
        }
    }
}

slots(50,100);