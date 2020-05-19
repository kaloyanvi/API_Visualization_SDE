import pandas as pd
import datetime as dt
from github import Github


def scrapeAPI(repos):

    ha_1 = '2is50-2019-2020-homework-assignment-1-pair-'  # repos to filter for; 
    ha_len = len('2is50-2019-2020-homework-assignment-1-')  # will be used for retrieving pair# by indexing
    staff_ids = ['sakce', 'kvidelov', 'mackees', 'sakehl', 'thatmariia', 'wstomv', 'sansteTUe', 'HDylanTV', 'gzwaan', 'dmarinissen']

    pair_numb = []
    authors = []
    emails = []
    date_time = []
    commit_messages = []

    for repo in repos: # iterating over all repositories associated with the login account

        if 'with-ta' in repo.name:
            pass

        elif ha_1 in repo.name:  # filtering only the assignment repos

            pair_id = int(str(repo.name)[len(ha_1):])  # getting the pair number from the repository name
            
            commits = repo.get_commits()  # iterable that contains the logs of each commit in the repo
            
            for commit in commits:  
                
                commit_date = commit.commit.author.date.date()  # getting the date and time of the commit
    

                if commit.author == None:  # checking whether the account is anonymous

                    author = 'Anonymous'

                    pair_numb.append(pair_id)
                    date_time.append(commit_date)
                    authors.append(author)  # author username
                    emails.append(commit.commit.author.email)  # author email
                    commit_messages.append(commit.commit.message)  # commit message 

                    #print(commit_date, ' Anonymous commit - Pair: ', pair_id)

                elif commit.author.login not in staff_ids:  # optimal case when the commit is by student


                    pair_numb.append(pair_id)
                    date_time.append(commit_date)
                    authors.append(commit.author.login)  # author username
                    emails.append(commit.commit.author.email)  # author email
                    commit_messages.append(commit.commit.message)  # commit message 

                
                elif commit.author.login in staff_ids:  # staff commits
                    pass
            

                else:  # for anything weird that I may not be taking into account
                    print('Issue!')
                    print(commit_date, 'Pair: ', pair_id, 'Username: ', commit.author.login)


        else:  # not an assignment repository
            pass

    api_data = {'Pair': pair_numb, 'Author': authors, 'Author_Email': emails, 'Date': date_time, 'Commit_Message': commit_messages}

    return api_data