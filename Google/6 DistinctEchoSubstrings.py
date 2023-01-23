class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        
        l = len(text)
        echoes = set()
        for i in range(l - 1):
            for j in range(i + 1, i + 1 + ((l - i) // 2)):
                if text[i : j] == text[j : 2 * j - i]:
                    echoes.add(text[i : j])
        return len(echoes)