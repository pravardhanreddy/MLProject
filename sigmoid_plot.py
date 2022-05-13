import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/Users/aparnak/Dropbox/Personal/Machine_Learning/gamma.csv')
Gamma = df['gamma'].tolist()
cost = df['cost'].tolist()
size = df['validation_accuracy'].tolist()
df = pd.DataFrame({
'x': Gamma,
'y': cost,
's': size
})

fig, ax = plt.subplots(facecolor='None')

ax.set_yscale('log')
ax.set_xscale('log')
for key, row in df.iterrows():
    ax.scatter(row['x'], row['y'], s=row['s']*5, alpha=.5)

for i, txt in enumerate(size):
    ax.annotate(txt, (Gamma[i],cost[i]),fontsize=10)

fig.suptitle('Gaussian grid search for Sample 6', fontsize=20)
plt.xlabel('Gamma', fontsize=16)
plt.ylabel('C', fontsize=16)
plt.show()
fig.savefig('gamma_val.jpg')