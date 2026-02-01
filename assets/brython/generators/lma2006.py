ACCESS_CODE_MAX = 99999

ALPHABET = "0123456789ABCDEFGHJKLMNPQRTUVWXY"
XOR_MASK = 0xCC0DE3A54E7550F4
PRIVATE_EXPONENT = 0xB4DF15C731EF8A39
MODULUS = 0x0102B112A82EE4F459

def _encode_integer(val, length=13):
    ret = []
    for _ in range(length):
        ret.append(ALPHABET[val & 0x1F])
        val >>= 5

    return ''.join(ret)


def _get_target_value(unique_id, index):
    x = (index << 8) & 0xFFFF
    y = unique_id & 0xFFFF
    z = MODULUS & 0xFFFF
    return x | (y << 16) | (z << 32)

def generateCode(accessCode, cheatID):
    # Verify domain of inputs
    if not (accessCode >= 0 and accessCode <= ACCESS_CODE_MAX
        and cheatID >= 0 and cheatID <= 32):
        return None

    target = _get_target_value(accessCode, cheatID)
    required_rsa_val = target ^ XOR_MASK
    s_val = pow(required_rsa_val, PRIVATE_EXPONENT, MODULUS)
    return _encode_integer(s_val)
