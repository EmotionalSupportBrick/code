import random 
ditt_slag = random.randint(1, 6)
print("Du slog en", ditt_slag)
datorn_slag = random.randint(1, 6)
print("Datorn slog en", datorn_slag)
print("Du vann!" if ditt_slag > datorn_slag else "Datorn vann!" if datorn_slag > ditt_slag else "Det blev oavgjort!")