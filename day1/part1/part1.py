def getInput():
  with open('input.txt', 'r') as file:
    input = file.readlines()
    input = [x.strip() for x in input]

    return input

def decodeWord(word):
  left,right  = 0, len(word) - 1

  while charIsNotNumber(word[left]) or charIsNotNumber(word[right]):
    if charIsNotNumber(word[left]):
      left += 1

    if charIsNotNumber(word[right]):
      right -=1

  return word[left] + word[right]


def charIsNotNumber(char):
  return ord(char) < 48 or ord(char) > 57


input = getInput()
sum = 0
for word in input:
  sum+=int(decodeWord(word))

print(sum)