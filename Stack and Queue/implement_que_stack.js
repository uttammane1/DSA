/*
Stack {
  push()
  top()
  pop()
  isEmpty()
}
*/

class Queue {
    constructor() {
        this.S1 = [];
        this.S2 = [];
    }

    push(value) {
        // Push all elements from S1 to S2
        while (this.S1.length > 0) {
            this.S2.push(this.S1.pop());
        }

        // Push the new element into S1
        this.S1.push(value);

        // Push everything back from S2 to S1
        while (this.S2.length > 0) {
            this.S1.push(this.S2.pop());
        }
    }

    pop() {
        if (this.S1.length === 0) {
            return -1;
        }
        return this.S1.pop();
    }

    front() {
        if (this.S1.length === 0) {
            return -1;
        }
        return this.S1[this.S1.length - 1];
    }

    isEmpty() {
        return this.S1.length === 0;
    }
}
