Here's a sample `README.md` file for the project described, covering the necessary details:

```markdown
# Age Calculator Project

## Project Overview

The Age Calculator Project is a simple Python application that calculates the age of a person based on their birth date. The application accepts a date input from the user in the format `YYYY-MM-DD`, calculates the age, and prints it out. The project is containerized using Docker, making it easy to deploy in various environments.

## Technology Stack

- **Python 3.9**: The core programming language used to write the age calculation logic.
- **Docker**: Used to containerize the Python application for easier deployment and portability.
- **Git**: Version control to manage the project source code.
- **Amazon EC2**: The cloud platform used for setting up and running the project.
  
## Folder Structure

```plaintext
pythoncode/
├── age_calculator.py      # Python script to calculate age
├── Dockerfile             # Dockerfile for containerizing the application
└── README.md              # Project documentation
```

## Instructions to Set Up and Run

### Prerequisites

1. **Docker** should be installed on the machine. Follow these steps to install Docker on Amazon EC2:
   ```bash
   sudo yum update -y
   sudo yum install docker -y
   sudo systemctl start docker
   sudo docker login
   ```

2. **Git** should be installed to push the code to the repository:
   ```bash
   sudo yum install git -y
   git config --global user.name "YogitaBadhe"
   git config --global user.email "ybadhe0990@gmail.com"
   git config --global credential.helper store
   git remote set-url origin https://Github_Token@github.com/YogitaBadhe/pythoncode.git
   ```

### Step 1: Set Up the Project Folder

1. SSH into your EC2 instance, create the project folder, and navigate into it:

   ```bash
   mkdir pythoncode
   cd pythoncode
   pwd
   ```

2. Create the Python script file `age_calculator.py`:

   ```bash
   touch age_calculator.py
   nano age_calculator.py
   ```

3. Add the following Python code to calculate age based on the birth date input:

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

4. Compile and run the script to test it:

   ```bash
   python3 age_calculator.py
   ```

### Step 2: Initialize Git

1. Create a `README.md` file and commit the changes:

   ```bash
   echo "# pythoncode" >> README.md
   git init
   git add README.md
   git commit -m "Added README file"
   git branch -M main
   git remote add origin https://github.com/YogitaBadhe/pythoncode.git
   git push -u origin main
   ```

### Step 3: Create Dockerfile

1. Create a `Dockerfile` in the project directory:

   ```bash
   touch Dockerfile
   nano Dockerfile
   ```

2. Add the following Docker configuration:

   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY age_calculator.py
   RUN python age_calculator.py
   CMD ["python", "age_calculator.py"]
   ```

### Step 4: Build and Push Docker Image

1. Build the Docker image:

   ```bash
   sudo docker build -t ybadhe/birthdaytoage .
   ```

2. Verify the Docker image:

   ```bash
   sudo docker images
   ```

3. Run the Docker container:

   ```bash
   sudo docker run ybadhe/birthdaytoage
   ```

4. Push the Docker image to Docker Hub:

   ```bash
   sudo docker push ybadhe/birthdaytoage
   ```

### Step 5: Commit and Push Changes

1. Add and commit the Dockerfile and Python script to Git:

   ```bash
   git add .
   git commit -m "Add Dockerfile and age_calculator script"
   git push origin main
   ```

## How to Use

1. **Run Locally**: You can run the Python script directly using:

   ```bash
   python3 age_calculator.py
   ```

2. **Run in Docker**: After building and pushing the Docker image, you can run the container:

   ```bash
   sudo docker run ybadhe/birthdaytoage
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

This README provides a comprehensive overview of the project, the steps to set it up, and how to run the application locally or in Docker.
