# EasiScript
## versions
- EasiScript v1.0 
- EasiScript v1.1 
- [EasiScriptX](https://github.com/PulewaveSoftware/EasiScriptX).

## Introduction  
EasiScript is a beginner-friendly, simplified programming language designed to make coding more accessible.  EasiScript offers a flexible syntax that allows developers to choose from multiple commands to perform the same operation. This flexibility increases ease of use and makes the language approachable for beginners and versatile for experienced developers.

## EasiScript 1.0 (Outdated, Not Recommended, not working properly) 
EasiScript 1.0 , the first version of EasiScript, Written in **Python** provided the foundation for a simplified coding experience with features including:
- Multiple syntax options for common operations
- Simplified arithmetic, conditional, and loop operations
- Easy-to-understand function definitions
- Support for lists and dictionaries
- Basic file handling and error management


While these features made EasiScript 1.0 a great starting point, There were many, many problems with it, so it has to be solved. leading to the development of EasiScript 1.1.


*If you want to know more about EasiScript v1.0, refer documentation. Since it is no longer supported, Detailed functions won't be displayed here.* 

## EasiScript 1.1 (Coming Soon)

EasiScript 1.1 marks a major update, bringing the language to a new level of functionality and performance. Written entirely in C++, this version is built to offer a robust and efficient programming environment. Only Lexer and Parser have been completed. While Interpreter is still in development, EasiScript 1.1 is set to introduce powerful features and enhancements, including:

### Technical Overview
- **Language Core**: Built from the ground up in C++, EasiScript 1.1 offers a high-performance execution environment.
- **Lexer and Parser**: The lexer supports 127 commands, offering a rich set of operations while the parser efficiently processes the syntax into meaningful code.
- **Interpreter**: Although under development, the interpreter is designed to accurately execute EasiScript commands, bridging the gap between EasiScript's flexible syntax and C++'s powerful execution capabilities.

### Key Features
- **Expanded Command Set**: EasiScript 1.1 expands on its predecessor by supporting 127 distinct commands, offering even greater flexibility and power.
- **Modular Design**: The language architecture is modular, allowing for future extensions and easy updates.
- **Cross-Platform Compatibility**: Thanks to the C++ foundation, EasiScript 1.1 will be compatible with a wide range of systems, ensuring that developers can code in their preferred environment.
- **Error Handling and Debugging**: Enhanced error handling features and better debugging support, thanks to integration with tools like GitHub Copilot and ChatGPT.
- **Automatic Memory Management and Garbage Collection In Interpreter** : You don't have to worry about memory mangement, The Interpreter automaticly collects unwanted stuff (Garbage).

### Print Function Syntax
```
print "Hello, World!"
display "Hello, World!"
say "Hello, World!"
show "Hello, World!"
```
All these will output:
```
Hello, World!
```


### Variable Assignment
```
set x = 10;
set name = "EasiScript 1.1";
```

### Arithmetic Operations
```
sum 5 + 3;
subtract 10 - 4;
times 2 * 6;
divide 8 / 2;
```
### Control Flow
```
if x > 10:
    print "x is greater than 10";
else:
    print "x is 10 or less";
```
### Loops
```
while x < 10:
    print x;
    set x = x + 1;
```
## Example programmes:
### Print function
`````EasiScript
print "Hello, World!"
display "Hello, World!"
say "Hello, World!"
show "Hello, World!"
`````
all these commands will output:
**Hello, World!** 

### Varible assign function
````` 
set x = 10;
set name = "EasiScript";
`````
### Arithmetic Functions
``````
sum add 5 + 3;          # Addition
subtract 10 - 4;        # Subtraction
times 2 * 6;            # Multiplication
divide 8 / 2;           # Division
``````
Or Use "print" 
`````
print 5 + 3;            # Outputs: 8
print 10 - 4;           # Outputs: 6
print 2 * 6;            # Outputs: 12
print 8 / 2;            # Outputs: 4
`````

### Control Flow - Conditional Statement functions
`````
set x = 15;

if x > 10:
    print "x is greater than 10";
else:
    print "x is 10 or less";
`````
This would output:
`````
x is greater than 10
`````
###  Loop Function 
`````
set x = 0;

while x < 5:
    print x;
    set x = x + 1;
`````
This would output:
`````
0
1
2
3
4
`````

### Lists function
`````
set fruits = ["apple", "banana", "cherry"];
print fruits[0];        
`````
Output: 
`````
Apple
`````
### Dictionaries Function
`````
set person = {"name": "John", "age": 30};
print person["name"];  
`````
Output:
`````
John
`````
### Comments
`````
# This is a single-line comment
print "This will print";  # This is an inline comment
`````

### File Handling Functions
`````
file open "example.txt" as f;
print f.read();
file close f;
`````
### Error Handling Functions
`````
try:
    divide 5 / 0;
except:
    print "Error: Division by zero!";
`````
This would output:
`````
Error: Division by zero!
`````
*These examples demonstrate the flexibility and simplicity of EasiScript, allowing users to perform various operations with intuitive commands.*

# All 127 Commands list

## Basic Commands
- `print`
- `display`
- `say`
- `show`

## Variable Assignment
- `set`
- `assign`

## Arithmetic Operations
- `sum`
- `add`
- `subtract`
- `times`
- `multiply`
- `divide`
- `mod`
- `increment`
- `decrement`

## Logical Operations
- `and`
- `or`
- `not`
- `equal`
- `greater`
- `less`
- `greater_or_equal`
- `less_or_equal`

## Conditional Statements
- `if`
- `else`
- `elif` (else if)
- `endif`
- `switch`
- `case`
- `default`
- `endcase`

## Loops
- `while`
- `for`
- `loop`
- `do`
- `until`
- `break`
- `continue`

## Functions
- `function`
- `endfunction`
- `return`
- `call`
- `def`

## Lists and Arrays
- `list`
- `append`
- `insert`
- `remove`
- `pop`
- `slice`
- `length`
- `index`
- `sort`
- `reverse`

## Dictionaries and Maps
- `dict`
- `set_key`
- `get_key`
- `remove_key`
- `has_key`
- `keys`
- `values`
- `items`

## File Handling
- `open`
- `read`
- `write`
- `close`
- `delete`
- `rename`
- `exists`

## Input/Output
- `input`
- `output`
- `readline`
- `writeline`
- `clear`

## Error Handling
- `try`
- `except`
- `finally`
- `raise`
- `assert`

## Math Functions
- `sqrt`
- `pow`
- `abs`
- `min`
- `max`
- `round`
- `ceil`
- `floor`
- `random`

## String Manipulation
- `concat`
- `split`
- `replace`
- `substring`
- `upper`
- `lower`
- `strip`
- `startswith`
- `endswith`

## Date and Time
- `now`
- `today`
- `timestamp`
- `format_date`
- `parse_date`
- `sleep`

## System Commands
- `execute`
- `run`
- `shell`
- `exit`
- `clear`
- `pause`

## Debugging
- `debug`
- `log`
- `trace`
- `inspect`
- `profile`

## Networking
- `connect`
- `disconnect`
- `send`
- `receive`
- `ping`

## Advanced Operations
- `thread`
- `lock`
- `unlock`
- `signal`
- `wait`
- `notify`

## Graphics and UI
- `draw`
- `render`
- `update`
- `clear_screen`
- `set_color`
- `set_font`
- `show_message`
- `hide_message`

## Miscellaneous
- `noop`
- `alias`
- `define`
- `include`
- `require`
- `import`
- `export`
- `namespace`

## End of Commands
This list includes all the 127 commands that are currently supported by EasiScript 1.1.

## Tools and Software used:
The development of EasiScript 1.1 is supported by a suite of powerful tools:

- C++ Compiler: MinGW is used as the compiler, ensuring efficient and fast code compilation.
- IDE: Visual Studio Code 2019 serves as the primary IDE, providing a feature-rich environment for coding.
- GitHub Copilot: Assisting in code writing by providing intelligent code suggestions.
- ChatGPT: Used for debugging support and helps troubleshoot issues during development.

## Looking ahead
EasiScript 1.1 is poised to be a game-changer in the world of beginner-friendly programming languages. With a robust C++ core, expanded command set, and enhanced features, it promises to be both powerful and accessible. Stay tuned for more updates as we finalize the interpreter and polish the language for release!

## License
This project is licensed under the MIT License.


