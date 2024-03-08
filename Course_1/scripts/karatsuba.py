def recursion_multifpy(x:int, y:int):
    if x < y:
        return recursion_multifpy(y, x)
    elif y > 0:
        return (x + recursion_multifpy(x, y - 1))
    else:
        return 0


def karatsuba_algorithm(x:int, y:int):
    a, b = str(x), str(y)
    l1, l2 = len(a), len(b)
    lm = max(l1, l2)
    if lm == 1:
        return x * y
    
    half = lm // 2
    shift = lm - half
    # make both have same length
    a = '0'*(lm - l1) + a
    b = '0'*(lm - l2) + b

    a0, a1 = int(a[:half]), int(a[half:])
    b0, b1 = int(b[:half]), int(b[half:])

    #   a0*10^shift + a1
    # * b0*10^shift + b1
    # -------------------
    # a0*b0*10^(shfit*2) + (a0*b1+a1*b0)*10^(shfit) + a1b1
    # -------------------
    # z0 = a0 * b0
    # z2 = a1 * b1
    # z1 = (a0 + a1)(b0 + b1) = a0b0 + a1b1 + a1b0 + a0b1
    # a0b1 + a1b0 = z1 - z0 - z2
    z0 = karatsuba_algorithm(a0, b0)
    z2 = karatsuba_algorithm(a1, b1)
    z1 = karatsuba_algorithm((a1 + a0), (b1 + b0))
    return z0*10**(2*shift) + (z1 - z0 - z2)*10**shift + z2


print(karatsuba_algorithm(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))
