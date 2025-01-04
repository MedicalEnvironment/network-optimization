import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 100  # Cable length in meters
T0 = 20  # Reference temperature in °C
alpha_copper = 0.00393  # Temperature coefficient for copper
alpha_aluminum = 0.00429  # Temperature coefficient for aluminum
rho_copper = 1.68e-8  # Resistivity of copper (Ohm·m)
rho_aluminum = 2.82e-8  # Resistivity of aluminum (Ohm·m)
A_cross = 1e-6  # Cross-sectional area (m^2)

# Temperatures to simulate
temperatures = np.linspace(20, 100, 100)

# Resistance Calculation
def calculate_resistance(rho, L, A_cross):
    return rho * L / A_cross

# Temperature Effect on Resistance
def resistance_with_temperature(R0, alpha, T, T0):
    return R0 * (1 + alpha * (T - T0))

# Attenuation Model (simplified for visualization)
def signal_attenuation(L, attenuation_per_km):
    # Calculate the attenuation in dB based on the cable length and attenuation per kilometer
    return L * attenuation_per_km / 1000

# Resistances for copper and aluminum at T0
R0_copper = calculate_resistance(rho_copper, L, A_cross)
R0_aluminum = calculate_resistance(rho_aluminum, L, A_cross)

# Resistance vs Temperature
resistance_copper = resistance_with_temperature(R0_copper, alpha_copper, temperatures, T0)
resistance_aluminum = resistance_with_temperature(R0_aluminum, alpha_aluminum, temperatures, T0)

# Attenuation
attenuation_per_km_copper = 0.2  # dB/km for copper
attenuation_per_km_fiber = 0.05  # dB/km for optical fiber
attenuation_copper = signal_attenuation(L, attenuation_per_km_copper)
attenuation_fiber = signal_attenuation(L, attenuation_per_km_fiber)

# Plot Resistance vs Temperature
plt.figure(figsize=(10, 6))
plt.plot(temperatures, resistance_copper, label="Copper Resistance (Ohms)")
plt.plot(temperatures, resistance_aluminum, label="Aluminum Resistance (Ohms)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Resistance (Ohms)")
plt.title("Resistance vs Temperature for Copper and Aluminum")
plt.legend()
plt.grid(True)
plt.show()

# Attenuation Results
print(f"Signal attenuation for copper (100m): {attenuation_copper:.2f} dB")
print(f"Signal attenuation for optical fiber (100m): {attenuation_fiber:.2f} dB")

# Optimal Recommendations
optimal_temperature = 40  # °C
print(f"Optimal operating temperature for hardware: {optimal_temperature} °C")
print("Recommendation: Use optical fiber for minimal signal loss.")
print("For cables, prefer copper over aluminum due to lower resistivity.")
