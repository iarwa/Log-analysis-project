# Logs Analysis Project

This project aims to build an internal reporting tool that will use information from the database and use SQL queries to analyze the log data, and print out the answers to some questions about the site's user activity.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

## Technologies used

1. PostgreSQL
2. Writing Python code with DB-API
3. Linux-based virtual machine (VM) Vagrant

### Prerequisites

1. Download [Vagrant](https://www.vagrantup.com/) and install.
2. Download [Virtual Box](https://www.virtualbox.org/) and install.
3. Clone this repository to a directory of your choice.
4. Download the [database file] (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) you will need to unzip this file after downloading it. The file inside is called **newsdata.sql**. Put this file and **newsDB.py** file from the repository into the **vagrant** directory within your VM.

### Installing

Run these commands from the terminal in the folder where your vagrant is installed in:

1. ```vagrant up``` to start up the VM.
2. ```vagrant ssh``` to log into the VM.
3. ```cd /vagrant``` to change to your vagrant directory.
4. ```psql -d news -f newsdata.sql``` to load the data and create the tables.
5. ```python newsDB.py``` to run the reporting tool.

## Versioning

This project use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/iarwa/Log-analysis-project).

## Authors

* **Arwa Alshathri** - *Initial work* - [iarwa](https://github.com/iarwa)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/iarwa/Log-analysis-project/blob/master/LICENSE) file for details
