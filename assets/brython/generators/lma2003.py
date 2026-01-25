from .rd1 import ACCESS_CODE_MAX, generateCode as _generateCode

def getBaseCodes():
    return ['LMA2003MA', 'LMA2003MB', 'LMA2003MC', 'LMA2003A', 'LMA2003B']

def generateCode(accessCode, cheatID):
    result = _generateCode(accessCode, cheatID)
    if result is None:
        return None

    return 'LMA3' + result
