---
layout: bonuscodes
title: "TOCA Race Driver"
subtitle: "(Pro Race Driver, DTM Race Driver, V8 Supercars) Bonus Codes"
excerpt: "Cheat Generator for TOCA Race Driver/Pro Race Driver/DTM Race Driver/V8 Supercars."
image: "assets/img/bonuscodes/cmr-2005.jpg"
order: 20
---

<script type="text/python">
from browser import document, html
from generators import rd1

def onGenerate(ev):
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

    document['outbox-window-full'].style.display = 'block'
    document['output-window'].clear()

    def gen():
        for index, cheat in enumerate(cheatCodes):
            cryptedCode = rd1.generateCode(accessCode, index)
            if cryptedCode:
                yield html.B(f'{cheat}: ') + html.CODE(cryptedCode)
    document['output-window'] <= html.UL(html.LI(ch) for ch in gen())

document['generate'].bind('click', onGenerate)
document['access-code'].min = 1
document['access-code'].max = rd1.ACCESS_CODE_MAX
</script>
