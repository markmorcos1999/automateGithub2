from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import os
import subprocess

### global variables
username = 'N/A'
password = 'N/A'
READ_ME = 1

open_command = [
    'xdg-open',
    '/home/mark/Projects'
]

linux_selected = 1
git_website = webdriver.Chrome(ChromeDriverManager().install())
repo_name = sys.argv[3]

### helper functions
def create_and_open_file(repo_name, extension, open_string):
    os.system('touch {0}.{1}'.format(repo_name, extension))
    subprocess.call('{0}'.format(open_string), shell=True)
    
def prepare_file(extension):
        if(linux_selected):
            command = "{0} {1}/{2}/{3}/{4}.{5}".format(open_command[0], open_command[1], sys.argv[1][2:], repo_name, repo_name, extension)
        else:
            command = "{0} {1} '{2}//{3}//{4}//{5}.{6}'".format(open_command[0], open_command[1], open_command[2], 
            sys.argv[1][2:], repo_name, repo_name, extension)
        create_and_open_file(repo_name, extension,  command)

### scraping functions
def start_chrome():
    # Open git_website
    git_website.get('https://github.com')

    git_website.maximize_window()

def login():
    # click sign in button
    signin_button = git_website.find_element_by_xpath('//a[contains(@href, "/login")]').click()

    # ---------Input username and password----------
    login_field = git_website.find_element_by_id('login_field')
    login_password = git_website.find_element_by_id('password')

    login_field.send_keys(username)
    login_password.send_keys(password)

    # Click on login/sign in
    git_website.find_element_by_name('commit').click()

def create_repo():
    #new_repo_button
    git_website.find_element_by_xpath('//*[@id=\"repos-container\"]/h2/a').click()
    repo_field = git_website.find_element_by_xpath('//*[@id=\"repository_name\"]')

    # type in repository's name
    repo_field.send_keys(sys.argv[3])
    if sys.argv[1] == '--private':
        private_button = git_website.find_element_by_xpath('//*[@id=\"repository_visibility_private\"]')
        private_button.click()
    
    if READ_ME:
        git_website.find_element_by_xpath('//*[@id=\"repository_auto_init\"]').click()

    time.sleep(1)

    # Create repo  //*[@id="new_repository"]/div[6]/button
    git_website.find_element_by_xpath('//*[@id=\"new_repository\"]/div[6]/button').click()

    time.sleep(4)

def clone_repo():

    os.system("git clone {0}{1}".format(git_website.current_url, '.git'))

    time.sleep(2)
    git_website.close()

def create_local_file():
    os.chdir("{0}".format(repo_name))

    extension = ''
    extension2 = ''
    command = ''

    if sys.argv[2] == '-p':
        extension = 'py'

    elif sys.argv[2] == '-j':
        extension = 'java'

    elif sys.argv[2] == '-c':
        extension = 'c'

    elif sys.argv[2] == '-cpp':
        extension = 'cpp'
        extension2 = 'h'

    elif sys.argv[2] == '-cs':
        extension = 'cs'

    #create header file for cpp
    if extension2 == "h":
        prepare_file(extension2)

    #create main file
    prepare_file(extension)

def push_repo():
    time.sleep(1)
    os.system('git add .')
    os.system('git commit -m \"Initial commit\"')
    os.system('git push')
    print('after os')

### Main logic
def main():
    start_chrome()
    login()
    create_repo()
    clone_repo()
    create_local_file()
    push_repo()

main()