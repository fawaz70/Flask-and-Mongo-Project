# OpenHouseAiTest

The code provided is the backend for the problem as requested.
The code uses FastApi (Flask) for REST purposes.

The code can run after install all the requirements as provided in the folder.
The requirements can be installed using pip install -r requirements.txt.
Another requirement would be to have a MongoDB installed on the PC with the connection mongodb://127.0.0.1:27017/ as shown in main.py.

Simply run uvicorn main:app --reload in the folder with main.py to turn on the server

Then open up your browser and go to http://127.0.0.1:8000

There you will see the documentation using FastApi. The POST and GET methods can be tested there

## Follow Up Question
The way to make this cloud scalable would be to have this same code run but on multiple different servers. Since
the code saves it to the same database, it would reduce the overall load of having 1 server into multiple servers.

The code is not deployable ready but it is production ready. Once testing beyond that point is complete then all
we would need to do is deploy it onto AWS for instance.

### If there are any issues running the code or would like me to show how it works, please don't hesitate to email or call

Thank you

Fawaz
