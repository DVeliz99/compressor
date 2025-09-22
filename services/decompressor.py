from utils.archive import read_file, write_file
from utils.constants import MAX_BITS, CLEAR, EOI

"""
    Descomprime un archivo LZW.
"""
    
def decompress_file(src_path, dst_path):
    data = read_file(src_path, "rb")
    dict_ = {i: bytes([i]) for i in range(256)}
    next_code = 258
    code_size = 9
    output = bytearray()

    def read_code(data, bit_pos, code_size):
        byte_pos = bit_pos // 8
        bit_offset = bit_pos % 8
        if byte_pos + (code_size + bit_offset + 7) // 8 > len(data):
            return None, bit_pos
        val = 0
        for i in range((code_size + bit_offset + 7) // 8):
            val |= data[byte_pos + i] << (8 * i)
        val >>= bit_offset
        code = val & ((1 << code_size) - 1)
        return code, bit_pos + code_size

    bit_pos = 0
    prev = None
    while True:
        code, bit_pos = read_code(data, bit_pos, code_size)
        if code is None or code == EOI:
            break
        if code == CLEAR:
            dict_ = {i: bytes([i]) for i in range(256)}
            next_code = 258
            code_size = 9
            prev = None
            continue

        if code in dict_:
            entry = dict_[code]
        elif code == next_code and prev is not None:
            entry = dict_[prev] + dict_[prev][:1]
        else:
            print(f"KeyError: code={code}, next_code={next_code}, prev={prev}, code_size={code_size}")
            raise KeyError(code)

        output.extend(entry)

        if prev is not None and next_code < (1 << MAX_BITS):
            dict_[next_code] = dict_[prev] + entry[:1]
            next_code += 1
            if next_code == (1 << code_size) and code_size < MAX_BITS:
                code_size += 1

        prev = code

    write_file(dst_path, output, "wb")
    return len(output)