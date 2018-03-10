function fibonacci(n) {
    var fib = [0,1];

    if(n == 0) {
        console.log(fib[n]);
    }
    else if(n == 1) {
        console.log(fib[n]);
    } 
    else if(n > 1) {
        for(var i =2; i <= n; i++) {
            fib.push(fib[i-1]+fib[i-2]);
        }
        console.log(fib[n]);
    }
}

fibonacci(6);