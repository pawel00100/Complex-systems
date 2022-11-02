import time

import optuna

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


def objective(trial: optuna.Trial):
    parameters = example_parameters.elite_equilibrium

    am = trial.suggest_float("am", parameters.am / 1.1, parameters.am * 1.1)
    aM = trial.suggest_float("aM", parameters.aM / 1.1, parameters.aM * 1.1)
    bc = trial.suggest_float("bc", parameters.bc / 1.1, parameters.bc * 1.1)
    be = trial.suggest_float("be", parameters.be / 1.1, parameters.be * 1.1)
    s = trial.suggest_float("s", parameters.s / 1.1, parameters.s * 1.1)
    rho = trial.suggest_float("rho", parameters.rho / 1.1, parameters.rho * 1.1)
    gamma = trial.suggest_float("gamma", parameters.gamma / 1.1, parameters.gamma * 1.1)
    lambda_ = trial.suggest_float("lambda_", parameters.lambda_ / 1.1, parameters.lambda_ * 1.1)
    # kappa = trial.suggest_float("kappa", 1, 100)
    kappa = trial.suggest_float("kappa", 1, 2)
    delta = trial.suggest_float("delta", parameters.delta / 1.1, parameters.delta * 1.1)
    xc = trial.suggest_float("xc", parameters.xc / 1.1, parameters.xc * 1.1)
    xe = trial.suggest_float("xe", parameters.xe / 1.1, parameters.xe * 1.1)
    y = trial.suggest_float("y", parameters.y / 1.1, parameters.y * 1.1)
    w = trial.suggest_float("w", parameters.w / 1.1, parameters.w * 1.1)

    return compute(Parameters(xc, xe, y, w, am, aM, bc, be, s, gamma, lambda_, kappa, delta, rho, 1000, 0.1), 1000, 0.1)


study = optuna.create_study(directions=["maximize", "maximize", "maximize", "maximize"])
start = time.time()
study.optimize(objective, n_trials=300, timeout=300, show_progress_bar=True)

print(f"Finished in {time.time() - start}")
print("Number of finished trials: ", len(study.trials))
# print("Best value: ", study.best_value)
# print("Beat params: ", study.best_params)
