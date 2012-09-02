
# PYTHONPATH=~/ephem2/build/lib.linux-i686-2.7/ python -m timeit -n 1 -r 1000 -s 'import sat1' 'sat1.july_minutes()'

import ephem

line1 = ('1 00005U 58002B   00179.78495062  '
         '.00000023  00000-0  28098-4 0  4753')
line2 = ('2 00005  34.2682 348.7242 1859667 '
         '331.7664  19.3264 10.82419157413667')

satellite = ephem.readtle('VANGUARD 1', line1, line2)
start = (2000, 7, 1)

def july_minutes():
    j = ephem.Date(start)
    for i in xrange(31 * 24):
        satellite.compute(j)
        satellite.ra            # force computation of its position
        j += ephem.hour

# Display starting position and ending position as a sanity check.

satellite.compute(start)
print satellite.g_ra, satellite.g_dec
july_minutes()
print satellite.g_ra, satellite.g_dec
