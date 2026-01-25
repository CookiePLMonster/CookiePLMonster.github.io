---
layout: bonuscodes
title: "LMA Manager 2004"
excerpt: "Cheat Generator for LMA Manager 2004."
image: "assets/img/bonuscodes/lma-manager-2004.jpg"
order: "lma manager 2004"
---

{:.credit}
Bonus Codes implemented by [Bo](https://32bits.substack.com){:target="_blank"}.

<script type="text/python">
from browser import ajax, bind, document, html
from generators import lma2004

@bind('#cheat-gen-form', 'submit')
def onGenerate(ev):
    data = ajax.form_data(ev.target)

    accessCode = int(data.get('access-code'))
    baseCheats = zip(['Rainbow trails', 'Toon sounds', 'Chariots of fire', 'Defying time', 'Full to the brim'],
                    lma2004.getBaseCodes())

    # LMA2004 has holes in cheat IDs
    cheatCodes = ['It always snows at matches', 'It is always sunny at matches', 'It always rains at matches', None, 'Moon ball', None,
                    'Helium shouts', 'Bass shouts', 'Card free zone', None, 'Crème de la crème', None, 'Healing hands',
                    'Do you want to be in my gang?', 'Rome wasn’t built in a day', 'Armchair selection', None,
                    'No more money worries', 'All bonuses']

    outputBlock = document['output-window']
    outputs = outputBlock.select_one('output')
    outputBlock.style.display = 'block'
    outputs.clear()

    def gen():
        for index, cheat in enumerate(cheatCodes):
            if cheat:
                cryptedCode = lma2004.generateCode(accessCode, index)
                if cryptedCode:
                    yield cheat, cryptedCode
        for cheat in baseCheats:
            yield cheat[0], cheat[1]
    outputs <= html.DL(html.DIV(html.DT(term + ':') + ' ' + html.DD(code)) for term, code in gen())

document['access-code'].min = 1
document['access-code'].max = lma2004.ACCESS_CODE_MAX
</script>
