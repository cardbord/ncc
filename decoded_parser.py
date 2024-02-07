from time import sleep

def remove_punc(text):
     punc = ['.',';',':',',','-','/','?','#']
     for p in punc:
          text = text.replace(p,'')
     return text

def count_standard_english(text):
     counter = 0
     word_index = []
     for word in text.split(' '):
          if not word in word_index:
               word_index.append(word)
     for word in word_index:
          if word in ['the','an','and','or','his','her','that','to','be','too','have','of','him','she','he','from'] and word != ' ':
               counter+=1
     return counter

def count_standard_nospace(line):
     counter = 0
     
     for word in ['the','an','and','or','his','her','that','to','be','too','have','of','him','she','he','from']:
          if word in line.lower():
               counter+=1
               line.replace(word,'')
     
     return counter

def find_as_dict(text):
     from PyDictionary import PyDictionary
     pdict = PyDictionary()
     new_ss = remove_punc(text)
     wcount = 0
     for word in new_ss.split(' '):
     
          if pdict.meaning(word,True) != None:
               wcount+=1
     if wcount >= len(new_ss.split(' '))//2:
          print('POSSIBILIY')
          sleep(0.5)
     


def main():
     try:
          with open(input('.decoded filename>>>')+'.decoded','r') as opened_decoded:
               lines = opened_decoded.readlines()
               for line in lines:
                    #if ' ' in line:
                    #     score = count_standard_english(line)
                    #     if score > 1:
                    #          print(f'Line of interest with a score of {score}: {line}')
                    #else:
                    score = count_standard_nospace(line)
                    if score > 6:
                         print(f'Line of interest with a score of {score}: {line}')
     except FileNotFoundError:
          print("this file does not exist.")
main()