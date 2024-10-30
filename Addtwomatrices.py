X = [[10,11,12],
    [13 ,14,15],
    [16 ,17,18]]

Y = [[19,20,21],
    [22,23,24],
    [25,26,27]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)
