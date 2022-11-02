from parameters import Parameters


def _elite_equilibrium():
    # metaparameters
    simulation_len = 1000
    epsilon = .1

    # constants
    am, aM = 0.01, 0.07  # normal and famine death rates
    bc, be = 0.03, 0.03  # commoner and elite birth rate
    s, rho = 5e-4, 5e-3  # Subsistence salary per capita, Threshold wealth per capita
    gamma, lambda_ = 0.01, 100  # nature regeneration rate, nature carrying capacity
    kappa, delta = 1, 1e-5  # inequality factor, depletion(production) factor

    # variables
    xc, xe, y, w = 100, 1, lambda_, 0  # commoner pop, elite pop, nature, accumulated wealth

    return Parameters(simulation_len, epsilon, am, aM, bc, be, s, rho, gamma, lambda_, kappa, delta, xc, xe, y, w)


elite_equilibrium = _elite_equilibrium()
