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

PROTOTYPE_OPTION = 'prototype'

@bind('#cheat-gen-form', 'submit')
def onGenerate(ev):
    data = ajax.form_data(ev.target)

    accessCode = int(data.get('access-code'))
    cheatCodes = ['GroupB with 2 cars', 'All Cars', 'All Tracks', 'Expert Mode', 'Auto - Upgrades', 'All Tests', 'Mirror Mode']
    prototype = PROTOTYPE_OPTION in data.getAll('options')

    outputBlock = document['output-window']
    outputs = outputBlock.select_one('output')
    outputBlock.style.display = 'block'
    outputs.clear()

    def gen():
        for index, cheat in enumerate(cheatCodes):
            cryptedCode = cmr04.generateCode(accessCode, index, prototype)
            if cryptedCode:
                yield cheat, cryptedCode
    outputs <= html.DL(html.DIV(html.DT(term + ':') + ' ' + html.DD(code)) for term, code in gen())

prototypeCheckbox = document['additional-option1']
prototypeCheckbox.style.display = 'inline'
prototypeCheckbox.select_one('label').text = 'Prototype:'
prototypeCheckbox.select_one('input').value = PROTOTYPE_OPTION

document['access-code'].min = 1
document['access-code'].max = cmr04.ACCESS_CODE_MAX
</script>
