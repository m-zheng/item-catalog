# About

This project is a part of Full Stack Developer Nanodegree from [Udacity](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

It provides a list of items within a variety of categories as well as provides a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items. The application also provides a JSON endpoint.
## Getting Started

  - Install [Python 2.7](https://www.python.org/downloads).
  - Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
  - Clone this repository to your local machine:
    ```
    git clone https://github.com/minghua1991/item-catalog.git
    ```
  - Go to the directory that contains all code of this repository:
    ```
    cd item-catalog
    ```
  - Set up VM:
    ```
    vagrant up
    ```
  - Login to the virtual machine via SSH:
    ```
    vagrant ssh
    ```
  - Go to catalog directory:
    ```
    cd /vagrant/item-catalog
    ```
  - Initialize the database:
    ```
    python database_setup.py
    ```
  - Setup dummy data in the database (Optional):
    ```
    python dummy_database.py
    ```
  - Run the web server:
    ```
    python project.py
    ```
  - Navigate to [http://localhost:8080/](http://localhost:8080/) in web browser.

    

License
----

MIT
