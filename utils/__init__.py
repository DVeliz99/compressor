#indica que la carpeta es un paquete

from .helpers import measure_time, compression_ratio
from .archive import read_file,write_file,file_exists,create_file

__all__ = ["read_file", "write_file","file_exists","create_file"]
__all__=["measure_time", "compression_ratio"] 