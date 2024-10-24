const LinkedListNode = class {
    constructor(nodeData) {
        this.data = nodeData;
        this.next = null;
    }
};

// Complete the function below
function insertNodeAtTail(head, data) {
    let newNode = new LinkedListNode(data);
    
    // If the list is empty, the new node becomes the head
    if (head === null) {
        return newNode;
    }
    
    // Traverse to the end of the list
    let current = head;
    while (current.next !== null) {
        current = current.next;
    }
    
    // Attach the new node at the end
    current.next = newNode;
    
    // Return the original head
    return head;
}

// Function to display the linked list
function display(head) {
    let current = head;
    let result = [];
    while (current !== null) {
        result.push(current.data);
        current = current.next;
    }
    console.log(result.join(" "));
}

// Input processing for Online Judge (OJ) environments
function main() {
    const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split(/\s+/);
    
    let n = parseInt(input[0]); // Number of elements to insert
    let head = null;
    for (let i = 1; i <= n; i++) {
        let value = parseInt(input[i]);
        head = insertNodeAtTail(head, value);
        display(head); // Display the list after each insertion
    }
}
