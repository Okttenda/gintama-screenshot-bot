import random


def Job():
    print("Tweet is processing!")
    rng = random.randrange(1, 3)
    if rng == 1:
        new_rng = random.randrange(0, 5718)
        path = f"./pics/Film_1/{new_rng}.png"
        return path
    elif rng == 2:
        new_rng = random.randrange(0, 6634)
        path = f"./pics/Film_2/{new_rng}.png"
        return path
    else:
        print("[ERROR] Could not choose an Option.")


