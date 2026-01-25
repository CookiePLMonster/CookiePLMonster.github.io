from .rd1 import ACCESS_CODE_MAX, generateCode as _generateCode

def getBaseCodes():
    return ['LMA2005MA', 'LMA2005MB', 'LMA2005MC', 'LMA2005A', 'LMA2005B']

def generateCode(accessCode, cheatID):
    result = _generateCode(accessCode, cheatID)
    if result is None:
        return None

    # Same algorithm as LMA2003, but with a 'swizzled' string
    return 'LMA2005' + result[5] + result[2] + result[3] + result[1] + result[0] + result[4]
