## Telligence Platform

Telligence is a multi-page web app built using python and streamlit and is used for three specific areas: Cybersecurity, Data Science and IT Operations. Users can register and log in, explore and visualise the data stored in an SQLite database.

This project was built for a module at Middlesex University (Year 1). The module involved building the project week by week, starting with establishing a secure login system, followed by database management, CRUD functions, an interactive dashboard and object oriented refactoring.

## Purpose 

Cybersecurity: respond to spikes in phishing attacks and spot workflow issues.

Data Science: manage large datasets and improve their quality.

IT operations: find which staff or steps slow down helpdesk tickets.

## How much is built

- User registration and login
- Passwords hashed with bcrypt (salted), never stored as plain text
- SQLite database for users and dataset metadata
- Dashboard page, available only after logging in. The dashboard includes filter, charts and a data table for exploring datasets

Tech Used
Python, SQLite, Streamlit, pandas, bcrypt

## How to run

1. Clone the repo and open the folder in a terminal
2. Create and activate a virtual environment 
3. Install the packages using: pip install -r requirements.txt
4. Create the database tables using: python app/schema.py
5. Start the app: streamlit run Home.py

## How the login works

- On registration, the password is hashed with a random salt using bcrypt. Only the hash is stored in the database.
- On login, the user is looked up with a parameterised SQL query, and bcrypt compares the typed password with the stored hash
- If the password matches the hash, a flag is stored in streamlit's state. Other pages check that flag and stop if the user is not logged in. 

## Project structure 

Home.py - login and registration 
pages/Dashboard.py - Dashboard (login is required here)
app/users.py - password hashing and user functions
app/datasets.py - database connection  
app/schema.py
DATA/

## How much is built

While the CSV dataset and brief were provided by my module leader, I wrote the login system, the database functions and the dashboard page.

## Not finished yet

- CRUD functions and pages for security incidents and IT tickets. While the sample data is in DATA it is yet to be used.

- Separate dashboards for each of the three domains 

- The optional AI chat assistant which has been removed at this time

- Unit tests for password functions

- Refactoring into classes

The sample in DATA/ is not real.
