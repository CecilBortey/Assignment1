year = int(input("Enter year of birth: "))
current_year = 2023
vote = current_year - year

print(vote, "years")
if vote >= 18:
    print("You are eligible to vote")
else:
    print("Sorry you cannot vote")
    