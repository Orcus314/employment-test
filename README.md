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

Note: The Database by default contains 2 of the user records I used for testing, these can be removed if requested

Error Handling:
The major errors that could occur in this system come from users entering non-existant entries and entries being deleted/privated after they are added to the database, as it stands the system will let the user know a push has failed and during the update if a user is no longer accessable the parser will simply skip past it and the data will not be updated. Another point that I would like to do more testing on is input sanitization, from my testing and understanding it shouldn't be possible for the user to send a DROP command to the database, but since that is a frequent flaw in sql systems I would want more testing

Future Improvements
The main improvement I would like to make would be to improve the performance of the parsing function, granted compared to the html waittimes it is fairly minor but I can see a few points that I believe could be improved once I gain a greated understanding of the beautifulsoup library, mainly the for loops.
