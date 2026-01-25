---
layout: bonuscodes
title: "LMA Manager 2006"
excerpt: "Cheat Generator for LMA Manager 2006."
image: "assets/img/bonuscodes/lma-manager-2006.jpg"
order: "lma manager 2006"
---

{:.credit}
Bonus Codes implemented by [Bo](https://32bits.substack.com){:target="_blank"}.

<script type="text/python">
from browser import ajax, bind, document, html
from generators import lma2006

@bind('#cheat-gen-form', 'submit')
def onGenerate(ev):
    data = ajax.form_data(ev.target)

    accessCode = int(data.get('access-code'))
    cheatCodes = ['It always snows at matches', 'It is always sunny at matches', 'It always rains at matches', 'Rainbow trails', 'Moon ball', 'Toon sounds',
                    'Helium shouts', 'Bass shouts', 'Card free zone', 'Chariots of Fire', 'Crème de la crème', 'Defying time', 'Healing hands',
                    'Do you want to be in my gang?', 'Rome wasn’t built in a day', 'Armchair selection', 'Full to the brim', 'No more money worries',
                    'Youth Stars', 'Transfer Free-For-All', 'Training Boost', 'Super Staff', 'Happy Talky Talky', 'Job for Life', 'Permanent Vote of Confidence',
                    'Transfer Market Shutdown', 'Fantasy Team in the Money', 'All bonuses']

    outputBlock = document['output-window']
    outputs = outputBlock.select_one('output')
    outputBlock.style.display = 'block'
    outputs.clear()

    def gen():
        for index, cheat in enumerate(cheatCodes):
            cryptedCode = lma2006.generateCode(accessCode, index)
            if cryptedCode:
                yield cheat, cryptedCode
    outputs <= html.DL(html.DIV(html.DT(term + ':') + ' ' + html.DD(code)) for term, code in gen())

document['access-code'].min = 1
document['access-code'].max = lma2006.ACCESS_CODE_MAX
</script>
