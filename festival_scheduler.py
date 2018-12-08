#Hard code variables for code development
#user_genre = ["Alternative", "Blues", "Christian", "Classical", "Country", "EDM", "Folk", "Hip Hop", "Indie", "Jazz", "Pop", "Rap", "Reggae", "Rock", "R&B"]
#user_locations = ["Austin", "New York", "Dallas", "San Francisco", "Santa Fe", "New Orleans"]


#Function that, given a location and genre, makes a list of possible festivals that the user would want to attend (including time conflicts, they will be accounted for in the scheduler)
def select_festival(location, genre, global_festivals_list):
	possible_festivals = []	
	#Iterate through the global festivals list
	for festival in global_festivals_list:
		#check that the item in the list matches location and genre, add to possibility list
		if (festival.location == location) and (genre in festival.genres):
			possible_festivals.append(festival)
	#Return error if there are no festivals
	if len(possible_festivals) == 0:
		return -1
	#Return a list of all festivals in the desired location
	else: 
		return possible_festivals