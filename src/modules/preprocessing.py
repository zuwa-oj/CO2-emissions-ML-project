# Emission rate needs to be converted from string to numeric and '-' entries will be converted to NaN

def co2_to_float(value):
    try:
        return float(value)
    except:
        return None