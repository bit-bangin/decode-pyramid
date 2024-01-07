def decode(message_file):
    """
    Function designed to decode a message encoded within a text file, 
    where each line of the file should be formatted with a number and a word, separated 
    by a space. The file's path is passed as an argument to the function. The number on 
    each line dictates the word's placement in the decoded message, based on a unique 
    pyramid-like numerical pattern.
    """
    # open and read the file
    with open(message_file, "r") as file:
        # read contents of file
        lines = file.readlines()

    # create a dictionary to store the words
    words = {}

    # iterate through lines and populate dictionary
    for line in lines:
        try:
            number, word = line.strip().split(" ")
            words[int(number)] = word
        except ValueError:
            print (f"Error processing line: {line}")
            continue

    # sort the numbers in ascending order
    sorted_numbers = sorted(words.keys())

    # arrange the numbers in a pyramid-like structure
    pyramid = []
    row_length = 1
    while sorted_numbers:
        row = sorted_numbers[:row_length]
        if row:
            pyramid.append(row)
            sorted_numbers = sorted_numbers[row_length:]
        row_length += 1

    # Decode the message using the last number of each row
    decoded_words = [words[line[-1]] for line in pyramid if line]

    # return the decoded message as STR
    return " ".join(decoded_words)

result = decode("coding_qual_input.txt")
print(result)

"""
The decode() function is designed to decode a message encoded within a text file, where each line 
of the file should be formatted with a number and a word, separated by a space. The file's path 
is passed as an argument to the function. The number on each line dictates the word's placement 
in the decoded message, based on a unique pyramid-like numerical pattern.

Upon execution, decode() performs the following steps:

  1. File Reading
      Opens the specified file in read mode and reads all its lines into a list using readlines().
  2. Dictionary Initialization
      Initializes an empty dictionary, words, mapping numbers (as keys) to words (as values). It 
      iterates over each line, splitting the line into a number and a word, converts the number to an 
      integer, and populates the words dictionary. If a line doesn't conform to the expected format, 
      an error message is printed, and the function continues to the next line.
  3. Sorting Numbers
      Sorts the keys of the words dictionary in ascending order and stores them in sorted_numbers.
  4. Pyramid Structure Creation
      Generates a pyramid-like structure, where each subsequent line contains one more element than 
      the previous, by sequentially selecting numbers from sorted_numbers.
  5. Decoding the Message
      Initializes an empty list, decoded_words. For each line in the pyramid, it takes the last number, 
      retrieves the corresponding word from the words dictionary, and appends this word to decoded_words.
  6. Returning the Decoded Message
      Joins all words in decoded_words into a single string using the join() method and returns this 
      string as the decoded message.

This function reconstructs the original message based on a specific numerical pattern derived from 
the input file, forming a distinctive decoding methodology.
"""
