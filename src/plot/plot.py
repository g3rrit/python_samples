import matplotlib.pyplot as plt
import sys

import numpy

#module for plotting textfile with array of numbers


def plot_txt(filen):
    data = []

    with open(filen) as isn:
        for line in isn:
            data.append(float(line))

    plt.plot(data);
    plt.show();

def plot_pcm(filen):
    data = numpy.memmap(filen, dtype='h', mode='r')

    plt.plot(data);
    plt.show();


if __name__ == "__main__":
    if sys.argv[2] == "txt":
        plot_txt(sys.argv[1]);
    elif sys.argv[2] == "pcm":        
        plot_pcm(sys.argv[1]);
