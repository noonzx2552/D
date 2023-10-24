table = []
averagemath = 0
averagesci = 0
averageeng = 0
with open("student_scores.csv", "r") as f:
    # Discard header.
    row = f.readline()

    # Read and process each rows.
    while row != "":
        row = f.readline()
        row = row.replace("\n","")   # Remove \n at end of line.
        columns = row.split(",") # Split line -> array of words.
        table.append(columns)

for i in range(10):
    averagemath += int(table[i][1])
    averagesci += int(table[i][2])
    averageeng += int(table[i][3])

averagemath = averagemath/10
averagesci = averagesci/10
averageeng = averageeng/10

for i in range(10):
    if table[i][1] < averagemath:
    if table[i][2] < averagesci:
    if table[i][3] < averageeng: