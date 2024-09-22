# C Bass Language 🐟

Welcome to **C Bass**, a fish-themed programming language designed to help children learn the basics of programming! 🐠 Inspired by the C language, C Bass incorporates simple syntax and concepts, making it fun and easy for beginners to get started with coding.

## Features

- **User-Friendly Constructs**: Includes basic programming structures like variable declaration, loops, conditionals, and output.
- **Simple Printing**: Use `splash()` to print text or variables to the console.
- **Conditional Logic**: Make decisions using `if` and `else`.
- **Loops**: Use the `swim` loop for iteration over ranges.

## Syntax Overview

### Variable Declaration
- Use `fish` for integers.
- Use `floatfish` for floats.
- Use `algae` for strings.

Example:
```
fish num_fish = 3;
floatfish fish_weight = 4.5;
algae fish_name = "Goldfish";
```

### Output (Splash)
Use splash() to print strings or variables to the console.

Example:
```
splash("Welcome to the ocean!");
splash("The fish name is:");
splash(fish_name);
```

### Conditionals (If-Else)
Make decisions with if and else.

Example:
```
if (num_fish > 2)
    splash("We have a big school of fish!");
else
    splash("Just a small group of fish here.");
```

### Loops (Swim)
Use the swim loop to iterate through a range of numbers.

Example:
```
swim (fish i = 0; i < num_fish; i = i + 1)
    splash(i);
```
## File Descriptions

- **cbass.py**: Main entry point to compile and run C Bass programs.

- **CBassTokenizer.py**: Tokenizes C Bass source code into tokens for parsing.

- **CBassParser.py**: Parses tokens into an abstract syntax tree (AST) for further processing.

- **CBassCodeGenerator.py**: Converts the AST into a set of instructions.

- **CBassAssembler.py**: Assembles instructions into bytecode for execution.

- **CBassVirtualMachine.py**: Executes the bytecode and simulates the C Bass virtual machine.

- **fishEstimate.cbass**: A sample C Bass program demonstrating variables, conditionals, and loops.

## How to Use C Bass

1. Clone the repository:
```
git clone https://github.com/your-username/cbass-language.git
cd cbass-language
```
2. Run the C Bass program:
```
python3 cbass.py fishEstimate.cbass
This will compile and execute the fishEstimate.cbass program.
```
### Example Code

The fishEstimate.cbass program:

```
fish num_fish = 3;
floatfish fish_weight = 4.5;
algae fish_name = "Goldfish";

splash("Welcome to the ocean!");
splash("The fish name is:");
splash(fish_name);

if (num_fish > 2)
    splash("We have a big school of fish!");
else
    splash("Just a small group of fish here.");

swim (fish i = 0; i < num_fish; i = i + 1)
    splash(i);
```

### Example Output

For the sample program fishEstimate.cbass, the output will be:
```
Welcome to the ocean!
The fish name is:
Goldfish
We have a big school of fish!
0
1
2
```

## Project Structure
The project is composed of several key components:

- **Tokenizer**: Splits the source code into meaningful tokens.
- **Parser**: Converts the tokens into an AST (Abstract Syntax Tree).
- **Code Generator**: Generates intermediate instructions based on the AST.
- **Assembler**: Converts instructions into bytecode.
- **Virtual Machine**: Executes the bytecode and simulates the program behavior.


## How It Works

- **Tokenization**: The C Bass code is first split into tokens by CBassTokenizer.py.
- **Parsing**: The tokens are parsed into an Abstract Syntax Tree (AST) by CBassParser.py.
- **Code Generation**: The AST is converted into a set of intermediate instructions by CBassCodeGenerator.py.
- **Assembly**: These instructions are assembled into bytecode by CBassAssembler.py.
- **Execution**: The bytecode is executed by the virtual machine (CBassVirtualMachine.py), which simulates the behavior of the program.

## Contributing

We welcome contributions! Whether it's reporting bugs, suggesting features, or submitting pull requests, we appreciate your help in improving C Bass.


Steps to Contribute:

1. Fork the repository.

2. Create a new branch for your feature or bugfix.

3. Commit your changes and create a pull request.

## Contact

For any questions, feel free to reach out via GitHub Issues or submit a pull request!

Happy coding with C Bass! 🐠
