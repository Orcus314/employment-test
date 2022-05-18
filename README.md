# employment-test

Hi Chris et al.

To initiate the system use the following command

docker-compose run -p 8080:8080 server

And to interact with the database and scraper, the following http requests have function

http://localhost:8080/pullall - Pulls a list containing all ID's in the database
http://localhost:8080/pull/{x} - Pulls the stored data associated with {x} (don't include brackets), note should be the UTF-8 encoding and is case sensitive

![image](https://user-images.githubusercontent.com/64340932/169168464-e0109902-9be2-4cf4-b33c-c762d397c7e8.png)

http://localhost:8080/push/{x} - Scrapes the data associated {x} (don't include brackets), note should be the UTF-8 encoding and is case sensitive

![image](https://user-images.githubusercontent.com/64340932/169168498-0f701cc9-5f0d-47ce-a5cf-869d068e3410.png)

http://localhost:8080/update - Manually forces the system to use the update command, updating all records

