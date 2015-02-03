# Essential git commands

### First some terms: 

*Repository* - A directory which is under version control. This is nothing else than a directory, with some extra files used by Git to store versions

*Git repository* - A directory under version control by Git.

*Commit* - Verb for setting a point in history.

### Set up ssh keys 

Note: On Windows we recommend using Cygwin to make this as easy as possible.

To be able to syncronize (pull and push) code to github, you need to identify yourself. But we do not 
want to login every time we run a command, and for this reason we use ssh-keys. This means that on your 
computer you need to have two files that contains a combination of charaters that uniquely identifies you, 
just like you are used to when identifying yourself with a combination of username and password.

The two files we need is called ``id_rsa`` and ``id_rsa.pub``. But we do not create these files yourself, 
we use a command line tool called ``ssh-keygen``. This tool gets available on your computer when you install
XCode (OSX) or Cygwin (Windows).

Note that ssh-keys are used by many services, so you may allready have an ssh-key on your computer. To check, 
go to your home directory with ``cd``. (This command without anything after, takes you to your home directory.)
Then run ``cd .ssh``. If you now get something like this you do not have a ssh key:

    ´´-bash: cd: .ssh: No such file or directory``

If you do not get this message, directory is changed to ``.ssh`` then you allready have a key you can use.

At this point you are ready to follow the description of using ssh keys on github. Go to the link below 
and choose "MAC" or "WINDOWS". But note that even if Github tries to tell you to "Forget the terminal" or 
"Skip this guide. Download our native app instead." you should continue with the description. We want to 
stay with the terminal at this point.

https://help.github.com/articles/generating-ssh-keys/

### Get a local copy of a repository found on github.com

    ´´git clone git@github.com:appressoas/appressoedu.git´´

Use ``ls`` to see your copy of the repository.

### See the current status of the repository

    ``git status``

### Syncronize your local repository with the content in the repository on github

    ``git pull``

### Tell git to save everything as it is right now

    ´´git commit -a -m "Added more information to the readme file"``

### Update the repository on github.com so that is equal to what I have on my machine

    ``git pull``
    ``git push``

Why this ``git pull`` first? Because you need to syncronize your local code first to avoid errors.

