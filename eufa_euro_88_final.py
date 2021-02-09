# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Assigment: Strings WINC Academy by Peter Klaassen


player0 = "Ruud Gullit"
player1 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = player0 + " " +str(goal_0) + " , " + player1  + " " +str(goal_1)
print(scorers)

report = f'{player0} scored in the {goal_0}th minute.\n{player1} scored in the {goal_1}th minute.'
print(report)

#Part 2


player2 = "Ronald Koeman"

find_space = player2.find(" ")
first_name = player2[:find_space]

print (first_name)

last_name = player2[-find_space:]
last_name_len = len(last_name)

print(last_name)
print(last_name_len)

name_short = player2[0]

print (name_short + ". " + last_name)

players_fn = player2[:find_space]
bang = "! "

first_name_with = players_fn + bang

players_fn_len = (len(players_fn))
chant = players_fn_len* first_name_with

space_at_end = chant[:-1]
good_chant = space_at_end[:-1] != " "

print (good_chant)
print (space_at_end)






