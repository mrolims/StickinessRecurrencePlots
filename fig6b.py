"""
Generates the data of Figure 6(b). Simply run

    $ python fig6b.py 1e11 200

Make sure to run

    $ python fig5a.py 1e11 200

before running this code.

Execution time: minutes
Author: Matheus Rolim Sales
Last modified: 23/02/2023
"""

import numpy as np # NumPy module
import pandas as pd # Pandas module to extract the data
import os # Module to check if the directory exists
from functions import get_trappingtimes, get_Qtau
import sys

# Total number of iterations
Ntot = int(float(sys.argv[1]))
exponent = int(np.log10(Ntot))
base = int(Ntot/10**exponent)
# Finite-time
n = int(sys.argv[2]) #200
# Path to where the data will be stored
path = 'Data/'
# Checks if path exists
if not os.path.exists(path):
    # If not, creates path
    os.system('mkdir %s' % path)
# Name of the file
datafile = path + 'fig5a_Ntot=%ie%i_n=%i.dat' % (base, exponent, n)
# Checks if datafile exists
if not os.path.isfile(datafile):
    print('%s does not exist!\nDid you run fig5a.py?\nStopping execution...' % (datafile))
    sys.exit()
print('Extracting data from %s...' % datafile)
df = pd.read_csv(datafile, header=None, delim_whitespace=True)
x = np.array(df[0])
# Fig 5bc - blue
s01a = 0.6
sf1a = 0.8
# Fig 5bc - red
s01b = 1.25
sf1b = 1.33
# Fig 5bc - green
s01c = sf1b
sf1c = 1.48
# Fig 5bc - black
s02 = sf1c
sf2 = 1.55
# Fig 6a - black
s03 = 2.5
sf3 = 4.0

tau1a = []
tau1b = []
tau1c = []
tau2 = []
tau3 = []

print('Finding trapping times 5 - blue...')
tau1a = get_trappingtimes(x, s01a, sf1a)

print('Finding trapping times 5 - red...')
tau1b = get_trappingtimes(x, s01b, sf1b)

print('Finding trapping times 5 - green...')
tau1c = get_trappingtimes(x, s01c, sf1c)

print('Finding trapping times 5 - black...')
tau2 = get_trappingtimes(x, s02, sf2)

print('Finding trapping times 6 - black...')
tau3 = get_trappingtimes(x, s03, sf3)

print('Sorting the trapping times...')
sorted_tau1a = sorted(tau1a)
sorted_tau1a = np.array(sorted_tau1a[::-1])

sorted_tau1b = sorted(tau1b)
sorted_tau1b = np.array(sorted_tau1b[::-1])

sorted_tau1c = sorted(tau1c)
sorted_tau1c = np.array(sorted_tau1c[::-1])

sorted_tau2 = sorted(tau2)
sorted_tau2 = np.array(sorted_tau2[::-1])

sorted_tau3 = sorted(tau3)
sorted_tau3 = np.array(sorted_tau3[::-1])

N1a = len(sorted_tau1a)
N1b = len(sorted_tau1b)
N1c = len(sorted_tau1c)
N2 = len(sorted_tau2)
N3 = len(sorted_tau3)
nts = 200

print('Calculating Q 5 - blue...')
t1a, Q1a = get_Qtau(sorted_tau1a, nts)

print('Calculating Q 5 - red...')
t1b, Q1b = get_Qtau(sorted_tau1b, nts)

print('Calculating Q 5 - green...')
t1c, Q1c = get_Qtau(sorted_tau1c, nts)

print('Calculating Q 5 - black...')
t2, Q2 = get_Qtau(sorted_tau2, nts)

print('Calculating Q 6 - black...')
t3, Q3 = get_Qtau(sorted_tau3, nts)

datafile = path + 'fig6b_Ntot=%ie%i_n=%i.dat' % (base, exponent, n)
print('Writing to the file %s...' % datafile)
with open(datafile, 'w') as df:
    for j in range(nts):
        df.write('%.15f %.15f %.15f %.15f %.15f %.15f %.15f %.15f %.15f %.15f\n' % (t1a[j], Q1a[j], t1b[j], Q1b[j], t1c[j], Q1c[j], t2[j], Q2[j], t3[j], Q3[j]))
