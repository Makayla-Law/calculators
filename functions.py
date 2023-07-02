num_x = 0.3529
num_y = 0.051

def hyp2(num1, num2, sf1, sf2):
  sigfigs1 = num1*sf1
  sigfigs2 = num2*sf2
  sq = (sigfigs1**2)+(sigfigs2**2)
  h = sq**(0.5)
  print(h)
  return(h)

num_x = 0.3529
num_y = 0.051
hyp2(num_x, num_y,(10**(-5)), (10**(-5)))
