---
layout: bonuscodes
title: "Colin McRae Rally 3"
excerpt: "Cheat Generator for Colin McRae Rally 3."
image: "assets/img/bonuscodes/cmr-3.jpg"
order: 1
---

<script type="text/python">
from browser import document, html, bind
from generators import cmr3

@bind('#generate', 'click')
def onGenerate(ev):
    try:
        accessCode = int(document['access-code'].value)
        if not (accessCode >= 1 and accessCode <= cmr3.ACCESS_CODE_MAX):
            raise ValueError
    except (TypeError, ValueError):
        document['invalid-access-code'].style.display = 'inline'
        return

    document['invalid-access-code'].style.display = 'none'
    cheatCodes = ['Buggy', 'Plane', 'Hovercraft', 'Battle Tank', 'RC Car', 'All Cars', 'All Tracks', 'All Parts',
                    'All Difficulties', 'Ford Super Focus']

    outputBlock = document['output-window']
    outputs = outputBlock.select_one('output')
    outputBlock.style.display = 'block'
    outputs.clear()

    def gen():
        for index, cheat in enumerate(cheatCodes):
            cryptedCode = cmr3.generateCode(accessCode, index)
            if cryptedCode:
                yield html.B(f'{cheat}: ') + html.CODE(cryptedCode)
    outputs <= html.UL(html.LI(ch) for ch in gen())

document['access-code'].min = 1
document['access-code'].max = cmr3.ACCESS_CODE_MAX
</script>
