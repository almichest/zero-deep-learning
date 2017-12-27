import p27

def XOR(x1, x2):
  s1 = p27.NAND(x1, x2)
  s2 = p27.OR(x1, x2)
  y = p27.AND(s1, s2)
  return y

print(XOR(0, 0))
print(XOR(0, 1))
print(XOR(1, 0))
print(XOR(1, 1))