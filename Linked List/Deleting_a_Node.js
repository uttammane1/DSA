const LinkedListNode = class {
    constructor(nodeData) {
        this.data = nodeData;
        this.next = null;
    }
};

// Complete the function below
function deleteNode(head, position) {
    // If the list is empty
    if (head === null) {
        return null;
    }

    // If the position is the head
    if (position === 0) {
        return head.next; // Return the next node as the new head
    }

    let current = head;
    let count = 0;

    // Traverse to find the node just before the one to delete
    while (current !== null && count < position - 1) {
        current = current.next;
        count++;
    }

    // If the current node is null, the position is out of bounds
    if (current === null || current.next === null) {
        return head; // Return the original head if position is invalid
    }

    // Skip the node to be deleted
    current.next = current.next.next;

    return head; // Return the head of the updated list
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

    // Reading the position of the node to delete
    const position = parseInt(readLine().trim(), 10);

    // Deleting the node at the specified position
    head = deleteNode(head, position);

    // Displaying the updated linked list
    display(head);
}
