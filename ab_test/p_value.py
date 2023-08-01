from statsmodels.stats.proportion import proportions_ztest

z_score, p_value = proportions_ztest(count=[1545,1670], nobs=[5000,5000], value=None, alternative='two-sided')
print(p_value)
