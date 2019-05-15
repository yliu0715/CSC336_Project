# CSC336_Project

### Setting up development environment
Tools:  
1. ~~Docker~~
2. ~~Docker-Compose~~
3. IDE

#### UPDATE [5/2019]:
1. Database is now hosted on GCloud. DO NOT USE THE KEYS OR THE DATABASE FOR ANYTHING SECURE!!!

#### ~~Setting up the Database:~~
1. ~~Make sure you have docker and docker-compose installed. Check by typing `docker-compose` in your console.~~
    * ~~If on a linux, you can run `tools/docker-ce.sh` to automate docker-compose install~~
2. ~~Run `docker-compose up --build` to see if it works.~~
3. ~~To run database in the background, run `docker-compose up --build -d`~~

#### Setting up server:
1. Install virtualenv: `pip install virtualenv`
1. Create environment: `virtualenv venv`
1. Switch environment: 
    * Windows: `venv\Scripts\activate` 
    * Mac: `source venv/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Run server: `python app/app.py`

#### Running sample:
1. Install mysql connector: `pip install mysql-connector`
2. `python app/populate.py init`
3. `python app/populate.py create`
4. `python app/populate.py query`

#### ~~Cleaning up development:~~
1. ~~If you're done with the development and would like to clean up, run `docker-compose down --rmi 'all'`~~  

### Warning!
Any sensitive data such as password and configuration settings are solely for testing. Do not use this for an actual product since its not intended to be.
