import sqlite3  # This is the package for all sqlite3 access in Python
import sys      # This helps with command-line parameters

# Connect to the database
conn = sqlite3.connect("/Users/sergio/Documents/UW Documents/UW Info 330/INFO330-AccessingDatabases/pokemon.sqlite")
cursor = conn.cursor()

# All the "against" column suffixes:
types = ["bug","dark","dragon","electric","fairy","fight",
    "fire","flying","ghost","grass","ground","ice","normal",
    "poison","psychic","rock","steel","water"]

# Take six parameters on the command-line
if len(sys.argv) < 6:
    print("You must give me six Pokemon to analyze!")
    sys.exit()

team = []
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue

    # Analyze the pokemon whose pokedex_number is in "arg"
    cursor.execute(f"SELECT * FROM pokemon WHERE pokedex_number = {arg}")
    result = cur.fetchnone()

    # You will need to write the SQL, extract the results, and compare
    # Remember to look at those "against_NNN" column values; greater than 1
    # means the Pokemon is strong against that type, and less than 1 means
    # the Pokemon is weak against that type
    name = result[1]
    print(f"Analyzing {name}:")
    for i, t in enumerate(types):
        against_column = f"against_{t}"
        against_value = result[i + 3]

        if against_value > 1:
            print(f" {name} is strong against {t}")
        elif against_value < 1:
            print(f" {name} is weak against {t}")
        else:
            print(f" {name} has no effect against {t}")


answer = input("Would you like to save this team? (Y)es or (N)o: ")
if answer.upper() == "Y" or answer.upper() == "YES":
    teamName = input("Enter the team name: ")

    # Write the pokemon team to the "teams" table
    print("Saving " + teamName + " ...")
else:
    print("Bye for now!")


# Closing the connection to the database
conn.close()

