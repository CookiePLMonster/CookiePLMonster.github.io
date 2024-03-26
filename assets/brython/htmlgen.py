from browser import html
from browser.template import Template

def newElement(template, *args, **kwargs):
    newFootnote = template.clone().content

    h4ck = html.DIV()
    h4ck <= newFootnote
    elem = html.DIV(h4ck)
    Template(h4ck).render(*args, **kwargs)

    return elem.child_nodes

def toStr(elems):
    result = ''
    for e in elems:
        if e.html is not None:
            result += e.html.strip()
    return result
