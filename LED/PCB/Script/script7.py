import string

import struct

out=open('Led.scr','w');

w=200.7
h=573.8

for j in range(120):

    wtf='add'+'  '+'connect'+';'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
    
    h=h-4.7
    wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
    wtf='pick'+'  '+'dbl'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
    wtf='add'+'  '+'connect'+';'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)

    w=w+0.6
    wtf='pick'+'  '+str(w)+'  '+str(h)+';'+'\n'
    out.write(wtf)
        
    h=h+4.7
    w=w-0.6
    wtf='done'+';'+'\n'
    out.write(wtf)


    w=w+2



