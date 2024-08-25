# EasiScript

EasiScript is a beginner-friendly, simplified programming language inspired by Python, C, and C++. It aims to make coding more accessible by offering multiple, easy-to-understand commands for performing the same operations. This allows developers to use the syntax they are most comfortable with, increasing flexibility and ease of use.

## Features
- Multiple syntax options for common operations
- Simplified arithmetic, conditional, and loop operations
- Easy-to-understand function definitions
- Support for lists and dictionaries
- Basic file handling and error management

## Installation & Setup
### Prerequisites
- **Python 3.6+**: EasiScript is built using Python, so you'll need Python installed on your machine.

### Setup
1. Download the EasiScript project files from the [GitHub repository](#).
2. Unzip the downloaded file.
3. Open a terminal and navigate to the directory containing the project files.
4. Run your EasiScript files with the following command:
   ```bash
   python easiscript_lexer.py hello_world.es
### Usage
**Printing to Console**

EasiScript provides multiple commands to print output to the console:

print "Hello, World!";
display "Hello, World!";
say "Hello, World!";
show "Hello, World!";
All of these commands will produce the same output: Hello, World!.

### Variables and Data Types

Assign values directly to variables without explicit type declaration:
set x = 10;
set name = "EasiScript";
### Arithmetic Operations

Simplify arithmetic operations with commands:
sum add 5 + 3;
subtract 10 - 4;
times 2 * 6;
divide 8 / 2;

Or use:

print 5 + 3;
print 10 - 4;
print 2 * 6;
print 8 / 2;

### Comments
Comments are initiated with the # symbol:
**#This is a single-line comment**
### Control Flow
Conditional Statements
Example of an **if** statement:


if x > 10:
    print "x is greater than 10";
else:
    print "x is 10 or less";

### Loops

Example of a while loop:

while x < 10:
    print x;
    set x = x + 1;
### Contributing
To contribute to EasiScript, follow these steps:

Fork the repository.
Create a new branch for your changes.
Make your changes and commit them.
Push your changes to your forked repository.
Submit a pull request with a clear description of your changes.
### License
This project is licensed under the MIT License.

### Troubleshooting EasiScript Execution

If the command `python easiscript_lexer.py hello_world.es` is not behaving as expected, try the following steps:

1. **Check File Paths**: Ensure `easiscript_lexer.py` and `hello_world.es` are in the same directory or provide the correct path.

2. **Verify Python Installation**: Ensure Python 3.6+ is properly installed and added to your system’s PATH.

3. **Check for Errors**: Look for error messages in the terminal when you run the script. These can provide clues about what might be going wrong.

4. **Review Script Code**: Verify that `easiscript_lexer.py` is correctly implemented and can handle `.es` files. 

5. **Update the Script**: Ensure that `easiscript_lexer.py` is compatible with the latest version of Python and the EasiScript syntax.


