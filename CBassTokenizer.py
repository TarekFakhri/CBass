import re

class CBassTokenizer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.keywords = ['fish', 'floatfish', 'algae', 'splash', 'if', 'else', 'swim']
        self.tokenize()

    def tokenize(self):
        code_lines = self.code.splitlines()
        for line in code_lines:
            # Remove comments starting with // bubbles
            line = line.split('//')[0].strip()
            if not line:
                continue

            # This regex handles string literals, numbers (both integers and floats), and symbols
            # It captures strings enclosed in quotes, including spaces inside the quotes
            tokens = re.findall(r'\".*?\"|\d+\.\d+|\d+|\w+|[();=<>]', line)
            self.tokens.extend(tokens)

    def get_tokens(self):
        return self.tokens
