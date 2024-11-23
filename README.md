Here's a `README.md` file based on your provided commands:

```markdown
# Age Calculator Project

## Project Overview
The Age Calculator project is a Python-based application that calculates a person's age based on their birth date. It allows users to input their birth date in the `YYYY-MM-DD` format and returns their age in years. This project is hosted on GitHub and can be built and run in a Docker container.

## Technology Used
- **Python** (for the main logic of calculating age)
- **Git** (version control and repository management)
- **Docker** (for containerizing the application)
- **Amazon EC2** (for hosting and running the application)

## Folder Structure
```
pythoncode/
│
├── Dockerfile           # Dockerfile to containerize the project
├── age_calculator.py    # Python script for age calculation
└── README.md            # Project README file
```

## Setting up the Project

### 1. Launch EC2 Instance
- Select **Linux OS**.
- Allow inbound SSH access (port 22) in your Security Group settings.

### 2. Install Required Tools

```bash
# Start Docker service
sudo systemctl start docker

# Log in to Docker
sudo docker login

# Update system and install Git
sudo yum update -y
sudo yum install git -y

# Verify Git installation
git --version

# Set global Git configurations
git config --global user.name "YogitaBadhe"
git config --global user.email "ybadhe0990@gmail.com"
git config --global credential.helper store
git remote set-url origin https://Github_Token@github.com/YogitaBadhe/pythoncode.git
```

### 3. Set Up the Project Folder
```bash
# Create a project folder
mkdir pythoncode
cd pythoncode

# Check current directory
pwd

# Create the Python script
touch age_calculator.py
cat age_calculator.py

# Open the file in the editor and add the code
nano age_calculator.py
```

#### Python Script (`age_calculator.py`)

```python
from datetime import datetime

def age_calculator(birth_date_str):
    """
    Calculate the age of a person based on their birth date.
    :param birth_date_str: Birth date in the format 'YYYY-MM-DD'
    :return: Age in years
    """
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

if __name__ == "__main__":
    birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
    age = age_calculator(birth_date_str)
    print(f"Your age is: {age}")
```

### 4. Run the Python Script

```bash
# Run the age_calculator script
python3 age_calculator.py
```

### 5. Initialize Git Repository

```bash
# Initialize a Git repository
echo "# pythoncode" >> README.md
git init
git add README.md
git commit -m "Added README file"
git branch -M main
git remote add origin https://github.com/YogitaBadhe/pythoncode.git
git push -u origin main
```

### 6. Create a Dockerfile

```bash
# Create Dockerfile
touch Dockerfile
nano Dockerfile
```

#### Dockerfile Content:

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY age_calculator.py .
RUN python age_calculator.py
CMD ["python", "age_calculator.py"]
```

### 7. Build and Run the Docker Image

```bash
# Build the Docker image
sudo docker build -t ybadhe/birthdaytoage .

# List Docker images
sudo docker images

# Run the Docker container
sudo docker run ybadhe/birthdaytoage

# Push the image to Docker Hub
sudo docker push ybadhe/birthdaytoage
```

### 8. Final Git Commit

```bash
# Add changes to Git
git add .
git commit -m "Add Dockerfile and age_calculator script"
git push origin main
```

## Conclusion
This project demonstrates a simple Python application for calculating age based on the birthdate, and it is containerized using Docker. The steps include setting up the EC2 instance, installing required tools, coding the Python script, initializing a Git repository, creating a Dockerfile, and running the application inside a Docker container.
