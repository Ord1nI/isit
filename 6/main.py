from pprint import pprint
b = 4
arr = []
for i in range(9):
    arr1 = []
    for j in range(9):
        if i <=3:
            ii =i+1
            jj= j+1
            arr1.append(round((b-0.375)*((b-ii/jj+5)/(1+(ii+jj))),4))
        if i > 3:
            ii = i+1
            jj = j+1
            arr1.append(round(ii*ii+(ii-jj**b)**1/2,4))
    arr.append(arr1)
pprint(arr)
sr = 0
for i in range(9):
    sr += arr[i][i]
sr = sr/9
count = 0
print(round(sr,4))
for i in range(9):
    for q in range(9):
        if arr[i][q] > sr:
            count+=1
print(count)
for i in range(9):
    arr[2][i],arr[5][i] = arr[5][i],arr[2][i]
pprint(arr)
vect = []
for i in range(9):
    vect.append(arr[i][i])
print()
pprint(vect)
for i in range(9):
    for q in range(i):
        if vect[i] < vect[q]:
            vect[i],vect[q] = vect[q],vect[i]
pprint(vect)
