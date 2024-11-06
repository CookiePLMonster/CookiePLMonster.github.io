ACCESS_CODE_MAX = 99999

def generateCode(accessCode, cheatID, prototype=False):
    # Verify domain of inputs
    if not (accessCode >= 0 and accessCode <= ACCESS_CODE_MAX
        and cheatID >= 0 and cheatID <= 99):
        return None

    # Helper functions
    def toSigned32(n):
        n = n & 0xffffffff
        return (n ^ 0x80000000) - 0x80000000

    # Division like int / int in C, rounding towards zero
    def idiv(x, y):
        return int(x / y)

    # Remainder like % in C
    def rem(x, y):
        return x - int(x / y) * y

    def calcSeed(input):
        if input != 0:
            seed = 0x181AB
            for _ in range(input - 1):
                seed = rem(toSigned32(0x181AB * seed), 0x5243)
        else:
            seed = 1
        return seed

    if prototype:
        cheatIDMagic = (0x13CB5B * cheatID) & 0xffffffff
        accessCodeMagic = ((accessCode % 100) ^ (0x20B9 * cheatIDMagic)) & 0xffffffff

        seed1 = calcSeed(accessCodeMagic % 0x853)
        seed2 = calcSeed((((accessCodeMagic ^ 0x114CF1) * ((0x41B * cheatIDMagic) ^ (accessCode // 100 % 100))) & 0xffffffff) % 0x8CB)
    else:
        cheatIDMagic = toSigned32(0x13CB5B * cheatID % 0x26DD)
        accessCodeMagic = toSigned32((accessCode % 1000) ^ (0x20B9 * cheatIDMagic))

        seed1 = calcSeed(rem(accessCodeMagic, 0x853))
        seed2 = calcSeed(rem(toSigned32((accessCodeMagic ^ 0x114CF1) * ((0x41B * cheatIDMagic) ^ (accessCode // 1000 % 1000))), 0x8CB))

    buffer = [0] * 6

    buffer[0] = rem(seed1, 26) + ord('A')
    buffer[1] = rem(idiv(seed1, 676), 26) + ord('A')
    buffer[2] = rem(idiv(seed1, 26), 26) + ord('A')
    buffer[3] = rem(idiv(seed2, 26), 26) + ord('A')
    buffer[4] = rem(idiv(seed2, 676), 26) + ord('A')
    buffer[5] = rem(seed2, 26) + ord('A')

    feedback1 = toSigned32((buffer[0] << 24) + (buffer[1] << 16) + (buffer[2] << 8) + buffer[3])
    if prototype:
        feedback2 = toSigned32((buffer[4] << 24) + (buffer[5] << 16) + (buffer[0] << 8) + buffer[1])
    else:
        sumAllButLast = toSigned32(sum(buffer[:-1]))
        feedback2 = toSigned32((buffer[4] << 24) + (buffer[5] << 16) + ((sumAllButLast + rem(cheatIDMagic ^ 0x197ABD9, seed1 & 0xFFFFFFFF)) << 8)
                    + sumAllButLast + rem(cheatIDMagic ^ 0x13478FDD, seed2 & 0xFFFFFFFF))

    IV = [491, 563, 613, 661, 733, 797, 857, 919, 983, 1039]

    for i in range(80):
        (feedback2, feedback1) = (feedback1 ^ IV[i % 10], feedback2 ^ feedback1)

    buffer[0] = rem((feedback2 >> 24) & 0xFF, 26) + ord('A')
    buffer[1] = rem((feedback2 >> 16) & 0xFF, 26) + ord('A')
    buffer[2] = rem((feedback1 >> 24) & 0xFF, 26) + ord('A')
    buffer[3] = rem((feedback1 >> 16) & 0xFF, 26) + ord('A')
    buffer[4] = rem((feedback1 >> 8) & 0xFF, 26) + ord('A')
    buffer[5] = rem(feedback1 & 0xFF, 26) + ord('A')
    return ''.join([chr(x) for x in buffer])
