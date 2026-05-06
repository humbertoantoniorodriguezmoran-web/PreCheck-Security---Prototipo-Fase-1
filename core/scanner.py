import hashlib
import os

#  BASE DE DATOS SIMULADA (FASE 1) 
# Hashes de archivos conocidos como los malware (Ejemplo: mi archivo EICAR)
MALWARE_DB = {
    "131f78150482393b9250d0069c96322924f3b86b51c04222070b09309a600238": "EICAR Test File (Simulación)",
    "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f": "EICAR (borra esa mierda mamawebo tu ere loco)"
}


# Dominios reportados
URL_BLACKLIST = [
    "malware-test.com",
    "sitio-phishing.net",
    "descarga-virus.org"
]

#  LÓGICA DE ESCANEO DE ARCHIVOS 
def generar_hash(ruta_archivo):
    """Genera la firma SHA-256 de un archivo."""
    sha256_hash = hashlib.sha256()
    try:
        with open(ruta_archivo, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def escanear_archivo(ruta):
    """Compara el archivo con la base de datos de firmas."""
    hash_calculado = generar_hash(ruta)
    
    if hash_calculado is None:
        return "Error", "El archivo no fue encontrado en la ruta especificada."
    
    if hash_calculado in MALWARE_DB:
        return "Peligro", f"Amenaza detectada: {MALWARE_DB[hash_calculado]}"
    
    return "Seguro", "No se detectaron amenazas conocidas en este archivo."

#  LÓGICA DE ESCANEO DE ENLACES (URLs) 
def escanear_url(url):
    """Analiza la seguridad de una URL."""
    url = url.lower().strip()
    
    # Verificación de protocolo seguro
    if not url.startswith("https://"):
        return "Advertencia", "El sitio no utiliza un protocolo seguro (HTTPS)."

    # Verificación en lista negra
    for dominio in URL_BLACKLIST:
        if dominio in url:
            return "Peligro", f"El dominio [{dominio}] está reportado por actividad maliciosa."

    return "Seguro", "El enlace no presenta anomalías conocidas en la Fase 1."