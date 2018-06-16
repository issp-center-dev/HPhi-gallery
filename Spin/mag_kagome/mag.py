import math
import cmath

energy = [0]*28
#[s] read energy
for Sz in range(1,28,2):
  #[s] read file
  f_name = 'Sz%d/output/zvo_energy.dat' % Sz
  f   = open(f_name)
  tmp = f.read()
  f.close
  #[e] read file
  line = tmp.split("\n")
  for name in line:
    x = name.split()
    if x[0] == "Energy":
      tmp_energy = float(x[1])
      break
  energy[Sz] = tmp_energy
#[e] read energy

#[s] output magnetization
f = open ('mag.dat','w')
for Sz in range(3,28,2):
  h = energy[Sz]-energy[Sz-2]
  m = Sz/27.0
  f.write('{0} {1} \n'.format(h,m))
f.close
#[e] output magnetization

#[s] output plot file
f = open ('mag.plt','w')
f.write('se key l    \n')
f.write('se xlabel "h"    \n')
f.write('se ylabel "m"    \n')
f.write('se yr[0:1]    \n')
f.write('se xr[0:3.05] \n')
f.write('p "mag.dat" w steps lc rgb "red",')
f.write('"mag.dat" w p     lc rgb "red" ps 2 pt 6\n')
f.close
#[e] output plot file
