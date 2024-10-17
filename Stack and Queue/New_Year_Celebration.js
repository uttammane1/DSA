function newYearCelebration(queries) {
    const queue = [];  
    const stack = [];  
    const results = []; 
    for (const query of queries) {
        const type = query[0];
        const value = query[1];

        if (type === 1) {
            queue.push(value);
        } else if (type === 2) {
            stack.push(value);
        } else if (type === 3) {
            if (queue.length > 0) {
                results.push(queue[0]); 
            } else {
                results.push(-1); 
            }
        } else if (type === 4) {
            if (stack.length > 0) {
                results.push(stack[stack.length - 1]); 
            } else {
                results.push(-1); 
            }
        } else if (type === 5) {
            if (queue.length > 0) {
                stack.push(queue.shift()); 
            } else {
                results.push(-1); 
            }
        }
    }
    
    console.log(results.join('\n'));
}

function runProgram(input) {
    const lines = input.trim().split('\n');
    const Q = parseInt(lines[0]); 
    const queries = [];

    for (let i = 1; i <= Q; i++) {
        const query = lines[i].trim().split(' ').map(Number);
        queries.push(query);
    }

    newYearCelebration(queries);
}

if (process.env.USER === "") {
    runProgram(``);
} else {
    process.stdin.resume();
    process.stdin.setEncoding("ascii");
    let read = "";
    process.stdin.on("data", function (input) {
        read += input;
    });
    process.stdin.on("end", function () {
        read = read.replace(/\n$/, "");
        read = read.replace(/\n$/, "");
        runProgram(read);
    });
    process.on("SIGINT", function () {
        read = read.replace(/\n$/, "");
        runProgram(read);
        process.exit(0);
    });
}
