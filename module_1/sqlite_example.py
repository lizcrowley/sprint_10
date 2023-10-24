# Step 0 - import sqlite3
import sqlite3

# Step 1
# Connect to the database
# triple-check the spelling of your database filename, else you may create a new database
connection = sqlite3.connect('rpg_db.sqlite3')


# Step 2 - Make the "cursor"
cursor = connection.cursor()


# Step 3 - Write a query
query = "SELECT character_id, name FROM charactercreator_character;"

# Step 4 - Execute the query on the cursor and fetch the results
# "pulling the results" from the cursor
results = cursor.execute(query).fetchall()

if __name__ == "__main__":
    print(results[:5])
