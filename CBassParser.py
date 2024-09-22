class CBassParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        ast = []  # Abstract Syntax Tree
        while self.position < len(self.tokens):
            ast.append(self.parse_statement())  # Parse each statement
        return ast

    def parse_statement(self):
        token = self.get_current_token()

        if token == 'fish' or token == 'floatfish' or token == 'algae':
            return self.parse_declaration()
        elif token == 'splash':
            return self.parse_splash()
        elif token == 'if':
            return self.parse_if_statement()
        elif token == 'swim':
            return self.parse_swim()
        else:
            raise SyntaxError(f"Unexpected token: {token}")

    def parse_declaration(self):
        var_type = self.get_current_token()  # e.g., fish, floatfish, algae
        self.advance()
        var_name = self.get_current_token()
        self.advance()
        self.expect('=')
        value = self.get_current_token()
        self.advance()
        self.expect(';')
        return ('declaration', var_type, var_name, value)

    def parse_splash(self):
        self.expect('splash')
        self.expect('(')
        value = self.get_current_token()
        self.advance()
        self.expect(')')
        self.expect(';')
        return ('splash', value)

    def parse_if_statement(self):
        self.expect('if')
        self.expect('(')
        var_name = self.get_current_token()
        self.advance()
        operator = self.get_current_token()
        self.advance()
        value = self.get_current_token()
        self.advance()
        self.expect(')')

        # Parse the true block
        true_block = self.parse_block()

        if self.get_current_token() == 'else':
            self.advance()
            false_block = self.parse_block()
            return ('if', var_name, operator, value, true_block, 'else', false_block)
        return ('if', var_name, operator, value, true_block)

    def parse_swim(self):
        self.expect('swim')
        self.expect('(')
        
        # Skip over the type declaration (e.g., 'fish' or 'floatfish')
        loop_type = self.get_current_token()  # Should be 'fish', 'floatfish', etc.
        self.advance()

        # Parse initialization: e.g., 'i = 0;'
        var_name = self.get_current_token()  # This should now be 'i'
        self.advance()
        
        self.expect('=')  # Expecting '=' after the loop variable 'i'
        init_value = self.get_current_token()  # This should be '0'
        self.advance()
        self.expect(';')  # Expecting semicolon to end initialization
        
        # Parse condition: e.g., 'i < num_fish;'
        loop_var = self.get_current_token()  # This should be 'i'
        self.advance()
        
        condition_op = self.get_current_token()  # This should be '<'
        self.advance()
        
        condition_value = self.get_current_token()  # This should be 'num_fish'
        self.advance()
        self.expect(';')  # Expecting semicolon to end the condition part
        
        # Parse increment: e.g., 'i = i + 1'
        increment_var = self.get_current_token()  # This should be 'i'
        self.advance()
        
        self.expect('=')  # Expecting '=' after the loop variable 'i'
        increment_expr_var = self.get_current_token()  # This should be 'i'
        self.advance()
        
        increment_value = self.get_current_token()  # This should be '1'
        self.advance()
        
        self.expect(')')  # Expecting closing parenthesis to end the loop declaration
        
        # Parse the body of the loop
        loop_body = self.parse_block()

        # Return the structure of the loop
        return ('swim', var_name, init_value, loop_var, condition_op, condition_value, increment_var, increment_expr_var, increment_value, loop_body)

    def parse_block(self):
        return self.parse_statement()

    def get_current_token(self):
        return self.tokens[self.position]

    def advance(self):
        self.position += 1

    def expect(self, expected_token):
        actual_token = self.get_current_token()
        if actual_token != expected_token:
            raise SyntaxError(f"Expected {expected_token} but got {actual_token}")
        self.advance()
