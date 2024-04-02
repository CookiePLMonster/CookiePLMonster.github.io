---
layout: bonuscodes
title: "TOCA Race Driver 3"
subtitle: "(DTM Race Driver 3, V8 Supercars 3, TOCA Race Driver 3 Challenge) Bonus Codes"
excerpt: "Cheat Generator for TOCA Race Driver 3/DTM Race Driver 3/V8 Supercars 3/TOCA Race Driver 3 Challenge."
image: "assets/img/bonuscodes/toca-race-driver-3.jpg"
order: 22
---

{:.disclaimer.info}
On PC, access code generation is broken and on 64-bit systems it always displays `????`.
See [Access Code Fix]({% link _games/toca-race-driver/toca-race-driver-3.md %}#access-code-fix){:target="_blank"} for a fix.

<script type="text/python">
from browser import document, html, bind
import htmlgen
from generators import rd2, rd3

@bind('#generate', 'click')
def onGenerate(ev):
    platform = document['platform']
    platformName = platform.options[platform.selectedIndex].value
    isPsp = platformName == 'psp'
    if isPsp:
        # TOCA Race Driver 3 Challenge uses RD2's PSP algorithm, but with shifted cheat IDs
        generateFn = lambda platformData, accessCode, cheatID: rd2.generateCode(platformData, accessCode, cheatID + 9)
        platformData = rd2.getPlatformData(platformName)
        platformData = (platformData, platformData)
    else:
        generateFn = rd3.generateCode
        platformData = rd3.getPlatformData(platformName)

    try:
        accessCode = int(document['access-code'].value)
        if not (accessCode >= 1 and accessCode <= rd3.ACCESS_CODE_MAX):
            raise ValueError
    except (TypeError, ValueError):
        document['invalid-access-code'].style.display = 'inline'
        return

    document['invalid-access-code'].style.display = 'none'
    if isPsp:
        cheatCodes = ['Unlock championships', 'Unlock bonus championships', 'Unlock cutscenes', 'Invincible cars']
    else:
        cheatCodes = ['Unlock championships', 'Unlock bonus championships', 'Boost for all cars', 'Turbo boost', 'Unlock toy cars', 'Unlock slot racer',
            'Invincible cars', 'Unlock cutscenes', '[unused]', 'Unlock Honda 2006', 'Unlock Honda', 'No streamed car sound']

    outputBlock = document['output-window']
    outputs = outputBlock.select_one('output')
    outputBlock.style.display = 'block'
    outputs.clear()

    noEffectFootnotes = 0
    hondaOnly = document['checkbox'].checked and not isPsp
    if not hondaOnly and not isPsp:
        cheatCodes[8] += htmlgen.newElement(document['footnote-sup'], id='no-effect', notenum=1, num=noEffectFootnotes)
        noEffectFootnotes += 1
        cheatCodes[11] += htmlgen.newElement(document['footnote-sup'], id='no-effect', notenum=1, num=noEffectFootnotes)
        noEffectFootnotes += 1

    def gen():
        for index, cheat in enumerate(cheatCodes):
            if hondaOnly and index != 9 and index != 10:
                continue
            cryptedCode = generateFn(platformData[0] if index != 9 and index != 10 else platformData[1], accessCode, index)
            if cryptedCode:
                yield html.B(cheat + ': ') + html.CODE(cryptedCode)

    outputFootnotesBlock = document['output-footnotes']
    outputFootnotes = outputFootnotesBlock.select_one('output')
    outputFootnotesBlock.style.display = 'block'
    outputFootnotes.clear()
    if noEffectFootnotes > 0:
        outputFootnotes <= html.OL(htmlgen.newElement(document['footnote-template'], id='no-effect', num=noEffectFootnotes, note='No effect.'))

    outputs <= html.UL(html.LI(ch) for ch in gen())

@bind('#platform', 'change')
def onPlatformChange(ev):
    platform = document['platform']
    if platform.options[platform.selectedIndex].value == 'psp':
        document['checkbox'].attrs['disabled'] = 'disabled'
    else:
        del document['checkbox'].attrs['disabled']

document['access-code'].min = 1
document['access-code'].max = rd3.ACCESS_CODE_MAX

document['platform-select'].style.display = 'inline'
document['platform'] <= (html.OPTION(n, value=i) for n, i in [('PC', 'pc'), ('PS2', 'ps2'), ('PSP (Race Driver 3 Challenge)', 'psp'), ('Xbox', 'xbox')])

document['additional-checkbox'].style.display = 'inline'
document['checkbox-label'].text = 'Honda codes only:'
</script>
