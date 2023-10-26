"""
Chapter 1 Ex 3
Write a Python program to display the current date and time.
"""
#In this program it will show the current date and time.
import datetime
c_datetime = datetime.datetime.now()
f_datetime = c_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:", f_datetime)
"""
1.import datetime: This line imports the datetime module, which provides classes for manipulating dates and times in Python.

2.c_datetime = datetime.datetime.now(): This line creates a datetime object named c_datetime using the datetime.now() method. This object represents the current date and time based on the system's clock.

3.f_datetime = c_datetime.strftime("%Y-%m-%d %H:%M:%S"): This line takes the c_datetime object and formats it into a human-readable string using the strftime() method. In this case, the format string "%Y-%m-%d %H:%M:%S" is used, which represents the date and time components in the following format: "YYYY-MM-DD HH:MM:SS".

4.print("Current Date and Time:", f_datetime): Finally, this line prints the formatted date and time string, along with a descriptive message. The result is a display of the current date and time in a standard format.
"""