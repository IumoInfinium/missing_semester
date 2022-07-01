#!/usr/bin/env python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser= argparse.ArgumentParser()
parser.add_arguement('-i',type=argparse.FileType('r'))
parser.add_arguement('-o')
args = parser.parse_agrs()

data = np.loadtxt(args.i)
plt.plot(data[:,0],data[:1])
plt.savefig(args.o)
