from . import tsl2591

def get_device(config: dict):
    return tsl2591.TSL2591(config)