from utils.archive import read_file, write_file
from utils.constants import MAX_BITS, CLEAR, EOI

"""
Comprime un archivo usando LZW y funciones de archive.py.
    
Args:
    src_path (str or Path): archivo de entrada
    dst_path (str or Path): archivo de salida comprimido
Returns:
    int: tamaño del archivo comprimido en bytes
"""
def compress_file(src_path, dst_path):

    # Leer archivo original en modo binario
    data = read_file(src_path)
    
    code_size, next_code = 9, 258
    dict_ = {bytes([i]): i for i in range(256)}
    buf, cur, nbits = bytearray(), 0, 0

    def emit(code):
        nonlocal cur, nbits
        cur |= code << nbits
        nbits += code_size
        while nbits >= 8:
            buf.append(cur & 0xFF)
            cur >>= 8
            nbits -= 8

    emit(CLEAR)
    w = b""
    for c in data:
        wc = w + bytes([c])
        if wc in dict_:
            w = wc
        else:
            emit(dict_[w])
            if next_code < (1 << MAX_BITS):
                dict_[wc] = next_code
                next_code += 1
                if next_code == (1 << code_size):
                    code_size += 1
            w = bytes([c])
    if w: emit(dict_[w])
    emit(EOI)
    buf.extend(cur.to_bytes((nbits + 7) // 8, "little"))

    # Escribir archivo comprimido usando archive.py
    write_file(dst_path, buf, "wb")
    return len(buf)
