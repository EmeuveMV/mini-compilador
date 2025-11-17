"""
SUITE DE PRUEBAS COMPLETA
Tests unitarios para todos los componentes del compilador
"""

import unittest
from lexer import Lexer, TokenType
from parser import Parser, ProgramNode, LineNode
from symbol_table import SymbolTable, SymbolType
from intermediate_code import IntermediateCodeGenerator
from main import SimpleDrawCompiler

class TestLexer(unittest.TestCase):
    """Pruebas del Analizador Léxico"""
    
    def test_tokenize_paper(self):
        """Test: Tokenizar comando Paper"""
        code = "Paper 100"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.PAPER)
        self.assertEqual(tokens[1].type, TokenType.NUMBER)
        self.assertEqual(tokens[1].value, 100)
    
    def test_tokenize_pen(self):
        """Test: Tokenizar comando Pen"""
        code = "Pen 5"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.PEN)
        self.assertEqual(tokens[1].type, TokenType.NUMBER)
        self.assertEqual(tokens[1].value, 5)
    
    def test_tokenize_line(self):
        """Test: Tokenizar comando Line con 4 números"""
        code = "Line 10 20 30 40"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.LINE)
        self.assertEqual(len([t for t in tokens if t.type == TokenType.NUMBER]), 4)
    
    def test_tokenize_circle(self):
        """Test: Tokenizar comando Circle"""
        code = "Circle 50 50 20"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.CIRCLE)
        self.assertEqual(len([t for t in tokens if t.type == TokenType.NUMBER]), 3)
    
    def test_tokenize_comment(self):
        """Test: Ignorar comentarios"""
        code = "# Este es un comentario\nPaper 100"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        # El comentario debe ser ignorado
        paper_token = next(t for t in tokens if t.type == TokenType.PAPER)
        self.assertIsNotNone(paper_token)
    
    def test_tokenize_multiline(self):
        """Test: Tokenizar múltiples líneas"""
        code = """Paper 100
Pen 5
Line 10 20 30 40"""
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        keywords = [t for t in tokens if t.type in [TokenType.PAPER, TokenType.PEN, TokenType.LINE]]
        self.assertEqual(len(keywords), 3)
    
    def test_float_numbers(self):
        """Test: Tokenizar números flotantes"""
        code = "Line 10.5 20.3 30.7 40.1"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        numbers = [t for t in tokens if t.type == TokenType.NUMBER]
        self.assertTrue(all(isinstance(t.value, float) for t in numbers))


class TestParser(unittest.TestCase):
    """Pruebas del Analizador Sintáctico"""
    
    def test_parse_paper(self):
        """Test: Parsear comando Paper"""
        code = "Paper 100"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        self.assertIsInstance(ast, ProgramNode)
        self.assertEqual(len(ast.statements), 1)
    
    def test_parse_line(self):
        """Test: Parsear comando Line"""
        code = "Line 10 20 30 40"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        self.assertIsInstance(ast.statements[0], LineNode)
        line = ast.statements[0]
        self.assertEqual(line.x1, 10)
        self.assertEqual(line.y1, 20)
        self.assertEqual(line.x2, 30)
        self.assertEqual(line.y2, 40)
    
    def test_parse_multiple_statements(self):
        """Test: Parsear múltiples declaraciones"""
        code = """Paper 100
Pen 5
Line 10 20 30 40"""
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        self.assertEqual(len(ast.statements), 3)
    
    def test_syntax_error(self):
        """Test: Detectar error de sintaxis"""
        code = "Paper"  # Falta el número
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        
        with self.assertRaises(SyntaxError):
            parser.parse()


class TestSymbolTable(unittest.TestCase):
    """Pruebas de la Tabla de Símbolos"""
    
    def setUp(self):
        self.symbol_table = SymbolTable()
    
    def test_add_config(self):
        """Test: Agregar configuración"""
        self.symbol_table.add_config("paper_size", 100, 1)
        
        self.assertTrue(self.symbol_table.exists("paper_size"))
        symbol = self.symbol_table.get_symbol("paper_size")
        self.assertEqual(symbol.value, 100)
        self.assertEqual(symbol.type, SymbolType.CONFIG)
    
    def test_add_shape(self):
        """Test: Agregar forma geométrica"""
        params = {"x1": 10, "y1": 20, "x2": 30, "y2": 40}
        self.symbol_table.add_shape("Line", params, 1)
        
        # Debe existir Line_1
        self.assertTrue(self.symbol_table.exists("Line_1"))
    
    def test_update_symbol(self):
        """Test: Actualizar valor de símbolo"""
        self.symbol_table.add_config("pen_width", 5, 1)
        self.symbol_table.update_symbol("pen_width", 10)
        
        symbol = self.symbol_table.get_symbol("pen_width")
        self.assertEqual(symbol.value, 10)
    
    def test_statistics(self):
        """Test: Obtener estadísticas"""
        self.symbol_table.add_config("paper_size", 100, 1)
        self.symbol_table.add_config("pen_width", 5, 2)
        self.symbol_table.add_shape("Line", {}, 3)
        
        stats = self.symbol_table.get_statistics()
        self.assertEqual(stats['configs'], 2)
        self.assertEqual(stats['shapes'], 1)
        self.assertEqual(stats['total'], 3)


