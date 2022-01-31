
def binary(n):
    return bin(n)[2:]

# バイナリ法
def pow_by_binary_exponentiation(a, x, n): # a^x mod n
    x = [int(b) for b in binary(x)]
    y = a
    for i in range(1, len(x)):
        y = (y**2) % n
        if x[i] == 1:
            y = (y * a) % n
    return y

u = -(2**62+2**55+1)
N = 36 * u**4 + 36 * u**3 + 24 * u**2 + 6 * u + 1
print(N)

print(binary(N))
ans = pow_by_binary_exponentiation(2, 40710, N)
print(hex(ans))