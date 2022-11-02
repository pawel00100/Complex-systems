import time

# import optuna
from SALib.sample import saltelli
from SALib.analyze import sobol
import numpy as np
import matplotlib.pyplot as plt

from parameters import Parameters
from model import *
import example_parameters


def normalize(array):
    max_ = max(array)
    return [x / max_ for x in array]


simulation_len = 1000
epsilon = .1

params = example_parameters.elite_equilibrium

# computation
def compute(parameters, simulation_len, epsilon):
    xc, xe, y, w, am, aM, bc, be, s, gamma, lambda_, kappa, delta, rho = parameters.unpacked()

    for i in range(int(simulation_len / epsilon)):
        xc, xe, y, w = step(xc, xe, y, w, am, aM, bc, be, s, gamma, lambda_, kappa, delta, rho, epsilon)

    return xc, xe, y, w


problem = {
    'num_vars': len(['xc', 'xe', 'y', 'am', 'aM', 'bc', 'be', 's', 'gamma', 'lambda_', 'kappa', 'delta', 'rho']),
    'names': ['xc', 'xe', 'y', 'am', 'aM', 'bc', 'be', 's', 'gamma', 'lambda_', 'kappa', 'delta', 'rho'],
    'bounds': [[params.xc / 1.1, params.xc * 1.1],
               [params.xe / 1.1, params.xe * 1.1],
               [params.y / 1.1, params.y * 1.1],
               [params.am / 1.1, params.am * 1.1],
               [params.aM / 1.1, params.aM * 1.1],
               [params.bc / 1.1, params.bc * 1.1],
               [params.be / 1.1, params.be * 1.1],
               [params.s / 1.1, params.s * 1.1],
               [params.rho / 1.1, params.rho * 1.1],
               [params.gamma / 1.1, params.gamma * 1.1],
               [params.lambda_ / 1.1, params.lambda_ * 1.1],
               [1, 100],
               [params.delta / 1.1, params.delta * 1.1]]
}

problem2 = {
    'num_vars': len(['xc', 'aM', 'bc', 'be']),
    'names': ['xc', 'aM', 'bc', 'be'],
    'bounds': [[params.xc / 2, params.xc * 2],
               [params.aM / 2, params.aM * 2],
               [params.bc / 2, params.bc * 2],
               [params.be / 2, params.be * 2]]
}

param_values = saltelli.sample(problem, 1024)

start = time.time()

Y = np.zeros([param_values.shape[0]])
for i, values in enumerate(param_values):
    Y[i] = compute(Parameters(32, 0.1, values[3], values[4], values[5], values[6], values[7], values[8], values[9], values[10], values[11], values[12], values[0], values[1], values[2], 0), 1000, 0.1)[0]

print(f"Finished in {time.time() - start}")

Si = sobol.analyze(problem, Y)
print(Si['S1'])


plt.plot()
Si.plot()
plt.show()
