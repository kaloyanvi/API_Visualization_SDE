# Visualization Dashboard - Software Development for Engineers

I made this visualization dashboard as a support tool for a course I am a teaching assistant. The repository focuses on getting data from the repositories of students who are following Software Development course at the Eindhoven University of Technology. The obtained data is used to make a visualization dashboard with JavaScript's D3 library, which can be found in this [ObserveableHQ notebook](https://observablehq.com/d/2eccff7de8a6b7e1). All the code regarding the visualizations can also be found in the notebook.

The assignments of the course focus on making a small applications in Python using the Tkinter library and all students must use version control. The students work in pairs of two for the two assignments, which makes the commits in their repositories a reasonable quantitive measure of input by each pair member.

The general purpose of this visualization dashboard is to come as a support tool for the teachers and assistants of the course. It provides overview of how the pair members are splitting their work, how much they are working and on some level whether or not everything is going according to plan for each pair.

## Setup

The code in this repository requires GitHub login credentials which are stored in **scripts/credentials.py**. This file is in _.gitignore_ for security purposes, so in order to make it work, you'll need to create the file and make the two functions needed for the authentication:

1. username() which returns your GitHub username as a string
2. password() which returns your GitHub password as a string

To avoid any package dependencies, using a virtual environment is recommended. You can install all libraries required for this project from the **requirements.txt** file, this can be done by typing and executing in the terminal (need to be at the root directory of this repository) the following:

**pip install -r requirements.txt**

## Data

The obtained data is for both of the assignments of the students in which they need to work in pairs and use version control to develop a small application. The file **scripts/data_API.py** is the one which gets the data from the API. The data is focused around each commit of all student repositories and contains pair number, commit author, author email, date of the commit, added lines, deleted lines, and commit message.

All the data aggregation needed is done in the **scripts/make_datasets.ipynb** file. Since there are 2 datasets used for each assignment, this file has to be executed twice with the correct assignment names adjusted before executing. The data is saved as .csv files in the **data/** folder, for privacy reasons, the obtained data that is used in the visualization dashboard is not included here.

The obtained **.csv** files are embedded in the ObserveableHQ notebook but can be changed or updated if needed.