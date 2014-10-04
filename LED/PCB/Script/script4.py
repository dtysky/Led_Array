import string

import struct

out=open('Led.scr','w');

w=201.3
h_s=724.8
for i in range(120):
    
    h=h_s
    
    
    for j in range(76):

        wtf='add'+'  '+'connect'+';'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
        out.write(wtf)

        w=w+0.7
        wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
        out.write(wtf)
        wtf='pick'+'  '+'dbl'+'  '+str(w)+'  '+str(h)+';'+'\n'
        out.write(wtf)

        wtf='done'+';'+'\n'
        out.write(wtf)

        w=w-0.7

        h=h-2

    w=w+2



