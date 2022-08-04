# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
plt.style.use(['science','nature','notebook'])
#%matplotlib inline 

# %%
df = pd.read_csv(r"C:\Users\KuChris\Desktop\plot\20220114\21120931_AEDFA-PM-NS_PER2.xls.txt", delimiter="\,",engine='python')

# %%
# df.columns.values[0] = 't'
# df.columns.values[1] = '1'
# df.columns.values[2] = '2'

# %%
df

# %%
t = df['Time']
a = df['1']
b = df['2']

# %%
plt.figure(figsize=(20,8))
plt.subplot(121)
plt.scatter(t,a, s=0.01)
plt.title("a")
plt.xlabel(r'$Hours$')
plt.ylabel(r'$Power(dBm)$')

plt.subplot(122)
plt.scatter(t,b, s=0.01)
plt.title("b")
plt.xlabel(r'$Hours$')
plt.ylabel(r'$Power(dBm)$')

plt.show()

# %%
from numpy import gradient

# %%
da = gradient(a,t)
db = gradient(b,t)

# %%
plt.figure(figsize=(20,8))
plt.subplot(121)
plt.plot(t,da,linewidth=0.1)
plt.title("da")
plt.xlabel(r'$Hours$')
#plt.ylabel(r'$Power(dBm)$')

plt.subplot(122)
plt.plot(t,db,linewidth=0.1)
plt.title("db")
plt.xlabel(r'$Hours$')
#plt.ylabel(r'$Power(dBm)$')
plt.show()

# %%
PC = 10* np.log10(a)

# %%

plt.plot(t,-a/b)

# %%
#dBm -> mW to the conversion
amw = 10**(a/10)
bmw = 10**(b/10)


# %%
avga = np.average(amw)
avgb = np.average(bmw)

plt.figure(figsize=(20,8))
plt.subplot(121)
plt.plot(t,amw,linewidth=0.1)
plt.axhline(avga,c='r',ls='--')

plt.subplot(122)
plt.plot(t,bmw,linewidth=0.1)
plt.axhline(avgb,c='r',ls='--')
print(avga,avgb)


# %%
damw = gradient(amw,t)
dbmw = gradient(bmw,t)

avgda = np.average(damw)
avgdb = np.average(dbmw)

plt.figure(figsize=(20,8))
plt.subplot(121)
plt.plot(t,damw,linewidth=0.1)
plt.axhline(avgda,c='r',ls='--')

plt.subplot(122)
plt.plot(t,dbmw,linewidth=0.1)
plt.axhline(avgdb,c='r',ls='--')

print(avgda,avgdb)

# %%
#%matplotlib qt
#%matplotlib notebook 
from scipy.signal import savgol_filter
rp= (bmw/amw).astype(np.float64)
#flat=max(rp)-min(rp)
smoothness = savgol_filter(rp, 51, 3)

avgpr = np.average(rp)


plt.figure()
#plt.ylim(0.0034,0.0042)
plt.ylim(240,280)
plt.scatter(t, rp, s=1 , label='Raw data')
plt.plot(t, smoothness, 'r', linewidth=0.5, label='smoothness')
plt.title("% vs hours")
plt.xlabel(r'Hours')
plt.ylabel(r'Power Ratio %')
plt.axhline(avgpr,c='g',ls='--')
plt.legend()

# %%
from scipy.signal import savgol_filter
rp1= np.log10(amw/bmw).astype(np.float64)
#flat=max(rp)-min(rp)
smoothness1 = savgol_filter(rp1, 51, 3)

avgpr1 = np.average(rp1)


plt.figure()
#plt.ylim(0.0034,0.0042)
plt.ylim(-2.38,-2.46)
plt.scatter(t, rp1, s=1 , label='Raw data')
plt.plot(t, smoothness1, 'r', linewidth=0.5, label='Smoothness')
plt.title("Polarization Crosstalk vs hours")
plt.xlabel(r'Hours')
plt.ylabel(r'Polarization Crosstalk(dB)')
#plt.axhline(avgpr,c='g',ls='--')
plt.legend()
plt.savefig('Polarization Crosstalk.png')

# %%



