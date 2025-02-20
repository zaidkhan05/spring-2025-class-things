import sys
import os

# Keywords for SPSCL
KEYWORDS = {
    'define', 'set', 'if', 'then', 'elseif', 'else', 'endif', 
    'case', 'value', 'endcase', 'function', 'return', 'endfun',
    'integer', 'float', 'double', 'char', 'string', 'bool', 'boolean',
    'IMPORT', 'USE', 'MAIN', 'GLOBAL', 'TRY', 'CATCH', 
    'FOR', 'WHILE', 'REPEAT', 'UNTIL', 'ENDTRY', 'ENDFOR', 
    'ENDWHILE', 'ENDREPEAT'
}

# Special Characters and Operators
SPECIAL_CHARACTERS = {
    '(', ')', '{', '}', '[', ']', ';', ':', ',', '.', 
    '+', '-', '*', '/', '%', '=', '<', '<=', '>', '>=', '==', '!=', 
    '&&', '||'
}

# Token Types
TOKEN_TYPES = {
    "KEYWORD", "IDENTIFIER", "NUMBER", "STRING", "SYMBOL", "COMMENT"
}

# State-driven approach for each FSM
class Scanner:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_pos = 0
        self.current_char = source_code[0] if source_code else None

    # Utility: Advance to the next character
    def advance(self):
        self.current_pos += 1
        self.current_char = self.source_code[self.current_pos] if self.current_pos < len(self.source_code) else None

    # Utility: Peek at the next character without consuming it
    def peek(self):
        peek_pos = self.current_pos + 1
        return self.source_code[peek_pos] if peek_pos < len(self.source_code) else None

    # FSM for Keywords and Identifiers
    def scan_identifier(self):
        lexeme = ""
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            lexeme += self.current_char
            self.advance()
        
        # Check if it's a keyword
        if lexeme in KEYWORDS:
            self.tokens.append(("KEYWORD", lexeme))
        else:
            self.tokens.append(("IDENTIFIER", lexeme))

    # FSM for Numerical Constants
    def scan_number(self):
        lexeme = ""
        state = 0  # Initial state

        while self.current_char:
            if state == 0:
                if self.current_char.isdigit():
                    state = 1
                    lexeme += self.current_char
                elif self.current_char == '-' and self.peek().isdigit():
                    state = 1
                    lexeme += self.current_char
                else:
                    break
            elif state == 1:
                if self.current_char.isdigit():
                    lexeme += self.current_char
                elif self.current_char == '.':
                    state = 2
                    lexeme += self.current_char
                elif self.current_char in "eE":
                    state = 3
                    lexeme += self.current_char
                else:
                    break
            elif state == 2:  # Floating point part
                if self.current_char.isdigit():
                    lexeme += self.current_char
                elif self.current_char in "eE":
                    state = 3
                    lexeme += self.current_char
                else:
                    break
            elif state == 3:  # Scientific notation part
                if self.current_char in "+-" and lexeme[-1] in "eE":
                    lexeme += self.current_char
                elif self.current_char.isdigit():
                    lexeme += self.current_char
                else:
                    break
            self.advance()

        self.tokens.append(("NUMBER", lexeme))

    # FSM for String Literals
    def scan_string(self):
        lexeme = '"'
        self.advance()  # Skip opening quote

        while self.current_char and self.current_char != '"':
            lexeme += self.current_char
            self.advance()

        if self.current_char == '"':
            lexeme += '"'
            self.advance()
            self.tokens.append(("STRING", lexeme))
        else:
            raise Exception("Unterminated string literal")

    # FSM for Comments
    def scan_comment(self):
        lexeme = ""
        if self.current_char == '/' and self.peek() == '/':  # Single-line comment
            while self.current_char and self.current_char != '\n':
                lexeme += self.current_char
                self.advance()
            self.tokens.append(("COMMENT", lexeme))
        elif self.current_char == '/' and self.peek() == '*':  # Multi-line comment
            self.advance()  # Skip /
            self.advance()  # Skip *
            while self.current_char and not (self.current_char == '*' and self.peek() == '/'):
                lexeme += self.current_char
                self.advance()
            if self.current_char == '*':
                self.advance()  # Skip *
                self.advance()  # Skip /
                self.tokens.append(("COMMENT", lexeme))
            else:
                raise Exception("Unterminated comment")

    # Special Characters
    def scan_special_character(self):
        lexeme = self.current_char
        self.advance()
        self.tokens.append(("SYMBOL", lexeme))

    # Main Scanner Loop
    def scan_tokens(self):
        while self.current_char:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char.isalpha() or self.current_char == '_':
                self.scan_identifier()
            elif self.current_char.isdigit() or (self.current_char == '-' and self.peek().isdigit()):
                self.scan_number()
            elif self.current_char == '"':
                self.scan_string()
            elif self.current_char == '/' and (self.peek() in ['/','*']):
                self.scan_comment()
            elif self.current_char in SPECIAL_CHARACTERS:
                self.scan_special_character()
            else:
                raise Exception(f"Unexpected character: {self.current_char}")
        return self.tokens

# Main function to read file and tokenize
def main():
    if len(sys.argv) != 2:
        print("Usage: python spscl_scanner.py <filename>.scl")
        return
    
    filename = sys.argv[1]
    if not filename.endswith(".scl"):
        print("Error: File must have a .scl extension.")
        return
    
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' not found.")
        return
    
    with open(filename, 'r') as file:
        source_code = file.read()
    
    scanner = Scanner(source_code)
    tokens = scanner.scan_tokens()
    for token in tokens:
        print(token)

if __name__ == "__main__":
    main()
