---
layout: bonuscodes
title: "TOCA Race Driver 2"
subtitle: "(DTM Race Driver 2, V8 Supercars 2, Race Driver 2006) Bonus Codes"
excerpt: "Cheat Generator for TOCA Race Driver 2/DTM Race Driver 2/V8 Supercars 2/Race Driver 2006."
image: "assets/img/bonuscodes/cmr-2005.jpg"
order: 21
---

<script type="text/python">
from browser import document, html
import htmlgen
from generators import rd2
from generators.rd2 import ps2

def onGenerate(ev):
    platform = document['platform']
    platformName = platform.options[platform.selectedIndex].value
    if ps2.supportsPlatform(platformName):
        generateFn = ps2.generateCode
        platformData = None
    else:
        generateFn = rd2.generateCode
        platformData = rd2.getPlatformData(platformName)

    try:
        accessCode = int(document['access-code'].value)
        if not (accessCode >= 1 and accessCode <= rd2.ACCESS_CODE_MAX):
            raise ValueError
    except (TypeError, ValueError):
        document['invalid-access-code'].style.display = 'inline'
        return

    numFootnotes = 0
    document['invalid-access-code'].style.display = 'none'
    cheatCodes = ['Unlock championships', 'Unlock bonus championships', 'Double engine power', 'Swap FWD to RWD and vice versa', 'Invincible cars', 'Unlock cutscenes']
    if platformName == 'psp':
        cheatCodes.append('Unlock all Trans World Cup events' + htmlgen.toStr(htmlgen.newElement(document['footnote-sup'], id='rd2006-only', notenum=1, num=0)))
        numFootnotes += 1

    document['outbox-window-full'].style.display = 'block'
    document['output-window'].clear()

    document['output-footnotes-full'].style.display = 'block'
    document['output-footnotes'].clear()
    if numFootnotes > 0:
        document['output-footnotes'] <= htmlgen.newElement(document['footnote-template'], id='rd2006-only', num=1, note='Race Driver 2006 only.')

    def gen():
        for index, cheat in enumerate(cheatCodes):
            cryptedCode = generateFn(platformData, accessCode, index)
            if cryptedCode:
                yield html.B(f'{cheat}: ') + html.CODE(cryptedCode)
    document['output-window'] <= html.UL(html.LI(ch) for ch in gen())

document['generate'].bind('click', onGenerate)
document['access-code'].min = 1
document['access-code'].max = rd2.ACCESS_CODE_MAX

document['platform-select'].style.display = 'inline'
document['platform'] <= (html.OPTION(n, value=i) for n, i in [('PC', 'pc'), ('PS2', 'ps2'), ('PSP', 'psp'), ('Xbox', 'xbox')])
</script>
