import re
class Solution:
    def myAtoi(self, stri: str) -> int:
        stri = stri.strip()
        # print('stri', stri)
        stri = re.split("[ a-zA-Z]", stri)
        print('stri', stri)
        if stri[0]:
            flag = stri[0][0] if '+' == stri[0][0] or stri[0][0] == '-' else False
            stri[0] = stri[0][1:] if '+' == stri[0][0] or stri[0][0] == '-' else stri[0]
            # if stri[0]:
        else:
            return 0
        
        # print('stri', stri)
        # print('flag', flag)
        if stri:
            if '.' in stri[0] and stri[0].count('.') == 1 and stri[0][:(stri[0].index('.'))].isdigit():
                return int(stri[0][:(stri[0].index('.'))])
            # else:
                # return 0
            if stri[0].isdecimal():
                stri = int(stri[0])
            else:
                return 0
            # print('stri', stri)
            
            # print('stri', stri)
            if flag:
                stri = -(stri) if flag == '-' else stri
                return ((-2 ** 31)) if stri <  ((-2 ** 31))else (stri )
            return ((2 ** 31) - 1) if stri >  ((2 ** 31) - 1) else (stri )
        else:
            return 0


print(Solution().myAtoi("987"))
