"""
TABLA DE SÍMBOLOS
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional
from enum import Enum

class SymbolType(Enum):
    CONFIG = "CONFIG"
    SHAPE = "SHAPE"
    VARIABLE = "VARIABLE"

@dataclass
class Symbol:
    name: str
    type: SymbolType
    value: Any
    line: int
    data_type: str
    
    def __repr__(self):
        return f"Symbol({self.name}, {self.type.name}, {self.data_type})"

class SymbolTable:
    def __init__(self):
        self.symbols: Dict[str, Symbol] = {}
        self.shape_counter = 0
    
    def add_symbol(self, name: str, symbol_type: SymbolType, value: Any, line: int, data_type: str):
        symbol = Symbol(name, symbol_type, value, line, data_type)
        self.symbols[name] = symbol
        return symbol
    
    def get_symbol(self, name: str) -> Optional[Symbol]:
        return self.symbols.get(name)
    
    def exists(self, name: str) -> bool:
        return name in self.symbols
    
    def add_config(self, config_name: str, value: Any, line: int):
        data_type = type(value).__name__
        return self.add_symbol(config_name, SymbolType.CONFIG, value, line, data_type)
    
    def add_shape(self, shape_type: str, params: Dict, line: int):
        self.shape_counter += 1
        shape_name = f"{shape_type}_{self.shape_counter}"
        return self.add_symbol(shape_name, SymbolType.SHAPE, params, line, shape_type)
    
    def print_table(self):
        print("\n" + "=" * 80)
        print("TABLA DE SÍMBOLOS".center(80))
        print("=" * 80)
        print(f"{'Nombre':<20} {'Tipo':<15} {'Tipo Dato':<15} {'Valor':<20} {'Línea':<10}")
        print("-" * 80)
        
        for name, symbol in self.symbols.items():
            value_str = str(symbol.value)
            if len(value_str) > 20:
                value_str = value_str[:17] + "..."
            print(f"{name:<20} {symbol.type.name:<15} {symbol.data_type:<15} {value_str:<20} {symbol.line:<10}")
        
        print("=" * 80)
    
    def get_statistics(self):
        return {
            'total': len(self.symbols),
            'configs': sum(1 for s in self.symbols.values() if s.type == SymbolType.CONFIG),
            'shapes': sum(1 for s in self.symbols.values() if s.type == SymbolType.SHAPE),
            'variables': sum(1 for s in self.symbols.values() if s.type == SymbolType.VARIABLE)
        }
