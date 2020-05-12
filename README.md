# Coronavirus_Flask

## WHAT IS IT
Uses a COVID19 API to compare 2 countries by the number of confirmed coronavirus cases. Most countries available.

Runs on a Flask app in browser.

Returns - Opens a new tab with an interactive HTML Plotly graph.


## HOW TO USE

1 -> Clone corona_virus_flask repository

2 -> Create a virtual environment
python3 -m venv venv/       -Creates an environment called venv/ you can replace “venv/” with a different name for your environment.

3 -> Activate the virtual envrionment
source venv/bin/activate

4 -> Set up and run Flask
export FLASK_APP=main.py
export FLASK_ENV=development
flask run

IF NECCESSARY -> Install requirements
pip freeze > requirements.txt       - Store the current packages in a txt file
pip install -r requirements.txt       - Install the packages from the requirements file


NOTES: when uploading to GitHub remove venv folder as well as __pycache__ (the file that contains the python code compiled for faster running)

![](images/example.png)
