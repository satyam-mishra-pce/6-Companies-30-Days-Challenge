class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        secretcount, guesscount = dict(), dict()
        bulls = 0
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                continue

            if secret[i] not in secretcount:
                secretcount[secret[i]] = 1
            else:
                secretcount[secret[i]] += 1
        
            if guess[i] not in guesscount:
                guesscount[guess[i]] = 1
            else:
                guesscount[guess[i]] += 1
        
        cows = 0
        for key in secretcount:
            if key in guesscount:
                cows += min(secretcount[key], guesscount[key])
        
        return str(bulls) + "A" + str(cows) + "B"