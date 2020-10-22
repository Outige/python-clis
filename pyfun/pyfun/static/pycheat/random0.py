import random

def random_random():
    # returns: float[0, 1)
    val = random.random()
    print(val)

def random_uniform():
    #returns: float[1, 5] - not too sure about inclusivity
    val = random.uniform(1, 5)
    print(val)


def random_choice():
    vals = [3,6,7,8,3]
    value = random.choice(vals)
    print(value)

def random_int():
    # returns: int[0, 9]
    val = random.randint(0, 9)
    print(val)

if __name__ == '__main__':
    random_random()
    random_uniform()
    random_choice()
    random_int()