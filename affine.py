from string import ascii_lowercase
def convert_from_affine(text):

    de = ascii_lowercase
    possible_a = [1,3,5,7,9,11,13,15,17,19,21,23,25]
    
    for a in possible_a:
        for b in range(1,27):
            new_str = ''
            for char in text:
                index = de.index(char)
                value = (a*(index-b))%26
                new_str+=de[value]
            print(new_str)

convert_from_affine('hi')