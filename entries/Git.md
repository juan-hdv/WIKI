# Git

Git is a version control tool that can be used to keep track of versions of a software project.

Git keep track of text files, for example: [Python](/wiki/Python), [HTML](/wiki/HTML) and [CSS](/wiki/CSS) files.

## GitHub

[GitHub](https://github.com/) is an online service for hosting git repositories.

**Some useful git commands**
	```
	git clone <url> : take a repository stored on a server (like GitHub) and downloads it
	________
	git checkout <branch name>: se cambia al branch
	________
	git branch: Shows the current branch
	git branch -a: List all branches
	git branch <branch name>: Create a new branch
	git branch -d <branch name> : Deletes a branch
	git branch -D <branch name>: force the deletion of local branch on your filesystem
	________
	git push: push any local changes (commits) to a remote server
	git push origin <branch name>: Push the branch on github
	git push <URL> <branch name>: Push the branch on github on the remote repository <URL>
	________
	git pull : pull any remote changes from a remote server to a local computer
	________
	git add -A: Stage all files recursively
	git add . : stage all files in the current directory, not recursively
	git add <filename(s)> : add files to the staging area to be included in the next commit
	________
	git commit -m "message" : take a snapshot of the repository and save it with a message about the changes
	git commit -am <filename(s)> "message" : add files and commit changes all in one
	________
	git status : print what is currently going on with the repository
	________
	git log : print a history of all the commits that have been made
	git reflog : print a list of all the different references to commits
	________
	git reset --hard <commit> : reset the repository to a given commit
	git reset --hard origin/master : reset the repository to its original state (e.g. the version cloned from GitHub)
	```
