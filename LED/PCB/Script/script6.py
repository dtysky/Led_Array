import string

import struct

out=open('Led.scr','w');

w=202
h=726.8

for j in range(120):

    wtf='add'+'  '+'connect'+';'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)

    w=w-1.3
    wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
    wtf='add'+'  '+'connect'+';'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)

    h=h-153
    wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
        
    w=w+1.3
    h=h+153
    wtf='done'+';'+'\n'
    out.write(wtf)


    w=w+2



