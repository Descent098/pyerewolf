# Werewolf

A web version of the werewolf game implemented in python using Flask.



## Quick-start

### Installation

#### From source

1. Clone this repo: (```git clone https://github.com/Descent098/werewolf```) or download a zip of it [https://github.com/Descent098/werewolf/archive/master.zip](https://github.com/Descent098/werewolf/archive/master.zip)
2. If you just need to run the game then install flask (```pip install flask``` or ```sudo pip3 install flask```)



#### Usage

Run ```python routes.py``` or ```python3 routes.py```. This will then start up the server on port 5000, which you can access locally through [http://localhost:5000/](http://localhost:5000/).



## Additional Documentation

(Work in progress) User documentation is available at [https://kieranwood.ca/werewolf](https://kieranwood.ca/werewolf)



## Development & Contribution guide

### Installing development dependencies

There are a few dependencies you will need to use to get started developing:

```
pytest 	# Used to run the test code in the tests directory
mkdocs	# Used to create HTML versions of the markdown docs in the docs directory
```

Just go through and run ```pip install <name>``` or ```sudo pip3 install <name>```. These dependencies will help you to automate documentation creation, and testing.



### Folder Structure

*A Brief explanation of how the project is set up for people trying to get into developing for it*



#### /werewolf

*Contains all the first party modules used in werewolf*



#### /docs

*Contains markdown source files to be used with [mkdocs](https://www.mkdocs.org/) to create html/pdf documentation.* 



#### /tests

*Contains tests to be run before release* 

**Before you can use this you will need to create tests, for more details take a look at [pytest](https://docs.pytest.org/en/latest/) **



#### Root Directory



**LICENSE**: This file contains the licensing information about the project.



**CHANGELOG.md**: Used to create a changelog of features you add, bugs you fix etc. as you release.



**mkdocs.yml**: Used to specify how to build documentation from the source markdown files.



**.gitignore**: A preconfigured gitignore file (info on .gitignore files can be found here: https://www.atlassian.com/git/tutorials/saving-changes/gitignore)



## Additional information

### Deployment

Recommended deployment is through Heroku (need to add details about this).




