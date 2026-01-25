---
layout: bonuscodes
title: "TOCA Race Driver"
subtitle: "(Pro Race Driver, DTM Race Driver, V8 Supercars) Bonus Codes"
excerpt: "Cheat Generator for TOCA Race Driver/Pro Race Driver/DTM Race Driver/V8 Supercars."
image: "assets/img/bonuscodes/toca-race-driver.jpg"
order: "toca race driver"
---

<script type="text/python">
from browser import ajax, bind, document, html
from generators import rd1

@bind('#cheat-gen-form', 'submit')
def onGenerate(ev):
    data = ajax.form_data(ev.target)

    accessCode = int(data.get('access-code'))
    plainCheats = rd1.getAlternateCodes()
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
                yield cheat, cryptedCode
    outputs <= html.DL(html.DIV(html.DT(term + ':') + ' ' + html.DD(code)) for term, code in gen())

document['access-code'].min = 1
document['access-code'].max = rd1.ACCESS_CODE_MAX
</script>
