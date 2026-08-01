"""
C-003 test: does adaptive-dynamics evolutionary branching transfer to a
two-layer LEARNING system built from ML primitives only?

System (minimal routed mixture-of-experts):
  tokens        y ~ N(0, sk^2)
  m experts     expert i sits at phi_i and predicts the constant phi_i
  routing       g_i(y) = softmax_i( -(y - phi_i)^2 / (2 tau) )     [COUPLED]
                g_i(y) = 1/m                                        [DECOUPLED]
  loss          L(phi) = E_y[ sum_i g_i(y) (y - phi_i)^2 ]
  slow layer    gradient descent on L   (this is U, the law-update layer)

COUPLED  = frequency-dependent: expert i's drift depends on where the others
           are (through the routing).  Fitness of a variant depends on the
           resident configuration.
DECOUPLED= resident-independent: each expert independently minimises
           E[(y-phi_i)^2].  This is exactly the C-003(a) autonomous-gradient
           setting (fitness = a fixed scalar function of phi alone).

ANALYTIC PREDICTION, derived independently from the model's own primitives
(m = 2, split coordinate v = (phi_1 - phi_2)/2, symmetric configuration v = 0):

  g_1(y) = sigmoid(2 v y / tau),  so
  L(v) = sk^2 + v^2 - 2 v E_y[ y tanh(v y / tau) ]
       = sk^2 + v^2 (1 - 2 sk^2 / tau) + 2 v^4 sk^4 / tau^3 + O(v^6)

  => d2L/dv2 |_{v=0} = 2 (1 - 2 sk^2 / tau)
  => unspecialised configuration stable  iff  tau >  2 sk^2
     experts split (branching)           iff  tau <  2 sk^2
  => supercritical pitchfork, and just below threshold
     v* = sqrt( (2 sk^2 / tau - 1) * tau^3 / (4 sk^4) )

Nothing below is fitted.  The threshold and the amplitude law come from the
model's primitives (routing temperature tau, token spread sk) and are then
checked against numerics computed from the model DEFINITION (not from the
expansion).
"""

import math

SK = 1.0                      # token std  =>  predicted threshold tau* = 2
PI = math.pi


# ---------------------------------------------------------------- quadrature
def gauss_grid(sk=SK, lo=-9.0, hi=9.0, n=2001):
    """Simpson nodes/weights for E_y[f(y)], y ~ N(0, sk^2).  n must be odd."""
    h = (hi - lo) / (n - 1)
    ys, ws = [], []
    for j in range(n):
        y = lo + j * h
        s = 1 if j in (0, n - 1) else (4 if j % 2 == 1 else 2)
        pdf = math.exp(-(y * y) / (2 * sk * sk)) / (sk * math.sqrt(2 * PI))
        ys.append(y)
        ws.append(s * h / 3 * pdf)
    return ys, ws


Y, W = gauss_grid()
_norm = sum(W)
_var = sum(w * y * y for y, w in zip(Y, W))


# ---------------------------------------------------------------- model
def loss(phi, tau, coupled=True):
    m = len(phi)
    total = 0.0
    for y, w in zip(Y, W):
        d = [(y - p) ** 2 for p in phi]
        if coupled:
            a = [-di / (2 * tau) for di in d]
            mx = max(a)
            e = [math.exp(ai - mx) for ai in a]
            se = sum(e)
            g = [ei / se for ei in e]
        else:
            g = [1.0 / m] * m
        total += w * sum(gi * di for gi, di in zip(g, d))
    return total


def gradient(phi, tau, coupled=True):
    """Analytic gradient.  dL/dphi_k = E_y[ g_k (y-phi_k) ((d_k - D)/tau - 2) ]
    in the coupled case;  E_y[ -2 (y-phi_k) / m ] in the decoupled case."""
    m = len(phi)
    out = [0.0] * m
    for y, w in zip(Y, W):
        d = [(y - p) ** 2 for p in phi]
        if coupled:
            a = [-di / (2 * tau) for di in d]
            mx = max(a)
            e = [math.exp(ai - mx) for ai in a]
            se = sum(e)
            g = [ei / se for ei in e]
            D = sum(gi * di for gi, di in zip(g, d))
            for k in range(m):
                out[k] += w * g[k] * (y - phi[k]) * ((d[k] - D) / tau - 2.0)
        else:
            for k in range(m):
                out[k] += w * (-2.0) * (y - phi[k]) / m
    return out


def descend(phi0, tau, coupled=True, lr=0.05, steps=40000, tol=1e-11):
    phi = list(phi0)
    for _ in range(steps):
        g = gradient(phi, tau, coupled)
        if max(abs(gi) for gi in g) < tol:
            break
        for k in range(len(phi)):
            phi[k] -= lr * g[k]
    return phi


