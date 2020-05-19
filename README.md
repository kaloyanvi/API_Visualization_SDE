# Students commit input - Software Development

This repository focuses on scraping data from the repositories of students who are following Software Development course at the TU/e. The scraped data is used to make a visualization dashboard with JavaScript's D3 library, which can be found in an ObserveableHQ notebook here:

The code in this repository requires GitHub login credentials which are stored in scripts/credentials.py. In order to make it work, you'll need a two functions in this file:
1. username() which returns your username as a string
2. password() which returns your password as a string

The obtained data is for one of the assignments in which they need to work in pairs and use version control. Thus, the focus of this dashboard is to show the commits distribution over time for all students and for specific pairs, this way if unproportionate amount of work is done by only one member will be noticed faster and easier. Nevertheless, commits are of course not necessarily the best measure of work given the fact that some students make many small commits while other students make just a few larger commits.