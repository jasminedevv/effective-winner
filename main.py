player_name = "Kenny"
def welcome():
    global player_name
    print ("Hello Player! Please enter your name.")
    player_name = raw_input('Name: ')
    print ("Ah, yes, a fine name!")
    print ("you are in for a sweet ride, " + player_name)

welcome()
