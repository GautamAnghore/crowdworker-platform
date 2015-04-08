crowdworker-platform
====================
A new Crowd Working Platform [ prototype for research purpose (http://crowdresearch.stanford.edu) ]

This is a prototype for a crowdresearch aimed at developing a new crowd sourcing platform overcoming a great leap of trust and power present in current platforms.

## Local Development Enviornment Setup :

1. Install virtualenv:
 ```
 install virtualenv
 pip install virtualenv
 ```
 or follow [this](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for installing virtualenv.

 If you do not have pip installed:
 ```
 sudo apt-get install python-pip
 ```

2. Clone the repository on local machine:
 ```
 git clone https://github.com/GautamAnghore/crowdworker-platform
 ```

 
3. cd into the project directory:
 ```
 cd crowdworker-platform
 ```

4. Create a new virtual enviornment with python version 2.7:
 ``` 
 virtualenv -p /usr/bin/python2.7 venv
 ```

5. Activate the virtual enviornment:
 ```
 source venv/bin/activate
 ```

6. Install the requirements:
 ```
 pip install -r requirements.txt
 ```

7. Install MySQL if not already installed.

