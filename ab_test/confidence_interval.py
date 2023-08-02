import numpy as np
from scipy.stats import norm

p1 = 1545/5000
p2 = 1670/5000
n1 = n2 = 5000
p = (n1*p1+n2*p2)/(n1+n2)


## 计算临界值
z_critical = norm.ppf(0.975)
print(z_critical)

## 计算边际误差
margin = z_critical*(p*(1-p)*(1/n1+1/n2))**0.5 
print(margin)

## 计算置信区间下限
lower = p - margin
## 计算置信区间上限
upper = p + margin

print((round(lower,2), round(upper,2)))

