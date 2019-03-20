# Prime number checker
def is_prime(x):
  if x < 2:
    return False
  elif x == 2:
    return True
  for n in range(2, x):
    if x % n == 0:
      return False
  else:
    return True

# Median from a list of integers
def median(lst):
  median = 0
  lsst = sorted(lst)
  print (lsst)
  lst
  if len(lsst) % 2 == 0:
    median = (lsst[(len(lsst) / 2) - 1] + lsst[len(lsst) / 2]) / 2.0
  elif len(lsst) < 2:
    median = lsst[0]
  else:
    median = lsst[(len(lsst) - 1) / 2]
  print (median)
  return median