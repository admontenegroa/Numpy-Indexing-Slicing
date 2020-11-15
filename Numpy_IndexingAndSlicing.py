import numpy as np


def localization(id_block=0):
    coordinates = {
        'z': int(np.floor(id_block / 9)),
        'y': int(np.floor(id_block % 9 / 3)),
        'x': id_block % 3
    }
    return coordinates


def exchange(first_block = 0, second_block=  17):
    """
    Exchange the position of two 3x3x3 blocks that make up
    a 9x9x9 block.

    The 3x3x3 blocks position is from 0 to 26.

    Keyword arguments:
    first_block -- the position of the first 3x3x3 block (default 0)
    second_block -- the position of the second 3x3x3 block (default 17)

    Returns:
    A 9x9x9 cube where the position of two 3x3x3 cubes was swapped.

    """
    if first_block > 26 or second_block > 26:
        raise ValueError("The position exceed the imaginary 3X3X3 block. The position must not be greater than 26!")

    if first_block == second_block:
        raise ValueError("The position of the two imaginary 3X3X3 block must not be the same!")

    m = np.arange(729).reshape(9, 9, 9)

    block_a = localization(first_block)

    A = m[block_a['z'] * 3:block_a['z'] * 3 + 3, block_a['y'] * 3:block_a['y'] * 3 + 3,
        block_a['x'] * 3:block_a['x'] * 3 + 3]

    block_b = localization(second_block)

    B = m[block_b['z'] * 3:block_b['z'] * 3 + 3, block_b['y'] * 3:block_b['y'] * 3 + 3,
        block_b['x'] * 3:block_b['x'] * 3 + 3]

    print('First Block')
    print(A)
    print('\n')
    print('Second Block')
    print(B)

    aux = A.copy()

    m[block_a['z'] * 3:block_a['z'] * 3 + 3, block_a['y'] * 3:block_a['y'] * 3 + 3,
    block_a['x'] * 3:block_a['x'] * 3 + 3] = B

    m[block_b['z'] * 3:block_b['z'] * 3 + 3, block_b['y'] * 3:block_b['y'] * 3 + 3,
    block_b['x'] * 3:block_b['x'] * 3 + 3] = aux

    return m


if __name__ == '__main__':
    m = exchange(2, 5)
    print(m)
