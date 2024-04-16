---
layout: bonuscodes
title: "Colin McRae Rally 04"
excerpt: "Cheat Generator for Colin McRae Rally 04."
image: "assets/img/bonuscodes/cmr-04.jpg"
order: 2
---

<script type="text/python">
from browser import ajax, bind, document, html
from generators import cmr04

@bind('#cheat-gen-form', 'submit')
def onGenerate(ev):
    data = ajax.form_data(ev.target)
    
    accessCode = int(data.get('access-code'))
    cheatCodes = ['GroupB with 2 cars', 'All Cars', 'All Tracks', 'Expert Mode', 'Auto - Upgrades', 'All Tests', 'Mirror Mode']

    outputBlock = document['output-window']
    outputs = outputBlock.select_one('output')
    outputBlock.style.display = 'block'
    outputs.clear()

    def gen():
        for index, cheat in enumerate(cheatCodes):
            cryptedCode = cmr04.generateCode(accessCode, index)
            if cryptedCode:
                yield html.B(f'{cheat}: ') + html.CODE(cryptedCode)
    outputs <= html.UL(html.LI(ch) for ch in gen())

document['access-code'].min = 1
document['access-code'].max = cmr04.ACCESS_CODE_MAX
</script>
