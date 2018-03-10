function fewBillion() {
    var ini = 0.01;

    for(var i = 0;i < 30; i++) {
        ini = ini + ini;
        // console.log(ini); Numbers got so big quickly so just added it to see each sum
    }
    return ini;
}

console.log(fewBillion());

// In our hypothetical situation, the servant would have been rewarded 
// 10737418.24$ after 30 days, starting with 0.01$ as first day payment.

// Counting stuff part starts here

function countToMoney(target) {
    var ini = 0.01;
    var days = 0;
    while(ini <= target) {
        ini = ini + ini;
        days ++;
    }

    return ini, days;
}

console.log(countToMoney(10000));
console.log(countToMoney(1000000000));
console.log(countToMoney(Infinity));

// It will take servant 20 days to receive 10000$
// It will take servant 37 days to receive 1 billion dollars
// ??? for infinity