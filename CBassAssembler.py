class CBassAssembler:
    def __init__(self, instructions):
        self.instructions = instructions
        self.bytecode = []

    def assemble(self):
        for instr in self.instructions:
            if isinstance(instr, tuple):
                if instr[0] == 'if':
                    # Handle the if instruction
                    self.bytecode.append(('if', instr[1], instr[2], instr[3], instr[4]))
                    if len(instr) == 7:  # if there is an else block
                        self.bytecode.append(('else', instr[6]))
                elif instr[0] == 'swim':
                    # Handle the swim loop
                    self.bytecode.append(('swim', instr[1], instr[2], instr[3], instr[4], instr[5], instr[6], instr[7], instr[8], instr[9]))
            else:
                if instr.startswith('DECL'):
                    self.bytecode.append(instr)
                elif instr.startswith('PRINT'):
                    self.bytecode.append(instr)

    def assemble_declaration(self, instr):
        parts = instr.split()
        return f'PUSH {parts[3]}'

    def assemble_print(self, instr):
        parts = instr.split()
        return f'OUTPUT {parts[1]}'

    def get_bytecode(self):
        return self.bytecode
