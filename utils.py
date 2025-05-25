
import random


def dice(nb_faces):
    faces = [i+1 for i in range(nb_faces)]
    dice_roll = random.choice(faces)
    return dice_roll

def round(x):
    return int(x) + (random.random()<(x-int(x)))


