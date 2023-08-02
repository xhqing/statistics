import numpy as np
from statsmodels.stats.proportion import proportion_effectsize

p1 = 1545/5000
p2 = 1670/5000

cohen_h = abs(proportion_effectsize(p1, p2))

print(f"Cohen's h: {cohen_h:.6f}")
