import random

metros_en_kilometros = 1000
avengers = ["Thor", "IronMan", "Hulk", "Wolverine"]


def tomar_extension(filename):
    return filename[filename.index(".") + 1:]

def tirar_dado(num):
    return random.randint(1, num)
