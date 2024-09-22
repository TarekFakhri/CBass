class CBassVirtualMachine:
    def __init__(self, bytecode):
        self.bytecode = bytecode
        self.variables = {}  # Dictionary to store variable values
        self.instruction_pointer = 0  # Track the instruction pointer

    def run(self):
        while self.instruction_pointer < len(self.bytecode):
            instr = self.bytecode[self.instruction_pointer]
            self.execute_instruction(instr)
    
    def execute_instruction(self, instr):
        if isinstance(instr, str) and instr.startswith('DECL'):
            # Handle declaration (e.g., DECL fish num_fish 3)
            parts = instr.split()
            var_type = parts[1]  # fish, floatfish, etc.
            var_name = parts[2]
            value = parts[3]
            
            # Handle different types correctly
            if var_type == 'fish':
                self.variables[var_name] = int(value)  # fish is treated as int
            elif var_type == 'floatfish':
                self.variables[var_name] = float(value)  # floatfish is treated as float
            elif var_type == 'algae':
                self.variables[var_name] = value  # algae is treated as string (no conversion)
            
            # Advance the instruction pointer
            self.instruction_pointer += 1

        elif isinstance(instr, str) and instr.startswith('PRINT'):
            # Handle print (splash)
            parts = instr.split(' ', 1)
            value = parts[1]

            # Check if it's a variable in the VM
            if value in self.variables:
                self.output(self.variables[value])  # Print the value of the variable
            else:
                self.output(value)  # Print the literal value (like a string)
            self.instruction_pointer += 1

        elif instr[0] == 'if':
            # Handle if condition
            condition_var = instr[1]
            operator = instr[2]
            condition_value = int(instr[3])

            if self.evaluate_condition(self.variables[condition_var], operator, condition_value):
                # If condition is true, execute the 'if' body (next instruction)
                self.execute_instruction(instr[4])
                # Skip the else part by advancing the instruction pointer to skip over it
                self.instruction_pointer += 2  # Skip the 'else' block and move past it
            else:
                # If condition is false, execute the 'else' block, if present
                if len(instr) > 5 and instr[5] == 'else':
                    self.execute_instruction(instr[6])
                self.instruction_pointer += 1

        elif instr[0] == 'swim':
            # Handle swim loop (like a for loop)
            loop_var = instr[1]          # Loop variable (e.g., 'i')
            init_value = int(instr[2])    # Initial value (e.g., '0')
            condition_var = instr[3]      # Condition variable (e.g., 'i')
            condition_op = instr[4]       # Condition operator (e.g., '<')
            condition_value = int(self.variables[instr[5]])  # Condition value (e.g., 'num_fish')
            increment_var = instr[6]      # Increment variable (e.g., 'i')
            increment_value = int(instr[8])  # Increment value (e.g., '1')

            # Initialize loop variable
            self.variables[loop_var] = init_value

            # Perform the loop while the condition is true
            while self.evaluate_condition(self.variables[loop_var], condition_op, condition_value):
                # Execute the body of the loop
                # Resolve the loop variable for the splash instruction
                loop_body = instr[9]
                if loop_body[0] == 'splash' and loop_body[1] == loop_var:
                    self.output(self.variables[loop_var])  # Output the value of the loop variable
                else:
                    self.execute_instruction(loop_body)  # Execute non-loop body instruction

                # Increment the loop variable
                self.variables[increment_var] += increment_value

            # After the loop ends, move the instruction pointer
            self.instruction_pointer += 1



    def output(self, value):
        if isinstance(value, str) and value.startswith('"') and value.endswith('"'):
            print(value[1:-1])  # Remove quotes for printing
        else:
            print(value)

    def evaluate_condition(self, left_value, operator, right_value):
        # Evaluate the if/swim condition
        if operator == '>':
            return left_value > right_value
        elif operator == '<':
            return left_value < right_value
        elif operator == '==':
            return left_value == right_value
        elif operator == '>=':
            return left_value >= right_value
        elif operator == '<=':
            return left_value <= right_value
        else:
            raise ValueError(f"Unknown operator {operator}")
