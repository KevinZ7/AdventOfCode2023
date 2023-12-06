# turn each map into an array of mappings, each mapping in is in the format (destinationStart, sourceStart, range)

def getInput(filename):
  with open(filename, 'r') as f:
    content = f.read()
    sections = content.strip().split('\n\n')

    seeds = [int(x) for x in sections[0][7:].split()]
    seedPairs = []

    for i in range(0,len(seeds),2):
      seedPairs.append((seeds[i],seeds[i+1]))

    maps = []

    for section in sections[1:]:
      map = []
      lines = section.split('\n')
      for i in range(1,len(lines)):
        mappingDetails = lines[i].split()
        map.append((int(mappingDetails[0]),int(mappingDetails[1]),int(mappingDetails[2])))
      maps.append(map)
    
    return seedPairs, maps



def binarySearch(map, target):
  left, right = 0, len(map) - 1
  
  while left <= right:
    mid = (left + right) // 2
    sourceStart,range = map[mid][1],map[mid][2]
    if sourceStart <= target <= sourceStart + range - 1:
      return mid
    elif map[mid][1] > target:
      right = mid - 1
    else:
      left = mid + 1

  return max(left,right)


seedPairs, maps = getInput('input.txt')

#sort maps based on sourceStart (index 1)

for i in range(len(maps)):
  maps[i].sort(key=lambda x: x[1])



# given a set of pairedInputs: (initialSeed, seedRange)
# we can produce a set of pariedOutputs: (initialDestination, destinationRange)


# for example

#  0       1          2
# {--}----{--------}-{---}
#  ^-|----|-

# (destinationFromBinarySearch, units until next section)


# 1. get the section the initial seed belongs to , suppose it is index k
# 2. calculate the pairedOutputs

minLocation = float('inf')

for seedPair in seedPairs:
  currentInput = [seedPair]
  for i in range(len(maps)):  
    map = maps[i]
    currentOutput = []
    for pair in currentInput: 
      currentSeed  = pair[0]
      lastSeed = currentSeed + pair[1] - 1
      k = binarySearch(map, currentSeed)


      while currentSeed < lastSeed:
        # print(currentSeed)
        if k >= len(map):
          seedsToAdd = lastSeed - currentSeed + 1
          currentOutput.append((currentSeed,seedsToAdd))
          currentSeed += seedsToAdd
        elif currentSeed < map[k][1]:
          seedsToAdd = min(map[k][1] - currentSeed, lastSeed - currentSeed)
          currentOutput.append((currentSeed, seedsToAdd))
          currentSeed += seedsToAdd
        else:
          seedsToAdd = min(map[k][1] + map[k][2] - currentSeed, lastSeed - currentSeed)
          currentOutput.append((map[k][0] + currentSeed - map[k][1], seedsToAdd))
          currentSeed += seedsToAdd
          k += 1
    
    currentInput = currentOutput
    if i == len(maps) - 1:
      for pair in currentInput:
        minLocation = min(minLocation, pair[0])


print(minLocation)






 
  
