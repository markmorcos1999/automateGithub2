from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import os
import subprocess

username = "N/A"
password = "N/A"
READ_ME = 0

open_command = [
    ""
]

linux_open_command = [
    "xdg-open",
    "/home/mark/Projects"
]

windows_open_command = [
    "\"/mnt/c/Windows/System32/cmd.exe\"",
    "/C",
    "start C://Users//markm//OneDrive//Desktop//PersonalProjects"
]

def create_and_open_file(repo_name, extension, open_string):
    os.system("touch {0}.{1}".format(repo_name, extension))
    subprocess.call("{0}".format(open_string), shell=True)

os_version = subprocess.run(["cat", "/proc/version"], stdout=subprocess.PIPE)

linux_selected = 0

if('Linux' in os_version.stdout.decode('utf-8')):
    open_command = linux_open_command
    linux_selected = 1
else:
    open_command = windows_open_command

# For running on terminal, set path for linux shell
git_website = webdriver.Chrome(ChromeDriverManager().install())

# For running on PyCharm, set path for windows command prompt
# git_website = webdriver.Chrome('C:/Users/markm/OneDrive/Desktop/PersonalProjects/chromedriver.exe')

# Open git_website
git_website.get("https://github.com")

git_website.maximize_window()

# click sign in button
signin_button = git_website.find_element_by_xpath('//a[contains(@href, "/login")]').click()

# ---------Input username and password----------
login_field = git_website.find_element_by_id("login_field")
login_password = git_website.find_element_by_id("password")

login_field.send_keys(username)
login_password.send_keys(password)

# Click on login/sign in
git_website.find_element_by_name("commit").click()

# click on new button (for new repo)
new = git_website.find_element_by_xpath("//*[@id=\"repos-container\"]/h2/a").click()

print(sys.argv)

repo_field = git_website.find_element_by_xpath("//*[@id=\"repository_name\"]")
# this represents location, --private/--public, -p/-j/-c, name

# type in repository's name
repo_field.send_keys(sys.argv[3])
repo_name = sys.argv[3]
if sys.argv[1] == '--private':
    private_button = git_website.find_element_by_xpath("//*[@id=\"repository_visibility_private\"]")
    private_button.click()

if READ_ME:
    git_website.find_element_by_xpath("//*[@id=\"repository_auto_init\"]").click()

time.sleep(1)

# Create repo  //*[@id="new_repository"]/div[6]/button
git_website.find_element_by_xpath("//*[@id=\"new_repository\"]/div[6]/button").click()

# press on clone
if(READ_ME):
     git_website.find_element_by_xpath(
    "//*[@id=\"js-repo-pjax-container\"]/div[3]/div/div[3]/span/get-repo-controller/details/summary").click()

#//*[@id="empty-setup-clone-url"]
url_field = git_website.find_element_by_xpath("//*[@id=\"empty-setup-clone-url\"]")

print(url_field.get_attribute("value"))

os.system("git clone {0}".format(url_field.get_attribute("value")))

time.sleep(2)

git_website.close()

os.chdir("{0}".format(repo_name))

extension = ""
extension2 = ""
command = ""

if sys.argv[2] == '-p':
    extension = "py"

elif sys.argv[2] == '-j':
    extension = "java"

elif sys.argv[2] == '-c':
    extension = "c"

elif sys.argv[2] == '-cpp':
    extension = "cpp"
    extension2 = "h"

elif sys.argv[2] == '-cs':
    extension = "cs"

#create header file for cpp
if extension2 == "h":
    if(linux_selected):
        command = "{0} {1}/{2}/{3}/{4}.{5}".format(open_command[0], open_command[1], sys.argv[1][2:], repo_name, repo_name, extension2)
    else:
        command = "{0} {1} '{2}//{3}//{4}//{5}.{6}'".format(open_command[0], open_command[1], open_command[2], 
        sys.argv[1][2:], repo_name, repo_name, extension2)
    create_and_open_file(repo_name, extension2,  command)

#create main file
if(linux_selected):
    command = "{0} {1}/{2}/{3}/{4}.{5}".format(open_command[0], open_command[1], sys.argv[1][2:], repo_name, repo_name, extension)
else:
    command = "{0} {1} '{2}//{3}//{4}//{5}.{6}'".format(open_command[0], open_command[1], open_command[2], 
    sys.argv[1][2:], repo_name, repo_name, extension)

create_and_open_file(repo_name, extension,  command)

time.sleep(1)
os.system("git add .")
os.system("git commit -m \"Initial commit\"")
os.system("git push")
print("after os")
