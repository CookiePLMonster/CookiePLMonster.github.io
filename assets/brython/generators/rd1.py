from .cmr3 import ACCESS_CODE_MAX, generateCode as _generateCode

def getAlternateCodes():
    return {2 : 'SIM', 3 : 'DAMAGE', 8 : 'CREDITS'}

def generateCode(accessCode, cheatID):
    result = _generateCode(accessCode, cheatID)
    if result is None:
        return None

    # CMR3's codes are generated as 'Z' - x, Race Driver's are x + 'A'
    return ''.join([chr(-ord(c) + ord('Z') + ord('A')) for c in result])
