class Power:
    def my_pow(self, x, n):
        result = 1
        for _ in range(n):
            result = result * x
        return result
p = Power()
print(p.my_pow(-2, 3)) 
print(p.my_pow(3, 5))
