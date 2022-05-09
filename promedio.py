#%%
arr = []
flag = True
for l in open("insurance.csv", "rt"):

    if flag:
        flag = False
        continue
    arr.append(float(l.split(",")[0]))

sum(arr)/len(arr)
#%%
import statistics
print(statistics.median(arr))