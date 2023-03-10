from cs5103 import BigNumberComputation

def testCase1 ():
  a=7*(10**1186)
  b=16*(10**1187)
  op="+"
  result=BigNumberComputation(a, op, b)
testCase1()

def testCase2 ():
  a=7*(10**1186)
  b=16*(10**1187)
  op="-"
  result=BigNumberComputation(a, op, b)
testCase2()

def testCase3(): #Should return "Operand Not Allowed"
  a=7*10e1123
  b=16*10e1187
  op="/"
  result=BigNumberComputation(a, op, b)
testCase3()