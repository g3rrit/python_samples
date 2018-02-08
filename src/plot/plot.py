import matplotlib.pyplot as plt
import sys

#module for plotting textfile with array of numbers


def plot(filen):
    data = []

    with open(filen) as isn:
        for line in isn:
            data.append(float(line))

    plt.plot(data);
    plt.show();


if __name__ == "__main__":
    plot(sys.argv[1]);
