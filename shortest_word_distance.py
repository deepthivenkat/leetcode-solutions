from collections import defaultdict
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        word_idxs = defaultdict(list)
        for idx,word in enumerate(words):
            word_idxs[word].append(idx)
        dist_word1 = word_idxs[word1]
        dist_word2 = word_idxs[word2]
        i,j=0,0
        len_1_word,len_2_word = len(dist_word1),len(dist_word2)
        min_diff = float("inf")
        print dist_word1,dist_word2
        while i < len_1_word and j < len_2_word:
            if abs(dist_word2[j]-dist_word1[i]) < min_diff:
                min_diff = abs(dist_word2[j]-dist_word1[i])
            if dist_word1[i] < dist_word2[j]:
                i+=1
            else:
                j+=1
        return min_diff