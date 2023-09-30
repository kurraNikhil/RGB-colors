import numpy as np

class RGBColor(np.dtype):
    """A custom data type to represent RGB colors."""

    name = 'rgb24'
    char = 'u'
    itemsize = 3
    fields = [('red', np.uint8), ('green', np.uint8), ('blue', np.uint8)]

def rgb_array(data):
    """Create a NumPy array of RGB colors from the given data."""
    return np.array(data, dtype=RGBColor)

# Example usage:

rgb_array([(255, 0, 0), (0, 255, 0), (0, 0, 255)])
