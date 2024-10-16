function nearestGreaterElement(arr, N) {
    let result = new Array(N).fill(-1);
    let stack = [];
  
    for (let i = 0; i < N; i++) {
      while (stack.length > 0 && arr[stack[stack.length - 1]] <= arr[i]) {
        stack.pop();
      }
      if (stack.length > 0) {
        result[i] = arr[stack[stack.length - 1]];
      }
      stack.push(i);
    }
  
    stack = [];
    for (let i = N - 1; i >= 0; i--) {
      while (stack.length > 0 && arr[stack[stack.length - 1]] <= arr[i]) {
        stack.pop();
      }
      if (stack.length > 0) {
        let leftGreater = result[i];
        let rightGreater = arr[stack[stack.length - 1]];
        if (leftGreater === -1 || (stack[stack.length - 1] - i < i - stack[stack.length - 1])) {
          result[i] = rightGreater;
        }
      }
      stack.push(i);
    }
  
    return result;
  }
  
  function runProgram(input) {
    const inputs = input.trim().split('\n');
    let t = parseInt(inputs[0]);
    let line = 1;
  
    for (let i = 0; i < t; i++) {
      let N = parseInt(inputs[line]);
      let arr = inputs[line + 1].split(' ').map(Number);
      let result = nearestGreaterElement(arr, N);
      console.log(result.join(' '));
      line += 2;
    }
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
  