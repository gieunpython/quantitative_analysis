import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

np.random.seed(0)

X, y = make_blobs(n_samples=5000, centers=[[4,4], [-2, -1], [2, -3], [1, 1]], cluster_std=0.9)
plt.scatter(X[:, 0], X[:, 1], marker='.')
plt.show()

k_means = KMeans(init = "k-means++", n_clusters= 4, n_init=12)
k_means.fit(X)
k_means_labels = k_means.labels_
k_means_cluster_centers = k_means.cluster_centers_

fig = plt.figure(figsize=(6,4))
colors = plt.cm.Spectral(np.linspace(0,1, len(set(k_means_labels))))
ax = fig.add_subplot(1,1,1)
for k, col in zip(range(len([[4,4],[-2,-1],[2,-3],[1,1]])), colors):
    my_members = (k_means_labels == k)
    cluster_center = k_means_cluster_centers[k]
    ax.plot(X[my_members, 0], X[my_members, 1], 'w', markerfacecolor=col, marker='.')
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,  markeredgecolor='k', markersize=6)
    # Title of the plot
ax.set_title('KMeans')

# Remove x-axis ticks
ax.set_xticks(())

# Remove y-axis ticks
ax.set_yticks(())

# Show the plot
plt.show()

k_means1 = KMeans(init = "k-means++", n_clusters = 3, n_init=12)
k_means1.fit(X)
fig = plt.figure(figsize=(6,4))
colors = plt.cm.Spectral(np.linspace(0,1, len(set(k_means1.labels_))))
ax = fig.add_subplot(1,1,1)
for k, col in zip(range(len(k_means1.cluster_centers_)), colors):
    my_members1 = (k_means1.labels_ == k)
    cluster_center1 = k_means1.cluster_centers_[k]
    ax.plot(X[my_members1, 0], X[my_members1, 1], 'w', markerfacecolor=col, marker='.')
    ax.plot(cluster_center1[0], cluster_center1[1], 'o', markerfacecolor=col,  markeredgecolor='k', markersize=6)
    # Title of the plot
ax.set_title('KMeans')
# Remove x-axis ticks
ax.set_xticks(())

# Remove y-axis ticks
ax.set_yticks(())

# Show the plot
plt.show()
