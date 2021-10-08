## Getting Started
_________
### About Version Control
Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.
1. Local Version Control Systems（VCS）  
A simple database that kept all the changes to files under revision control.
2. Centralized Version Control Systems（CVCS）  
Shared repository.
3. Distributed Version Control Systems（DVCS）  
Clients fully mirror the repository,including its full history.

### What is Git
1. Snapshots   
Git thinks of its data more like a series of snapshots of a miniature filesystem. With Git, every time you commit, or save the state of your project, Git basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot. To be efficient, if files have not changed, Git doesn’t store the file again, just a link to the previous identical file it has already stored. Git thinks about its data more like a stream of snapshots.   
2. Nearly Every Operation Is Local  
Most operations in Git need only local files and resources to operate.
3. Git Has Integrity  
Everything in Git is checksummed before it is stored and is then referred to by that checksum.
4. Git Generally Only Adds Data  
5. **The Three States**
   - modified:you have changed the file but not committed it to your database yet.
   - staged:you have marked a modified file in its current version to go into your next commit snapshot.
   - committed:the data is safely stored in your local database.
6. The Command Line  

### Installing Git
1. Installing on Windows  
[Git for Windows](https://git-scm.com/download/win)
2. Customizing your Git environment
   - [path]/etc/gitconfig file:git config --system
   - ~/.gitconfig file:git config --global
   - config file in the Git directory:git config --local   
  
    You can view all of your settings and where they are coming from using:  
    `git config --list --show-origin`  
3. Your Identity  
The first thing you should do when you install Git is to set your user name and email address. This is important because every Git commit uses this information, and it’s immutably baked into the commits you start creating:  
`git config --global user.name "name"`  
`git config --global user.email name@example.com`  
4. Your Editor  
Now that your identity is set up, you can configure the default text editor that will be used when Git needs you to type in a message.
`git config --global core.editor notepad`
5. Yourd default branch name  
By default Git will create a branch called master when you create a new repository.But you can set a different name for the initial branch.
`git config --global init.defaultBranch main`
6. Checking your settings  
You can list all the settings or each unique key:  
`git config --list`  
`git config core.editor`
7. Getting help  
If you ever need help while using Git, there are three equivalent ways to get the comprehensive manual page (manpage) help for any of the Git commands:  
`git help <verb>`  
`git <verb> --help`  
`man git-<verb>`  
You also can ask for the more concise “help” output with the -h option:  
`git <verb> -h`

## Git Basics
_____________
### Getting a Git Repository
1. Initializing a Repository in an existing Director  
First，you need to go to that project’s directory and type:  
`cd D:/Your Directory`  
`git init`  
This creates a new subdirectory named .git that contains all of your necessary repository files — a Git repository skeleton. At this point, nothing in your project is tracked yet.  
If you want to start version-controlling existing files (as opposed to an empty directory), you should probably begin tracking those files and do an initial commit. You can accomplish that with a few *git add* commands that specify the files you want to track, followed by a git commit:  
`git add files`  
`git commit -m 'Initial project version'`
2. Cloning an existing Repository
If you want to get a copy of an existing Git repository, the command you need is git clone.Git receives a full copy of nearly all data that the server has.  
`git clone https://github.com/libgit2/libgit2 your-directory`  

### Recording Changes to the Repository
Each file in your working directory can be in one of two states: tracked or untracked. Tracked files are files that Git knows about.Untracked files are everything else.  
![Git Stages](Image\git-figure2.png)
![The lifecycle of the status of your files](image\Git-figure1.png)

1. Checking the Status of Your Files  
The main tool you use to determine which files are in which state is the *git status* command.  
`git status`  
2. Tracking New Files  
In order to begin tracking a new file, you use the command *git add*.   The command takes a path name for either a file or a directory; if it’s a directory, the command adds all the files in that directory recursively.  
`git add new-files`
3. Staging Modified Files  
You can run the *git add* command to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved.  
`git add modified-files`
4. Ignoring Files  
Often, you’ll have a class of files that you don’t want Git to automatically add or even show you as being untracked. In such cases, you can create a file listing patterns to match them named *.gitignore*.
5. Viewing Your Staged and Unstaged Changes  
If you want to know exactly what you changed, not just which files were changed — you can use the *git diff* command.
6. Committing Your Change  
You can commit your changes by using the command *git commit*. You can type your commit message inline with the commit command by specifying it after a *-m* flag.  Remember that the commit records the snapshot you set up in your staging area. Anything you didn’t stage is still sitting there modified; you can do another commit to add it to your history. Every time you perform a commit, you’re recording a snapshot of your project that you can revert to or compare to later.   
`git commit`  
7. Skipping the Staging Area  
If you want to skip the staging area, Git provides a simple shortcut. Adding the *-a* option to the *git commit* command makes Git automatically stage every file that is already tracked before doing the commit, letting you skip the *git add* part.  
`git commit -a`  
8. Removing Files  
To remove a file from Git, you have to remove it from your tracked files (more accurately, remove it from your staging area) and then commit.The *git rm* command does that, and also removes the file from your working directory so you don’t see it as an untracked file the next time around.  
`git rm`
9. Moving Files  
If you want to rename a file in Git, you can run the *git mv* command.  
`git mv file_from file_to`  
10. Viewing the Commit History  
After you have created several commits, or if you have cloned a repository with an existing commit history, you’ll probably want to look back to see what has happened. The most basic and powerful tool to do this is the git log command.  
`git log`  
11. Limiting Log Output  
 In fact, you can do *-<n>*, where n is any integer to show the last n commits.In addtion, the time-limiting options such as *--since* and *--until* are very useful. The *--author* option allows you to filter on a specific author, and the *--grep* option lets you search for keywords in the commit messages.  
 `git log --para`
 12. Undoing Things  
One of the common undos takes place when you commit too early and possibly forget to add some files, or you mess up your commit message. If you want to redo that commit, make the additional changes you forgot, stage them, and commit again using the *--amend* option.  
`git commit --amend`   
13. Unstaging a Staged File  
`git reset HEAD <files>`
14. Unmodifying a Modified File  
`git checkout -- <files>`
15. Undoing things with git restore
    - Unstaging a Staged File:`git restore --staged <file>`
    - Unmodified a Modified File:`git restore <file>`

### Working with Remotes
Managing remote repositories includes knowing how to add remote repositories, remove remotes that are no longer valid, manage various remote branches and define them as being tracked or not, and more.
1. Showing Your Remotes  
The *git remote* command lists the shortnames of each remote handle you’ve specified. If you’ve cloned your repository, you should at least see origin — that is the default name Git gives to the server you cloned from.  
`git remote -v`
2. Adding Remote Repositories  
To add a new remote Git epository as a shortname you can reference easily, run:  
`git remote add <shortname> <url>`
3. Fetching and Pulling from Your Remotes  
To get data from your remote projects, you can run:  
`git fetch <remote>`  
The command goes out to that remote project and pulls down all the data from that remote project that you don’t have yet.
4. Pushing to Your Remotes  
When you have your project at a point that you want to share, you have to push it upstream. The command for this is simple:  
`git push <remote> <branch>`
5. Inspecting a Remote  
If you want to see more information about a particular remote, you can use the command.  
`git remote show <remote> `
6. Renaming and Removing Remotes  
You can run git remote rename to change a remote’s shortname.  
`git remote rename old new`  
If you want to remove a remote for some reason, you can either use:  
`git remote remove or git remote rm`
7. Tagging  
 Git has the ability to tag specific points in a repository’s history as being important.
   - Listing Yours Tags:`git tag`
   - Creating Tags:lightweight and annotated
   - Annotated Tags:`git tag -a <tag> -m <message>`
   - Lightweight Tags:`git tag <tag-name>`
   - Sharing Tags:`git push <remote> <tagname>`
   - Deleting Tags:`git tag -d <tagname>`
   - Checking out Tags:`git checkout <tag>`
8. Git Aliases  
`git config --global alias.name command`