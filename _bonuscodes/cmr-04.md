---
layout: bonuscodes
title: "Colin McRae Rally 04"
excerpt: "Cheat Generator for Colin McRae Rally 04."
image: "assets/img/bonuscodes/cmr-04.jpg"
order: 2
---

<script type="text/python">
from browser import document, html
from generators import cmr04

def onGenerate(ev):
    try:
        accessCode = int(document['access-code'].value)
        if not (accessCode >= 1 and accessCode <= cmr04.ACCESS_CODE_MAX):
            raise ValueError
    except (TypeError, ValueError):
        document['invalid-access-code'].style.display = 'inline'
        return

    document['invalid-access-code'].style.display = 'none'
    cheatCodes = ['GroupB with 2 cars', 'All Cars', 'All Tracks', 'Expert Mode', 'Auto - Upgrades', 'All Tests', 'Mirror Mode']

    document['outbox-window-full'].style.display = 'block'
    document['output-window'].clear()

    def gen():
        for index, cheat in enumerate(cheatCodes):
            cryptedCode = cmr04.generateCode(accessCode, index)
            if cryptedCode:
                yield html.B(f'{cheat}: ') + html.CODE(cryptedCode)
    document['output-window'] <= html.UL(html.LI(ch) for ch in gen())

document['generate'].bind('click', onGenerate)
document['access-code'].min = 1
document['access-code'].max = cmr04.ACCESS_CODE_MAX
</script>
