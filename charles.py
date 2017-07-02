from matplotlib import *
from pylab import *
import nbodykit.lab as nlab

cat = nlab.HDFCatalog('fof_1.0000.hdf5', 'FOFGroups')
cat.columns
print(cat.columns)
print(cat.dtype)
cat['Position'][:10].compute()

cat['Position'] = cat['Position'] * cat.attrs['BoxSize']
cat['VelocityOffset'] = cat['Velocity'] * cat.attrs['BoxSize']
"# add RSD\n",
cat['Position'] = cat['Position'] + cat['VelocityOffset'] * [0, 0, 1]
cat['Selection'] = cat['Length'] * 1e12 > 1e13

cat['Position'][:10].compute()
cat['VelocityOffset'][:10].compute()

r = nlab.FFTPower(cat, mode='2d', Nmesh=128)

plot(r.power['k'], abs(r.power['power']))
xscale('log')
yscale('log')
show()
