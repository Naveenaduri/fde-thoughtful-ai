def sort(width, height, length, mass):
    volume = width * height * length
    is_bulky = volume >= 10**6 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    return "REJECTED" if is_bulky and is_heavy else ("SPECIAL" if is_bulky or is_heavy else "STANDARD")
