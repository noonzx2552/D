table = []
average = ["student_id",0,0,0]
averagemath = 0
averagesci = 0
averageeng = 0
with open("student_scores.csv", "r") as f:
    row = f.readline()
    # Read and process each rows.
    while row != "":
        row = f.readline()
        row = row.replace("\n","")   # Remove \n at end of line.
        columns = row.split(",") # Split line -> array of words.
        table.append(columns)

for i in range(4):
    for j in range(10):
        averagemath += table[i][j]
for i in table:
    print(i)
print(average)