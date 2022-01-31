import math

class binary:
    def binary(n):
        return bin(n)[2:]
    #a**x mod n
    def pow_by_binary_exponentiation(a, x, n):
        x = [int(b) for b in binary(x)]
        y = a
        for i in range(1, len(x)):
            y= (y**2) % n
            if x[i] == 1:
                y = (y * a) % n
        return y




#class Montgomery:
#    def __init__(self, ):

    #def calculateN()


if __name__ == '__main__':
    u = -(2**62+2**55+1)
    N = 36 * u**4 + 36 * u**3 + 24 * u**2 + 6 * u + 1
    print(N)

    b = binary()
    b.binary(N)
    b.pow_by_binary_exponentiation(40710, N)


