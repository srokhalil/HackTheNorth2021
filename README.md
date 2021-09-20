# Worklax
### Introduction:
This app takes in your weekly work schedule and time availability, and provides you with an activity filled schedule.
The activities are based on user preference.

The app is designed to work on [Google Cloud](https://cloud.google.com/gcp?utm_source=google&utm_medium=cpc&utm_campaign=na-CA-test-all-en-dr-bkws-all-all-trial-e-dr-1009892&utm_content=text-ad-none-any-DEV_c-CRE_491349600625-ADGP_Desk%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20Storage%20~%20Cloud%20Storage_Cloud-KWID_43700064423315754-kwd-26415313501&utm_term=KW_google%20cloud%20platform-ST_google%20cloud%20platform&gclid=Cj0KCQjwv5uKBhD6ARIsAGv9a-yk4xIpD3_jx-9HJ2wgm9dwjZdOKpuEn5idfEKt8D6B_ve0TF-GPRoaAkSAEALw_wcB&gclsrc=aw.ds), specifically using the following tools:
* Secrets Manager
* Google Cloud SQL
* Google APP Engine

The app is currently hosted [here](https://htn2021-c2360.ue.r.appspot.com/).

### Components:
The app consists of a Flask+Python supported Backend and React+NodeJS Frontend.
It is structured to support deployment through
```
gcloud app deploy
```

### Contributors: 
* [Suha Khalil](https://github.com/srokhalil)
* [Amrit Sehgal](https://github.com/amrits1)
* [Zhuo En Chua](https://github.com/ze-2)
* [Sharon Xiao](https://github.com/sharxiao)

 
### Dev Notes
this runs on google clound but you could run locally by commenting out the:

[*main.py*](./main.py#L12-L15)
```
@app.before_first_request
def init_db():
    db.create_tables()
```
and [*python.py*](./python/app.py#L13-L14)
```
if body.get(CONTRACT.get("PERSONAL")):
            add_user(body.get(CONTRACT.get("PERSONAL")))
```

Then install Node modules for React (Front End) and pip files for Flask (Back End):
```
npm i
# activate venv
python3 -m venv .
source ./bin/activate
pip3 install -r requirements.txt
```

Then run Flask server:
```
# FLASK_DEBUG 1 allows server to be redeployed on updates to files
env FLASK_APP=main.py FLASK_DEBUG=1 flask run
```
