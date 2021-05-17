== birthdays ==  
Python script for terminal users that allows you input birthdays and be reminded of upcoming birthdays in the next 33 days.
Instructions are for BASH shells but it should work with any other shell.
Requires Python3.

I made this for personal use as I do not use a calander but it is free for anyone to download and use under GNU 3 public licence.
(See Licence.txt for more details)


== Installation (BASH) ==  
Make sure you have Python3 installed.
Download to a directory of your choice.
Include the following line at the end of your .bashrc file. Be sure to change it to include the path to the directory containing the birthdays.py script.  
    python3 ~/<path to directory>/birthdays.py
    

== Usage ==  
If you have added the line above to your .bashrc, the program will run automatically every time you open a BASH terminal.
If there are no stored birthdays soon, there will be no output.

To add a birthday to the list, run the script with the -a or --add argument.  
  python3 ./birthdays.py -a
  
After entering valid data you will be asked to confirm your choice.
Make sure this is correct as there is currently no way to remove a birthday outside of opening the birthdays.JSON file and manually removing the entry.

== Arguments ==  
-a --add : add a birthday
-p --print : print all stored birthdays

(Coming soon)
-h --help : User guide
-d --del : Delete a stored birthday.

----------------------------------------------------------------------------------------------------------------------------------------------------------
