class Solution:
    def intToRoman(self, num: int) -> str:
        # List of tuples representing Roman numerals and their corresponding integer values.
        romans = [
            (1000, "M"),  # 1000 is represented by 'M'
            (900, "CM"),  # 900 is represented by 'CM'
            (500, "D"),   # 500 is represented by 'D'
            (400, "CD"),  # 400 is represented by 'CD'
            (100, "C"),   # 100 is represented by 'C'
            (90, "XC"),   # 90 is represented by 'XC'
            (50, "L"),    # 50 is represented by 'L'
            (40, "XL"),   # 40 is represented by 'XL'
            (10, "X"),    # 10 is represented by 'X'
            (9, "IX"),    # 9 is represented by 'IX'
            (5, "V"),     # 5 is represented by 'V'
            (4, "IV"),    # 4 is represented by 'IV'
            (1, "I")      # 1 is represented by 'I'
        ]

        # String to store the resulting Roman numeral
        romanNum = ""

        # Iterate through the Roman numeral values
        for divider in romans:
            # Append the Roman numeral to the result for the quotient of num // divider[0]
            # For example, if num is 3000, 'M' will be appended 3 times
            romanNum += divider[1] * (num // divider[0])
            # Update num to the remainder of num % divider[0]
            # This step reduces num for the next iteration
            num %= divider[0]

        # Return the final Roman numeral string
        return romanNum


# Another Solution found in the discussion section
# class Solution {
#     public String intToRoman(int num) {
#         String ones[] = {"","I","II","III","IV","V","VI","VII","VIII","IX"};
#         String tens[] = {"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
#         String hrns[] = {"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
#         String ths[]={"","M","MM","MMM"};
        
#         return ths[num/1000] + hrns[(num%1000)/100] + tens[(num%100)/10] + ones[num%10];
#     }
# }