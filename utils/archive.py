import pathlib

"""
Lee un archivo y devuelve su contenido.
    
Args:
    file_path (str or Path): Ruta del archivo a leer.
    mode (str): Modo de apertura ('rb' para binario, 'r' para texto)
        
Returns:
    bytes o str: Contenido del archivo
        
"""
    
def read_file(file_path, mode="rb"):

    return pathlib.Path(file_path).read_bytes() if "b" in mode else pathlib.Path(file_path).read_text()

"""
Escribe datos en un archivo.
    
Args:
    file_path (str or Path): Ruta del archivo a escribir.
    data (bytes o str): Datos a escribir.
    mode (str): Modo de apertura ('wb' para binario, 'w' para texto)
"""

def write_file(file_path, data, mode="wb"):
    
    if "b" in mode:
        pathlib.Path(file_path).write_bytes(data)
    else:
        pathlib.Path(file_path).write_text(data)

"""
Verifica si un archivo existe.
    
Args:
    file_path (str or Path): Ruta del archivo.
        
Returns:
    bool: True si existe, False si no
"""

def file_exists(file_path):

    return pathlib.Path(file_path).exists()

"""
    Crea un archivo vacío (o lo sobrescribe si ya existe).
    
    Args:
        file_path (str or Path): Ruta del archivo a crear.
"""

def create_file(file_path):

    pathlib.Path(file_path).write_bytes(b"")
