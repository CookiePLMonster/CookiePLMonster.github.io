---
layout: bonuscodes
title: "LMA Manager 2003"
excerpt: "Cheat Generator for LMA Manager 2003."
image: "assets/img/bonuscodes/lma-manager-2003.jpg"
order: "lma manager 2003"
---

{:.credit}
Bonus Codes implemented by [Bo](https://32bits.substack.com){:target="_blank"}.

<script type="text/python">
from browser import ajax, bind, document, html
from generators import lma2003

@bind('#cheat-gen-form', 'submit')
def onGenerate(ev):
    data = ajax.form_data(ev.target)

    accessCode = int(data.get('access-code'))
    baseCheats = zip(['Sell Out', 'Anytime, Any Place', 'That’s All Folks', 'Loadza Money', 'Low Gravity Ball'],
                    lma2003.getBaseCodes())
    cheatCodes = ['Too Much Coffee', 'Rainbow Trails', 'Win, Win, Win', 'Psycho Team', 'Selective Sight', 'Medicine Man', 'Instant Stadium',
                    'Dream Team', 'Super Team', 'Sit Back And Relax', 'Winter Sport', 'You Are My Sunshine', 'Rain God', 'Forever Young',
                    'Super Coach', 'Don’t Worry, Be Happy', 'Teamwork', 'Pinky and Perky', 'Lucifer', 'Go Now']

    outputBlock = document['output-window']
    outputs = outputBlock.select_one('output')
    outputBlock.style.display = 'block'
    outputs.clear()

    def gen():
        for index, cheat in enumerate(cheatCodes):
            cryptedCode = lma2003.generateCode(accessCode, index)
            if cryptedCode:
                yield cheat, cryptedCode
        for cheat in baseCheats:
            yield cheat[0], cheat[1]
    outputs <= html.DL(html.DIV(html.DT(term + ':') + ' ' + html.DD(code)) for term, code in gen())

document['access-code'].min = 1
document['access-code'].max = lma2003.ACCESS_CODE_MAX
</script>
