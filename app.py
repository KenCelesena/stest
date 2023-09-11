# FILL YOUR GITHUB HISTORY
# How to create a repo?
        # Log into your a github account 
        # create a new public repo
        # clone it to your computer and enter into it
        # copy this file app.py into it
# set SSH permission
# run code


import os
from random import randint
from datetime import datetime, timedelta

# variables for commits
username = 'KenCelesena'
email = 'ken.celesena@gmail.com'
startDaysAgo = 321
endDaysAgo = 3
minCommitsPerDay = 0
maxCommitsPerDay = 1

# Get today's date
today = datetime.now()

os.system(f'git config user.name {username}')
os.system(f'git config user.email {email}')

# can do this manually instead
os.system('git add app.py')
os.system('git add pycode/app.py')

for i in range(endDaysAgo, startDaysAgo):
    mydate = today - timedelta(days=i)
    # formated = mydate.isoformat()
    formated = mydate.strftime('%Y-%m-%dT%H:%M:%S')
    # formated = formated[:21]

    print(formated)

    for j in range(0, randint(minCommitsPerDay, maxCommitsPerDay)):
        d = str(i) + ' days and '+ str(j)+' commits'
        with open('file.txt', 'w') as file:
                file.write(d)
        os.system('git add .')
        
        cmd = f'GIT_AUTHOR_DATE={formated} GIT_COMMITTER_DATE={formated} git commit --author="{username} <{email}>" -m "{formated}"'
        os.system(cmd)        

os.system('git push -u origin main')
