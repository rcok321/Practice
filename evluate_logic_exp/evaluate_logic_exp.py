class Solution:

    @staticmethod
    def evaluate_logic(p1, p2, oper):
        if oper == 'O':
            return 'T' if (p1=='T' or  p2 =='T') else 'F'
        elif oper == 'A':
            return 'T' if (p1=='T' and  p2 =='T') else 'F'

    @staticmethod
    def evaluate_logic_no_bracket(s):
        output = 'T'
        oper = 'A'
        for c in s:
            if c == 'T' or c == 'F':
                output = Solution.evaluate_logic(output,c,oper)
            elif c == 'O' or c == 'A':
                oper = c
            else:
                pass
        return output

    @staticmethod
    def evaluate_logic_exp(s):
        if ')' in s:
            s_left = s.split(')')[0]
            s_right = s_left[0].split('(')
            return Solution.evaluate_logic_exp('('.join(s_right[:-1])+Solution.evaluate_logic_no_bracket(s_right[-1])+')'.join(s_left[1:]))
        else:
            return Solution.evaluate_logic_no_bracket(s)

if __name__ == '__main__':
    s = 'FAT'
    print(s)
    print(Solution.evaluate_logic_exp(s))




