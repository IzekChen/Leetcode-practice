def make_multiplier(coefficient):
    product = 1

    def multiplier():
        nonlocal product
        product *= coefficient
        return product

    return multiplier


multipler3 = make_multiplier(3)
print(multipler3())