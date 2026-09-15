import matplotlib.pyplot as plt
import numpy as np

N = 10000

x = np.random.uniform(-0.5, 0.5, N)
y = np.random.uniform(-0.5, 0.5, N)

afstande = np.sqrt(x**2 + y**2)
indenfor = afstande <= 0.5

antal_indenfor = np.sum(indenfor)
pi_estimat = 4 * antal_indenfor / N

print("Estimeret pi:", pi_estimat)

plt.figure(figsize=(6, 6))
plt.scatter(x[indenfor], y[indenfor], color="red", s=1)
plt.scatter(x[~indenfor], y[~indenfor], color="blue", s=1)

vinkel = np.linspace(0, 2 * np.pi, 100)
cirkel_x = 0.5 * np.cos(vinkel)
cirkel_y = 0.5 * np.sin(vinkel)
plt.plot(cirkel_x, cirkel_y, color="black")

plt.axis("equal")
plt.show()
