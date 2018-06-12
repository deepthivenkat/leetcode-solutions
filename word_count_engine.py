import string
from collections import Counter,defaultdict


class Word_props(object):
  def __init__(self,word,freq,idx):
    self.word = word
    self.freq = freq
    self.idx = idx

  
def word_count_engine(document):
  document = document.strip().split(' ')
  punc = set(string.punctuation)
  word_Counter = defaultdict(int)
  for idx,word in enumerate(document):
    document[idx] = "".join([c for c in word if c not in punc]).lower()
    word_Counter[document[idx]]+=1
  document = filter(lambda x: x!="",document)
  print word_Counter
  print document
  word_obj ={}
  for idx,word in enumerate(document):
    word_obj[word]=Word_props(word,word_Counter[word],idx) if not word_obj.get(word) else word_obj[word]
  ret_arr = sorted(word_obj.values(),key=lambda x: (x.freq,-1*x.idx),reverse=True)
  return [[w.word,str(w.freq)] for w in ret_arr]
  #return ret_arr
    
  
    
    

print word_count_engine("Every book is a quotation; and every house is a quotation out of all forests, and mines, and stone quarries; and every man is a quotation from all his ancestors. ")