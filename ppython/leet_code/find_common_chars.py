class Solution:
    def commonChars(self, A):
        str1 = sorted(list(A[0]))
        str2 = sorted(list(A[1]))
        
        len_str1 = len(str1)
        len_str2 = len(str2)
        idx1 = idx2 = 0
        comm = []
        while idx1 < len_str1 and idx2 < len_str2:
            if ord(str1[idx1]) == ord(str2[idx2]):
                comm.append(str1[idx1])
                idx1 += 1
                idx2 += 1
            if idx1 < len_str1 and idx2 < len_str2:
                if  ord(str1[idx1]) > ord(str2[idx2]):
                    idx2 += 1
                elif ord(str1[idx1]) < ord(str2[idx2]):
                    idx1 += 1
        print('comm', comm)

        for str1 in A[2:]:
            str1 = sorted(list(str1))
            str2 = comm
            
            len_str1 = len(str1)
            len_str2 = len(str2)
            
            comm = []
            idx1 = idx2 = 0
            while idx1 < len_str1 and idx2 < len_str2:
                if ord(str1[idx1]) == ord(str2[idx2]):
                    comm.append(str1[idx1])
                    idx1 += 1
                    idx2 += 1
                if idx1 < len_str1 and idx2 < len_str2:
                    if  ord(str1[idx1]) > ord(str2[idx2]):
                        idx2 += 1
                    elif ord(str1[idx1]) < ord(str2[idx2]):
                        idx1 += 1
           
        return comm


print(Solution().commonChars(["bella","label","roller"]))
