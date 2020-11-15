import numpy as np


def subcube_extractor(id_block=0):
    """
    Locate the position of one of the 27 3x3x3 cubes inside a 9x9x9 cube
    and return all its 27 values

    :param id_block: Number identification of one of the 27 3x3x3 cube
    :return block: A 3x3x3 subcube that contain 27 values
    """
    coordinates = {
        'z': int(np.floor(id_block / 9)),
        'y': int(np.floor(id_block % 9 / 3)),
        'x': id_block % 3
    }

    block = m[coordinates['z'] * 3:coordinates['z'] * 3 + 3, coordinates['y'] * 3:coordinates['y'] * 3 + 3,
            coordinates['x'] * 3:coordinates['x'] * 3 + 3]
    return block


def exchange(first_block=0, second_block=17):
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

    a = subcube_extractor(first_block)

    b = subcube_extractor(second_block)

    print('First Block')
    print(a)
    print('\n')
    print('Second Block')
    print(b)

    aux = a.copy()

    m[block_a['z'] * 3:block_a['z'] * 3 + 3, block_a['y'] * 3:block_a['y'] * 3 + 3,
    block_a['x'] * 3:block_a['x'] * 3 + 3] = b

    m[block_b['z'] * 3:block_b['z'] * 3 + 3, block_b['y'] * 3:block_b['y'] * 3 + 3,
    block_b['x'] * 3:block_b['x'] * 3 + 3] = aux

    return m


if __name__ == '__main__':
    cube = exchange(2, 5)
    print(cube)
