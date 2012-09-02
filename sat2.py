
# PYTHONPATH=~/sgp4 pypy -m timeit -n 1 -r 1000 -s 'import sat2' 'sat2.july_minutes()'

from math import atan2, pi, sqrt
from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv

line1 = ('1 00005U 58002B   00179.78495062  '
         '.00000023  00000-0  28098-4 0  4753')
line2 = ('2 00005  34.2682 348.7242 1859667 '
         '331.7664  19.3264 10.82419157413667')

satellite = twoline2rv(line1, line2, wgs72)

def propagate(satellite, y, m, d, h):
    (x, y, z), velocity = satellite.propagate(y, m, d, h)
    xxyy = x*x + y*y
    r = sqrt(xxyy + z*z)
    ra = atan2(-y, -x) + pi     # turn atan2() [-pi, pi] range into [0, 2pi]
    dec = atan2(z, sqrt(xxyy))
    return r, ra, dec

def july_minutes():
    hours = range(0, 24)
    for day in xrange(1, 32):
        for hour in hours:
            r, ra, dec = propagate(satellite, 2000, 7, day, hour)
    return r, ra, dec

# Display starting position and ending position as a sanity check.

def display(ra, dec):
    rhours, remainder = divmod(12.*ra/pi, 1.)
    rminutes, rseconds = divmod(remainder * 3600., 60.)
    print '%d:%02d:%02f' % (rhours, rminutes, rseconds),

    ddegrees, remainder = divmod(180.*dec/pi, 1.)
    dminutes, dseconds = divmod(remainder * 3600., 60.)
    print '%d:%02d:%02f' % (ddegrees, dminutes, dseconds)

r, ra, dec = propagate(satellite, 2000, 7, 1, 0)
display(ra, dec)
r, ra, dec = july_minutes()
display(ra, dec)
