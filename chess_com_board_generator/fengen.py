import numpy as np
import time
fen_chars=list('_KQRBNPkqrbnp')


def gen():
    fen_arr = np.random.choice(fen_chars, 64)
    fen_param = "".join(fen_arr)
    fen_arr = np.hstack(np.split(fen_arr, 8)[::-1])
    fen_arr[fen_arr == fen_chars[0]] = "1"
    img_filename_prefix = "/".join(map("".join, np.split(fen_arr, 8)))
    return img_filename_prefix
while True:
    print(gen())
    time.sleep(0.2)