class Solution:
    def maximum69Number (self, num: int) -> int:

        input = str(num)
        output = ''
        checker = True

        for i in range(len(input)):
            if input[i] == '9':
                output += '9'
            else:
                if checker:
                    output += '9'
                    checker = not checker
                else:
                    output += '6'
                

        return int(output)
        