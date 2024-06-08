# Setting up and Testing Basic Postgres infrastructure with Docker

This project tests my ability to successfully setup, load data and interact with postgres from python. 
To do this, i'll be creating a postgres server using docker and docker compose.

## Technologies used
1. Docker - To containerize my application.
2. Git and github - To run my commits and push my work for review.
3. Dbeaver - To connect to my database.

## Steps
1. I created a new local branch which i named "task_1".

*git checkout -b task 1*

2. In my new branch task_1 i created a folder called postgres_docker_init.

*mkdir postgres_docker_init*

3. In the same directory, i created a data folder called "data", in this folder i loaded my csv file "supermarket_sales" using the following command

*mkdir data* - create the data folder
*cp /Users/mac/Downloads/supermarket_sales.csv /Users/mac/DE_Portfolio/Data_Engineering_portfolio/data* - copy the dataset from my computer into the data folder

4. I then created a folder called "infra_setup", in this folder i created an "init.sql" file where i wrote some simple sql syntax to create a new schema, table and load my csv file.

*mkdir infra_setup*
*touch init.sql*

5. I created a docker compose file and  setup up the various credentials i'll need for connection.

*touch docker-compose.yml*

6. I created an src folder, inside it i created a script.py, i then wrote some python code to connect to my postgres database and i executed a query to count the number of records in my table.

*mkdir src*
*touch script.py*

## Spinning up my server
To spin up my server, i started my docker engine then ran the "docker-compose-up" command in the project root folder and this started my postgress service.
I then connected to my database via DBEAVER using the credentials provided in my "docker-compose.yml" file.

## Challenges Encountered
1. I couldn't start my docker engine because i ran into some errors. so all i had to do was to fix the errors i was having in my init.sql file.


