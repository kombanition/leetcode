class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        output = []
        for i, word in enumerate(s.split()):
            output.append(word)
            if i == k - 1:
                return(" ".join(output))
                break

# first try :-)