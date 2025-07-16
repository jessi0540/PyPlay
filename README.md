# PyPlay - Automatización de pruebas para Parabank con Playwright y POM

Proyecto para automatizar el registro de usuarios en [Parabank](https://parabank.parasoft.com/parabank) usando Python, Playwright, el patrón Page Object Model (POM) y herramientas modernas como Poetry y pytest-html.

---

## 🧱 Estructura del Proyecto

```
PyPlay/
├── pages/               # Objetos de página (POM)
├── tests/               # Casos de prueba
├── utils/               # Configuraciones (como BASE_URL)
├── screenshots/         # Capturas automáticas en fallos
├── reports/             # Reportes HTML generados
├── .github/workflows/   # CI con GitHub Actions (opcional)
├── conftest.py          # Fixtures de Playwright
├── pytest.ini           # Configuración pytest-html
├── pyproject.toml       # Configuración de Poetry
├── requirements.txt     # Dependencias (si no usas Poetry)
├── run_all.bat          # Limpieza, pruebas y apertura del reporte
└── README.md
```

---

## 🚀 Instalación y configuración

### Requisitos:
- Python 3.12
- Poetry instalado: [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

### Instalación del proyecto:

```bash
poetry install
poetry run playwright install
```

---

## 🧪 Ejecución de pruebas

```bash
pytest
```

O usando el script:

```bash
run_all.bat
```
Este script limpia archivos temporales, instala dependencias, ejecuta las pruebas y abre el reporte HTML generado.

---

## 📊 Reporte HTML

Se genera automáticamente gracias a `pytest.ini`. El archivo final estará en:

```
reports/report.html
```

Puedes abrirlo manualmente o automáticamente desde el `.bat`.

---

## 🔧 Scripts incluidos

- `run_all.bat`: Limpieza, instalación, pruebas y apertura de reporte

---

## 🧼 Linting y formateo (opcional)

Usa estas herramientas si las instalaste con Poetry:

```bash
poetry run flake8
poetry run black .
```

---

## ✨ Autor

Jessica Esquivel

