import cv2
import heapq
from collections import defaultdict

class Node:
    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(frequencies):
    heap = [Node(pixel, freq) for pixel, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_huffman_codes(root, current_code, huffman_codes):
    if root is None:
        return

    if root.value is not None:
        huffman_codes[root.value] = current_code
        return

    generate_huffman_codes(root.left, current_code + '0', huffman_codes)
    generate_huffman_codes(root.right, current_code + '1', huffman_codes)

def huffman_encoding(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is valid
    if image is None:
        print("Unable to read the image.")
        return

    # Flatten the 2D array into a 1D sequence
    flat_sequence = image.flatten()

    # Calculate pixel frequencies
    frequencies = defaultdict(int)
    for pixel in flat_sequence:
        frequencies[pixel] += 1

    # Build Huffman tree
    huffman_tree = build_huffman_tree(frequencies)

    # Generate Huffman codes
    huffman_codes = {}
    generate_huffman_codes(huffman_tree, '', huffman_codes)

    # Encode the image
    encoded_data = ''.join(huffman_codes[pixel] for pixel in flat_sequence)

    return encoded_data, huffman_tree

# Example usage
image_path =  r'C:\Users\admin\Downloads\XLA\image\gojo.jpg'  # Change the path to your actual image
encoded_data, huffman_tree = huffman_encoding(image_path)

print("Encoded Data Length:", len(encoded_data))
print("Huffman Tree:", huffman_tree)
