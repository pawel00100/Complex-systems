from parameters import Parameters


def _elite_equilibrium():
    # metaparameters
    # oscylacja do stałej
    simulation_len = 600
    epsilon = .1

    # constants
    am, aM = 0.01, 0.07  # normal and famine death rates
    bc, be = 0.065, 0.02  # commoner and elite birth rate
    s, rho = 5e-4, 5e-3  # Subsistence salary per capita, Threshold wealth per capita
    gamma, lambda_ = 0.01, 100  # nature regeneration rate, nature carrying capacity
    kappa, delta = 10, 8.72e-5  # inequality factor, depletion(production) factor

    # variables
    xc, xe, y, w = 10000, 10000, lambda_, 0  # commoner pop, elite pop, nature, accumulated wealth

    return Parameters(simulation_len, epsilon, am, aM, bc, be, s, rho, gamma, lambda_, kappa, delta, xc, xe, y, w)

def _elite_equilibrium2():
    # metaparameters
    # oscylacja do stałej
    simulation_len = 600
    epsilon = .1

    # constants
    am, aM = 0.01, 0.06  # normal and famine death rates
    bc, be = 0.06, 0.016  # commoner and elite birth rate
    s, rho = 6e-4, 6e-3  # Subsistence salary per capita, Threshold wealth per capita
    gamma, lambda_ = 0.011, 110  # nature regeneration rate, nature carrying capacity
    kappa, delta = 11, 8e-5  # inequality factor, depletion(production) factor

    # variables
    xc, xe, y, w = 10000, 10000, lambda_, 0  # commoner pop, elite pop, nature, accumulated wealth

    return Parameters(simulation_len, epsilon, am, aM, bc, be, s, rho, gamma, lambda_, kappa, delta, xc, xe, y, w)


elite_equilibrium = _elite_equilibrium()


# natura się nie regeneruje
am, aM = 0.01, 0.03  # normal and famine death rates
bc, be = 0.03, 0.03  # commoner and elite birth rate
s, rho = 5e-4, 5e-3  # Subsistence salary per capita, Threshold wealth per capita
gamma, lambda_ = 0.005, 100  # nature regeneration rate, nature carrying capacity
kappa, delta = 1.5, 1e-5  # inequality factor, depletion(production) factor




# wyginięcie, bogaci przejedli wszystko
simulation_len = 500
epsilon = .01

# constants
am, aM = 0.01, 0.07  # normal and famine death rates
bc, be = 0.03, 0.03  # commoner and elite birth rate
s, rho = 5e-4, 5e-3  # Subsistence salary per capita, Threshold wealth per capita
gamma, lambda_ = 0.01, 100  # nature regeneration rate, nature carrying capacity
kappa, delta = 10, 1e-4  # inequality factor, depletion(production) factor

# variables
xc, xe, y, w = 100, 100, lambda_, 0  # commoner pop, elite pop, nature, accumulated wealth




# cykl kryzysów
simulation_len = 1000
epsilon = .1

# constants
am, aM = 0.01, 0.07  # normal and famine death rates
bc, be = 0.03, 0.025  # commoner and elite birth rate
s, rho = 5e-4, 5e-3  # Subsistence salary per capita, Threshold wealth per capita
gamma, lambda_ = 0.01, 100  # nature regeneration rate, nature carrying capacity
kappa, delta = 10, 1.27957670693e-4  # inequality factor, depletion(production) factor

# variables
xc, xe, y, w = 100, 100, lambda_, 0  # commoner pop, elite pop, nature, accumulated wealth






#oscylacja do stałej
simulation_len = 600
epsilon = .01

# constants
am, aM = 0.01, 0.07  # normal and famine death rates
bc, be = 0.065, 0.02  # commoner and elite birth rate
s, rho = 5e-4, 5e-3  # Subsistence salary per capita, Threshold wealth per capita
gamma, lambda_ = 0.01, 100  # nature regeneration rate, nature carrying capacity
kappa, delta = 10, 8.72e-5  # inequality factor, depletion(production) factor

# variables
xc, xe, y, w = 10000, 3000, lambda_, 0  # commoner pop, elite pop, nature, accumulated wealth