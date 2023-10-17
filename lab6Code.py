data = yaml.safe_load(open('crai0263-credentials.yml'))

user = data ['creds']['username']
token = data ['creds']['token']

g = Github(token)

repo = get_repo(f"{user}/gitrepos")

branch = 0
pulls = 0
commit = 0

for _ in repo.get_branch():
    branch += 1

for _ in repo.get_pulls(state='all'):
    pulls += 1

default_branch = repo.get_branch(repo.default_branch)
for _ in repo.get_commits(default_branch.commit.sha)
    commit += 1

print(f"There are {branch} branches")
print(f"There are {pulls} pulls")
print(f"There are {commit} commit")