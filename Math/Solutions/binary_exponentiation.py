def power(base, exponent, MOD):
    res = 1

    while exponent > 0:
        # odd exponent? multiply the result by the base
        if exponent % 2 == 1:
            res = (res * base) % MOD

        # Square the base and halve the exponent
        base = (base * base) % MOD
        exponent //= 2

    return res
