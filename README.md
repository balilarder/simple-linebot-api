# simple-linebot-api


### Commit #1
* Create a empty project


### Commit #2
* Create a vitrual environment for the nesscessary packages: line-bot-sdk, pymongo, flask
* Create a test channel![image](https://hackmd.io/_uploads/S1BqQyqcp.png)
* Generate Line Message API config for the **channel access token** and **channel secret**
* Put my config to the server.py
* use a GET API to test the server![image](https://hackmd.io/_uploads/HJ4mL1996.png)


### Commit #3
* Create a python file `model_setup.py` creating the model object definitioin and the connection to mongodb
* import model_setup in the `server.py`
* You can execute `python model_setup.py` directly to initialize the mongodb by deleting all the documents. 


### Commit #4
* Install ngrok
* `./ngrok http 5000` forward the localhost:5000 to the public endpoint [image]
* Verify the Webhook in Line Developer [image]
* launch the mongodb: `brew services start mongodb-community`
* Send a message and save it. [image]


### Commit #5
* Create a API broadcasting a message to all friends to this channel.
* Use POST method with the message in the request body. [image]


### Commit #6
* Create an API to push_message to a specific user.
* specify the userid in the request body.
* The messages include all user's message stored before and the timestamps. [image]