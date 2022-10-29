# Local Crimes Map

A Django project that displays crime data from the data.police.uk RESTful API on a map, and as a report style breakdown. The crime data from the report style breakdown is then saved in a PostGIS.

This project is deployed on [here](https://localcrimesmap.callums-stuff.net/).

## Important Info

This project uses the dj_database_url package to set the database connection in settings.py. This connection string must be specified in a .env file that should be placed in the `localcrimesmap` directory, following the format of the example below.

> DATABASE_URL=postgis://{DBUSERNAME}:{DBPASSWORD}@localhost:{PORT}/{DBNAME}

'SECRETKEY'and 'DJANGODEBUG' must also be set as a string enviroment variables

GDAL must be installed on whatever machine you are running this project on.

## Docker

There is a docker-compose file to launch the two required services for the app (the Django web app, and the postgres database). You'll need to create a .env file within the `/src` directory with the required environment variables for the docker-compose file.

The docker-compose.yaml is specific to its deployment environment, for instance being available in an external network used by a reverse proxy. 

Once deployed, you can run the migrations using:
`docker-compose run localcrimesmap_webapp python manage.py migrate`
