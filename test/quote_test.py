
import re
text = '<quote:123>\nsf gsg \nsagds\n'




tt1 = 'adggds\nasgdg\nagfdgs\n    sgdfsgfg\n<quote:551255>'



print([text])



def _readq2(text,n=1):

    tt = None
    form = '<quoteb:%s>\n%s\n' + '    '*(n-1) +  '<quotee:%s>\n'

    ids = re.findall(r'<quote:(\d+)>',text)
    if not ids:
        return text
    for i in ids:
        tt = tt1

        tt = tt.split('\n')
        tt = [ '    '*n + t for t in tt]
        tt = '\n'.join(tt)

        text = text.replace('<quote:%s>'%i,form % (i,tt,i))
    return text # _readq(text)


def _readq(text,n=1):

    tt = None
    form = '<quoteb:%s>\n%s\n' + '    '*(n-1) +  '<quotee:%s>\n'

    ids = re.findall(r'<quote:(\d+)>',text)
    if not ids:
        return text
    for i in ids:
        tt = tt1

        tt = tt.split('\n')
        tt = [ '    '*n + t for t in tt]
        tt = '\n'.join(tt)

        text = text.replace('<quote:%s>'%i,form % (i,tt,i))
    return _readq2(text,n+1)



text = _readq(text)

print([text])

def quote_re(text):
    res = re.findall(r'<quoteb:(\d+)>([\w\W]+)<quotee:(\d+)>(\n)',text)
    for r in res:
        if r[0] == r[2]:
            replacetext = '<quoteb:%s>%s<quotee:%s>%s' % r
            text = text.replace(replacetext,'<quote:%s>' % r[0])
        else:
            raise ValueError('出错了')
    if res:
        return quote_re(text)
    else:
        return text
text = quote_re(text)

print([text])

