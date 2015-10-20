
# coding: utf-8

# In[57]:

"""
While taking a class on the culture of China, you have learned about the Chinese zodiac in which people fall into 1 of 12 categories, depending on the year of their birth. The categories, numbered 0 to 11, correspond to the following animals:

(0) monkey
(1) rooster
(2) dog
(3) pig
(4) rat
(5) ox
(6) tiger
(7) rabbit
(8) dragon
(9) snake
(10) horse
(11) goat

Those who believe in this zodiac think that the year of a person's birth influences both their personality and fortune in life.

Your task is to build a program that will ask a user for their birth year and tell them their zodiac sign.  If the user does not enter a number that can be interpreted as a year then an error message must be shown and the user given another chance.  If the user types "quit" then the program halts.

For extra credit: save each year that is input to a file and print a chart showing how many of each type or animal have been returned.

To find your zodiac sign, divide the year of your birth by 12. The remainder then determines your sign. For example: The remainder when we divide 1985 by 12, is 5; therefore, a person born in 1985 is an ox according to the Chinese zodiac.
"""


# In[8]:

# We are going to plan the program here.

# ZodiacSetup will do all the opening, loading and closing of files/data.
# Will retrun ZodiacList
def ZodiacSetup():
    # Class: Open the zodiac descriptions file
    ZodiacText = open('zodiacDescriptions.txt', 'r')
    # WL: open 'filename', options ('r' = read only, 'w'= write)
    # WL: default break up for files in python is lines. Default for strings of text is character.
    # WL: comment out print lines used to check each step
    # Every for loop needs some actions associated with it (indented afterwards). If actions in the
    # for loop are commented out, then the for loop also needs to be commented out.
    # Class: Read/Load the zodiac descriptions file. To do this, make a list with each line of file
    # as a list item.
    ZodiacList = []
    for animal in ZodiacText:
        ZodiacList.append(animal)
    # Class: Close the zodiac descriptions file as soon as we're done with it
    ZodiacText.close()

    return (ZodiacList)

#WL: Putting each step on a different line for easier readable and easier to follow
#zodiacCalculation will collect birthyear and determine zodiac sign and then display. 
# With error tracking.
# Will return birthYear
def zodiacCalculation():
    birthYear = input("What year were you born? ")
    try:
        birthYear = int(birthYear)
        ZodiacIndex = birthYear % 12
        print("Your Chinese Zodiac animal is", zodiacList[ZodiacIndex - 4])

    # special conditional like IF    
    except ValueError:
        # birthYear = 'null' <- works but not clean
        print('You did not provide a year in the form of an integer.')

    return birthYear
# Class: Repeat

zodiacList = ZodiacSetup()

birthYear = 0
while type(birthYear) is int:
    birthYear = zodiacCalculation()

# type will tell you what kind of variable a variable is

# WL: Can tab to autocomplete variables.
# WL: Close files as soon as you're done with them, because it forces the program to save stuff.


# In[ ]:




# In[ ]:



