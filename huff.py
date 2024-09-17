string = 'BCAADDDCCACACAC'

# Class representing a node in the Huffman tree
class NodeTree(object):
    def __init__(self, left=None, right=None):
        """
        Initialize a node in the Huffman tree.
        Each node has two children (left and right).
        
        :param left: The left child node (or a character in leaf nodes)
        :param right: The right child node (or a character in leaf nodes)
        """
        self.left = left
        self.right = right

    def children(self):
        """
        Return the left and right children of the node.
        
        :return: A tuple containing the left and right children
        """
        return (self.left, self.right)

    def nodes(self):
        """
        Alias for the children() method. Returns the left and right children.
        
        :return: A tuple containing the left and right children
        """
        return (self.left, self.right)

    def __str__(self):
        """
        String representation of the node, displaying the left and right children.
        
        :return: A string combining the left and right children
        """
        return '%s_%s' % (self.left, self.right)


# Function to generate Huffman codes from the Huffman tree
def huffman_code_tree(node, left=True, binString=''):
    """
    Traverse the Huffman tree and generate binary codes for each character.
    
    :param node: The current node of the Huffman tree (could be a NodeTree object or a character)
    :param left: A boolean to differentiate between left (True) and right (False) traversal
    :param binString: The current binary string (Huffman code) being built
    :return: A dictionary mapping characters to their respective Huffman codes
    """
    if type(node) is str:
        # Base case: If the node is a leaf (a character), return its binary code
        return {node: binString}
    
    # Recursively generate Huffman codes for left and right children
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))  # Left child: append '0'
    d.update(huffman_code_tree(r, False, binString + '1'))  # Right child: append '1'
    return d


# Step 1: Calculate the frequency of each character in the input string
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

# Sort characters by their frequencies in descending order
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Step 2: Build the initial list of nodes (characters with their frequencies)
nodes = freq

# Step 3: Construct the Huffman tree by combining the least frequent nodes
while len(nodes) > 1:
    # Extract the two least frequent nodes
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    
    # Remove these two nodes from the list
    nodes = nodes[:-2]
    
    # Create a new internal node with these two nodes as children
    node = NodeTree(key1, key2)
    
    # Add the new node back to the list with the combined frequency
    nodes.append((node, c1 + c2))
    
    # Sort the nodes again by frequency in descending order
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

# Step 4: Generate the Huffman codes using the tree
huffmanCode = huffman_code_tree(nodes[0][0])

# Step 5: Display the Huffman codes for each character
print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))
