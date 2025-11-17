"""
ANALIZADOR LÉXICO (LEXER)
Tokeniza el código fuente del lenguaje SimpleDraw
"""

import re
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional

class TokenType(Enum):
    # Palabras clave
    PAPER = "PAPER"
    PEN = "PEN"
    LINE = "LINE"
    CIRCLE = "CIRCLE"
    RECT = "RECT"
    
    # Literales
    NUMBER = "NUMBER"
    STRING = "STRING"
    
    # Símbolos
    NEWLINE = "NEWLINE"
    EOF = "EOF"
    UNKNOWN = "UNKNOWN"

@dataclass
class Token:
    type: TokenType
    value: any
    line: int
    column: int
    
    def __repr__(self):
        return f"Token({self.type.name}, {self.value}, L{self.line}:C{self.column})"

class Lexer:
    def __init__(self, source_code: str):
        self.source = source_code
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
        
        # Palabras clave
        self.keywords = {
            'Paper': TokenType.PAPER,
            'Pen': TokenType.PEN,
            'Line': TokenType.LINE,
            'Circle': TokenType.CIRCLE,
            'Rect': TokenType.RECT,
        }
    
    def current_char(self) -> Optional[str]:
        if self.position >= len(self.source):
            return None
        return self.source[self.position]
    
    def peek_char(self, offset=1) -> Optional[str]:
        pos = self.position + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]
    
    def advance(self):
        if self.position < len(self.source):
            if self.source[self.position] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.position += 1
    
    def skip_whitespace(self):
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()
    
    def skip_comment(self):
        if self.current_char() == '#':
            while self.current_char() and self.current_char() != '\n':
                self.advance()
    
    def read_number(self) -> Token:
        start_line = self.line
        start_col = self.column
        num_str = ''
        
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            num_str += self.current_char()
            self.advance()
        
        value = float(num_str) if '.' in num_str else int(num_str)
        return Token(TokenType.NUMBER, value, start_line, start_col)
    
    def read_word(self) -> Token:
        start_line = self.line
        start_col = self.column
        word = ''
        
        while self.current_char() and (self.current_char().isalnum() or self.current_char() == '_'):
            word += self.current_char()
            self.advance()
        
        token_type = self.keywords.get(word, TokenType.UNKNOWN)
        return Token(token_type, word, start_line, start_col)
    
    def read_string(self) -> Token:
        start_line = self.line
        start_col = self.column
        quote_char = self.current_char()
        self.advance()
        
        string_value = ''
        while self.current_char() and self.current_char() != quote_char:
            string_value += self.current_char()
            self.advance()
        
        if self.current_char() == quote_char:
            self.advance()
        
        return Token(TokenType.STRING, string_value, start_line, start_col)
    
    def tokenize(self) -> List[Token]:
        while self.position < len(self.source):
            self.skip_whitespace()
            
            if not self.current_char():
                break
            
            if self.current_char() == '#':
                self.skip_comment()
                continue
            
            if self.current_char() == '\n':
                token = Token(TokenType.NEWLINE, '\\n', self.line, self.column)
                self.tokens.append(token)
                self.advance()
                continue
            
            if self.current_char().isdigit():
                self.tokens.append(self.read_number())
                continue
            
            if self.current_char() in '"\'':
                self.tokens.append(self.read_string())
                continue
            
            if self.current_char().isalpha():
                self.tokens.append(self.read_word())
                continue
            
            token = Token(TokenType.UNKNOWN, self.current_char(), self.line, self.column)
            self.tokens.append(token)
            self.advance()
        
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens
    
    def print_tokens(self):
        print("\n=== TOKENS GENERADOS ===")
        for i, token in enumerate(self.tokens):
            print(f"{i}: {token}")


if __name__ == "__main__":
    code = """
Paper 100
Pen 5
Line 50 77 22 27
"""
    
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    lexer.print_tokens()
