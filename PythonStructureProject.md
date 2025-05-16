https://www.pythonbynight.com/blog/starting-python-project
https://guicommits.com/organize-python-code-like-a-pro/

Use lowercase_with_underscores for module, package, function, method, variable, and constant names.
Use UpperCamelCase for class names.

mi_proyecto/
│
├── src/ # Código fuente principal
│ └── mi_proyecto/ # Módulo principal
│ ├── **init**.py
│ ├── core/ # Funcionalidad central
│ ├── utils/ # Utilidades
│ └── config/ # Configuraciones
│
├── tests/ # Pruebas
│ ├── **init**.py
│ ├── test_core/
│ └── test_utils/
│
├── docs/ # Documentación
│ ├── api/
│ └── user_guide/
│
├── requirements/ # Dependencias
│ ├── base.txt
│ ├── dev.txt
│ └── test.txt
│
├── .gitignore # Archivos ignorados por git
├── README.md # Documentación principal
├── setup.py # Script de instalación
├── pyproject.toml # Configuración de herramientas
└── requirements.txt # Dependencias principales
