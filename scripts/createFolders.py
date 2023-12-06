import os

def createFolders():
  rootFolder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  for i in range(6,26):
    folder = os.path.join(rootFolder,f"day{i}")
    if not os.path.exists(folder):
      os.mkdir(folder)

      part1Folder = os.path.join(folder,"part1")
      part2Folder = os.path.join(folder,"part2")
      os.mkdir(part1Folder)
      os.mkdir(part2Folder)

      createFiles(part1Folder,f"part1")
      createFiles(part2Folder,f"part2")

def createFiles(folder,filename):
  pythonFilePath = os.path.join(folder,f"{filename}.py")
  with open(pythonFilePath,'w') as f:
    f.write('')
  

  inputFilePath = os.path.join(folder,"input.txt")
  with open(inputFilePath,'w') as f:
    f.write('')

if __name__ == "__main__":
  parentFolder = os.path.dirname(os.path.abspath(__file__))
  createFolders() 