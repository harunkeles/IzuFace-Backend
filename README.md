# Izu Face Backend

This is based on git@GIT.izu.edu.tr:four-force/izuFace.git

```bash
# Get the code

# Virtualenv modules installation
- pip install virtualenv
- virtualenv env

# Virtualenv modules activation
source env/Scripts/activate 

# Install modules - SQLite Database
pip install -r requirements.txt

# Check module version
py -m 'module_name' --version

# Control the new python modules version
pip list --outdated

# Update module
pip install -U 'module_name'

# Preparing db files
python manage.py makemigrations
# Files migrate to db 
python manage.py migrate

# Run server 
python manage.py runserver

# Access the dashboard in browser: http://127.0.0.1:8000/
