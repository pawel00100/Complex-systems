
def step(xc, xe, y, w, am, aM, bc, be, s, gamma, lambda_, kappa, delta, rho, epsilon):
    w_th = rho * xc + kappa * rho * xe
    cc = min(1, w / w_th) * s * xc
    ce = min(1, w / w_th) * kappa * s * xe
    ac = am + max(0, 1 - cc / (s * xc)) * (aM - am)
    ae = am + max(0, 1 - ce / (s * xe)) * (aM - am)

    xc1 = xc + epsilon * (bc * xc - ac * xc)  # common pop birth and deaths
    xe1 = xe + epsilon * (be * xe - ae * xe)  # elite pop birth and deaths
    y1 = y + epsilon * (gamma * y * (lambda_ - y) - delta * xc * y)  # nature growth/depletion
    w1 = w + epsilon * (delta * xc * y - cc - ce)  # wealth increase / decrease
    return xc1, xe1, y1, w1

