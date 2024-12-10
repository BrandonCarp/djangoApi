# djangoApi

Prerequisites
Before running the project, make sure you have the following installed on your local machine:

Python 3.6 or higher
pip (Python's package installer)
Virtual Environment (optional but recommended)
Setup Instructions
1. Clone the repository
Clone the project to your local machine:

bash
Copy code
git clone https://github.com/yourusername/your-django-api-project.git
cd your-django-api-project
2. Set up a virtual environment (optional but recommended)
Create a virtual environment to manage project dependencies:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
# OR
venv\Scripts\activate  # For Windows
3. Install dependencies
Install the required dependencies using pip:

bash
Copy code
pip install -r requirements.txt
The requirements.txt should include the necessary packages like Django and Django REST Framework. Example:

makefile
Copy code
Django==5.1.4
djangorestframework==3.14.0
If you don't have a requirements.txt, you can manually install the necessary packages:

bash
Copy code
pip install django djangorestframework
4. Apply migrations to set up the database
Run the following commands to apply migrations and create the necessary database tables:

bash
Copy code
python manage.py migrate
5. Create a superuser (optional)
If you want to access the Django admin interface, create a superuser:

bash
Copy code
python manage.py createsuperuser
You will be prompted to enter a username, email, and password.

6. Run the development server
Start the Django development server:

bash
Copy code
python manage.py runserver
Your project will now be running locally at http://127.0.0.1:8000/.