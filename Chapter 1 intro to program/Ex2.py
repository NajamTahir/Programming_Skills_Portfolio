"""
chapter 1 Ex2
Write a Python program to get the Python version you are using.
"""
#It will print the version of the python the user is using
import sys
print("python version")
print(sys.version)
print("Version info.")
print(sys.version_info)
"""
1.import sys: This line imports the sys module, which provides access to system-specific parameters and functions, including information about the Python interpreter and environment.

2.print("Python version"): This line is a simple print statement that displays the text "Python version" in the console.

3.print(sys.version): This line prints the Python version, which is retrieved from the sys.version attribute. The sys.version attribute contains a string representing the version of the Python interpreter currently in use. It provides details such as the Python version number and additional information like the build date.

4.print("Version info."): This line is another print statement that displays the text "Version info." in the console.

5.print(sys.version_info): This line prints the Python version information, which is retrieved from the sys.version_info attribute. sys.version_info is a tuple containing details about the Python version, such as the major and minor version numbers, micro version, release level, and serial number.
"""