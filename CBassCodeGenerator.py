class CBassCodeGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.instructions = []

    def generate(self):
        for node in self.ast:
            self.generate_code(node)

    def generate_code(self, node):
        node_type = node[0]
        if node_type == 'declaration':
            self.generate_declaration(node)
        elif node_type == 'splash':
            self.generate_splash(node)
        elif node_type == 'if':
            self.generate_if(node)
        elif node_type == 'swim':
            self.generate_swim(node)

    def generate_if(self, node):
        # Extract the condition and true/false blocks from the node
        var_name, operator, value = node[1], node[2], node[3]  # The condition part (e.g., num_fish > 2)
        true_block = node[4]  # The 'if' true block (e.g., splash)
        
        # Check if there's an 'else' block
        if len(node) == 7:
            false_block = node[6]  # The 'else' block (e.g., splash)
            self.instructions.append(('if', var_name, operator, value, true_block, 'else', false_block))
        else:
            # No else block
            self.instructions.append(('if', var_name, operator, value, true_block))

    def generate_swim(self, node):
        # Extract parts of the swim node
        var_name = node[1]          # Loop variable (e.g., 'i')
        init_value = node[2]        # Initial value (e.g., '0')
        condition_var = node[3]     # Condition variable (e.g., 'i')
        condition_op = node[4]      # Condition operator (e.g., '<')
        condition_value = node[5]   # Condition value (e.g., 'num_fish')
        increment_var = node[6]     # Increment variable (e.g., 'i')
        increment_expr_var = node[7]# Expression variable (e.g., 'i')
        increment_value = node[8]   # Increment value (e.g., '1')
        loop_body = node[9]         # The body of the loop (e.g., ('splash', 'i'))

        # Add the instruction for the swim loop
        self.instructions.append(('swim', var_name, init_value, condition_var, condition_op, condition_value, increment_var, increment_expr_var, increment_value, loop_body))


    def generate_declaration(self, node):
        var_type, var_name, value = node[1:]
        self.instructions.append(f'DECL {var_type} {var_name} {value}')

    def generate_splash(self, node):
        value = node[1]
        self.instructions.append(f'PRINT {value}')

    def get_instructions(self):
        return self.instructions
