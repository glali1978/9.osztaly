MOD = 10**9 + 7

def sum_of_sigma(n):
    total = 0
    i = 1
    while i <= n:
        q = n // i
        j = n // q
        count = j - i + 1
        # összeadás képlete: (q * (i + j) * count) // 2
        total += (q * (i + j) * count // 2) % MOD
        total %= MOD
        i = j + 1
    return total

# Példa futtatás
n = int(input("Add meg n értékét: "))
print(sum_of_sigma(n))
