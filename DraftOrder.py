#Fantasy Football Draft Picker
#Author: Rudy Faile
#Date: 8/11/17

import random
from time import sleep


print ('''
***************************************************************************************************
***_.-=""=-._**************************************************************************************
*.'\\-++++-//'.																	   
(  ||      ||  ) Welcome to the 2017 Faile Football Federation Draft Order Drawing!         
*'.//      \\.'																	  
***`'-=..=-'`**************************************************************************************
***************************************************************************************************
''')

Faile_Football_Federation_Members = ["Dallas", "Jim", "Papa Rudy", "Rudy", "Randall",
									 "Kristen", "Megan", "Jeff", "Bruce", "Brad"]
			


pick = ["Coveted First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth and Final"]
			
Draft_Order = Faile_Football_Federation_Members[:]

random.shuffle(Draft_Order)

def wait_art():
	randomize_state = ['|', '/', '-', '\\']
	count = 0
	which_state = 0
	while count < 40:
		print (randomize_state[which_state])
		count += 1
		which_state +=1
		if which_state >= 4:
			which_state = 0
		sleep(.100)

def and_the_order_is():
	global Draft_Order
	count = 0
	while count < 10:
		print ("The {} Pick in the Draft Goes to: {}!!".format(pick[count],Draft_Order[count]))
		count += 1
		input("")
		wait_art()
		
	

input("Press any key to begin The Draft.")
wait_art()
and_the_order_is()
input ("Finished.")