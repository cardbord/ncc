def count_standard_english(text):
     counter = 0
     word_index = []
     for word in text.split(' '):
          if not word in word_index:
               word_index.append(word)
     for word in word_index:
          if word in ['the','an','and','or','his','her','that','to','be','in','too','have','of','him','she','he','from'] and word != ' ':
               counter+=1
     return counter

def main():
     try:
          with open(input('.decoded filename>>>')+'.decoded','r') as opened_decoded:
               lines = opened_decoded.readlines()
               for line in lines:
                    score = count_standard_english(line)
                    if score > 1:
                         print(f'Line of interest with a score of {score}: {line}')
     except FileNotFoundError:
          print("this file does not exist.")
main()