import string

import struct

out=open('Led.scr','w');

w=202
h=536.8

for j in range(120):

    wtf='add'+'  '+'connect'+';'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)

    
    h=h-114
    wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
    wtf='pick'+'  '+'dbl'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)

    w=w-0.6
    wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
    
    w=w+0.6    
    h=h+114
    wtf='done'+';'+'\n'
    out.write(wtf)


    w=w+2



