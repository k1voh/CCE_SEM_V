# %%
import pandas as pd
import math

# %%
data = pd.read_csv("Dataset.csv", skiprows=1, header=None)

# %%
data.head()

# %%
dataset = data.values.tolist()
print(dataset)

# %% [markdown]
# # MODEL BUILDING

# %% [markdown]
# ## INITIALISATION

# %%
K = int(input("Enter the number of clusters : "))

# %%
clusters = {}
centroid = {}
for i in range(1,K+1):
  clusters[i] = [dataset[i-1]]
  centroid[i] = dataset[i-1]

# %% [markdown]
# ## DISTANCE VECTOR

# %%
def euclidean(Xc,Yc,Xo,Yo):
  return math.sqrt((Xo-Xc)**2 + (Yo-Yc)**2)

# %% [markdown]
# ## MODEL BUILDING

# %%
sumX = 0
sumY = 0
for i in range(K,len(dataset)):
  sumX = 0
  sumY = 0
  min_list = []
  for k in range(len(clusters)):
    min_list.append(int(euclidean(list(centroid.values())[k][0], list(centroid.values())[k][1], dataset[i][0], dataset[i][1])))
  cluster_number = min_list.index(min(min_list))+1
  new_list = list(clusters[cluster_number])
  new_list.append(dataset[i])
  clusters[cluster_number] = new_list
  for j in new_list:
    sumX += j[0]
    sumY += j[1]
  avgX = sumX//(len(new_list))
  avgY = sumY//(len(new_list))
  centroid[cluster_number] = [avgX,avgY]
print(clusters)


# %% [markdown]
# # VISUALISATION
# 


