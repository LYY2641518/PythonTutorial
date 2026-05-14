import numpy as np

# d1 = np.array([])
# for i in range(6):
#     a = np.arange(0+i*10,6+i*10)
#     d1 = np.append(d1, a,axis=0)
d1 = np.array(range(60)).reshape(6,10)[:,0:6]
d2 = d1.reshape(6,6)
print(f"陣列:\n{d2}")
d3 = d2[0::5,0::5]
print(f"四個角落:\n{d3}")
d4 = d2[2:4,3:5]
print(f"黃框:\n{d4}")

for i in range(6):
    print("當行總和：", np.sum(d2[i,:]))
