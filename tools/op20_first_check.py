# OP-20 first check: verify the second-order structure at the collapsed point
# of the P-11 system by quadrature against the model DEFINITION (loss computed
# from the integral, never from the Taylor expansion). Pure stdlib, matching
# tools/c003_branching_check.py.
#
# Analytic predictions (collapsed point (0,0), tokens y ~ N(0, sigma^2)):
#   per-expert loss  ell(p, p') = E[ sigmoid((p'-p)(y-(p+p')/2)/tau) (y-p')^2 ]
#     d11 ell = sigma^2/(4 tau)
#     d12 ell = sigma^2/(2 tau)
#     d22 ell = 1 - 5 sigma^2/(4 tau)
#   joint loss L(p1,p2) = ell(p2,p1) + ell(p1,p2)
#     a = d11 L = 1 - sigma^2/tau
#     b = d12 L = sigma^2/tau
#     lambda_even = a + b = 1  (tau-independent)
#     lambda_odd  = a - b = 1 - 2 sigma^2/tau   (P-11: d^2L/dv^2 = 2*lambda_odd)

import math


def expect(f, sigma, n=8000, span=12.0):
    # Simpson's rule for E[f(y)], y ~ N(0, sigma^2), over [-span*sigma, span*sigma].
    lo, hi = -span * sigma, span * sigma
    h = (hi - lo) / n
    c = 1.0 / (sigma * math.sqrt(2.0 * math.pi))
    total = 0.0
    for i in range(n + 1):
        y = lo + i * h
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        total += w * f(y) * math.exp(-0.5 * (y / sigma) ** 2)
    return c * total * h / 3.0


def sig(z):
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    e = math.exp(z)
    return e / (1.0 + e)


def ell(p, pp, tau, sigma):
    return expect(lambda y: sig((pp - p) * (y - (p + pp) / 2.0) / tau) * (y - pp) ** 2, sigma)


def L(p1, p2, tau, sigma):
    return ell(p2, p1, tau, sigma) + ell(p1, p2, tau, sigma)


def second_partials(F, tau, sigma, h=1e-3):
    f = lambda u, v: F(u, v, tau, sigma)
    d11 = (f(h, 0) - 2 * f(0, 0) + f(-h, 0)) / h**2
    d22 = (f(0, h) - 2 * f(0, 0) + f(0, -h)) / h**2
    d12 = (f(h, h) - f(h, -h) - f(-h, h) + f(-h, -h)) / (4 * h**2)
    return d11, d12, d22


for sigma in (1.0, 1.3):
    s2 = sigma**2
    print(f"\nsigma = {sigma}   (predicted threshold tau* = 2 sigma^2 = {2*s2})")
    hdr = f"{'tau':>6} | {'d11 ell':>9} {'pred':>9} | {'d12 ell':>9} {'pred':>9} | " \
          f"{'d22 ell':>9} {'pred':>9} | {'a=d11 L':>9} {'pred':>9} | " \
          f"{'b=d12 L':>9} {'pred':>9} | {'a-b':>9} {'pred':>9}"
    print(hdr)
    for tau in (0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0, 5.0):
        e11, e12, e22 = second_partials(ell, tau, sigma)
        a, b, a2 = second_partials(L, tau, sigma)
        assert abs(a - a2) < 1e-6  # exchange symmetry: d11 L = d22 L
        print(f"{tau:>6.2f} | {e11:>9.6f} {s2/(4*tau):>9.6f} | {e12:>9.6f} {s2/(2*tau):>9.6f} | "
              f"{e22:>9.6f} {1-5*s2/(4*tau):>9.6f} | {a:>9.6f} {1-s2/tau:>9.6f} | "
              f"{b:>9.6f} {s2/tau:>9.6f} | {a-b:>9.6f} {1-2*s2/tau:>9.6f}")

# Sum-rule and identity checks:
sigma, tau = 1.0, 1.5
e11, e12, e22 = second_partials(ell, tau, sigma)
a, b, _ = second_partials(L, tau, sigma)
print("\nchecks (sigma=1, tau=1.5):")
print(f"  diagonal sum rule (d11+2*d12+d22) ell = {e11 + 2*e12 + e22:.6f}   (pred 1, since ell(p,p)=(s2+p^2)/2)")
print(f"  b = 2*d12 ell:  {b:.6f} vs {2*e12:.6f}")
print(f"  lambda_odd(L) = (d11-2*d12+d22) ell:  {a - b:.6f} vs {e11 - 2*e12 + e22:.6f}")
print(f"  lambda_even = a+b = {a + b:.6f}   (pred 1, tau-independent)")
