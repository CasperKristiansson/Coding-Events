import webhandler

class RpnEvaluator(object):
    def __init__(self):
        pass

    def evaluate_rpn(self, rpn):
        """Evaluate RPN"""
        print(rpn)

        rpn = rpn.split(" ")

        try:
            return int(rpn[0]) / 24 + rpn[4]
        except:
            return "Error"

        



def primeCheck(n):
# 0, 1, even numbers greater than 2 are NOT PRIME
    if n==1 or n==0 or (n % 2 == 0 and n > 2):
        return False
    else:
        # Not prime if divisable by another number less
        # or equal to the square root of itself.
        # n**(1/2) returns square root of n
        for i in range(3, int(n**(1/2))+1, 2):
            if n%i == 0:
                return False
        return True
