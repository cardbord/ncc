a = input("text>>>").replace(" ","")
b = int(input("Enter len>>>"))
a = list(a)
nlist = {}
for i in range(0,len(a),b):
    if not str(a[i])+str(a[i+1]) in nlist:
        nlist[str(a[i])+str(a[i+1])] = 0
for xvar in nlist:
    for i in range(0,len(a),b):
        if str(a[i])+str(a[i+1]) == i:
            i+=1


print(nlist)



