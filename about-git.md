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
![The lifecycle of the status of your files](image\Git-figure1.png)

1. Checking the Status of Your Files  
The main tool you use to determine which files are in which state is the git status command.  
`git status`