class Parameters:
    def __init__(self, simulation_len, epsilon, am, aM, bc, be, s, rho, gamma, lambda_, kappa, delta, xc, xe, y, w) -> None:
        # metaparameters
        self.simulation_len = simulation_len
        self.epsilon = epsilon

        # constants
        self.am, self.aM = am, aM  # normal and famine death rates
        self.bc, self.be = bc, be  # commoner and elite birth rate
        self.s, self.rho = s, rho  # Subsistence salary per capita, Threshold wealth per capita
        self.gamma, self.lambda_ = gamma, lambda_  # nature regeneration rate, nature carrying capacity
        self.kappa, self.delta = kappa, delta  # inequality factor, depletion(production) factor

        # variables
        self.xc, self.xe, self.y, self.w = xc, xe, y, w  # commoner pop, elite pop, nature, accumulated wealth

    def unpacked(self):
        return self.xc, self.xe, self.y, self.w, self.am, self.aM, self.bc, self.be, self.s, self.gamma, self.lambda_, self.kappa, self.delta, self.rho

