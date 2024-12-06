---
layout: bonuscodes
title: "Colin McRae Rally 3"
excerpt: "Cheat Generator for Colin McRae Rally 3."
image: "assets/img/bonuscodes/cmr-3.jpg"
order: 1
---

<script type="text/python">
from browser import ajax, bind, document, html
from generators import cmr3

@bind('#cheat-gen-form', 'submit')
def onGenerate(ev):
    data = ajax.form_data(ev.target)

    accessCode = int(data.get('access-code'))
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
                yield cheat, cryptedCode
    outputs <= html.DL(html.DIV(html.DT(term + ':') + ' ' + html.DD(code)) for term, code in gen())

document['access-code'].min = 1
document['access-code'].max = cmr3.ACCESS_CODE_MAX
</script>
