---
layout: bonuscodes
title: "TOCA Race Driver"
subtitle: "(Pro Race Driver, DTM Race Driver, V8 Supercars) Bonus Codes"
excerpt: "Cheat Generator for TOCA Race Driver/Pro Race Driver/DTM Race Driver/V8 Supercars."
image: "assets/img/bonuscodes/toca-race-driver.jpg"
order: 20
---

<script type="text/python">
from browser import document, html, bind
from generators import rd1

@bind('#generate', 'click')
def onGenerate(ev):
    plainCheats = rd1.getAlternateCodes()
    try:
        accessCode = int(document['access-code'].value)
        if not (accessCode >= 1 and accessCode <= rd1.ACCESS_CODE_MAX):
            raise ValueError
    except (TypeError, ValueError):
        document['invalid-access-code'].style.display = 'inline'
        return

    document['invalid-access-code'].style.display = 'none'
    cheatCodes = ['All cars', 'All tracks', 'Realistic handling', 'Realistic damage', 'All championships', 'All Pro Challenges',
                    'Different handling', 'Invincible cars', 'Unlock credits']

    outputBlock = document['output-window']
    outputs = outputBlock.select_one('output')
    outputBlock.style.display = 'block'
    outputs.clear()

    def gen():
        for index, cheat in enumerate(cheatCodes):
            cryptedCode = rd1.generateCode(accessCode, index)
            if cryptedCode:
                plainCode = plainCheats.get(index)
                if plainCode:
                    cryptedCode += '&nbsp;/&nbsp;' + plainCode
                yield html.B(f'{cheat}: ') + html.CODE(cryptedCode)
    outputs <= html.UL(html.LI(ch) for ch in gen())

document['access-code'].min = 1
document['access-code'].max = rd1.ACCESS_CODE_MAX
</script>