---
layout: bonuscodes
title: "LMA Manager 2005"
excerpt: "Cheat Generator for LMA Manager 2005."
image: "assets/img/bonuscodes/lma-manager-2005.jpg"
order: "lma manager 2005"
---

{:.credit}
Bonus Codes implemented by [Bo](https://32bits.substack.com){:target="_blank"}.

<script type="text/python">
from browser import ajax, bind, document, html
from generators import lma2005

@bind('#cheat-gen-form', 'submit')
def onGenerate(ev):
    data = ajax.form_data(ev.target)

    accessCode = int(data.get('access-code'))
    baseCheats = zip(['Moon ball', 'Helium shouts', 'Bass shouts', 'Healing hands', 'No more money worries'],
                    lma2005.getBaseCodes())

    # LMA2005 has holes in cheat IDs
    cheatCodes = ['It always snows at matches', 'It is always sunny at matches', 'It always rains at matches', 'Rainbow trails', None,
                    'Toon sounds', None, None, 'Card free zone', 'Chariots of fire', 'Crème de la crème', 'Defying time', None,
                    'Do you want to be in my gang?', 'Rome wasn’t built in a day', 'Armchair selection', 'Full to the brim', None,
                    'All bonuses']

    outputBlock = document['output-window']
    outputs = outputBlock.select_one('output')
    outputBlock.style.display = 'block'
    outputs.clear()

    def gen():
        for index, cheat in enumerate(cheatCodes):
            if cheat:
                cryptedCode = lma2005.generateCode(accessCode, index)
                if cryptedCode:
                    yield cheat, cryptedCode
        for cheat in baseCheats:
            yield cheat[0], cheat[1]
    outputs <= html.DL(html.DIV(html.DT(term + ':') + ' ' + html.DD(code)) for term, code in gen())

document['access-code'].min = 1
document['access-code'].max = lma2005.ACCESS_CODE_MAX
</script>
