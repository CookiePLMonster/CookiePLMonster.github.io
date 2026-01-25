from .rd1 import ACCESS_CODE_MAX, generateCode as _generateCode

def getBaseCodes():
    return ['LMA2004MC', 'LMA2004MB', 'LMA2004B', 'LMA2004A', 'LMA2004MA']

def generateCode(accessCode, cheatID):
    result = _generateCode(accessCode, cheatID)
    if result is None:
        return None

    # Same algorithm as LMA2003, but with a 'swizzled' string
    return 'LMA2004' + result[3] + result[1] + result[2] + result[5] + result[4] + result[0]
