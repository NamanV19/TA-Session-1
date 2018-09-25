row = 5
for i in range(0,row):
    print(" " * (row + 1 - i) + "* " * (i+1))
for i in range(row, 0-1, -1):
    print(" " * (row + 1 - i) + "* " * (i+1))