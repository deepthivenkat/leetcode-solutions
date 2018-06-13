import string
from collections import Counter,defaultdict
def word_count_engine(document):
  document = document.strip().split(' ')
  punc = set(string.punctuation)
  word_Counter = defaultdict(int)
  uniq_words = []
  for idx,word in enumerate(document):
    word = document[idx] = "".join([c for c in word if c not in punc]).lower()
    if not word_Counter[word] and word:
      uniq_words.append(word)
    word_Counter[word]+=1
  #print word_Counter, uniq_words
    
  document = filter(lambda x: x!="",document)
  freq_word_arr = [[] for word in document]
  for word in uniq_words:
    val = word_Counter[word]
    freq_word_arr[val].append(word)
  rev_freq = freq_word_arr[::-1]
  result = []
  for item in rev_freq:
    for x in item:
      res_item = [x,word_Counter[x]]
      if not result or res_item!=result[-1]:
        result.append([x,str(word_Counter[x])])
  return result
      
    
  #return ret_arr
    
  
    
    

print word_count_engine("Every book is a quotation; and every house is a quotation out of all forests, and mines, and stone quarries; and every man is a quotation from all his ancestors. ")