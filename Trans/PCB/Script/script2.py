import string

import struct

out=open('Led.scr','w');

w_s=103
h_s=52.87

for k in range(2):
	w=w_s
	h=h_s
	
##	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'180'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
##	out.write(wtf)
##	
##	w=w+25
##	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'180'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
##	out.write(wtf)
##	
##	w=w+26
##	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'180'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
##	out.write(wtf)
##	
##	w=w+25
##	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'180'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
##	out.write(wtf)
##	
##	w=w+26
##	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'180'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
##	out.write(wtf)
##	
##	w=w+26
##	wtf='pop mirror'+'\n'+'rotate'+'\n'+'iangle'+' '+'180'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
##	out.write(wtf)
##	
##	wtf='pop mirror'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
##	out.write(wtf)
##	
##	w=w+25
##	wtf='pop mirror'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
##	out.write(wtf)
##	
##	w=w+26
##	wtf='pop mirror'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
##	out.write(wtf)
##	
##	w=w+25
##	wtf='pop mirror'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
##	out.write(wtf)
##	
##	w=w+26
##	wtf='pop mirror'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
##	out.write(wtf)
##	
##	w=w+26
##	wtf='pop mirror'+'\n'+'pick'+'  '+str(w)+'  '+str(h)+'\n'
##	out.write(wtf)
	
	wtf='pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)
	
	w=w+25
	wtf='pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)
	
	w=w+26
	wtf='pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)
	
	w=w+25
	wtf='pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)
	
	w=w+26
	wtf='pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)
	
	w=w+26
	wtf='pick'+'  '+str(w)+'  '+str(h)+'\n'
	out.write(wtf)
	
	w_s=w_s-19
	h_s=h_s-5.74


