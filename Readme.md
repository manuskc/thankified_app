
# Thankified
![thankified](./resource/logo.png)
Enhance Teamwork and Recognition with Thankified today. Join us in making your workplace more appreciative and productive



## App features
Simple slack plugin to thank someone

* User thanks someone - "Thank you @someone" 
* The app detects the event
* User gets a prompt to send a virtual gift for the help they received
* The gift helps track the kind of sipport provided (helped me, helped my team, solved a customer issue or above and beyond)
* The app keeps track of all the great work of the team
* One can pull the list of such collaborations by simply sending the command `/thankified`
* The list can be posted as a public message by `/thankified publish`
* One can also create a public profile and share their great work by registering a profile `/thankified profile me@email.com`


## Setup
1. Update config.py with all your production secrets and configurations
2. Define env variables in host box as per config.py
3. Create a slack app and connect appropriate links in app.py to receive envets, reactions and commands
4. Deploy the app on your host box via `./deploy.sh`



To run locally, checkout the code and run:
```
uvicorn main:app --reload
```

   
