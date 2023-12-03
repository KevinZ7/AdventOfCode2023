
# z: zero
# o: one
# t: two, three
# f: four, five,
# s: six, seven,
# e: eight
# n: nine

# to locate first digit, we go through each Char from left to right

# at each char, if its a dec, we return it

# otherwise:

# locate the possible words that start with this char
#   for each of those words, check if the str[i:i+len(word)] == word
#     if so, return the number that matches up to the word



# to locate last digit, do the same but use the reverse dictionary


#Constants
DIGIT_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
WORDS_TO_DIGITS = {
  'zero': 0,
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five':5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9,
  'orez': 0,
  'eno': 1,
  'owt': 2,
  'eerht': 3,
  'ruof': 4,
  'evif': 5,
  'xis': 6,
  'neves': 7,
  'thgie': 8,
  'enin': 9

}

#Helper functions
def buildLeadingLetterDict(words, reverse=False):
  leadingLetterDict = {}
  for word in words:
    if reverse:
      word = word[::-1]
    leadingLetterDict[word[0]] = leadingLetterDict.get(word[0], []) + [word]
  return leadingLetterDict

def getInput(filename):
  with open(filename, 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
  return lines

def charIsNotNumber(char):
  return ord(char) < 48 or ord(char) > 57


def findFirstWord(word, dict):
  for index,char in enumerate(word):
    if not charIsNotNumber(char):
      return int(char)
    elif char in dict:
      for possibleWord in dict[char]:
        if word[index:index+len(possibleWord)] == possibleWord:
          return WORDS_TO_DIGITS[possibleWord]



input = getInput('input.txt')

leadingLetterDict = buildLeadingLetterDict(DIGIT_WORDS)
leadingLetterDictReverse = buildLeadingLetterDict(DIGIT_WORDS, reverse=True)

sum = 0
for word in input:
  firstDecimal = findFirstWord(word, leadingLetterDict)
  lastDecimal = findFirstWord(word[::-1], leadingLetterDictReverse)
  sum += int(str(firstDecimal) + str(lastDecimal))

print(sum)






 