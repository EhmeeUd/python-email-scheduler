# Python Email Scheduler

This Python application automates the sending of scheduled emails. It uses **GitHub Actions** for Continuous Integration and Deployment (CI/CD) and automatically deploys to an **AWS EC2 instance**.

## Prerequisites

Before starting, ensure you have the following:

- **Python 3.x** installed on your local machine.
- An **AWS EC2 instance** set up for deployment (instructions [here][def]).
- **GitHub Actions** set up for automated testing and deployment.

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/EhmeeUd/python-email-scheduler.git
cd python-email-scheduler
```
### 2. Create and Activate the Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 3. Set Up ```.env``` File
Create a .env file to store your environment variables:
```bash
cp .env.example .env
```
Fill in the required variables inside ```.env```:

```env
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
LOGIN=your_login@example.com
PASSWORD=your_password
TO=recipient@example.com
```

### 4. Ensure Your Application Loads ```.env```
Make sure your Python app is configured to load the ```.env``` file. Ensure you have the ```python-dotenv``` library installed and add the following code at the start of your Python script (e.g., ```app.py``` or ```email_sender.py```):

```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Example usage of environment variables
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
to_addresses = os.getenv("TO").split(',')
```
Install the ```python-dotenv``` package if you haven't already:

```bash
pip install python-dotenv
```

### 5. Run the Application Locally
Once the environment is set up, you can run the app locally:

```bash
python email_sender.py
```
## CI/CD Pipeline
This project uses **GitHub Actions** for continuous integration and deployment. Every push to the main branch triggers a workflow that:

1. Installs dependencies.
2. Runs unit tests.
3. Deploys the app to a staging environment on an AWS EC2 instance (after tests pass).
You can find more details on the CI/CD process in the workflow file: ```.github/workflows/ci-cd.yml```.

## Deployment Instructions
For detailed instructions on setting up the AWS EC2 instance and deploying your application, see the [Server Setup Guide][def].

## Contributing
Fork the repository.
1. Create a new branch (```git checkout -b feature-branch```).
2. Commit your changes (```git commit -m 'Add new feature'```).
3. Push to the branch (```git push origin feature-branch```).
4. Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

[def]: ./docs/server-setup.md