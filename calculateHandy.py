import math

import matplotlib.pyplot as plt

import example_parameters
from model import *


def normalize_array(array):
    max_ = max(array)
    if max_ == 0:
        return array
    return [x / max_ for x in array]


# simulation_len = 10000
# epsilon = .1

params = example_parameters.elite_equilibrium
simulation_len = params.simulation_len
epsilon = params.epsilon

# computation
def compute_for_visualization(parameters, simulation_len, epsilon, normalize = True):
    xc, xe, y, w, am, aM, bc, be, s, gamma, lambda_, kappa, delta, rho = parameters.unpacked()

    xcs, xes, ys, ws = [], [], [], []

    for i in range(int(simulation_len / epsilon)):
        xc, xe, y, w = step(xc, xe, y, w, am, aM, bc, be, s, gamma, lambda_, kappa, delta, rho, epsilon)
        xcs.append(xc)
        xes.append(xe)
        ys.append(y)
        ws.append(w)

    return xcs, xes, ys, ws


xcs, xes, ys, ws = compute_for_visualization(params, simulation_len, epsilon)
print(xcs[-1], xes[-1], ys[-1], ws[-1])
print(max(xcs), max(xes), max(ys), max(ws))

normalize = True
if normalize:
    xcs = normalize_array(xcs)
    xes = normalize_array(xes)
    ys = normalize_array(ys)
    ws = normalize_array(ws)

def plot(xcs, xes, ys, ws):
    plt.plot(xcs, label="Common people")
    plt.plot(xes, label="Elite population")
    plt.plot(ys, label="Nature")
    plt.plot(ws, label="Accumulated wealth")
    plt.legend()
    plt.show()


plot(xcs, xes, ys, ws)
