ACCESS_CODE_MAX = 9999

def generateCode(accessCode, cheatID):
    # Verify domain of inputs
    if not (accessCode >= 0 and accessCode <= ACCESS_CODE_MAX
        and cheatID >= 0 and cheatID <= 99):
        return None

    whole, part = divmod(accessCode, 100)
    exp1 = pow(0x39, cheatID ^ part, 0x44A5)
    exp2 = pow(0x39, cheatID ^ (whole % 100), 0x44A5)

    buffer = [
        ord('Z') - exp1 % 26,
        ord('Z') - exp1 // 676 % 26,
        ord('Z') - exp1 // 26 % 26,
        ord('Z') - exp2 // 26 % 26,
        ord('Z') - exp2 // 676 % 26,
        ord('Z') - exp2 % 26
    ]
    return ''.join([chr(x) for x in buffer])
