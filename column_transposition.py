from itertools import permutations

def solve(arr,key):
    result = ""
    
    keylist = list(key)
    for x in range(len(arr)):
        for i in range(len(arr[x])):
            result+= arr[x][int(keylist[i])]

    return result

def bruteforce(columned_array, keylength):
    print("started bruteforce")
    result_array = []
    key=""
    for n in range(keylength):
        key+=str(n)
    permutations_of_key = [''.join(p) for p in permutations(key)]
    
    
    

    for n in permutations_of_key:
        result = solve(columned_array, n)
        result_array.append(result+'\n')


        


    with open(f'{columned_array[0][0]}.decoded','w') as writable:
            writable.writelines(result_array)
            print(f'{writable.name} written.')


def main():
    scrambled = input("Enter scrambled text>>> ").replace(' ','')
    guessed_key_length = int(input("Enter estimated key length>>> "))
    
    #the length of the scrambled text should be factored by the key length, so we'll test that

    scrambled = list(scrambled)
    if len(scrambled) % guessed_key_length == 0:
        columned_array = [[]]
        n=0
        k=1
        for i in range(0,len(scrambled)):
            print(scrambled)
            columned_array[n].append(scrambled[0])
            
            scrambled.pop(0)
            if k==guessed_key_length:
                k=0
                
                columned_array.append([])
                
                n+=1
            k+=1
        columned_array.pop()
        print(columned_array)

        bruteforce(columned_array,guessed_key_length)



    
if __name__ == '__main__':
    main()



