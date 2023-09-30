import numpy as np

class GeoCoordinate(np.dtype):
    """A custom data type to represent geographic coordinates."""

    name = 'geocoordinate'
    char = 'g'
    itemsize = 16
    fields = [('latitude', np.float64), ('longitude', np.float64)]

def geocoordinate_array(data):
    """Create a NumPy array of geographic coordinates from the given data."""
    return np.array(data, dtype=GeoCoordinate)

# Example usage:

geocoordinate_array([(37.7833, -122.4167), (40.7127, -74.0059)])
