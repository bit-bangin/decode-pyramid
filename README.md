# decode-pyramid
Repository for a function designed to decode a message encoded within a text file. 

## Requirements
  1. Create a function called `decode(message_file)`
  2. `decode(message_file)` should have the following functionality:
        - read an encoded message from a .txt file
        - decode encoded message
        - return the decoded version as STR
  
## Assumptions
The encoded message will be in the following format:
  - 3 love
  -  6 computers
  -  2 dogs
  -  4 cats
  -  1 I
  -  5 you

## Functionality
1. Read the file
    - functions:  `open()`
    - methods:    `readlines()`
2. Decode the message
    - Separate each number from the associated word.
       - functions:
       - methods:    `split()`, `strip()`
    - Order all numbers from smallest to biggest. Arrange them like a pyramid, where each line +1 than previous line. 
       - functions:
       - methods:    `append()`
    - For example, the numbers above would be arranged like this:
      - 1
      - 2 3
      - 4 5 6
    - Take the number at the end of each line (1, 3, 6) and use it to find the corresponding word in the message.

4. Return the decoded message as a string  "I love computers"
     - funtions:
     - methods:    `join()`
