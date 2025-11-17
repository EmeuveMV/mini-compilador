# Makefile para SimpleDraw Compiler

.PHONY: help install test run clean examples docs

help:
	@echo "SimpleDraw Compiler - Comandos disponibles:"
	@echo "  make install   - Instalar el proyecto"
	@echo "  make test      - Ejecutar pruebas"
	@echo "  make run       - Ejecutar ejemplo por defecto"
	@echo "  make examples  - Compilar todos los ejemplos"
	@echo "  make clean     - Limpiar archivos generados"
	@echo "  make docs      - Generar documentación"

install:
	python -m pip install -e .

test:
	python -m pytest tests/ -v

run:
	python main.py

examples:
	@echo "Compilando ejemplos..."
	@for file in examples/*.sd; do \
		echo "Compilando $$file..."; \
		python main.py "$$file"; \
	done

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*_tokens.json" -delete
	find . -type f -name "*_intermediate.json" -delete
	rm -rf output/*.svg
	rm -rf build/ dist/ *.egg-info

docs:
	@echo "Documentación disponible en DOCUMENTATION.md"
