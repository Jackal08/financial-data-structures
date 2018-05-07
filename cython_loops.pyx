# Author: Jacques Joubert
# Email: jacques@quantsportal.com

# Core functions that need speed improvements
# All functions in this file are compiled via Cython
# Terminal: python setup.py build_ext --inplace

def set_row_groups(int units, data):
    """
    Used to set the groups for the Volume and Dollar bars.

    :param units: Number of units before a bar is created. For dollar
    bars this means the transaction size, for volume bars it means total
    volume processed before a new bar is created.
    :param data: numpy ndarray, represents the tick data
    :return: tick data with relevant groups
    """

    cdef long threshold = units
    cdef int g_count = 0
    cdef long i

    for i in range(0, data.shape[0]):
        # If value below threshold then set group
        # else increment group and set
        if data[i, 10] < threshold:
            data[i, 9] = g_count
        else:
            threshold = threshold + units
            g_count += 1
            data[i, 9] = g_count

    return data
