import subprocess
from time import sleep


def first_repo_push(push_link):
    subprocess.run('git init')
    subprocess.run('git config --global user.name "deepu1067"')
    subprocess.run('git config --global user.email "dshahadat10@gmail.com"')
    sleep(2)
    subprocess.run('git add .')
    subprocess.run('git status')
    sleep(5)
    subprocess.run('git commit -m "First commit"')
    sleep(3)
    subprocess.run('git remote add origin {}'.format(push_link))
    subprocess.run('git push -u origin master')


def file_update_push(commit_comment):
    subprocess.run('git status')
    sleep(2)
    subprocess.run('git add .')
    sleep(2)
    subprocess.run('git commit -m "{}"'.format(commit_comment))
    sleep(2)
    subprocess.run('git push -u origin master')


while True:
    print('''
    Press 1 to push your files to github for the first time
    Press 2 to push your files to your repo
    Press 3 to quit
    '''
          )
    choice = input("Enter choice:")
    if choice == '1':
        link = input("Enter the repo link: ")
        first_repo_push(link)
    elif choice == '2':
        comment = input("Enter you commit comment: ")
        file_update_push(comment)
    elif choice == '3':
        print("Thanks for your choice. Have a nice day")
        break
