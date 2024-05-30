class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decodeDic = {" ": " "}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        for letter in key:
            if (letter not in decodeDic):
                decodeDic[letter] = alphabet[i]
                i += 1
        
        decodeMsg = ""

        for letter in message: 
            decodeMsg += decodeDic[letter]
        
        return decodeMsg
