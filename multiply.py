# using recursion, write a multiply function
# FUNCTION multi(INTEGER a,INTEGER b) RETURNS INTEGER a X b

def multiply(a, b)
  return a + multiply(a, b-1) if b>1 else a
