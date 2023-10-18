def powermod(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
        print("Base:", base, "Exponent:", exponent, "Modulus:", modulus)
    return result


a = powermod(809, 399, 775)
