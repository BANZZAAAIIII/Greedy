import math


# Node Class for creating the binary tree
class Node(object):
    left = None
    right = None
    item = None
    frequency = 0

    def __init__(self, char, frequency, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right


def sort_by_frequency(node):
    return node.frequency * 1000000 + ord(node.char[0])  # Sort by frequency or alphabetical if conflict


# Class for using the algorithm and encoding a message
class HuffmanEncoder:
    def __init__(self):
        self.chars = {}
        self.huffmancodes = {}
        self.tree = []
        self.message = ""

    # Finds the frequency of each character in the message
    def frequency_analysis(self):
        self.chars = {}
        for char in self.message:
            self.chars[char] = self.chars.get(char, 0) + 1

    # Goes through the tree to create the codes
    def traverse_tree(self, node, path=""):
        if node.left == None:
                self.huffmancodes[node.char] = path
        else:
            self.traverse_tree(node.left, path + "0")
            self.traverse_tree(node.right, path + "1")

    def encode(self, message):
        self.message = message

        # Finds the characters and their frequency
        self.frequency_analysis()

        # Convert list of symbols into a binary Tree structure
        # Step 1: Generate list of Nodes...
        # Generate a list of nodes
        self.tree = []
        for char in self.chars.keys():
            self.tree.append((Node(char, self.chars[char], None, None)))

        # Sort the nodes in the tree based on frequency of the characters
        self.tree.sort(key=sort_by_frequency)

        # Sorts the nodes into a binary tree until there is only one root node
        while len(self.tree) > 1:
            left_node = self.tree.pop(0)
            right_node = self.tree.pop(0)
            new_node = Node(left_node.char + right_node.char, left_node.frequency + right_node.frequency, left_node,
                           right_node)
            self.tree.append(new_node)
            self.tree.sort(key=sort_by_frequency)

        # Create the Huffman Codes for each character
        self.huffmancodes = {}
        self.traverse_tree(self.tree[0])

        encoded_message = ""

        # Add the characters and their codes to the start of the text
        for char in self.huffmancodes.keys():
            code = self.huffmancodes[char]
            encoded_message = encoded_message + char + code

        encoded_message = encoded_message + "message:"

        # Encode the message using the Huffman Codes
        for char in message:
            encoded_message = encoded_message + self.huffmancodes[char]

        self.print_codes()
        return encoded_message

    def fixed_length_encode(self, message):
        max_code_length = math.ceil(math.log(len(self.chars), 2))
        temp_dict, code_dict = {}, {}
        counter = 0
        for key in self.chars:
            temp_dict[key] = bin(counter)[2:].zfill(max_code_length)
            counter += 1

        encoded_message = ''
        # Add the characters and their codes to the start of the text
        for char in temp_dict.keys():
            code = temp_dict[char]
            encoded_message = encoded_message + char + code


        encoded_message = encoded_message + "message:"

        # Encode the message using the Huffman Codes
        for char in message:
            encoded_message = encoded_message + temp_dict[char]

        for char in temp_dict.keys():
            print(f'Character: {char}, Code: {temp_dict[char]}')

        return encoded_message

    def print_codes(self):

        for char in self.huffmancodes.keys():
            print(f'Character: {char}, Code: {self.huffmancodes[char]}')


def main():
    message = "In this assignment, you should make a lossless compressor using Huffman coding. " \
              "Make an application that can take as input an arbitrary text consisting of the 29 Norwegian characters " \
              "and compress the text using:"

    encoder = HuffmanEncoder()
    print("Variable length: ")
    encoded_message = encoder.encode(message)
    print(encoded_message)

    print('\n')
    print("Fixed length: ")
    encoded_message = encoder.fixed_length_encode(message)
    print(encoded_message)


if __name__ == '__main__':
    main()