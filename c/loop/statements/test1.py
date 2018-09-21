n = input("Enter a inuput : ")
for i in range(1, n + 1):
          # Print leading space
          for j in range(n -  i,  0,  -1):
               print(" "),
          # Print numbers      
          for j in range(i, 0, -1):
               print(j),
          for j in range(2, i + 1):
               print(j),
          print("") 
