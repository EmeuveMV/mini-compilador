"""
GENERADOR DE CÓDIGO INTERMEDIO
"""

from dataclasses import dataclass
from typing import List
from parser import *

@dataclass
class IntermediateInstruction:
    op: str
    arg1: any = None
    arg2: any = None
    arg3: any = None
    result: any = None
    
    def __repr__(self):
        if self.op in ['PAPER', 'PEN']:
            return f"{self.op} {self.arg1}"
        elif self.op == 'LINE':
            return f"{self.op} {self.arg1}, {self.arg2}, {self.arg3}, {self.result}"
        elif self.op == 'CIRCLE':
            return f"{self.op} {self.arg1}, {self.arg2}, {self.arg3}"
        elif self.op == 'RECT':
            return f"{self.op} {self.arg1}, {self.arg2}, {self.arg3}, {self.result}"
        return f"{self.op}"

class IntermediateCodeGenerator:
    def __init__(self):
        self.instructions: List[IntermediateInstruction] = []
    
    def emit(self, op: str, arg1=None, arg2=None, arg3=None, result=None):
        instruction = IntermediateInstruction(op, arg1, arg2, arg3, result)
        self.instructions.append(instruction)
        return instruction
    
    def generate_from_ast(self, node: ASTNode):
        if isinstance(node, ProgramNode):
            for stmt in node.statements:
                self.generate_from_ast(stmt)
        elif isinstance(node, PaperNode):
            self.emit('PAPER', node.size)
        elif isinstance(node, PenNode):
            self.emit('PEN', node.width)
        elif isinstance(node, LineNode):
            self.emit('LINE', node.x1, node.y1, node.x2, node.y2)
        elif isinstance(node, CircleNode):
            self.emit('CIRCLE', node.x, node.y, node.radius)
        elif isinstance(node, RectNode):
            self.emit('RECT', node.x, node.y, node.width, node.height)
    
    def print_code(self):
        print("\n" + "=" * 60)
        print("CÓDIGO INTERMEDIO".center(60))
        print("=" * 60)
        for i, inst in enumerate(self.instructions):
            print(f"{i:3d}: {inst}")
        print("=" * 60)
    
    def to_json(self):
        import json
        return json.dumps([{
            'op': i.op, 'arg1': i.arg1, 'arg2': i.arg2,
            'arg3': i.arg3, 'result': i.result
        } for i in self.instructions], indent=2)
    
    def optimize(self):
        optimized = []
        prev = None
        for inst in self.instructions:
            if inst != prev:
                optimized.append(inst)
            prev = inst
        removed = len(self.instructions) - len(optimized)
        self.instructions = optimized
        return removed
