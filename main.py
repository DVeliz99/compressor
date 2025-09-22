import os
from utils.helpers import measure_time, compression_ratio
from services.compressor import compress_file
from services.decompressor import decompress_file

src_file = "data/input.txt"
compressed_file = "data/compressed.lzw"
decompressed_file = "data/decompressed.txt"

# Medir tiempo de compresión
size_compressed, time_compress = measure_time(compress_file, src_file, compressed_file)

# Medir tiempo de descompresión
size_decompressed, time_decompress = measure_time(decompress_file, compressed_file, decompressed_file)

# Calcular tasa de compresión
tasa = compression_ratio(src_file, compressed_file)

print(f"Tamaño original: {os.path.getsize(src_file)} bytes")
print(f"Tamaño comprimido: {size_compressed} bytes")
print(f"Tasa de compresión: {tasa:.2f}")
print(f"Tiempo de compresión: {time_compress:.4f} s")
print(f"Tiempo de descompresión: {time_decompress:.4f} s")
print(f"Archivo descomprimido coincide con original: {size_decompressed == os.path.getsize(src_file)}")
