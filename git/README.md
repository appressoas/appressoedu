# Essential git commands

### First some terms: 

*Repository* - A directory which is under version control. This is nothing else than a directory, with some extra files used by Git to store versions

*Git repository* - A directory under version control by Git.

*Commit* - Verb for setting a point in history.

### Get a local copy of a repository found on github.com

    ´´git clone git@github.com:appressoas/appressoedu.git´´

Use ``ls`` to see your copy of the repository.

### See the current status of the repository

    ``git status``

### Tell git to save everything as it is right now

    ´´git commit -a -m "Added more information to the readme file"``

### Update the repository on github.com so that is equal to what I have on my machine

    ``git push``

