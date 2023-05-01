from cs5103 import BigNumberComputation, stringNumber
import decimal 
def testCase1 ():
  a=7*(10**1186)
  b=16*(10**1187)
  op="+"
  result=BigNumberComputation(a, op, b)
  target=167*(10**1186)
  testResult=decimal.Decimal(target)
  if (result % testResult==0):
    print ("Test Case 1 Passed")
  else:
    print ("Test Case 1 Failed")
testCase1() 

def testCase2 ():
  a=7*(10**1186)
  b=16*(10**1187)
  op="-"
  result=BigNumberComputation(a, op, b)
  target=153*(10**1186)
  testResult=decimal.Decimal(target)
  if (result % testResult==0):
    print ("Test Case 2 Passed")
  else:
    print ("Test Case 2 Failed")
testCase2() 

def testCase3(): #Should return "Operand Not Allowed"
  a=7*(10**1186)
  b=16*(10**1187)
  op="/"
  result=BigNumberComputation(a, op, b)
  if (result):
    print ("Test Case 3 Passed")
  else:
    print ("Test Case 3 Failed")
testCase3()

def testCase4(): #Return commas
  a=7*(10**1186)
  b=16*(10**1187)
  op="+"
  result=BigNumberComputation(a, op, b)
  strResult=stringNumber(result)
  if ',' in strResult:
    print ("Test Case 4 Passed")
  else:
    print ("Test Case 4 Failed")
testCase4()

def testCase5(): #test with decimals
  a=decimal.Decimal(7*(10**1186))
  fraction1=decimal.Decimal(0.3)
  Anumber=a+fraction1
  b=decimal.Decimal(16*(10**1187))
  fraction2=decimal.Decimal(0.9)
  Bnumber=b+fraction2
  op="+"
  result=BigNumberComputation(Anumber, op, Bnumber)
  if result >=0:
    print ("Test Case 5 Passed")
  else:
    print ("Test Case 5 Failed")
testCase5()