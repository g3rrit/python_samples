import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

rax = plt.axes([0.035, 0.5, 0.15, 0.15])
radio = RadioButtons(rax, ("complex", "real"), active = 0)

active_dim = 0

s_val_ax = plt.axes([0.25, 0.1, 0.65, 0.03])
s_val = Slider(s_val_ax, "real", -10.0, 10.0, valinit=0)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, "Reset")

def reset(event):
    ax.clear()
    ax.set_xlabel("real")
    ax.set_ylabel("complex")
    ax.set_zlabel("real")
    radio.set_active(0)
button.on_clicked(reset)


def plot_change(label):
    print("label change to" + label)
    global active_dim
    if label == "complex":
        active_dim = 1
        s_val.label = "complex"
        ax.set_zlabel("complex")
    else:
        active_dim = 0
        s_val.label = "real"
        ax.set_zlabel("real")
radio.on_clicked(plot_change)

def update_array(val):
    global active_dim
    resarr = get_array(val)

    n_arr = [[],[],[]]
    count = 0
    for n_val in resarr[0]:
        n_arr[0].append(resarr[1][count].real)
        n_arr[1].append(resarr[1][count].imag)
        n_arr[2].append(n_val)
        count += 1

    plot_array(n_arr)
s_val.on_changed(update_array)

def get_array(val):
    resarr = []
    #start end numsamples
    resarr.append(np.linspace(-10, 10, 50))
    resarr.append([])

    for o_val in resarr[0]:
        if active_dim == 1:
            c_num = complex(val, o_val)
        else:
            c_num = complex(o_val, val)
        resarr[1].append(c_num * c_num)

    return resarr


def plot_array(arr):
    #ax.clear()
    ax.plot(arr[0], arr[1], arr[2])


def main():
    ax.set_xlabel("real")
    ax.set_ylabel("complex")
    ax.set_zlabel("real")

    plt.show()


if __name__ == "__main__":
    main()
