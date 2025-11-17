# 🎨 SimpleDraw Compiler

Un compilador completo desarrollado en Python que traduce un lenguaje de dibujo vectorial simple a SVG.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

## 🚀 Quick Start

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/simpledraw-compiler.git
cd simpledraw-compiler

# Ejecutar ejemplo
python main.py

# Compilar tu propio archivo
python main.py mi_dibujo.sd
```

## 📸 Screenshot

```simpledraw
Paper 100
Pen 3

# Dibuja un triángulo
Line 50 10 10 90
Line 10 90 90 90
Line 90 90 50 10
```

![Output Example](https://via.placeholder.com/200x200.svg?text=Triangle)

## ✨ Características

- ✅ **Analizador Léxico** - Tokenización robusta
- ✅ **Analizador Sintáctico** - Parser recursivo descendente
- ✅ **AST** - Árbol de Sintaxis Abstracta
- ✅ **Tabla de Símbolos** - Gestión de variables y configuraciones
- ✅ **Código Intermedio** - Three-Address Code
- ✅ **Generador SVG** - Salida visual
- ✅ **Optimización** - Eliminación de código redundante

## 📋 Fases del Compilador

```
Código Fuente → Lexer → Parser → Tabla de Símbolos → Código Intermedio → SVG
```

## 🎯 Sintaxis del Lenguaje

### Comandos Básicos

```simpledraw
Paper 100          # Tamaño del lienzo
Pen 5              # Grosor del trazo
Line x1 y1 x2 y2   # Dibujar línea
Circle x y radio   # Dibujar círculo
Rect x y w h       # Dibujar rectángulo
```

### Ejemplo Completo

```simpledraw
# Configuración
Paper 150
Pen 2

# Casa
Rect 30 60 90 60
Line 30 60 75 20
Line 75 20 120 60

# Puerta
Rect 60 90 30 30

# Ventana
Rect 45 75 15 15
```

## 📦 Estructura del Proyecto

```
simpledraw-compiler/
├── lexer.py              # Analizador Léxico
├── parser.py             # Analizador Sintáctico
├── symbol_table.py       # Tabla de Símbolos
├── intermediate_code.py  # Generador de Código Intermedio
├── main.py               # Programa Principal
├── examples/             # Ejemplos de código
└── tests/                # Pruebas unitarias
```

## 🔧 Instalación

### Requisitos

- Python 3.7 o superior
- Sin dependencias externas (solo stdlib)

### Pasos

```bash
# 1. Clonar
git clone https://github.com/tu-usuario/simpledraw-compiler.git

# 2. Entrar al directorio
cd simpledraw-compiler

# 3. Ejecutar
python main.py
```

## 💡 Ejemplos de Uso

### Desde Línea de Comandos

```bash
# Compilar archivo
python main.py ejemplos/triangulo.sd

# Ver solo el análisis léxico
python lexer.py

# Ver solo el análisis sintáctico
python parser.py
```

### Desde Python

```python
from main import SimpleDrawCompiler

compiler = SimpleDrawCompiler()
code = """
Paper 100
Pen 3
Circle 50 50 30
"""

success = compiler.compile(code)
if success:
    compiler.generate_svg("output.svg")
```

## 📊 Salidas del Compilador

El compilador genera tres archivos:

1. **output_tokens.json** - Lista de tokens del análisis léxico
2. **output_intermediate.json** - Código intermedio generado
3. **output_output.svg** - Imagen SVG resultante

## 🧪 Testing

```bash
# Ejecutar todas las pruebas
python -m pytest tests/

# Prueba específica
python -m pytest tests/test_lexer.py -v
```

## 📚 Documentación Completa

Ver [DOCUMENTATION.md](DOCUMENTATION.md) para documentación detallada que incluye:

- Arquitectura del compilador
- Gramática del lenguaje
- API completa
- Guía de desarrollo
- Casos de prueba

## 🎓 Conceptos Implementados

Este proyecto implementa conceptos fundamentales de:

- **Teoría de Compiladores**: Análisis léxico y sintáctico
- **Estructuras de Datos**: AST, Tabla de Símbolos
- **Algoritmos**: Parser recursivo descendente
- **Optimización**: Eliminación de código redundante
- **Generación de Código**: Traducción a SVG

## 🚧 Roadmap

- [ ] Variables y expresiones aritméticas
- [ ] Estructuras de control (if/else, loops)
- [ ] Funciones definidas por usuario
- [ ] Soporte para colores
- [ ] Transformaciones geométricas
- [ ] Exportación a PNG/PDF
- [ ] IDE con syntax highlighting

## 🤝 Contribuir

¡Las contribuciones son bienvenidas!

1. Fork el proyecto
2. Crea tu rama (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Changelog

### v1.0.0 (2025-11-15)
- ✨ Lanzamiento inicial
- ✅ Implementación completa del compilador
- ✅ Generación de SVG
- ✅ Documentación completa

## 👨‍💻 Autor

**Vladimir Diaz**

- GitHub: [EmeuveMV](https://github.com/EmeuveMV)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver [LICENSE](LICENSE) para detalles.

## 🙏 Agradecimientos

- Inspirado por el proyecto [sbn](https://github.com/alexmonnet/sbn)
- Basado en "Compilers: Principles, Techniques, and Tools" (Dragon Book)
- Desarrollado para la asignatura de Compiladores

## ⭐ Star History

Si este proyecto te fue útil, ¡considera darle una estrella! ⭐

---

<div align="center">
  
**¡Hecho con ❤️ y mucho ☕!**

[Reportar Bug](https://github.com/tu-usuario/simpledraw-compiler/issues) · [Solicitar Feature](https://github.com/tu-usuario/simpledraw-compiler/issues) · [Ver Demo](https://github.com/tu-usuario/simpledraw-compiler)

</div>