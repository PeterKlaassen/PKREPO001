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

anwser0 = player0
anwser1 = goal_0
anwser2 = player1
anwser3 = goal_1
report = (f'{anwser0} scored in the {anwser1}th minute.\n{anwser2} scored in the {anwser3}th minute.')
print(report)

#testing print(player0 +str(goal_0), player1 + str(goal_1))
#testing print(player0 + str(goal_0))


#Part 2


player2 = "Ronald Koeman"

first_name = player2[:6]
find = player2.find("R")

#testing print (first_name)
#testing print (find, first_name)
#testing print (find)

last_name_len = player2[7:]
find = player2.find("Koeman")
#testing print(len(last_name_len))
#testing print(find, len(last_name_len))
#testing print(find)

name_short = player2[:1]
find = player2.find("R")
#testing print (name_short + ". " + last_name_len)
#testing print (find, name_short + ". " + last_name_len)
#testing print (find)
players_fn = player0[:4]
bang = "!  "

first_name_with = players_fn + bang

players_fn_len = (len(players_fn))
chant = players_fn_len* first_name_with
string_len = (len(chant))

space_at_end = chant[-1]

good_chant = chant[0:26]

print (good_chant)


#testing print(chant[0:23])
#testing print (space_at_end)
#testing print(players_fn_len)
#testing print(string_len)
#testing print (chant[:24]
#testing print (players_fn)





