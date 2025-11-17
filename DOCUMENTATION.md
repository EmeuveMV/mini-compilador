# Mini Compiler - Documentación Completa

## 📋 Tabla de Contenidos
1. [Introducción](#introducción)
2. [Características](#características)
3. [Arquitectura del Compilador](#arquitectura-del-compilador)
4. [Instalación](#instalación)
5. [Uso](#uso)
6. [Lenguaje Mini](#lenguaje-Mini)
7. [Ejemplos](#ejemplos)
8. [Estructura del Proyecto](#estructura-del-proyecto)

---

## 🎯 Introducción

**Mini Compiler** es un compilador completo desarrollado en Python que traduce un lenguaje de dibujo vectorial simple a código SVG. El proyecto implementa todas las fases de un compilador moderno:

- ✅ Analizador Léxico (Lexer)
- ✅ Analizador Sintáctico (Parser)
- ✅ Generación de AST (Abstract Syntax Tree)
- ✅ Tabla de Símbolos
- ✅ Generador de Código Intermedio
- ✅ Generador de Código Final (SVG)

---

## ⚡ Características

- **Análisis Léxico Robusto**: Tokenización completa con soporte para números, palabras clave y comentarios
- **Parser Recursivo Descendente**: Análisis sintáctico con manejo de errores
- **AST Detallado**: Representación estructurada del programa
- **Tabla de Símbolos**: Seguimiento de variables, configuraciones y formas
- **Código Intermedio**: Representación de tres direcciones (Three-Address Code)
- **Optimización**: Eliminación de instrucciones duplicadas
- **Generación de SVG**: Salida visual en formato estándar
- **Exportación de Datos**: JSON con tokens, AST y código intermedio

---

## 🏗️ Arquitectura del Compilador

```
┌─────────────────┐
│  Código Fuente  │
│   (Mini)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ LEXER (Léxico)  │◄─── Genera tokens
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ PARSER (Sint.)  │◄─── Construye AST
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Tabla Símbolos  │◄─── Almacena variables
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Código Interm.  │◄─── Three-Address Code
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Gen. de Código  │◄─── Produce SVG
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Archivo SVG    │
└─────────────────┘
```

---

## 💻 Instalación

### Requisitos
- Python 3.7 o superior
- No requiere librerías externas (solo stdlib)

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/Mini-compiler.git
cd Mini-compiler

# 2. Verificar la instalación
python main.py

# 3. (Opcional) Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

---

## 🚀 Uso

### Uso Básico

```bash
# Compilar código de ejemplo incluido
python main.py

# Compilar desde archivo
python main.py mi_dibujo.sd

# Compilar y ver solo una fase
python lexer.py              # Solo análisis léxico
python parser.py             # Solo análisis sintáctico
python intermediate_code.py  # Solo código intermedio
```

### Archivos Generados

Después de compilar, se generan:
- `output_tokens.json` - Tokens del análisis léxico
- `output_intermediate.json` - Código intermedio
- `output_output.svg` - Imagen SVG resultante

---

## 📝 Lenguaje Mini

### Sintaxis

#### 1. Configuración del Lienzo
```
Paper <tamaño>
```
Define el tamaño del lienzo cuadrado (en píxeles).

**Ejemplo:**
```
Paper 100
```

#### 2. Grosor del Trazo
```
Pen <grosor>
```
Define el grosor de las líneas a dibujar.

**Ejemplo:**
```
Pen 5
```

#### 3. Línea
```
Line <x1> <y1> <x2> <y2>
```
Dibuja una línea desde (x1,y1) hasta (x2,y2).

**Ejemplo:**
```
Line 10 10 90 90
```

#### 4. Círculo
```
Circle <x> <y> <radio>
```
Dibuja un círculo centrado en (x,y) con el radio especificado.

**Ejemplo:**
```
Circle 50 50 20
```

#### 5. Rectángulo
```
Rect <x> <y> <ancho> <alto>
```
Dibuja un rectángulo desde (x,y) con las dimensiones especificadas.

**Ejemplo:**
```
Rect 20 20 30 40
```

### Comentarios
```
# Este es un comentario de una línea
```

---

## 📚 Ejemplos

### Ejemplo 1: Triángulo Simple
```Mini
Paper 100
Pen 3

# Dibuja un triángulo equilátero
Line 50 10 10 90
Line 10 90 90 90
Line 90 90 50 10
```

### Ejemplo 2: Casa
```Mini
Paper 150
Pen 2

# Base de la casa
Rect 30 60 90 60

# Techo
Line 30 60 75 20
Line 75 20 120 60

# Puerta
Rect 60 90 30 30

# Ventana
Rect 45 75 15 15
```

### Ejemplo 3: Figuras Concéntricas
```Mini
Paper 200
Pen 2

# Círculos concéntricos
Circle 100 100 80
Circle 100 100 60
Circle 100 100 40
Circle 100 100 20
```

### Ejemplo 4: Patrón Geométrico
```Mini
Paper 120
Pen 1

# Cuadrados rotados
Rect 20 20 80 80
Rect 30 30 60 60
Rect 40 40 40 40
Rect 50 50 20 20

# Círculo central
Circle 60 60 10
```

---

## 📁 Estructura del Proyecto

```
Mini-compiler/
│
├── lexer.py                 # Analizador Léxico
├── parser.py                # Analizador Sintáctico + AST
├── symbol_table.py          # Tabla de Símbolos
├── intermediate_code.py     # Generador de Código Intermedio
├── main.py                  # Programa Principal
│
├── examples/                # Ejemplos de código
│   ├── triangle.sd
│   ├── house.sd
│   └── pattern.sd
│
├── docs/                    # Documentación adicional
│   ├── MANUAL.md
│   └── API.md
│
├── tests/                   # Pruebas unitarias
│   ├── test_lexer.py
│   ├── test_parser.py
│   └── test_compiler.py
│
└── README.md               # Este archivo
```

---

## 🔍 Detalles de Implementación

### 1. Analizador Léxico (lexer.py)

**Responsabilidades:**
- Lectura del código fuente carácter por carácter
- Identificación de tokens (palabras clave, números, símbolos)
- Manejo de espacios en blanco y comentarios
- Reporte de posición (línea y columna)

**Tokens Reconocidos:**
- `PAPER`, `PEN`, `LINE`, `CIRCLE`, `RECT` (palabras clave)
- `NUMBER` (enteros y flotantes)
- `STRING` (cadenas entre comillas)
- `NEWLINE` (saltos de línea)
- `EOF` (fin de archivo)

### 2. Analizador Sintáctico (parser.py)

**Técnica:** Parser de descenso recursivo

**Gramática Mini:**
```
programa    → declaración*
declaración → paper | pen | línea | círculo | rectángulo
paper       → PAPER NUMBER
pen         → PEN NUMBER
línea       → LINE NUMBER NUMBER NUMBER NUMBER
círculo     → CIRCLE NUMBER NUMBER NUMBER
rectángulo  → RECT NUMBER NUMBER NUMBER NUMBER
```

### 3. Tabla de Símbolos (symbol_table.py)

**Información Almacenada:**
- Nombre del símbolo
- Tipo (CONFIG, SHAPE, VARIABLE)
- Valor actual
- Tipo de dato
- Número de línea donde se definió

### 4. Código Intermedio (intermediate_code.py)

**Formato:** Three-Address Code (Código de Tres Direcciones)

**Ejemplo de Transformación:**
```
Código Fuente:    Line 10 20 30 40
Código Intermedio: LINE 10, 20, 30, 40
```

**Optimizaciones Implementadas:**
- Eliminación de instrucciones duplicadas consecutivas

---

## 🧪 Pruebas

### Ejecutar Pruebas Unitarias

```bash
# Todas las pruebas
python -m pytest tests/

# Prueba específica
python -m pytest tests/test_lexer.py -v
```

### Casos de Prueba Incluidos

1. ✅ Tokenización correcta
2. ✅ Parsing de sintaxis válida
3. ✅ Detección de errores sintácticos
4. ✅ Construcción de tabla de símbolos
5. ✅ Generación de código intermedio
6. ✅ Generación de SVG

---

## 🐛 Manejo de Errores

El compilador detecta y reporta:

1. **Errores Léxicos**: Caracteres no reconocidos
2. **Errores Sintácticos**: Construcciones inválidas
3. **Errores Semánticos**: Uso incorrecto de comandos

**Ejemplo de Error:**
```
Error de Sintaxis: Se esperaba NUMBER, 
pero se encontró UNKNOWN en línea 5
```

---

## 🎓 Conceptos Implementados

### Teoría de Compiladores

- ✅ **Análisis Léxico**: Expresiones regulares y autómatas finitos
- ✅ **Análisis Sintáctico**: Gramáticas libres de contexto
- ✅ **Árbol de Sintaxis Abstracta**: Representación estructurada
- ✅ **Tabla de Símbolos**: Gestión de identificadores
- ✅ **Código Intermedio**: Representación independiente del lenguaje
- ✅ **Optimización**: Eliminación de código redundante
- ✅ **Generación de Código**: Traducción a lenguaje objetivo

---

## 📈 Extensiones Futuras

- [ ] Soporte para variables y expresiones
- [ ] Condicionales y bucles
- [ ] Funciones definidas por el usuario
- [ ] Colores y estilos
- [ ] Transformaciones (rotación, escala)
- [ ] Importación de archivos
- [ ] Generación de otros formatos (PNG, PDF)
- [ ] Depurador interactivo

---

## 👥 Autor

**Vladimir Diaz**
- GitHub: [EmeuveMV](https://github.com/EmeuveMV)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

---

## 🙏 Agradecimientos

- Basado en los conceptos del libro "Compilers: Principles, Techniques, and Tools" (Dragon Book)
- Inspirado en el proyecto "sbn" de @alexmonnet
- Desarrollado como proyecto educativo para la asignatura de Compiladores

---

## 📞 Soporte

Si encuentras algún problema o tienes sugerencias:

1. Abre un issue en GitHub
2. Envía un pull request con mejoras
3. Contacta al autor por email

---

**¡Gracias por usar Mini Compiler! 🎨**