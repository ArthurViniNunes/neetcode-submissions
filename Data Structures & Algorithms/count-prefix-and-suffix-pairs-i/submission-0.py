class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isPrefixAndSuffix(w1, w2):
            n = len(w1)
            print(w2[:n], w2[-n:])
            return w2[:n] == w1 and w2[-n:] == w1

        n = 0
        for i in range(0, len(words)):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    n+=1
        return n