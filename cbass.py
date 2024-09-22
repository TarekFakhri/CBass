import sys
from CBassTokenizer import CBassTokenizer
from CBassParser import CBassParser
from CBassCodeGenerator import CBassCodeGenerator
from CBassAssembler import CBassAssembler
from CBassVirtualMachine import CBassVirtualMachine

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 cbass.py <source-file>")
        return

    # Read the source file
    source_file = sys.argv[1]
    with open(source_file, 'r') as f:
        code = f.read()

    # Tokenize the code
    tokenizer = CBassTokenizer(code)
    tokens = tokenizer.get_tokens()

    # Parse the tokens into an AST (Abstract Syntax Tree)
    parser = CBassParser(tokens)
    ast = parser.parse()

    # Generate intermediate code (instructions) from the AST
    code_generator = CBassCodeGenerator(ast)
    code_generator.generate()
    instructions = code_generator.instructions

    # Assemble the instructions into bytecode
    assembler = CBassAssembler(instructions)
    assembler.assemble()
    bytecode = assembler.bytecode

    # Execute the bytecode in the virtual machine
    vm = CBassVirtualMachine(bytecode)
    vm.run()

if __name__ == "__main__":
    main()
