from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import zt_ind_solve_power

effect_size = proportion_effectsize(prop1=0.3, prop2=0.33, method='normal')
sample_size = zt_ind_solve_power(effect_size=effect_size, nobs1=None, alpha=0.05, power=0.8, ratio=1.0, alternative='two-sided')

print(effect_size)
print(round(sample_size))
