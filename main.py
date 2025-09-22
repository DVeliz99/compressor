import os
from utils.helpers import measure_time, compression_ratio
from services.compressor import compress_file


src_file = "data/input.txt"
compressed_file = "data/compressed.lzw"


# Medir tiempo de compresión
size_compressed, time_compress = measure_time(compress_file, src_file, compressed_file)


# Calcular tasa de compresión
tasa = compression_ratio(src_file, compressed_file)

print(f"Tamaño original: {os.path.getsize(src_file)} bytes")
print(f"Tamaño comprimido: {size_compressed} bytes")
print(f"Tasa de compresión: {tasa:.2f}")
print(f"Tiempo de compresión: {time_compress:.4f} s")

