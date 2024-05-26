class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        output = ""
        i = 0
        while(i < n):
            if (command[i] == "G"):
                output += "G"
                i += 1
            elif (command[i:i+2] == "()"):
                output += "o"
                i += 2
            else:
                output += "al"
                i += 4
        
        return output


# Another solution found in the discussion section
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")