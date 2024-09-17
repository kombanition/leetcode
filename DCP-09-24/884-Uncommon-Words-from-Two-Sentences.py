class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        output = []
        for word in s1:
            if word not in s2 and s1.count(word) < 2:
                output.append(word)
        for word in s2:
            if word not in s1 and s2.count(word) <2:
                output.append(word)
        return output