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
    data = read_file(src_path)
    code_size, next_code = 9, 258
    dict_ = {bytes([i]): i for i in range(256)}
    buf, cur, nbits = bytearray(), 0, 0

    def emit(code, size):
        nonlocal cur, nbits
        cur |= code << nbits
        nbits += size
        while nbits >= 8:
            buf.append(cur & 0xFF)
            cur >>= 8
            nbits -= 8

    emit(CLEAR, code_size)
    w = b""
    for c in data:
        wc = w + bytes([c])
        if wc in dict_:
            w = wc
        else:
            emit(dict_[w], code_size)
            if next_code < (1 << MAX_BITS):
                dict_[wc] = next_code
                next_code += 1
                if next_code == (1 << code_size) and code_size < MAX_BITS:
                    code_size += 1
            w = bytes([c])
    if w:
        emit(dict_[w], code_size)
    emit(EOI, code_size)
    buf.extend(cur.to_bytes((nbits + 7) // 8, "little"))
    write_file(dst_path, buf, "wb")
    return len(buf)