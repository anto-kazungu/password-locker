# Password Locker

## Description
A web application that allows users to save their account credentials, including usernames and passwords. The application can also generate strong passwords for users.

## Prerequisites

### Getting the Project
1. You require a GitHub account.
   
   To create a GitHub account, [click here](https://github.com/).

2. Install Git on your machine:
   ```bash
   sudo apt-get install git-all
   ```

### Setup

To access this project on your local machine, clone it using these steps:

1. Open your terminal.
2. Use this command to clone the repository:
   ```bash
   git clone https://github.com/changawa-antony/password-locker
   ```
   This will clone the repository into your local folder.

3. This project uses Python. Use the following commands to install Python:
   ```bash
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt update
   sudo apt install python3.6
   ```

4. Confirm installation by running:
   ```bash
   python3.6
   ```
   To exit the interpreter, run:
   ```bash
   quit()
   ```

## Using the Project
### Running the CLI Version

1. Locate where you cloned the project.
2. Open the project in your terminal.
3. Run:
   ```bash
   python3.6 interaction.py
   ```
4. The program should start in your terminal.
5. To exit the program, run:
   ```bash
   quit()
   ```

*Keep exploring* :rocket:

### Running the Flask Web Application

1. Ensure all dependencies are installed by running:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Flask application:
   ```bash
   python3.6 flask_app.py
   ```
3. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```
4. Interact with the password locker web interface.

## Author

Antony Kazungu

### License

This project is under the [MIT](LICENSE) license.

*Copyright (c) 2021 (Changawa-antony)*

