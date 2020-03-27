

class Solution:
    def middleNode(self, head):
        sp = head
        dp = head
        
        while dp and dp.next:
            sp = sp.next
            dp = dp.next
            #  this condition is not necessary
            #  we are checking in while loop
            #  dp.next also
            # below one is better
            if dp:
                dp = dp.next
                
        return sp


class Solution:
    def middleNode(self, head):
        sp = head
        dp = head
        
        while dp and dp.next:
            sp = sp.next
            dp = dp.next.next
                
        return sp
