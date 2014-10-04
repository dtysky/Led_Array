import string

import struct

out=open('Led.scr','w');

w=200.1
h=726.85

for j in range(38):

    wtf='add'+'  '+'connect'+';'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
    w=w-0.5
    wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
    wtf='pick'+'  '+'dbl'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
    h=h-0.3
    wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
    wtf='done'+';'+'\n'
    out.write(wtf)
    h=h+0.3
    w=w+0.5
    h=h+2
