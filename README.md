# JSuite
[![Actions Status](https://github.com/Jungle-Software/JSuite/workflows/JSuite%20CI/badge.svg)](https://github.com/Jungle-Software/JSuite/actions)

Everything you need to know is right here https://github.com/Jungle-Software/JSuite/wiki

### Installation
Installing our project has never been easier!
Simply clone and run the following command in the root of the project (this also goes for every other `docker-compose` command in the project):
- `docker-compose up -d --build`
Now, you can access the app by navigating to http://localhost:3000/ in your browser.

In order to access the admin panel, you will need to create a super user in Django. You can do so by running the following command:
- `docker-compose exec django python manage.py createsuperuser` 
and following the prompt.
Then, you can access the admin panel at http://localhost:8080/graphql/admin to perform CRUD (create, read, update and delete) operations on any object/model locally.

For more info, check the wiki. The link is at the top of this README.