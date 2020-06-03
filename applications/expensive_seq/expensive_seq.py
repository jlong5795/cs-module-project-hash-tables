def expensive_seq(x, y, z, cache={}):
    # declare an empty cache if one isn't passed in

    # skip caching for simple case
    if x <= 0:
        return y + z
    # for complex case check the cache
    if x > 0:
        # if key isn't found, compute and store
        if (x,y,z) not in cache:
            cache[(x,y,z)] = expensive_seq(x - 1, y + 1, z) + expensive_seq(x - 2, y + 2, z * 2) + expensive_seq(x - 3, y + 3, z * 3)
        # else return found value
        return cache[(x,y,z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
