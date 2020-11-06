import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

ax.plot([1,2,3,4], [1,1,0,1])
fig.savefig('graph.png')