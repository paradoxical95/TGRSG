import random
import time
#import termcolor
# Created by Paradoxical. Yes, I was bored and did not wanted to open my browser to find a picker wheel. So I coded this to have a random Episode/Series and enjoy watching Top Gear
series = 1
episode = 1
episode_max= 10
series_min = 1
series_max = 22

#S1,S2,S4,S10,S22       	10
#S3,S5,S18		            9
#S8,S12,S16		            8
#S7,S9,S13,S14,S19,S21	    7
#S11,S15,S17,S20		    6
#S6			                11

def GetRandomSeriesEpisode(min,max):
    series = random.randint(min,max)
    
    if series == 1 or series == 2 or series == 4 or series == 10 or series == 22: 
        #10 Episodes in these series'
        episode_max = 10
        episode = random.randint(1,10)
        
    elif series == 3 or series == 5 or series == 18:
        episode_max = 9
        episode = random.randint(1,9)
        #9 Episodes in these series'
    
    elif series == 8 or series == 12 or series == 16:
        episode_max = 8
        episode = random.randint(1,8)
        #8 Episodes in these series'
        
    elif series == 7 or series == 9 or series == 13 or series == 14 or series == 19 or series == 21 :
        episode_max = 7
        episode = random.randint(1,7)
        #7 Episodes in these series'
        
    elif series == 11 or series == 15 or series == 17 or series == 20 :
        episode_max = 6
        episode = random.randint(1,6)
        #6 Episodes in these series'
        
    else:
        episode_max = 11 #has to be Series 6 then. Which has 11 episodes
        episode = random.randint(1,11)
        
    print("\n_________________________________________________________________________")
    print(f"\nYou should watch Series {series} and Episode {episode} .\n\nRemember, Top Gear. Ambitious but rubbish !\n\n(Top Gear BBC London W12 whatever the address was.)")
    #print(termcolor.coloured((f"\nYou should watch Series {series} and Episode {episode} ."),'red'))

print("Welcome to 'Top Gear Random Series Generator' (TGRSG) !")

def ExitScene():
    exit_ans = input("\nType [1] to do this again (if you're James May with OCD) \nOR Type [2] to exit (like Hammond would if he sees water)  = ")
    if exit_ans == '2' or exit_ans == '[2]':
        print("\nSee you in the next one !")
        time.sleep(3)
        exit()
    else:
        print("\nYour genius is almost frightening...\n")
        time.sleep(1)
        Intro()

def Intro():
    custom = input("Do you want to enter a range for Series [1-22] (Y or N) = ")
    if custom == 'Y' or custom == 'y' or custom == 'yes' or custom == 'Yes':
        series_min = input("Which series to start from? =  ")
        series_max = input("Which series to end at? =  ")
        print(f"\nGenerating random Series in range {series_min} and {series_max}")
        time.sleep(2)
        GetRandomSeriesEpisode(int(series_min),int(series_max))
        ExitScene()
    else: 
        print("\nGenerating random Series and Episode...")
        time.sleep(2)
        GetRandomSeriesEpisode(1,22)
        ExitScene()

Intro()
