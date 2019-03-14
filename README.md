# CSC336_Project

### Setting up development environment
Tools:  
1. Docker
2. Docker-Compose
3. IDE

#### Setting up PostGres:
1. Make sure you have docker and docker-compose installed. Check by typing `docker-compose` in your console.
    * If on a linux, you can run `tools/docker-ce.sh` to automate docker-compose install
2. Run `docker-compose up` to see if it works.
3. To run database in the background, run `docker-compose up -d`

#### Cleaning up development:
1. If you're done with the development and would like to clean up, run `docker-compose down --rmi 'all'`  
    * This cleans up the docker container entirely. The `postgres-data` folder preserves all the files so you can remove this entirely.
