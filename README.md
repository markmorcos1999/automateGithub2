# automateGithub2
Python script that automates the process of starting a gitHub project on linux (debian based) distros.  

### Example

`$ construct --private -p repoName`

Command: Name of function in the bash.txt file which can be replaced to other words (currently construct)  
1st parameter: --private/--public creates a private/public repo respectively  
2nd parameter: -p/-j/-c/-cpp creates a "repoName.ext" where ext is py, java, c, cpp + h respectively  
3rd parameter: Github's repository's name  

### Description
  1. Opens chrome, logs in, creates a new public/private "repoName" repository.  
    Note: Login credentials are set in global variables at the top of automateGithub.py  
    Note: ReadMe file is created based on value of README variable at top of automateGithub.py (1 creates README, 0 does not)  
  2. Clones repo into the private/public folder specified in bash file.  
  3. Creates a repoName.ext based on flags in that folder (private/public based on Step2).  
    Note: For cpp files, it creates a .h and a .cpp files  
  4. Opens all files created in default application (repoName.ext)  
  4. Adds, commits, and pushes the folder to the Github repo.  
  
  
### Final Result of Example
  
  .../private(or public)/repoName has:
  README.md
  repoName.py
  
### Requirements
Linux:
 1. Python3 (you can check if python is installed by calling `python3` in the linux shell)
 2. xdg-open
 3. webdriver_manager (you can install by running `pip3 install webdriver_manager` in the shell)
    Note that sudo priviledges might be required.
 4. git and a github account

Windows (coming soon):
To use this repository, make sure chromdriver.exe is installed and the path to that folder is located in the enivronment variables. You have to manually convert location (from windows to linux acceptable location) into the automateGithub.py file.
Selenium python library.

### Instructions
Linux:
  1. Head to the directory where your Github files should be saved.
  2. Create a 'private' and 'public' directories in that folder and navigate to the public folder.
  3. Clone this repository on your linux machine by using `git clone <url-here>`
  4. Python changes:  
       username: "N/A"         --> replace N/A with actual github username  
       password: "N/A"         --> replace N/A with actual github password  
       "/home/mark/Projects/   --> replace with repository to save folders in  

     Bash changes (under "For Linux" header):  
       cd "/home/mark/Projects/" --> replace with cd "<directory that contains private and public directories>"
  5. Save changes
  6. Copy and paste all lines of code under the "For Linux:" header at the end of the .bashrc file located in home directory
    (`cd ~` will get you to the home directory)
    Note if the .bashrc file does not exist, create one and add the bash script to it
  7. run `. .bashrc`
  

### Disclaimer
Bash script runs certain commands as root. Please check the bash and python scripts before running on your local machine. Developer is not responsible for any issues caused by running the scripts.
