import csv
import mysql.connector

# Set up the MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toxicity"
)

# Create a cursor to execute SQL queries
cursor = db.cursor()

# Open the CSV file and loop through its rows
with open('C:/Users/Calvi/PycharmProjects/CSVtoMYSQL/submission (4).csv', encoding='utf-8',) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        # Extract the values from the row
        steamid = row[0]
        name = row[1]
        comment_text = row[2]
        toxic = row[3]
        severe_toxic = row[4]
        obscene = row[5]
        threat = row[6]
        insult = row[7]
        identity_hate = row[8]

        # Insert the row into the MySQL table
        query = "INSERT INTO chatlogs (steamid, name, comment_text, toxic, severe_toxic, obscene, threat, insult, identity_hate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (steamid, name, comment_text, toxic, severe_toxic, obscene, threat, insult, identity_hate)
        cursor.execute(query, values)

        print(query)


# Commit the changes to the database
db.commit()

# Close the database connection
db.close()