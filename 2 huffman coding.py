import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def generate_huffman_tree(chars, freq):
    pq = []
    
    # Create priority queue of nodes
    for i in range(len(chars)):
        heapq.heappush(pq, Node(freq[i], chars[i]))
    
    while len(pq) > 1:
        # Remove two nodes with lowest frequency
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        
        # Create a new internal node with combined frequency
        new_node = Node(left.freq + right.freq, None, left, right)
        
        # Push the new node back into the priority queue
        heapq.heappush(pq, new_node)
    
    # Return the root of the Huffman tree
    return pq[0]

def generate_huffman_codes(node, current_code, huffman_codes):
    if node.symbol is not None:
        huffman_codes[node.symbol] = current_code
    else:
        generate_huffman_codes(node.left, current_code + "0", huffman_codes)
        generate_huffman_codes(node.right, current_code + "1", huffman_codes)

def print_huffman_codes(root):
    huffman_codes = {}
    generate_huffman_codes(root, "", huffman_codes)
    
    print("Huffman Codes:")
    for symbol, code in huffman_codes.items():
        print(f"{symbol} -> {code}")

def main():
    n = int(input("Enter number of characters: "))
    chars = []
    freq = []
    
    for i in range(n):
        char = input(f"Enter character {i + 1}: ")
        chars.append(char)
        f = int(input(f"Enter frequency for {char}: "))
        freq.append(f)

    root = generate_huffman_tree(chars, freq)
    print_huffman_codes(root)

if __name__ == "__main__":
    main()
