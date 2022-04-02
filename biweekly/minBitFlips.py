class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        startBit = bin(start)[2:]
        goalBit = bin(goal)[2:]
   
        
        maxlen  = max(len(startBit), len(goalBit))
        minlen = min(len(startBit), len(goalBit))
        difflen = maxlen - minlen 
        if len(startBit) == minlen: 
            startBit = "0" * difflen + startBit 
        if len(goalBit) == minlen: 
            goalBit = "0" * difflen + goalBit 
        print(startBit, goalBit)
        flips = 0 
        for i in range(0, len(startBit)): 
            if startBit[i] != goalBit[i]: 
                flips += 1 
        return flips 