class TestIntermediateCode(unittest.TestCase):
    """Pruebas del Generador de Código Intermedio"""
    
    def test_generate_paper(self):
        """Test: Generar código para Paper"""
        code = "Paper 100"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        code_gen = IntermediateCodeGenerator()
        code_gen.generate_from_ast(ast)
        
        self.assertEqual(len(code_gen.instructions), 1)
        self.assertEqual(code_gen.instructions[0].op, 'PAPER')
        self.assertEqual(code_gen.instructions[0].arg1, 100)
    
    def test_generate_line(self):
        """Test: Generar código para Line"""
        code = "Line 10 20 30 40"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        code_gen = IntermediateCodeGenerator()
        code_gen.generate_from_ast(ast)
        
        inst = code_gen.instructions[0]
        self.assertEqual(inst.op, 'LINE')
        self.assertEqual(inst.arg1, 10)
        self.assertEqual(inst.arg2, 20)
    
    def test_optimization(self):
        """Test: Optimización elimina duplicados"""
        code = """Line 10 20 30 40
Line 10 20 30 40"""
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        code_gen = IntermediateCodeGenerator()
        code_gen.generate_from_ast(ast)
        
        initial_count = len(code_gen.instructions)
        removed = code_gen.optimize()
        
        self.assertGreater(removed, 0)
        self.assertLess(len(code_gen.instructions), initial_count)


class TestCompiler(unittest.TestCase):
    """Pruebas del Compilador Completo"""
    
    def test_compile_simple_program(self):
        """Test: Compilar programa simple"""
        code = """Paper 100
Pen 5
Line 10 20 30 40"""
        
        compiler = SimpleDrawCompiler()
        success = compiler.compile(code)
        
        self.assertTrue(success)
        self.assertIsNotNone(compiler.ast)
        self.assertGreater(len(compiler.tokens), 0)
    
    def test_compile_with_comments(self):
        """Test: Compilar con comentarios"""
        code = """# Configuración
Paper 100
# Trazo
Pen 5"""
        
        compiler = SimpleDrawCompiler()
        success = compiler.compile(code)
        
        self.assertTrue(success)
    
    def test_compile_invalid_syntax(self):
        """Test: Detectar sintaxis inválida"""
        code = "Paper"  # Sintaxis inválida
        
        compiler = SimpleDrawCompiler()
        success = compiler.compile(code)
        
        self.assertFalse(success)
        self.assertGreater(len(compiler.errors), 0)
    
    def test_svg_generation(self):
        """Test: Generar SVG"""
        code = """Paper 100
Pen 3
Line 10 10 90 90"""
        
        compiler = SimpleDrawCompiler()
        success = compiler.compile(code)
        
        if success:
            svg = compiler.generate_svg("test_output.svg")
            self.assertIn('<svg', svg)
            self.assertIn('<line', svg)


class TestIntegration(unittest.TestCase):
    """Pruebas de Integración Completas"""
    
    def test_triangle_program(self):
        """Test: Compilar programa de triángulo completo"""
        code = """Paper 100
Pen 3
Line 50 10 10 90
Line 10 90 90 90
Line 90 90 50 10"""
        
        compiler = SimpleDrawCompiler()
        success = compiler.compile(code)
        
        self.assertTrue(success)
        self.assertEqual(len(compiler.code_generator.instructions), 5)
        
        # Verificar tabla de símbolos
        stats = compiler.symbol_table.get_statistics()
        self.assertEqual(stats['configs'], 2)
        self.assertEqual(stats['shapes'], 3)
    
    def test_complex_program(self):
        """Test: Compilar programa complejo con todas las formas"""
        code = """Paper 150
Pen 2
Line 10 10 90 90
Circle 50 50 20
Rect 20 20 30 40"""
        
        compiler = SimpleDrawCompiler()
        success = compiler.compile(code)
        
        self.assertTrue(success)
        
        # Verificar todas las formas fueron procesadas
        shapes = [s for s in compiler.symbol_table.symbols.values() 
                 if s.type == SymbolType.SHAPE]
        self.assertEqual(len(shapes), 3)


def run_tests():
    """Ejecuta todos los tests"""
    # Crear suite de tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Agregar tests
    suite.addTests(loader.loadTestsFromTestCase(TestLexer))
    suite.addTests(loader.loadTestsFromTestCase(TestParser))
    suite.addTests(loader.loadTestsFromTestCase(TestSymbolTable))
    suite.addTests(loader.loadTestsFromTestCase(TestIntermediateCode))
    suite.addTests(loader.loadTestsFromTestCase(TestCompiler))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Ejecutar tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Resumen
    print("\n" + "="*70)
    print("RESUMEN DE PRUEBAS".center(70))
    print("="*70)
    print(f"Tests ejecutados: {result.testsRun}")
    print(f"Exitosos: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Fallidos: {len(result.failures)}")
    print(f"Errores: {len(result.errors)}")
    print("="*70)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)