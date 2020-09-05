# Create mysql server based on the official image from the dockerhub
FROM mysql
# Add a database & root password

EXPOSE 3306

# optionnaly, run initial scripts for creating tables
COPY ./sql-scripts/ /docker-entrypoint-initdb.d/
