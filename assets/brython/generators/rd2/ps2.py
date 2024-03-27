from . import base as base

def supportsPlatform(platform):
    return platform == 'ps2'

def generateCode(_, accessCode, cheatID):
    # Verify domain of inputs
    if not (accessCode >= 0 and accessCode <= base.ACCESS_CODE_MAX
        and cheatID >= 0 and cheatID <= 99):
        return None

    # Helper functions
    # Division like int / int in C, rounding towards zero
    def idiv(x, y):
        return int(x / y)

    # Remainder like % in C
    def rem(x, y):
        return x - int(x / y) * y

    def rem64(x):
        return rem(x, 0xFFFFFFFB)

    val1 = 1
    val2 = (accessCode + 19) * (cheatID + 17)

    loopCtr = 10007
    while loopCtr != 0:
        if loopCtr & 1:
            a = rem64(val1 * val2)
            b = rem64((val1 >> 32) * val2)
            a = rem64(a + (b * 64))
            b = rem64(val1 * (val2 >> 32))
            a = rem64(a + (b * 64))
            b = rem64((val1 >> 32) * (val2 >> 32))
            val1 = rem64(a + (b * 128))

        a = rem64(val2 * val2)
        b = rem64((val2 >> 32) * val2)
        a = rem64(a + (b * 64))
        b = rem64(val2 * (val2 >> 32))
        a = rem64(a + (b * 64))
        b = rem64((val2 >> 32) * (val2 >> 32))
        val2 = rem64(a + (b * 128))
        loopCtr >>= 1

    val1 = rem(val1 ^ 0xFA47D181, 0x309F1020EF)
    seed = (val1 ^ ((val1 ^ (val1 >> 8) ^ (val1 >> 16) ^ (val1 >> 24) ^ (val1 >> 32) ^ (val1 >> 40) ^ (val1 >> 48) ^ (val1 >> 56)) << 33)) & 0x1FFFFFFFFFF
    buffer = []
    for x in range(8):
        buffer.append(rem(idiv(seed, 26**x), 26))

    return ''.join([chr(x + ord('A')) for x in buffer])
