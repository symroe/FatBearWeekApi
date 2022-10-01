# Fat Bear Week API

#### Project aim: a totally unofficial but well-intentioned API to serve data about Katmai National Park's fat bears.

[What is Fat Bear Week?](https://explore.org/fat-bear-week)

This is one of those "can't sleep at 4am" projects, so it may or may not actually go anywhere. 

This project will use Python > 3.8 and Postgres. The rest is TBD.

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

## TODO:
- Decide on a framework
  - Fast API (shiny new thing)
  - Flask (I know what I'm doing)
  - Django (would be a useful learning experience)
- Actually learn some DevOps so I know how this ends
- Outline some useful endpoints

