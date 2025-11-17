"""
ANALIZADOR SINTÁCTICO (PARSER)
Genera el Árbol de Sintaxis Abstracta (AST)
"""

from dataclasses import dataclass
from typing import List, Optional
from lexer import Token, TokenType, Lexer

@dataclass
class ASTNode:
    pass

@dataclass
class ProgramNode(ASTNode):
    statements: List[ASTNode]

@dataclass
class PaperNode(ASTNode):
    size: int

@dataclass
class PenNode(ASTNode):
    width: int

@dataclass
class LineNode(ASTNode):
    x1: float
    y1: float
    x2: float
    y2: float

@dataclass
class CircleNode(ASTNode):
    x: float
    y: float
    radius: float

@dataclass
class RectNode(ASTNode):
    x: float
    y: float
    width: float
    height: float

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[0] if tokens else None
    
    def advance(self):
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None
    
    def expect(self, token_type: TokenType) -> Token:
        if not self.current_token or self.current_token.type != token_type:
            raise SyntaxError(
                f"Error de sintaxis: Se esperaba {token_type.name}, "
                f"pero se encontró {self.current_token.type.name if self.current_token else 'EOF'} "
                f"en línea {self.current_token.line if self.current_token else 'N/A'}"
            )
        token = self.current_token
        self.advance()
        return token
    
    def skip_newlines(self):
        while self.current_token and self.current_token.type == TokenType.NEWLINE:
            self.advance()
    
    def parse_paper(self) -> PaperNode:
        self.expect(TokenType.PAPER)
        size_token = self.expect(TokenType.NUMBER)
        return PaperNode(size=int(size_token.value))
    
    def parse_pen(self) -> PenNode:
        self.expect(TokenType.PEN)
        width_token = self.expect(TokenType.NUMBER)
        return PenNode(width=int(width_token.value))
    
    def parse_line(self) -> LineNode:
        self.expect(TokenType.LINE)
        x1 = self.expect(TokenType.NUMBER).value
        y1 = self.expect(TokenType.NUMBER).value
        x2 = self.expect(TokenType.NUMBER).value
        y2 = self.expect(TokenType.NUMBER).value
        return LineNode(x1=x1, y1=y1, x2=x2, y2=y2)
    
    def parse_circle(self) -> CircleNode:
        self.expect(TokenType.CIRCLE)
        x = self.expect(TokenType.NUMBER).value
        y = self.expect(TokenType.NUMBER).value
        radius = self.expect(TokenType.NUMBER).value
        return CircleNode(x=x, y=y, radius=radius)
    
    def parse_rect(self) -> RectNode:
        self.expect(TokenType.RECT)
        x = self.expect(TokenType.NUMBER).value
        y = self.expect(TokenType.NUMBER).value
        width = self.expect(TokenType.NUMBER).value
        height = self.expect(TokenType.NUMBER).value
        return RectNode(x=x, y=y, width=width, height=height)
    
    def parse_statement(self) -> Optional[ASTNode]:
        self.skip_newlines()
        
        if not self.current_token or self.current_token.type == TokenType.EOF:
            return None
        
        token_type = self.current_token.type
        
        if token_type == TokenType.PAPER:
            return self.parse_paper()
        elif token_type == TokenType.PEN:
            return self.parse_pen()
        elif token_type == TokenType.LINE:
            return self.parse_line()
        elif token_type == TokenType.CIRCLE:
            return self.parse_circle()
        elif token_type == TokenType.RECT:
            return self.parse_rect()
        else:
            raise SyntaxError(f"Declaración inesperada: {token_type.name}")
    
    def parse(self) -> ProgramNode:
        statements = []
        
        while self.current_token and self.current_token.type != TokenType.EOF:
            self.skip_newlines()
            if self.current_token and self.current_token.type != TokenType.EOF:
                stmt = self.parse_statement()
                if stmt:
                    statements.append(stmt)
                self.skip_newlines()
        
        return ProgramNode(statements=statements)
    
    def print_ast(self, node: ASTNode, indent=0):
        prefix = "  " * indent
        if isinstance(node, ProgramNode):
            print(f"{prefix}Program:")
            for stmt in node.statements:
                self.print_ast(stmt, indent + 1)
        else:
            print(f"{prefix}{node}")


if __name__ == "__main__":
    code = """
Paper 100
Pen 5
Line 50 77 22 27
"""
    
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    print("\n=== AST ===")
    parser.print_ast(ast)
