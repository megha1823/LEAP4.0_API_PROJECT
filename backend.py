#Date: 08-07-2021
#Created by: Megha.N

from github import Github
g = Github('access token')

#fetching the repositories for an organization
org = g.get_organization('')
repos = org.get_repos()
repos_id_lsit=[]
for repo in repos:
	repos_id_lsit.append(repo.id)

#fetching collaborators for a repository
collaborators = repo.get_collaborators()
collaborators_list = []
for collaborator in collaborators:
	collaborators_list.append(collaborator)

#fetching commits on a repository
commits = repo.get_commits()
commits_list = []
for commit in commits:
	commits_list.append(commit.sha)

#Get a single commit
commit = repo.get_commit(commits_list[0])


#Get contributors to a repo
contributors = repo.get_contributors()


#Get events for a repository
events = repo.get_events()

#Get forks for a repository
forks = repo.get_forks()

#Get readme of a repo
readme = repo.get_readme()

#Get commit activity stats for a repo
commit_activity = repo.get_stats_commit_activity()

#getting contributors statistics for a repository
contributors_stats = repo.get_stats_contributors()
