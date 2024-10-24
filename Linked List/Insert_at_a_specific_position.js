const LinkedListNode = class {
    constructor(nodeData) {
        this.data = nodeData;
        this.next = null;
    }
};

// Complete the function below
function insertNodeAtPosition(head, data, position) {
    const newNode = new LinkedListNode(data);
    
    // If inserting at the head (position 0)
    if (position === 0) {
        newNode.next = head;
        return newNode;
    }
    
    let current = head;
    let count = 0;

    // Traverse to find the position to insert the node
    while (count < position - 1 && current !== null) {
        current = current.next;
        count++;
    }
    
    // Insert the new node at the correct position
    newNode.next = current.next;
    current.next = newNode;
    
    return head;
}

// Function to display the linked list
function display(head) {
    let current = head;
    const result = [];
    while (current !== null) {
        result.push(current.data);
        current = current.next;
    }
    console.log(result.join(" "));
}

// Input and output processing
function main() {
    const n = parseInt(readLine().trim(), 10);
    let head = null;
    let current = null;
    
    // Building the linked list
    for (let i = 0; i < n; i++) {
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
    
    // Reading data to insert and the position
    const dataToInsert = parseInt(readLine().trim(), 10);
    const position = parseInt(readLine().trim(), 10);
    
    // Inserting the node at the specified position
    head = insertNodeAtPosition(head, dataToInsert, position);
    
    // Displaying the updated linked list
    display(head);
}
