import math

# distance = (time - speed) * speed

# distance = y
# speed = x
# time = K


# y < kx - x^2
# x^2 - kx + y < 0


# x = (-b ± √ (b2 - 4ac) )/2a to find root

#return input as [(time1, distance1), (time2, distance2)]
def getInput(filename):
  with open(filename,'r') as f:
    input = f.readlines()
    input = [line.split(':') for line in input]
    input[0] = input[0][1].strip().split()
    input[1] = input[1][1].strip().split()

    return input

# distance = 9
# time = 7

# a = 1
# b = -1 * time
# c = distance



# x1=((-1)*b + math.sqrt(b**2 - 4*a*c))/(2*a)
# x2=((-1)*b - math.sqrt(b**2 - 4*a*c))/(2*a)



if __name__ == '__main__':
  input = getInput('input.txt')
  totalSum = 1
  for i in range(len(input[0])):
    time = int(input[0][i])
    distance = int(input[1][i])

    a = 1
    b = -1 * time
    c = distance

    x1 = math.floor(((-1)*b + math.sqrt(b**2 - 4*a*c))/(2*a))
    x2 = math.ceil(((-1)*b - math.sqrt(b**2 - 4*a*c))/(2*a))

    totalSum *= (abs(x1 - x2) + 1)

    print(totalSum)

  print(totalSum)





