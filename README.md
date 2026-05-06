PreCheck Security - Prototipo Fase 1
Este proyecto es un sistema de validación de seguridad modular diseñado para el reconocimiento de archivos maliciosos mediante el uso de hashes SHA-256. El sistema permite escanear archivos y compararlos con una base de datos de amenazas conocidas, además de analizar la integridad de enlaces URL.

🚀 Características
Escaneo de Malware: Simulación de escaneo basada en firmas digitales únicas (Hashes).

Interfaz Gráfica (GUI): Entorno visual moderno e intuitivo desarrollado con CustomTkinter.

Arquitectura Modular: Código organizado profesionalmente en capas (Core, GUI, Tests).

Seguridad de Datos: Implementación de algoritmos SHA-256 para validación de integridad.

🛠️ Tecnologías utilizadas
Python 3.13: Lenguaje base del proyecto.

CustomTkinter: Para la interfaz gráfica de usuario.

Hashlib: Biblioteca estándar para la generación de hashes.

📋 Manual de Instalación y Uso
1. Requisitos Previos
Asegúrate de tener instalado Python 3.10 o superior en tu sistema.

2. Instalación de Dependencias
Para que la interfaz gráfica funcione correctamente, debes instalar la librería CustomTkinter ejecutando el siguiente comando en tu terminal (Git Bash o CMD):

Bash
pip install customtkinter
3. Descarga y Ejecución
Clonar el repositorio:

Bash
git clone https://github.com/humbertoantoniorodriguezmoran-web/PreCheck-Security---Prototipo-Fase-1.git
Entrar a la carpeta del proyecto:

Bash
cd PreCheck-Security---Prototipo-Fase-1
Ejecutar la aplicación:

Bash
python main.py
🧪 Pruebas y Verificación (Carpeta /tests)
El proyecto incluye una carpeta de pruebas para verificar el funcionamiento del motor de detección:

Cómo probar: Desde la interfaz del programa, haz clic en "Seleccionar Archivo" y navega hasta la carpeta tests. Al seleccionar los archivos allí presentes, el sistema generará el hash y mostrará si coincide con una amenaza conocida.

🔗 Escaneo de Enlaces
El sistema permite validar protocolos de seguridad en URLs (ej: [https://www.google.com](https://www.google.com)) para verificar que el formato sea correcto y simular un análisis de reputación.

✒️ Autor
Humberto Rodriguez - Ingeniería de Sistemas / Especialista en Ciberseguridad