from sympy import symbols, exp, diff, integrate

print("=== Bacterial Population Growth Calculator ===")

P0_val = float(input("Enter initial population (P0): "))
k_val = float(input("Enter growth constant k (e.g., 0.4): "))
a = float(input("Enter start time (a): "))
b = float(input("Enter end time (b): "))

t, P0, k = symbols('t P0 k')

P = P0 * exp(k * t)

growth_rate = diff(P, t)

total_added = integrate(growth_rate, (t, a, b))


print("\n=== RESULTS ===")
print("Population function P(t):", P)
print("Growth rate dP/dt:", growth_rate)

pop_at_b = P.subs({P0: P0_val, k: k_val, t: b})
pop_at_a = P.subs({P0: P0_val, k: k_val, t: a})
added_pop = float(total_added.subs({P0: P0_val, k: k_val}))

print(f"\nPopulation at t={a}: {float(pop_at_a):.2f}")
print(f"Population at t={b}: {float(pop_at_b):.2f}")
print(f"Total population added from t={a} to t={b}: {added_pop:.2f}")