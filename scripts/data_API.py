import pandas as pd
import datetime as dt
from github import Github

def commitSize(commit): 
 
    commit_files = commit.files  # all files affected by the commit
    commit_additions = 0
    commit_deletions = 0

    for one_file in commit_files:

        if one_file.filename[-3:] == '.py':
            
            commit_additions += one_file.additions
            commit_deletions += one_file.deletions

    return [commit_additions, commit_deletions]


def dataAPI(repos):

    ha_1 = '2is50-2019-2020-homework-assignment-1-pair-'  # repos to filter for;
    staff_ids = ['sakce', 'kvidelov', 'mackees', 'sakehl', 'thatmariia', 'wstomv', 'sansteTUe', 'HDylanTV', 'gzwaan', 'dmarinissen']

    pair_numb = []
    authors = []
    emails = []
    date_time = []
    commit_messages = []
    additions = []
    deletions = []

    count = 0  # counter to indicated progress

    for repo in repos: # iterating over all repositories associated with the login account

        if 'with-ta' in repo.name:
            pass

        elif ha_1 in repo.name:  # filtering only the assignment repos

            pair_id = int(str(repo.name)[len(ha_1):])  # getting the pair number from the repository name
            repo_commits = repo.get_commits()  # iterable that contains the logs of each commit in the repo
            
            for commit in repo_commits:  
                
                commit_date = commit.commit.author.date.date()  # getting the date and time of the commit
                commit_size =commitSize(commit)

                if commit.author == None:  # checking whether the account is anonymous

                    author = 'Anonymous'
                    pair_numb.append(pair_id)
                    date_time.append(commit_date)
                    authors.append(author)  # author username
                    emails.append(commit.commit.author.email)  # author email
                    commit_messages.append(commit.commit.message)  # commit message 
                    additions.append(commit_size[0])
                    deletions.append(commit_size[1])

                elif commit.author.login not in staff_ids:  # optimal case when the commit is by student

                    pair_numb.append(pair_id)
                    date_time.append(commit_date)
                    authors.append(commit.author.login)  # author username
                    emails.append(commit.commit.author.email)  # author email
                    commit_messages.append(commit.commit.message)  # commit message 
                    additions.append(commit_size[0])
                    deletions.append(commit_size[1])

                elif commit.author.login in staff_ids:  # staff commits
                    pass
            
                else:  # everything else that may be unaccounter for
                    print('Issue!')
                    print(commit_date, 'Pair: ', pair_id, 'Username: ', commit.author.login)

            count += 1
            print(count)

        else:  # not an assignment repository
            pass



    api_data = {'Pair': pair_numb, 'Author': authors, 'Author_Email': emails, 'Date': date_time, 'Additions': additions, 'Deletions': deletions, 'Commit_Message': commit_messages}

    return api_data