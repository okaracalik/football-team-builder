# Football Team Builder

  > A football team builder app for the popular video game.

    - You can search players through this app.
    - You can set budget and tactic, any you'll see best footballers you could play with.

  > [➡️ Demo](https://orkutkaracalik.info/portfolio/football-team-builder/)

## 🚀 Used Technologies

- 🗄️ Backend
  - Python
    - Web server development
  - [MySQL](https://dev.mysql.com/doc/)
  - [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
    - Database ORM to handle MySQL operations
  - [Pandas](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)
    - Pre-processing raw data and developing a team building algorithm
  - [Pulp](https://www.coin-or.org/PuLP/pulp.html)
    - A Linear programming library which is utilized for finding the best lineup
  - Nginx
    - As a proxy servers, it's used for deployment of web app on VPS.

- 🖥️ Frontend
  - [Vue.js](https://vuejs.org/v2/guide/)
    - Building frontend business logic
  - [Quasar](https://quasar.dev/introduction-to-quasar)
    - For user interface components

- 📦 Packaging
  - [Docker](https://www.docker.com/)
    - Packing up the database, backend and frontend and deployment

The app is deployed on [Digital Ocean](https://www.digitalocean.com/).
## ℹ️ Info

- Player photos in web app are not included for this repository due to size.
- Data is taken from the [Kaggle](https://www.kaggle.com/karangadiya/fifa19).

## Installation

- To run whole app on local
  ```bash
    docker-compose up
  ```
  ⚠️ Make sure you provided followings:
    - MySQL credentials in `docker-compose.yml`, `backend/config.json`
    - Certificates in `nginx/ssl/`

- However you just execute followings in `bash` to run locally:

  - 1st terminal:
    - ```bash
      cd backend
      python app.py
      ```
      ⚠️ Make sure you installed: `python` 3.7 and packages in `backend/requirements.txt`.
  - 2nd terminal:
    - ```bash
      cd frontend
      yarn install
      quasar dev
      ```
      ⚠️ Make sure you installed: `node` 10 and `yarn`.