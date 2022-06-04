# JSuite
[![Actions Status](https://github.com/JR-prog/JSuite/workflows/Django%20CI/badge.svg)](https://github.com/JR-prog/JSuite/actions)
[![Actions Status](https://github.com/JR-prog/JSuite/workflows/Node.js%20CI/badge.svg)](https://github.com/JR-prog/JSuite/actions)

This is a project where I build my own web application for practice and to beef up my resume. 

### Installation (Dev)
- Clone this repository
- In the jsuite directory (backend), run `pip install -r requirements.txt`
  - In the dependencies (either directly with your python installation or in a venv (highly recommended)), navigate to `/site-packages/graphene_django/utils/utils.py`
  - Replace all instances of "force_text" to "force_str"
- Then, in the jsuite-frontend directory, run `npm install`

### Running (Dev)
- Run `bash jsuite.sh` to start both the backend api and front-end.

or, if you don't have access to bash:
- In the jsuite directory, run `python manage.py runserver 8080`
- In the jsuite-frontend directory, run `npm start`
