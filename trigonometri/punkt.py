from math import cos, sin, radians

def punkt(vinkel, lengde):
    x = int(cos(radians(vinkel)) * lengde)
    y = int(sin(radians(vinkel)) * lengde)

    return x, y