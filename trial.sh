#!/bin/bash

set -e
THISDIR=$(dirname ${BASH_SOURCE[0]})

if [ ! -d $THISDIR/pyephem ]
then
    git clone https://github.com/brandon-rhodes/pyephem.git $THISDIR/pyephem
    (cd $THISDIR/pyephem; patch -p1 < ../c.patch)
    (cd $THISDIR/pyephem; python setup.py build)
fi

if [ ! -d $THISDIR/sgp4 ]
then
    git clone https://github.com/brandon-rhodes/python-sgp4.git $THISDIR/sgp4
fi

echo
echo "PyEphem's libastro C-language back-end, running under Python:"
echo

PYTHONPATH=$THISDIR/pyephem/build/lib.linux-i686-2.7/ \
    python -m timeit -n 1 -r 1000 \
    -s 'import sat1' 'sat1.july_minutes()'

echo
echo "Pure-Python sgp4, running under PyPy:"
echo

PYTHONPATH=$THISDIR/sgp4 \
    pypy -m timeit -n 1 -r 1000 \
    -s 'import sat2' 'sat2.july_minutes()'
