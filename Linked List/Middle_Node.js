const LinkedListNode = class {
    constructor(nodeData) {
        this.data = nodeData;
        this.next = null;
    }
};

var middleNode = function(head) {
    let slow = head;
    let fast = head;

    while (fast !== null && fast.next !== null) {
        slow = slow.next;      
        fast = fast.next.next; 
    }

    return slow; 
};

function display(head) {
    let current = head;
    const result = [];
    while (current !== null) {
        result.push(current.data);
        current = current.next;
    }
    console.log(result.join(" "));
}

function main() {
    const t = parseInt(readLine().trim(), 10); 
    let head = null;
    let current = null;

    for (let i = 0; i < t; i++) {
        const data = parseInt(readLine().trim(), 10);
        const newNode = new LinkedListNode(data);

        if (head === null) {
            head = newNode;
            current = head;
        } else {
            current.next = newNode;
            current = newNode;
        }
    }

    const middle = middleNode(head);

    console.log(middle.data);
}
