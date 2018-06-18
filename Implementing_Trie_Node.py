class TrieNode(object):
    def __init__(self,end_of_word=False):
        self.char = {}
        self.end_of_word = end_of_word
    # def __repr__(self):
    #     return "TrieNode"
    # def __str__(self):
    #     emp_char = ""
    #     if self.char:
    #         keys = self.char.keys()
    #         emp_char += ''.join([str(x) for x in keys])
    #     return emp_char
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def print_if_word(self, word):
        start = self.root
        i=0
        while i<len(word):
            start = start.char.get(word[i])
            if start:
                print word[i]
            else:
                return
            i+=1
        eof = start.char.get("__eof__",None)
        if eof:
            print eof.end_of_word

    def insert(self, word):
        #print "insert", word
        prev,init,len_word = self.root,self.root,len(word)
        i = 0
        while i < len_word:
            init = init.char.get(word[i],None)
            if init:
                prev = init
                i+=1
                continue
            else:
                curr_node = TrieNode()
                prev.char[word[i]] = curr_node
                prev=init = curr_node
                i+=1
        last_dummy = TrieNode(True)
        init.char["_eof_"] = last_dummy
        #self.print_if_word(word)
            

    def search(self, word):
        #print "search",word
        start,i,len_word = self.root,0,len(word)
        while i<len_word:
            #print word[i]
            start = start.char.get(word[i],None)
            if not start:
                return False
            i+=1
        return start.char["_eof_"].end_of_word if start.char.get("_eof_",None) else False

    def startsWith(self, prefix):
        #print "startsWith", prefix
        word = prefix
        start,i,len_word = self.root,0,len(word)
        while i<len_word:
            #print word[i]
            start = start.char.get(word[i],None)
            if not start:
                return False
            i+=1
        return True

        
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)