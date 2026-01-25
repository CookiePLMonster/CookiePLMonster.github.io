import struct
from collections import namedtuple

ACCESS_CODE_MAX = 9999

def getPlatformData(platform):
    KeyPrimes = namedtuple('KeyPrimes', ['p', 'q'])
    PlatformData = namedtuple('PlatformData', ['d', 'n'])
    platforms = {
        'pc': (KeyPrimes(800275543, 33679599593), KeyPrimes(736102667, 32321152561)),
        'ps2': (KeyPrimes(755290271, 25307185187), KeyPrimes(957791771, 22229576947)),
        'xbox': (KeyPrimes(975859499, 20674904099), KeyPrimes(919308361, 33019433663))
    }
    e = 65537
    keys = platforms[platform]

    keyNormal = PlatformData(pow(e, -1, (keys[0].p-1) * (keys[0].q-1)), keys[0].p * keys[0].q)
    keyHonda = PlatformData(pow(e, -1, (keys[1].p-1) * (keys[1].q-1)), keys[1].p * keys[1].q)
    return (keyNormal, keyHonda)

def generateCode(platformData, accessCode, cheatID):
    # Verify domain of inputs
    if not (accessCode >= 0 and accessCode <= ACCESS_CODE_MAX
        and cheatID >= 0 and cheatID <= 32):
        return None

    xor = 14703658657559957748
    salt = platformData.n & 0xFFFF
    packed = int.from_bytes(struct.pack('<BBHH', 0, cheatID, accessCode, salt), 'little') ^ xor
    encrypted = pow(packed, platformData.d, platformData.n)

    alphabet = '0123456789ABCDEFGHJKLMNPQRTUVWXY'
    result = ''
    # As discovered by HOR163, generated cheat strings must always be 13 characters long
    for _ in range(13):
        result += alphabet[encrypted & 0x1F]
        encrypted >>= 5
    return result
