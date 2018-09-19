usernum = int(input('Enter a number to figure if it is prime [or not]'))

# the range in a new list
newlist = []

factors = [1, usernum]

# place the number in a range from 1 until that number
for x in range(1, usernum+1):
  if usernum % x == 0:
    newlist.append(x)
  print(newlist)
# searches for those bad boys that are prime numbers
  if factors == newlist:
    print('Prime Number Alert!')
  else:
    print('Not A Prime Number')