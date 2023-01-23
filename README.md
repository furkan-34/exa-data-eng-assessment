# Description
Program scans the files are below to the path (data) and inserts them to mongodb database.
Anybody can run the program through python commands or using docker commands.

## How to run?
* Do not forget to activate your virtual environment for python commands
#### Python:
```
pip install -r requirements.txt
python run main.py
```
#### Docker:
```
docker build -t emis-python .
docker run emis-python
```
## Tech Stack
* Programming Language: Python
* Data Layer: MongoDB
* Library: Pandas, Pymongo
