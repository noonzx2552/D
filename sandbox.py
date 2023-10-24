table = []

with open("student_scores.csv", "r") as f:
    # Discard header.
    row = f.readline()

    # Read and process each rows.
    while row != "":
        row = f.readline()
        row = row.replace("\n","")   # Remove \n at end of line.
        columns = row.split(",") # Split line -> array of words.
        table.append(columns)

# Use table in code.
print(table)