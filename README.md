# Unlimited-Treasures
This project is for DBMS 578

## Feature Branches
When adding to this repo the branch file should use the following format
from master branch run the following
<code>git checkout -b {ticket_number}-{ticket_name}-{ticket_name}</code>

## local setup
## Pre requisite
Install python3
Install virtualenv for [python3](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)
## run local server
1. set SECRET_KEY in the base.py or secret.txt file (this file is in gitignore and will not be in version control) 
source secret.txt file ( this file is one line and should have the following:
<code>export SECRET_KEY='{your key here}'</code>
2. Activate virtual env 
<code> source venv/bin/activate</code>

3. git clone Unlimited-Treasures repo and cd into the repo dir
4. <code> pip3 install -r requirements.txt </code>
the above command will install all of the needed packages to run your app locally
5. cd to mysite folder
6. python3 manage.py runserver
Run <code>python3 manage.py runserver</code>
7. Create mysql database and tables
    -  <code>python3 manage.py makemigrations mysite </code>
    -  <code>python3 manage.py migrate</code>
