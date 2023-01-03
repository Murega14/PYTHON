#lists are used to store multiple items in a variable

teams = ["chelsea", "liverpool", "real madrid", "arsenal", "bayern"]
print(teams)

#if i wanted to add an item at the end of the list
teams.append("ajax")
#if i wanted to remove say liverpool from the list
teams.remove("liverpool")
#if i wanted to add a team at a certain position say 2nd
teams.insert(1, "Psg")
#if i wanted to remove the last element in the list
teams.pop()
#to sort the teams alphabetically
teams.sort()

for x in teams:
    print(x)
