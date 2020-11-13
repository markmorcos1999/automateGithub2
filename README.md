# automateGithub
Python script that automates the process of starting a gitHub project on windows using a linux shell. 

### Example1: 

_~$ construct --private -p repoName_

Command: Name of function in the bash.txt file which can be replaced to other words (currently construct)
1st parameter: --private/--public creates a private/public repo respectively
2nd parameter: -p/-j/-c/-cpp creates a "repoName.ext" where ext is py, java, c, cpp + h respectively
3rd parameter: Github's repository's name

### The program:
  1. Opens chrome, logs in, creates a new public/private "repoName" repository.
    Note: Login credentials are set in global variables at the top of automateGithub.py
    Note: ReadMe file is created based on value of README variable at top of automateGithub.py (1 creates README, 0 does not)
  2. Clones repo into the private/public folder specified in bash file.
  3. Creates a repoName.ext based on flags in that folder (private/public based on Step2).
    Note: For cpp files, it creates a .h and a .cpp files
  4. Opens all files created in default application (repoName.ext)
  4. Adds, commits, and pushes the folder to the Github repo.
  
  
### Final Result of Example1:
  
  .../private/repoName has:
  README.md
  repoName.py
  
### Requirements:

To use this repository, make sure chromdriver.exe is installed and the path to that folder is located in the enivronment variables. You have to manually convert location (from windows to linux acceptable location) into the automateGithub.py file.
Selenium python library.

