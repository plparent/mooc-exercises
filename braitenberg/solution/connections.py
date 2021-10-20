from typing import Tuple

import numpy as np

def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    """res = 0.5 * np.ones(shape=shape[1], dtype="float32")
    res = np.tril(res)
    res = res[shape[1] - shape[0]:shape[1], :shape[1]]
    res[:shape[0] // 4] = 0"""
    res = np.zeros(shape=shape, dtype="float32")
    res[shape[0] // 2:, :shape[1] // 2] = 1
    #res[shape[0] // 2:, shape[1] // 2:] = -1
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    """res = 0.5 * np.ones(shape=shape[1], dtype="float32")
    res = np.flip(np.tril(res), axis=1)
    res = res[shape[1] - shape[0]:shape[1], :shape[1]]
    res[:shape[0] // 4] = 0"""
    res = np.zeros(shape=shape, dtype="float32")
    #res[shape[0] // 2:, :shape[1] // 2] = -1
    res[shape[0] // 2:, shape[1] // 2:] = 1
    return res
