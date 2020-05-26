# Students commit input - Software Development

This repository focuses on getting data from the repositories of students who are following Software Development course at the TU/e. The scraped data is used to make a visualization dashboard with JavaScript's D3 library, which can be found in an ObserveableHQ notebook here: NOT INCLUDED FOR NOW

## Setup

The code in this repository requires GitHub login credentials which are stored in **_scripts/credentials.py_**. This file is in _.gitignore_ for security purposes, so in order to make it work, you'll need two create the file and make the functions needed for authentication:

1. username() which returns your username as a string
2. password() which returns your password as a string

To avoid any dependencies, use a virtual environment and install all libraries from the **requirements.txt** file. You can do that by typing in the terminal (need to be at the root directory of this repository):

**pip install -r requirements.txt**

## Data

The obtained data is for one of the assignments of the students in which they need to work in pairs and use version control to develop a small application. Thus, the focus of the dashboard is to show the commits distribution over time for all students and for specific pairs, this way if unproportional amount of work is done by only one member, it will be noticed faster and easier. Nevertheless, commits are of course not necessarily the best measure of work given the fact that some students make many small commits while other students make just a few larger commits.