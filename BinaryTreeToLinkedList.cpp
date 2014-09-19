//nodeList class has FIFO push/pop order

struct node
{
    int value;
    node* left;
    node* right;
};

node* ConvertBinaryTreeToLinkedList(node* treeHead)
{
    // Variables that you need
    nodeList list = new nodeList;
    node* linkedListHead = null;
    node* linkedListEnd = null;
    node* tempNode = null;
    
    // Error condition - empty tree
    if (treeHead == null)
    {
        return null;
    }
    
    // Start the algorithm off with the head
    list.push(treeHead);
    
    while (list.size != 0)
    {
        // Pop, process, and sanitize the current node off the list
        tempNode = list.pop();
        list.push(tempNode->left);
        list.push(tempNode->right);
        tempNode->left = null;
        tempNode->right = null;

        // First list element condition
        if (linkedListHead == null)
        {
            linkedListHead = tempNode;
            linkedListEnd = tempNode;
        }
        // Regular condition
        else
        {
            // Attach the node to the end of the list, then we're done with the pointer tempNode
            linkedListEnd->left = tempnode;
            linkedlistEnd = tempNode;        
            tempNode = null;
        }
    }
    
    return linkedListHead;
}

   o
  / \
 o   o