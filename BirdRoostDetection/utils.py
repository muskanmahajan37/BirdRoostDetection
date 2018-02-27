from enum import Enum

RADAR_FILE_DIR = 'radarfiles/'
RADAR_IMAGE_DIR = 'radarimages/'


class ML_Set(Enum):
    """Machine learning set enum, includes validation, train, and test."""
    validation = 0, 'Validation'
    training = 1, 'Training'
    testing = 2, 'Testing'

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value


class Radar_Products(Enum):
    """Radar Product enum, includes reflectivity, velocity, rho_hv, and zdr."""
    reflectivity = 0, 'Reflectivity'
    velocity = 1, 'Velocity'
    rho_hv = 2, 'Rho_HV'
    zdr = 3, 'Zdr'

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value