def min_over_v(tau, coupled=True, vmax=3.0, n=1200, rounds=10):
    """Minimise L(v) = loss([v,-v]) over v >= 0: coarse scan, then repeated
    local rescan on a shrinking bracket (robust, no bracketing assumptions)."""
    f = lambda v: loss([v, -v], tau, coupled)
    best_v, best_f = 0.0, f(0.0)
    for i in range(1, n + 1):
        v = vmax * i / n
        fv = f(v)
        if fv < best_f:
            best_v, best_f = v, fv
    h = vmax / n
    for _ in range(rounds):
        for i in range(-10, 11):
            v = best_v + i * h / 10
            if v < 0:
                continue
            fv = f(v)
            if fv < best_f:
                best_v, best_f = v, fv
        h /= 10
    return best_v


def d2L_dv2(tau, coupled=True, h=1e-3):
    f = lambda v: loss([v, -v], tau, coupled)
    return (f(h) - 2 * f(0.0) + f(-h)) / (h * h)


# ---------------------------------------------------------------- run
print(__doc__)
print("=" * 78)
print(f"quadrature check:  sum(w) = {_norm:.12f}   E[y^2] = {_var:.12f}  (want 1, {SK**2})")
print(f"sk = {SK}   =>   predicted branching threshold  tau* = 2 sk^2 = {2*SK**2}")
print("=" * 78)

print("\n[1] Curvature of the loss along the split direction at v = 0.")
print("    Tests the DERIVATION, not just the qualitative outcome.\n")
print(f"    {'tau':>7} {'analytic 2(1-2sk^2/tau)':>25} {'numeric':>14} {'rel.err':>11}")
for tau in [0.5, 1.0, 1.5, 1.9, 2.0, 2.1, 3.0, 5.0]:
    a = 2 * (1 - 2 * SK**2 / tau)
    nnum = d2L_dv2(tau)
    rel = abs(nnum - a) / max(abs(a), 1e-12)
    print(f"    {tau:7.2f} {a:25.6f} {nnum:14.6f} {rel:11.2e}")

print("\n[2] COUPLED arm (frequency-dependent routing): does the population split?")
print("    L(v) minimised directly from the model definition, m = 2.\n")
print(f"    {'tau':>7} {'argmin |v|':>12} {'v* predicted':>14} {'verdict':>10}")
for tau in [0.4, 0.8, 1.2, 1.6, 1.8, 1.9, 1.95, 2.0, 2.05, 2.2, 3.0, 5.0]:
    v = min_over_v(tau, coupled=True)
    if tau < 2 * SK**2:
        vstar = math.sqrt((2 * SK**2 / tau - 1) * tau**3 / (4 * SK**4))
    else:
        vstar = 0.0
    verdict = "SPLIT" if v > 1e-3 else "no split"
    print(f"    {tau:7.2f} {v:12.6f} {vstar:14.4f} {verdict:>10}")

print("\n[3] Pitchfork amplitude law just below threshold (quartic theory is")
print("    only valid near tau* = 2; ratio -> 1 as tau -> tau*).\n")
print(f"    {'tau':>7} {'|v| numeric':>13} {'v* quartic':>12} {'ratio':>8}")
for tau in [1.995, 1.99, 1.98, 1.96, 1.94, 1.90, 1.80]:
    v = min_over_v(tau, coupled=True, vmax=1.0)
    vstar = math.sqrt((2 * SK**2 / tau - 1) * tau**3 / (4 * SK**4))
    print(f"    {tau:7.3f} {v:13.6f} {vstar:12.6f} {v/vstar:8.4f}")

print("\n[4] DECOUPLED arm: routing independent of expert positions")
print("    = resident-independent fitness = the C-003(a) autonomous case.")
print("    P-10 predicts NO split at any tau.\n")
print(f"    {'tau':>7} {'argmin |v|':>12} {'verdict':>10}")
for tau in [0.4, 0.8, 1.2, 1.6, 2.0, 3.0, 5.0]:
    v = min_over_v(tau, coupled=False)
    verdict = "SPLIT" if v > 1e-3 else "no split"
    print(f"    {tau:7.2f} {v:12.6f} {verdict:>10}")

print("\n[5] m = 4 experts, coupled, gradient descent from a near-symmetric start:")
print("    how many distinct positions survive?  (coarser grid for speed;")
print("    'resid' = max|dL/dphi| at stop, so unconverged runs are visible)\n")
Y, W = gauss_grid(n=601)  # coarser quadrature for the descent runs
print(f"    {'tau':>7} {'clusters':>9} {'resid':>10}   final positions")
seed = [0.021, -0.008, 0.013, -0.026]
for tau in [0.15, 0.3, 0.6, 1.0, 1.5, 2.0, 3.0]:
    phi = descend(seed, tau, coupled=True, lr=0.10, steps=60000)
    resid = max(abs(g) for g in gradient(phi, tau, True))
    s = sorted(phi)
    clusters = 1 + sum(1 for i in range(len(s) - 1) if s[i + 1] - s[i] > 1e-2)
    print(f"    {tau:7.2f} {clusters:9d} {resid:10.2e}   [{', '.join(f'{p:7.3f}' for p in s)}]")

print("\ndone.")
