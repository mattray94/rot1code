'''
I am using this fie to practise using GitHub for version control

In order to track a folder with Git use the command $git init once in the folder. This creates a .git directory. Remove this directory to stop tracking.

Before we start to commit anything, check the status of the repository...

$git status

If you have a file in this location that you don't want other people to see (eg. personal preferences
specific to your OS, don't need to be tracked) - we need to ignore these files.
$touch .gitignore

Creates a .gitignore file. Open up in a text editor and add the files you do not want people to see.

.DS_Store	#will ignore the folder .DS_Store
.project 	#will ignore the file .project
*.pyc 		#will ignore all files with the .pyc extension

Having saved this file, rerun git status and you will see that the files/folders you have put into git ignore will no longer be visible, and so will not be tracked. Simply remove them from the .gitignore file to go back.

There are three 'levels' at which github works. The working directory, where changes are made locally on the machine. The staging area, where we fix files we have changed ready to be uplaoded to github, and finally the .git directory, which is the synced online repository to which files must be committed.

To add a file to the staging area (for example demo.py) use:

$git add demo.py	#adds a specific python file to the staging area
$git add .gitignore	#adds the .gitignore file to the staging area
$git add -A		#adds all current untracked files to the staging area

Now running $git status shows us staged files which are ready to be committed in green, as well as the untracked files in red.

To remove files from the staging area, use the command:

$git reset .gitignore	#removes .gitignore from the staging area
$git status		#would now show .gitignore in red (untracked) and other staged files in green.
$git reset		#empties the staging area of all files
$git status		#would now show all files as red (untracked).

To commit files into the repository, first stage them, then run a commit command. This takes an argument -m for a message which accompanies the commit. BE AS DETAILED AS YOU CAN!

$git add -A				#adds all to staging area
$git commit -m "Initial Commit"		#commits all to repository with the message "Initial Commit". Use the message to document commit individual code files with detailed changes.

'''
print("Open this file for notes on how to use Git!")

