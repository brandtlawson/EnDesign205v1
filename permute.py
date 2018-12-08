class Permute(n):

    def perm(n):
        ans = []
        for i in range(2 ** n - 1):
            ans.append(binary(i + 1, n))
        return ans


    def binary(m, n):
        bin = []
        while (m != 0):
            b = m % 2
            bin.append(int(b))
            m -= b
            m = m / 2
        for i in range(n - len(bin)):
            bin.append(0)
        return bin
