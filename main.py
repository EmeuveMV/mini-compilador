"""
COMPILADOR SIMPLEDRAW - MAIN
"""

import sys
import json
from lexer import Lexer
from parser import Parser, ProgramNode, PaperNode, PenNode, LineNode, CircleNode, RectNode
from symbol_table import SymbolTable
from intermediate_code import IntermediateCodeGenerator

class SimpleDrawCompiler:
    def __init__(self):
        self.lexer = None
        self.parser = None
        self.symbol_table = SymbolTable()
        self.code_generator = IntermediateCodeGenerator()
        self.tokens = []
        self.ast = None
        self.errors = []
    
    def compile(self, source_code: str) -> bool:
        self.errors = []
        
        try:
            print("\n" + "="*70)
            print("FASE 1: ANÁLISIS LÉXICO".center(70))
            print("="*70)
            self.lexer = Lexer(source_code)
            self.tokens = self.lexer.tokenize()
            self.lexer.print_tokens()
            
            print("\n" + "="*70)
            print("FASE 2: ANÁLISIS SINTÁCTICO".center(70))
            print("="*70)
            self.parser = Parser(self.tokens)
            self.ast = self.parser.parse()
            self.parser.print_ast(self.ast)
            
            print("\n" + "="*70)
            print("FASE 3: TABLA DE SÍMBOLOS".center(70))
            print("="*70)
            self.build_symbol_table(self.ast)
            self.symbol_table.print_table()
            
            print("\n" + "="*70)
            print("FASE 4: CÓDIGO INTERMEDIO".center(70))
            print("="*70)
            self.code_generator.generate_from_ast(self.ast)
            self.code_generator.print_code()
            
            removed = self.code_generator.optimize()
            if removed > 0:
                print(f"\n✓ Optimización: {removed} instrucción(es) eliminada(s)")
            
            print("\n" + "="*70)
            print("✓ COMPILACIÓN EXITOSA".center(70))
            print("="*70)
            return True
            
        except SyntaxError as e:
            self.errors.append(f"Error: {e}")
            print(f"\n✗ ERROR: {e}")
            return False
        except Exception as e:
            self.errors.append(f"Error: {e}")
            print(f"\n✗ ERROR: {e}")
            return False
    
    def build_symbol_table(self, node):
        if isinstance(node, ProgramNode):
            line = 1
            for stmt in node.statements:
                if isinstance(stmt, PaperNode):
                    self.symbol_table.add_config("paper_size", stmt.size, line)
                elif isinstance(stmt, PenNode):
                    self.symbol_table.add_config("pen_width", stmt.width, line)
                elif isinstance(stmt, LineNode):
                    params = {"x1": stmt.x1, "y1": stmt.y1, "x2": stmt.x2, "y2": stmt.y2}
                    self.symbol_table.add_shape("Line", params, line)
                elif isinstance(stmt, CircleNode):
                    params = {"x": stmt.x, "y": stmt.y, "radius": stmt.radius}
                    self.symbol_table.add_shape("Circle", params, line)
                elif isinstance(stmt, RectNode):
                    params = {"x": stmt.x, "y": stmt.y, "width": stmt.width, "height": stmt.height}
                    self.symbol_table.add_shape("Rect", params, line)
                line += 1
    
    def generate_svg(self, output_file: str):
        paper_size = 100
        pen_width = 1
        
        if self.symbol_table.exists("paper_size"):
            paper_size = self.symbol_table.get_symbol("paper_size").value
        if self.symbol_table.exists("pen_width"):
            pen_width = self.symbol_table.get_symbol("pen_width").value
        
        svg_lines = [
            f'<svg width="{paper_size}" height="{paper_size}" xmlns="http://www.w3.org/2000/svg">',
            f'  <rect width="100%" height="100%" fill="white"/>',
            f'  <g stroke="black" stroke-width="{pen_width}" fill="none">'
        ]
        
        for inst in self.code_generator.instructions:
            if inst.op == 'LINE':
                svg_lines.append(f'    <line x1="{inst.arg1}" y1="{inst.arg2}" x2="{inst.arg3}" y2="{inst.result}"/>')
            elif inst.op == 'CIRCLE':
                svg_lines.append(f'    <circle cx="{inst.arg1}" cy="{inst.arg2}" r="{inst.arg3}"/>')
            elif inst.op == 'RECT':
                svg_lines.append(f'    <rect x="{inst.arg1}" y="{inst.arg2}" width="{inst.arg3}" height="{inst.result}"/>')
        
        svg_lines.extend(['  </g>', '</svg>'])
        svg_content = '\n'.join(svg_lines)
        
        with open(output_file, 'w') as f:
            f.write(svg_content)
        
        print(f"\n✓ SVG generado: {output_file}")
        return svg_content
    
    def export_results(self, base_filename: str):
        with open(f"{base_filename}_tokens.json", 'w') as f:
            json.dump([{"type": t.type.name, "value": t.value, "line": t.line} for t in self.tokens], f, indent=2)
        
        with open(f"{base_filename}_intermediate.json", 'w') as f:
            f.write(self.code_generator.to_json())
        
        self.generate_svg(f"{base_filename}_output.svg")
        print(f"\n✓ Archivos exportados: {base_filename}_*")


def main():
    print("="*70)
    print("COMPILADOR MINI COMPILER v1.0".center(70))
    print("="*70)
    
    example_code = """# Triángulo
Paper 100
Pen 3
Line 50 10 10 90
Line 10 90 90 90
Line 90 90 50 10
"""
    
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], 'r') as f:
                source_code = f.read()
            print(f"Archivo: {sys.argv[1]}")
        except FileNotFoundError:
            print(f"Error: Archivo no encontrado")
            return
    else:
        print("\nUsando ejemplo...")
        source_code = example_code
    
    print("\n" + "-"*70)
    print("CÓDIGO:")
    print("-"*70)
    print(source_code)
    print("-"*70)
    
    compiler = SimpleDrawCompiler()
    success = compiler.compile(source_code)
    
    if success:
        compiler.export_results("output")
        stats = compiler.symbol_table.get_statistics()
        print(f"\n✓ Tokens: {len(compiler.tokens)}")
        print(f"✓ Símbolos: {stats['total']}")
        print(f"✓ Instrucciones: {len(compiler.code_generator.instructions)}")


if __name__ == "__main__":
    main()
