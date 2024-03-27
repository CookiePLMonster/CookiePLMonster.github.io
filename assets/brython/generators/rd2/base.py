ACCESS_CODE_MAX = 9999

def getPlatformData(platform):
    platforms = {
        'pc': (79838997, 107, 453889, 456959),
        # PS2 uses an alternate algorithm, despite having defined its own platform data for the original algo
        'ps2': (11131719, 263, 453889, 456959),
        'psp': (31873457, 211, 453889, 456959),
        'xbox': (93199323, 179, 453889, 456959)
    }
    return platforms[platform]

def generateCode(platformData, accessCode, cheatID):
    # Verify domain of inputs
    if not (accessCode >= 0 and accessCode <= ACCESS_CODE_MAX
        and cheatID >= 0 and cheatID <= 99):
        return None

    # Helper functions
    # Division like int / int in C, rounding towards zero
    def idiv(x, y):
        return int(x / y)

    # Remainder like % in C
    def rem(x, y):
        return x - int(x / y) * y

    def calcSeed(input, mult):
        if input != 0:
            seed = platformData[1]
            for _ in range(input - 1):
                seed = rem((platformData[2] + seed * platformData[1] * mult) & 0xFFFFFFFF, platformData[3])
        else:
            seed = 1
        return seed

    seed1 = calcSeed(rem(cheatID, 100) ^ rem(accessCode, 100) ^ rem(platformData[0], 100), rem(idiv(platformData[0], 10000), 100))
    seed2 = calcSeed(rem(cheatID, 100) ^ rem(idiv(platformData[0], 100), 100) ^ rem(idiv(accessCode, 100), 100), rem(idiv(platformData[0], 1000000), 100))

    buffer = [0] * 8

    buffer[0] = rem(seed1, 26)
    buffer[1] = rem(idiv(seed1, 26), 26)
    buffer[2] = rem(idiv(seed1, 676), 26)
    buffer[3] = rem(idiv(seed1, 17576), 26)
    buffer[4] = rem(seed2, 26)
    buffer[5] = rem(idiv(seed2, 26), 26)
    buffer[6] = rem(idiv(seed2, 676), 26)
    buffer[7] = rem(idiv(seed2, 17576), 26)
    return ''.join([chr(x + ord('A')) for x in buffer])
