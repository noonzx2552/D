table = []
averagemath = 0
averagesci = 0
averageeng = 0
with open("student_scores.csv", "r") as f:
    # Discard header.
    row = f.readline()

    # Read and process each row.
    while row != "":
        row = f.readline()
        row = row.replace("\n", "")   # Remove \n at the end of the line.
        columns = row.split(",")  # Split line -> array of words.
        table.append(columns)
    
# Calculate the average scores for each subject.
    #print(f"id:{a} math:{b} science:{c} english:{d}")
for i in range(10):
    averagemath += int(table[i][1])
    averagesci += int(table[i][2])
    averageeng += int(table[i][3])


averagemath /= 10
averagesci /= 10
averageeng /= 10
print(averagemath)

for i in range(10):
    table[i].insert(2, "😢" if float(table[i][1]) < averagemath else "-") 
    table[i].insert(4, "😢" if float(table[i][3]) < averagesci else "-")
    table[i].insert(6, "😢" if float(table[i][5]) < averageeng else "-")

# Iterate through the table and mark scores below average with "😢".
#for i in range(10):
#    if int(table[i][1]) < averagemath:
#        table[i][1] = "😢"
#        table[i][2] = "😢"
#    if int(table[i][3]) < averageeng:
#        table[i][3] = "😢"

print(type(table))

for i in table:
    print(i)
