"""This module provides an implementation of the timeADT.

The ADT is implemented in class Time.

Author: Nadia Aly (naaly)
"""


class Time:
    def __init__(self, hour, minutes, seconds):
        """The time ADT is a time holder of sorts.  User inputs a time
        in hours, minutes, and seconds and the class initializes a way to store
        and manipulate that information. Init method also contains some error catching
        as far as input times being out of range.

        arguments: integer input of hours, minute input, second input

        precondition: cannot be outside the realm of the typical 24 hour clock;
        1-23 acceptable for hour argument
        0-59 acceptable for minute argument
        0-59 acceptable for second argument

        """


        assert type(hour)==int,"please try again with integer value only"
        assert type(minutes)==int,"please try again with integer value only"
        assert type(seconds)==int,"please try again with integer only"

        assert hour>=0 and hour<24,"hour must be between 0 and 23 (inclusive)"
        assert minutes>=0 and minutes<60, "minutes must be between 0 and 59 (inclusive)"
        assert seconds>=0 and seconds<60, "minutes must be between 0 and 59 (inclusive)"



        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
        self.totalSeconds = (hour * 3600) + (minutes * 60) + seconds
        self.helperDif = 0

    def hour(self):
        """
        return an integer of the hour for the requested time object
        arguments: none
        precondition: a time object initialized and given a time within the limits of acceptable time
        :return:  an integer of the hour for the requested time object, 0-23, without formatting
        """

        return self.hour

    def minutes(self):
        """
        desc: returns an integer of the minute for the requested time object
        arguments: none
        precondition: a time object initialized and given a time within the limits of acceptable time
        :return: returns an integer of the minute for the requested time object, 0-59, without formatting
        """

        return self.minutes

    def seconds(self):
        """
        desc: returns an integer of the second for the requested time object
        arguments: none
        precondition: a time object initialized and given a time within the limits of acceptable time
        return: returns an integer of the second for the requested time object, 0-59, without formatting
        """

        return self.seconds

    def numSeconds(self, otherTime):
        """
        calculate the difference between two times in seconds; specifically the time of the time object
                    and the "othertime" time object
        arguments otherTime: an object of the time class
        :return: the difference in seconds between the two times, in absolute terms.  No negative values can be
                 returned
        """
        assert type(otherTime) == Time, "Please only compare time objects"
        returnDif = otherTime.totalSeconds - self.totalSeconds
        self.helperDif = returnDif
        returnDif = abs(returnDif)
        return returnDif

    def isAM(self):
        """return True if Time is before 12:00 PM, false otherwise"""
        if self.hour < 12:
            return True
        else:
            return False

    def isPM(self):
        """return True if Time is after 12:00 pm, false otherwise"""
        if self.hour >= 12:
            return True
        else:
            return False


    def __ne__(self,otherTime):
        """return True if the two times compared are not equal.  Precondition that each are of Time class"""
        assert type(otherTime)==Time
        if self.totalSeconds==otherTime.totalSeconds:
            return False
        else:
            return True




    def __lt__(self,other):
        """ return true if the lhs Time is less than the rhs.  False otherwise.
        Precondition: both class objects of the Time class
        These are flipped (y.__lt(x)) because ?"""
        assert type(other)==Time
        difLT = self.totalSeconds - other.totalSeconds
        if difLT < 0:
            return True
        else:
            return False

    def __le__(self, other):
        assert type(other)==Time
        difLT = self.totalSeconds - other.totalSeconds
        if difLT > 0:
            return False
        elif difLT < 0:
            return True
        else:
            return True


    def __str__(self):
        """
        return string of the time, in format xx:xx:xx PM/AM depending.

        There are 9 cases as far as the time is concerned and printing correctly:
        case 1-3: (1) 12 exactly, (2) less than 2 digit minute, (3) less than 2 digit second
        case 4-6: (4) between 1 and 9 pm (inclusive), (5) less than 2 digit minute, (6) less than 2 digit second
        case 7-9: (7) 1-9 am , (8) less than 2 digit minute, (9) less than 2 digit second
        """
        # 12 exactly - output should be 12:xx:xx PM
        if self.hour == 12:
            if self.minutes < 10:
                if self.seconds < 10:
                    return str(self.hour) + ":" + str(0) + str(self.minutes) + ":" + str(0) + str(self.seconds) + " PM"
                else:
                    return str(self.hour) + ":" + str(0) + str(self.minutes) + ":" + str(self.seconds) + " PM"
            else:
                return str(self.hour) + ":" + str(self.minutes) + ":" + str(self.seconds) + " PM"

        # know it's am since otherwise would hit case 1
        # must be between 1 to 9 pm; add leading 0 to hour at a minimum.  All 3 at a maximum
        #output should be 0k:xx:xx PM
        elif self.hour >= 13 and self.hour < 22:
            if self.minutes < 10:
                if self.seconds < 10:
                    return str(0) + str(self.hour - 12) + ":" + str(0) + str(self.minutes) + ":" + str(0) + str(
                        self.seconds) + " PM"
                else:
                    return str(0) + str(self.hour - 12) + ":" + str(0) + str(self.minutes) + ":" + str(
                        self.seconds) + " PM"
            elif self.seconds < 10:
                return str(0) + str(self.hour - 12) + ":" + str(self.minutes) + ":" + str(0) + str(self.seconds) + " PM"
            else:
                return str(0) + str(self.hour - 12) + ":" + str(self.minutes) + ":" + str(self.seconds) + " PM"
        # must be either 10, 11 pm.  12 becomes am
        elif self.hour >= 22 and self.hour < 24:
            if self.minutes < 10:
                if self.seconds < 10:
                    return str(self.hour - 12) + ":" + str(0) + str(self.minutes) + ":" + str(0) + str(
                        self.seconds) + " PM"
                else:
                    return str(self.hour - 12) + ":" + str(0) + str(self.minutes) + ":" + str(
                        self.seconds) + " PM"
            elif self.seconds < 10:
                return str(self.hour - 12) + ":" + str(self.minutes) + ":" + str(0) + str(self.seconds) + " PM"
            else:
                return str(self.hour - 12) + ":" + str(self.minutes) + ":" + str(self.seconds) + " PM"
        # must be 10 or 11 am; thus does not need to add a leading 0 to hour
        elif self.hour == 10 or self.hour == 11:
            if self.minutes < 10:
                if self.seconds < 10:
                    return str(0) + str(self.hour) + ":" + str(0) + str(self.minutes) + ":" + str(0) + str(
                        self.seconds) + " AM"
                else:
                    return str(0) + str(self.hour) + ":" + str(0) + str(self.minutes) + ":" + str(self.seconds) + " AM"
            else:
                return str(0) + str(self.hour) + ":" + str(self.minutes) + ":" + str(self.seconds) + " AM"
        else:
            if self.hour < 10:
                if self.minutes < 10:
                    if self.seconds < 10:
                        return str(0) + str(self.hour) + ":" + str(0) + str(self.minutes) + ":" + str(0) + str(
                            self.seconds) + " AM"
                    else:
                        return str(0) + str(self.hour) + ":" + str(0) + str(self.minutes) + ":" + str(
                            self.seconds) + " AM"
                else:
                    return str(0) + str(self.hour) + ":" + str(self.minutes) + ":" + str(self.seconds) + " AM"
            return str(self.hour) + ":" + str(self.minutes) + ":" + str(self.seconds) + " AM"