import time
import os

"""
Mide el tiempo de ejecución de una función.
    
Args:
    func (callable): función a ejecutar.
    *args, **kwargs: argumentos de la función.
    
Returns:
    tuple: (resultado de la función, tiempo de ejecución en segundos)
"""
def measure_time(func, *args, **kwargs):

    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return result, end - start

"""
Calcula la tasa de compresión de un archivo.
    
Args:
    original_file (str or Path): ruta del archivo original.
    compressed_file (str or Path): ruta del archivo comprimido.
    
Returns:
    float: relación comprimido/original (tasa de compresión)
"""
def compression_ratio(original_file, compressed_file):

    size_original = os.path.getsize(original_file)
    size_compressed = os.path.getsize(compressed_file)
    return size_compressed / size_original
