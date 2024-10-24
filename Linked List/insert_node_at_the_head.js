const LinkedListNode = class {
    constructor(nodeData) {
        this.data = nodeData;
        this.next = null;
    }
};

// Complete the function below
function insertNodeAtHead(head, data) {
    const newNode = new LinkedListNode(data); // Create a new node with the given data
    newNode.next = head; // Point the new node's next to the current head
    return newNode; // Return the new node as the new head of the list
}
