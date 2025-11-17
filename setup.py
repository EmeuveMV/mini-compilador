from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="simpledraw-compiler",
    version="1.0.0",
    author="Tu Nombre",
    author_email="tu-email@ejemplo.com",
    description="Un compilador completo para lenguaje de dibujo vectorial SimpleDraw",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/simpledraw-compiler",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Compilers",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "simpledraw=main:main",
        ],
    },
)
