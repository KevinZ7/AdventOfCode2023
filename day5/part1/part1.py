# turn each map into an array of mappings, each mapping in is in the format (destinationStart, sourceStart, range)

def getInput(filename):
  with open(filename, 'r') as f:
    content = f.read()
    sections = content.strip().split('\n\n')

    seeds = [int(x) for x in sections[0][7:].split()]
    maps = []

    for section in sections[1:]:
      map = []
      lines = section.split('\n')
      for i in range(1,len(lines)):
        mappingDetails = lines[i].split()
        map.append((int(mappingDetails[0]),int(mappingDetails[1]),int(mappingDetails[2])))
      maps.append(map)
    
    return seeds, maps



def binarySearch(map, target):
  left, right = 0, len(map) - 1
  
  while left <= right:
    mid = (left + right) // 2
    desinationStart,sourceStart,range = map[mid][0],map[mid][1],map[mid][2]
    if sourceStart <= target <= sourceStart + range - 1:
      return desinationStart + target - sourceStart
    elif map[mid][1] > target:
      right = mid - 1
    else:
      left = mid + 1

  return target


seeds, maps = getInput('input.txt')

#sort maps based on sourceStart (index 1)

for i in range(len(maps)):
  maps[i].sort(key=lambda x: x[1])



# for each seed, go through each mapping and perform binary serach to find the destination
#   carry on this destination to the next mapping and repeat until we get the location
#       compare the location to the global min location

minLocation = float('inf')

for seed in seeds:
  current = seed
  for i in range(len(maps)):
    current = binarySearch(maps[i], current)
    if i == len(maps) - 1:
      minLocation = min(minLocation, current)
  


print(minLocation)



