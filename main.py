with open("file1.txt") as _:
  file_1 =_.readlines()
  
with open("file2.txt") as _:
  file_2 =_.readlines()

result = [int(file_1[i]) for i in range(len(file_1)) if file_1[i] in file_2] 


print(result)