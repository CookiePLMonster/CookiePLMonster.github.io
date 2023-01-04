---
layout: bonuscodes
title: "Colin McRae Rally 3"
excerpt: "Cheat Generator for Colin McRae Rally 3."
image: "assets/img/bonuscodes/cmr-3.jpg"
order: 1
---

<script type="text/python">
from browser import document, html

ACCESS_CODE_MAX = 9999

def generateCode(accessCode, cheatID):
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
            seed = 0x39
            for _ in range(input - 1):
                seed = rem(toSigned32(0x39 * seed), 0x44A5)
        else:
            seed = 1
        return seed

    seed1 = calcSeed(rem(cheatID, 100) ^ rem(accessCode, 100))
    seed2 = calcSeed(rem(cheatID, 100) ^ rem(idiv(accessCode, 100), 100))

    buffer = [0] * 6

    buffer[0] = ord('Z') - rem(seed1, 26)
    buffer[1] = ord('Z') - rem(idiv(seed1, 676), 26)
    buffer[2] = ord('Z') - rem(idiv(seed1, 26), 26)
    buffer[3] = ord('Z') - rem(idiv(seed2, 26), 26)
    buffer[4] = ord('Z') - rem(idiv(seed2, 676), 26)
    buffer[5] = ord('Z') - rem(seed2, 26)
    return ''.join([chr(x) for x in buffer])

def onGenerate(ev):
    try:
        accessCode = int(document['access-code'].value)
        if not (accessCode >= 1 and accessCode <= ACCESS_CODE_MAX):
            raise ValueError 
    except (TypeError, ValueError):
        document['invalid-access-code'].style.display = 'inline'
        return

    document['invalid-access-code'].style.display = 'none'
    cheatCodes = ['Buggy', 'Plane', 'Hovercraft', 'Battle Tank', 'RC Car', 'All Cars', 'All Tracks', 'All Parts',
                    'All Difficulties', 'Ford Super Focus']

    document['outbox-window-full'].style.display = 'block'
    document['output-window'].clear()
    for index, cheat in enumerate(cheatCodes):
        cryptedCode = generateCode(accessCode, index)
        if cryptedCode:
            document['output-window'] <= html.B(f'{cheat}: ') + html.CODE(f'{cryptedCode}') + html.BR()

document['generate'].bind('click', onGenerate)
document['access-code'].min = 1
document['access-code'].max = ACCESS_CODE_MAX
</script>
