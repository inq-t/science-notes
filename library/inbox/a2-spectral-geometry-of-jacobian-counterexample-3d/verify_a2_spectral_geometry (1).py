#!/usr/bin/env python3
"""
Exact verification for the A2 normal form of the 2026 Jacobian counterexample.

Checks:
  1. depressed-cubic identity;
  2. discriminant identity;
  3. coordinate-Jacobian identity and nonvanishing on Gamma;
  4. cusp certificate in the manuscript's generators;
  5. discriminant of Delta as a quadratic in r.

All calculations use exact SymPy arithmetic.
"""

import sympy as sp

p, q, r, s, u = sp.symbols("p q r s u")

Phi = 2*p*s**3 - q*s**2 + 2*s - r
Delta = q**2 - 16*p - q**3*r + 18*p*q*r - 27*p**2*r**2

a = (12*p - q**2)/(12*p**2)
b = (-q**3 + 18*p*q - 54*p**2*r)/(108*p**3)

depressed = sp.expand(Phi.subs(s, u + q/(6*p))/(2*p))
assert sp.simplify(depressed - (u**3 + a*u + b)) == 0

assert sp.factor(Delta - 4*p**4*(-4*a**3 - 27*b**2)) == 0

coord_jac = sp.factor(sp.Matrix([q, a, b]).jacobian([p, q, r]).det())
expected_jac = (q**2 - 6*p)/(12*p**4)
assert sp.simplify(coord_jac - expected_jac) == 0

on_gamma = sp.simplify(coord_jac.subs(p, q**2/12))
assert sp.simplify(on_gamma - 864/q**6) == 0

g = 12*p - q**2
h = 3*q*r - 4
U = 2*(h + 4)**2*g + 2*h*q**2*(h - 4)

certificate = sp.factor(U**2 + 64*q**4*h**3 + 192*q**2*(h + 4)**2*Delta)
assert certificate == 0

disc_in_r = sp.factor(sp.discriminant(sp.Poly(Delta, r), r))
assert disc_in_r == -(12*p - q**2)**3

print("All exact checks passed.")
print()
print("Depressed cubic:")
print("  Phi(u + q/(6p))/(2p) =", sp.factor(depressed))
print()
print("Discriminant identity:")
print("  Delta = 4*p^4*(-4*a^3 - 27*b^2)")
print()
print("Coordinate Jacobian:")
print("  det d(q,a,b)/d(p,q,r) =", coord_jac)
print("  on Gamma =", on_gamma)
print()
print("Cusp certificate:")
print("  U^2 + 64*q^4*h^3 = -192*q^2*(h+4)^2*Delta")
print()
print("Discriminant of Delta as a quadratic in r:")
print(" ", disc_in_r)
