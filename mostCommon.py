from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        if not paragraph:
            return None
        banned_set = set(banned)
        paragraph = paragraph.split()
        paragraph = [x.lower().strip("!?',;.") for x in paragraph]
        num_words = len(paragraph)
        word_count = Counter(paragraph)
        best, best_count = None,-1
        for word,count in word_count.iteritems():
            if count >= best_count and not word in banned_set:
                best_count = count
                best = word
        return best