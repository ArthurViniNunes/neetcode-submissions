class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        record = {}
        delta = len(s1)
        for char in s1:
            record[char] = record.get(char, 0) + 1
        

        for l in range(len(s2)):
            if s2[l] in record:
                test = {}
                for char in s2[l:l+delta]:
                    test[char] = test.get(char, 0) + 1
                if test == record:
                    return True

        return False