# Fat Bear Week API

#### Project aim: a totally unofficial but well-intentioned API to serve data about Katmai National Park's fat bears.

[What is Fat Bear Week?](https://explore.org/fat-bear-week)

This is one of those "can't sleep at 4am" projects, so it may or may not actually go anywhere. 

This project runs Python > 3.8 with Django and Postgres. 

## DB Setup
If you just want to look at the schema, check out the `schema.sql` file in `/database`.

You'll need Postgres if you don't already have it 
```commandline
brew install postgres
```

There is a dumpfile in the `/database` folder which should contain all you need to start messing around with the data. 

Create a database called `fat_bear_week` and restore the dump.
```commandline
createdb fat_bear_week
pg_restore -d fat_bear_week -C database.dump
```
_I'm just noodling around at the moment so I'll come back to users and ownership later_

If there are any DB schema changes, the models will need to be regenerated using 
```commandline
python manage.py inspectdb > fat_bear_week_api/models.py
```
At the moment this change is breaking, because it removes the `related_name` property of some foreign keys - this is an 
issue when one table is linked multiple times as we see in `results` and `brackets`. It also pluralises the models. 
This needs a little manual intervention to fix.

## Run
Make sure you've got a venv up with the requirements installed.
```commandline
pip install -r requirements.txt
```
Make sure you've got your DB connection info in `settings.py/DATABASES`

From there it's just standard Django fare
```commandline
python manage.py runserver  
```

## Endpoints
Current endpoints:
- `/api/bears GET` - all info held about every bear on our books
- `/api/champions GET` - all bears that have won a final round, date of final and basic bear ID

Proposed endpoints:
#### GET
- `/bears/{uuid}`, `/bears/{bear_number}` 
  - all the ID information held about a specific bear
- `/matchups/{year}`
  - a simple bear vs. bear list of matchups and dates for the given year
- `/finalists` 
  - all bears who have made it to the final round with no. instances
- `/rivals` 
  - every bear and their no. 1 rival (the bear that has beat them in a 1-1 the most times)
- `/info/{year}`
  - admin stuff, e.g. no. rounds, participants, start-end dates, winner, no. votes cast

#### POST (stretch goal as these will need to be locked down)
- `/results/{bracket_uuid}`
  - write a result record for a given bracket uuid. 
- `/bears`
  - create/update a bear 


## TODO:
- ~~Decide on a framework~~
  - Fast API (shiny new thing)
  - Flask (I know what I'm doing)
  - Django (would be a useful learning experience)
- Actually learn some DevOps so I know how this ends
- ~~Outline some useful endpoints~~

