# ICPC Global WorldFinals 2019 Problem A
# https://icpc.global/xwiki/wiki/public/download/worldfinals/WebHome/icpc2019.pdf

totalNum = input("N:")                          # Ask for N value
R = 4                                           # Initialize variables
C = int(totalNum)
topRow = []
botRow = []
outMatrix = []

inputMatrix = []
print("Enter the values from left to right, up to down:")
for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    inputMatrix.append(a)

for i in range(R):
    for j in range(C):
        print(inputMatrix[i][j], end=" ")   # Get the input matrix
    print()

workMatrix = inputMatrix
for p in range(int(totalNum)):
    aCheap = workMatrix[0][0]                   # Set the cheapest to the first value of the matrix (first row of A)
    aTall = workMatrix[1][0]                    # Set the tallest to the first value of the matrix (second row of A)
    for i in range(C):                          # Check for the cheapest values. If they are equal, go with the tallest
        if aCheap == workMatrix[0][i]:
            if aTall <= workMatrix[1][i]:
                aIndex = i
                aCheap = workMatrix[0][aIndex]
                aTall = workMatrix[1][aIndex]
        if aCheap > workMatrix[0][i]:
            aIndex = i
            aCheap = workMatrix[0][aIndex]
            aTall = workMatrix[1][aIndex]

    bCheap = workMatrix[2][0]
    bTall = workMatrix[3][0]
    for i in range(C):                          # Repeat the check from row A for row B
        if bCheap == workMatrix[2][i]:
            if bTall <= workMatrix[3][i]:
                bIndex = i
                bCheap = workMatrix[2][bIndex]
                bTall = workMatrix[3][bIndex]
        if bCheap > workMatrix[2][i]:
            bIndex = i
            bCheap = workMatrix[2][bIndex]
            bTall = workMatrix[3][bIndex]
    if bTall >= aTall:                          # If the values will not work, print impossible and quit
        print(aIndex)
        print("impossible\n")
        quit()
    topRow.append(aIndex + 1)                   # Add the values that were found to an output matrix
    botRow.append(bIndex + 1)

    workMatrix[0][aIndex] = 1000000000          # Set the used values to numbers outside of constraints
    workMatrix[1][aIndex] = 0
    workMatrix[2][bIndex] = 1000000000
    workMatrix[3][bIndex] = 0
    #print(inputMatrix)

outMatrix.append(topRow)                        # Combine answers into a single output matrix
outMatrix.append(botRow)

print("\n\nAnswer:\n")
for i in range(2):
    for j in range(C):
        print(outMatrix[i][j], end=" ")   # Get the input matrix
    print()
