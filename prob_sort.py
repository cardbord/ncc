def search_highest(dictionary):
    highest = 'a'
    for key in dictionary:
        if dictionary[key] > dictionary[highest]:
            highest = key
    return highest

def sort_probabilities(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1]))

        

probability_dict = {'a':8.2,'b':1.5,'c':2.8,'d':4.3,'e':12.7,
                    'f':2.2,'g':2.0,'h':6.1,'i':7.0,'j':0.15,
                    'k':0.77,'l':4.0,'m':2.4,'n':6.7,'o':7.5,
                    'p':1.9,'q':0.095,'r':6.0,'s':6.3,'t':9.1,
                    'u':2.8,'v':0.98,'w':2.4,'x':0.15,'y':2.0,
                    'z':0.074
                    }



ciphertext = input("Enter ciphertext: ").lower()

ciphertext_probability = {'a':0,
'b':0,
'c':0,
'd':0,
'e':0,
'f':0,
'g':0,
'h':0,
'i':0,
'j':0,
'k':0,
'l':0,
'm':0,
'n':0,
'o':0,
'p':0,
'q':0,
'r':0,
's':0,
't':0,
'u':0,
'v':0,
'w':0,
'x':0,
'y':0,
'z':0,
}
og_ciphertext = ciphertext
ciphertext = ciphertext.replace(';','').replace(' ','').replace('.','').replace('?','').replace('-','').replace(',','').replace(':','')
for letter in list(ciphertext):
    ciphertext_probability[letter] += 1

for letter in ciphertext_probability:
    ciphertext_probability[letter] = (ciphertext_probability[letter]/len(ciphertext))*100

new_deciphered_string = ''

decoded_dictionary = {'a':0,
'b':0,
'c':0,
'd':0,
'e':0,
'f':0,
'g':0,
'h':0,
'i':0,
'j':0,
'k':0,
'l':0,
'm':0,
'n':0,
'o':0,
'p':0,
'q':0,
'r':0,
's':0,
't':0,
'u':0,
'v':0,
'w':0,
'x':0,
'y':0,
'z':0,
}

decoded_dictionary['e'] = search_highest(ciphertext_probability)

decoded_dictionary = sort_probabilities(ciphertext_probability)

print(decoded_dictionary)

arranged_probabilities = sort_probabilities(probability_dict)

print(arranged_probabilities)

for char in list(og_ciphertext.lower()):
    if char in probability_dict.keys():
        new_deciphered_string+=(list(arranged_probabilities)[list(decoded_dictionary).index(char)])
    else:
        new_deciphered_string+=char    

print(ciphertext)
print(ciphertext_probability)
print(search_highest(ciphertext_probability))

print(new_deciphered_string)