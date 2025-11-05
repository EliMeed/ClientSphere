# ClientSphere

ClientSphere is a full-stack Django web application for managing client records with authentication and CRUD functionality.  
It combines Django’s backend framework, Bootstrap styling, and PostgreSQL to deliver a responsive, secure, and extendable platform.  

---

## 🎬 Demo Preview

<video src="https://raw.githubusercontent.com/EliMeed/_ClientSphere/main/demo.webm"
       autoplay
       loop
       muted
       playsinline
       width="720">
</video>
## ⚙️ Tech Stack

| Layer | Technology |
|-------|-------------|
| Frontend | Django Templates, Bootstrap 5, Custom CSS |
| Backend | Django 5.x (Python 3) |
| Database | PostgreSQL |
| Authentication | Django built-in auth system |
| Version Control | Git + GitHub |
| Environment | Ubuntu 22.04 / venv |
| Planned Enhancements | MFA (Multi-Factor Authentication), Role-Based Access Control (RBAC) |

---

## 🌐 Features

### Authentication
- Secure login and logout flow using Django’s authentication system  
- User registration with form validation  
- Admin management through the Django admin panel

### Client Management
- Add, edit, delete, and view client records  
- Data displayed in a clean, responsive Bootstrap table  
- Only authenticated users can access records

### Interface and Styling
- Responsive layout using Bootstrap and custom CSS  
- Simplified forms and consistent color scheme  
- Navigation bar for quick access to sections

### System Design
- Modular Django app structure (crm and website)  
- Environment-based configuration using dotenv  
- Requirements file for reproducible dependencies

---

## 🚀 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/EliMeed/_ClientSphere.git
cd _ClientSphere

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create a superuser
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver

