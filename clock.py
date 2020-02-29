#------------------------------------------------------------------------------
#clock.py
#------------------------------------------------------------------------------
class Time(object):
    def __init__(self, hour=0, mins=0, secs=0):
        '''This function takes three parameters which are then turned into 
        instance variables that are used in the other functions.'''
        if type(hour)==int:
            self.__hour=hour
            self.__mins=mins
            self.__secs=secs
    def __repr__(self):
        '''This function takes the instance variables and returns a string 
        containing "Class Time:" and the variables in the format "hh:mm:ss" as 
        specified.'''
        return "Class Time: {:02d}:{:02d}:{:02d}".format(self.__hour, self.__mins, self.__secs)
    def __str__(self):
        '''This function takes the instance variables and returns them in the 
        format "hh:mm:ss" as specified.'''
        return "{:02d}:{:02d}:{:02d}".format(self.__hour, self.__mins, self.__secs)
    def from_str(self, string):
        '''This function takes the reference to the current object and a string.
        The string is then split into 3 parts, the hours, minutes and seconds, 
        which are all added to a list. Using the list, three instance variables
        are made for hours, minutes and seconds which can be used in the other 
        two functions.'''
        self.__str=string
        lst=self.__str.split(":")
        self.__hour=int(lst[0])
        self.__mins=int(lst[1])
        self.__secs=int(lst[2])
        
        