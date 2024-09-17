# Huffman-Coding

Overview
This project implements Huffman Coding, a lossless data compression algorithm that assigns variable-length codes to characters based on their frequencies. The goal of this implementation is to compress a string by encoding the characters into binary codes such that the most frequent characters have the shortest codes.

Features
Frequency Calculation: The program calculates the frequency of each character in the input string.
Huffman Tree Construction: A binary tree is built using the characters and their frequencies.
Huffman Code Generation: The program assigns binary codes to each character based on the tree structure.
Display Huffman Codes: The Huffman code for each character in the string is displayed in a table.
Code Structure
NodeTree Class: This class represents a node in the Huffman tree. Each node can have two children (left and right), which can either be other nodes or characters from the string.

huffman_code_tree() Function: This recursive function traverses the Huffman tree and generates binary codes for each character.

Main Logic: The main part of the code calculates character frequencies, builds the Huffman tree, and then generates and prints the Huffman codes.

How Huffman Coding Works
Frequency Calculation: The frequency of each character in the input string is determined.
Tree Construction: A binary tree is built where each character is a leaf, and the nodes represent the combined frequency of their children. The least frequent characters are positioned deeper in the tree.
Code Assignment: Binary codes are assigned to each character by traversing the tree. A '0' is appended when moving left, and a '1' is appended when moving right.
Compression: The resulting binary codes can be used to compress the string efficiently, where more frequent characters are assigned shorter codes.
Requirements
Python 3.x
No additional libraries required.

Contribution
If you would like to contribute to this project, feel free to open an issue or submit a pull request.
