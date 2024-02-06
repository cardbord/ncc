a = input("text>>>").replace(" ","")
b = int(input("Enter len>>>"))
a = list(a)
nlist = {}

def concat_arr_terms(arr,start,stop):
    total = ""
    for i in range(start,stop):
        total+=str(arr[i])
    return total

for i in range(0,len(a),b):
    if not concat_arr_terms(a,i,i+b) in nlist:
        nlist[concat_arr_terms(a,i,i+b)] = 0

for xvar in nlist:
    for i in range(0,len(a),b):
        if concat_arr_terms(a,i,i+b) == xvar:
            nlist[xvar]+=1


print(nlist)



