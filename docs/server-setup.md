# Server Setup and Deployment on AWS EC2

This guide provides step-by-step instructions for setting up an AWS EC2 instance, deploying the Python Email Scheduler application, and configuring the CI/CD pipeline.

---

## 1. Launch and Configure an EC2 Instance

### Step 1: Launch an EC2 Instance
1. Go to the **AWS Management Console**.
2. Navigate to **EC2 Dashboard** and click **Launch Instance**.
3. Choose the **Ubuntu AMI** and select the instance type (e.g., `t2.micro` for free-tier).
4. Create a new key pair or use an existing one to access your instance.
5. Configure security groups to allow SSH (port 22) and HTTP/HTTPS if needed.
6. Click **Launch**.

### Step 2: Connect to Your EC2 Instance
Once the instance is running, SSH into it using the key pair:
```bash
ssh -i path-to-your-key.pem ubuntu@<your-ec2-ip>
```

## 2. Set Up the EC2 Server
### Step 1: Update the Server
```bash
sudo apt update && sudo apt upgrade -y
```
### Step 2: Install Required Packages
Install Python, Pip, Git, and virtual environment tools:

```bash
sudo apt install python3 python3-pip python3-venv git -y
```
### Step 3: Clone the Repository
```bash
cd /home/ubuntu
git clone https://github.com/EhmeeUd/python-email-scheduler.git
cd python-email-scheduler
```
### Step 4: Create and Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```
## 3. Configure systemd to Run Your App as a Service
### Step 1: Create the systemd Service File
```bash
sudo nano /etc/systemd/system/emailapp.service
```
Add the following content:

```ini
[Unit]
Description=Python Email Scheduler
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/python-email-scheduler
ExecStart=/home/ubuntu/python-email-scheduler/venv/bin/python /home/ubuntu/python-email-scheduler/email_sender.py
Restart=always
EnvironmentFile=/home/ubuntu/python-email-scheduler/.env

[Install]
WantedBy=multi-user.target
```
### Step 2: Reload systemd and Start the Service
```bash
sudo systemctl daemon-reload
sudo systemctl start emailapp.service
sudo systemctl enable emailapp.service
```
### Step 3: Check the Service Status
```bash
sudo systemctl status emailapp.service
```

## 4. CI/CD Pipeline Configuration
### Step 1: Add SSH Key to GitHub Secrets
1. In your GitHub repository, navigate to Settings > Secrets and Variables > Actions.
2. Add the following secrets:
```AWS_EC2_HOST```: The public IP or DNS of your EC2 instance.
```AWS_SSH_KEY```: The private SSH key for accessing your EC2 instance.
### Step 2: Configure the GitHub Actions Workflow
In your repository, the ```.github/workflows/ci-cd.yml``` file automates the following:

1. Checks out the code.
2. Installs dependencies.
3. Runs unit tests.
4. Deploys the app to the EC2 instance if tests pass.
The deployment step uses ```ssh-action``` to SSH into the EC2 instance and pull the latest code. It also ensures that the virtual environment is set up and dependencies are installed.

## 5. Ensure Environment Variables Persist
Make sure that the ```.env``` file is created on the EC2 instance:

```bash
nano /home/ubuntu/python-email-scheduler/.env
```
Add your environment variables:

```env
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
LOGIN=your_login@example.com
PASSWORD=your_password
TO=recipient@example.com
```
Ensure the ```.env``` file is not overwritten by adding it to ```.gitignore```:

```bash
echo ".env" >> .gitignore
```
# Conclusion
Once everything is set up, you can push changes to the ```main``` branch, and the CI/CD pipeline will automatically build, test, and deploy your Python app to the AWS EC2 instance.

For any additional questions, refer to the project's README.md or open an issue in the GitHub repository.
