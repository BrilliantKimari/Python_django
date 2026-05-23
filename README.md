# Wildlife Kenya 🦁

A beautiful Django web application for exploring Kenya's incredible wildlife and learning about wildlife conservation.

## About

Wildlife Kenya is an educational platform dedicated to fostering appreciation for Kenya's unique biodiversity. The website provides information about iconic African animals and promotes conservation awareness.

## Features

- **User Authentication** - Register and login with email and password
- **Home Page** - Welcome page with beautiful hero section
- **Animals Gallery** - Interactive grid showcasing Kenya's wildlife with descriptions
- **About Section** - Learn about our mission and wildlife conservation
- **Secure Login System** - Email-based authentication with password validation
- **Responsive Design** - Beautiful wildlife-themed green color scheme
- **User Profiles** - Personalized welcome messages for logged-in users

## Technology Stack

- **Backend**: Django 6.0.5
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3
- **Authentication**: Django built-in authentication system
- **Environment Management**: python-dotenv

## Installation & Setup

1. **Clone the repository** (or navigate to project directory)
```bash
cd Python_django
```

2. **Activate virtual environment**
```bash
source venv/Scripts/activate  # On Windows Git Bash
# or
.\venv\Scripts\activate  # On Windows PowerShell
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run database migrations**
```bash
python manage.py migrate
```

5. **Start the development server**
```bash
python manage.py runserver
```

6. **Visit the application**
```
http://localhost:8000/
```

## Usage

### Creating an Account
- Click "Login/Register" in the navigation
- Switch to the "Register" tab
- Enter your name, email, and password
- Click "Register"

### Logging In
- Click "Login/Register"
- Enter your registered email and password
- Click "Login"

### Exploring the Site
- **Home** - View the welcome message
- **Animals** - Browse Kenya's iconic wildlife with descriptions
- **About** - Learn about wildlife conservation

## Pages

- `/` - Home page
- `/auth/` - Login/Registration page
- `/animals/` - Wildlife gallery
- `/about/` - About Wildlife Kenya
- `/logout/` - Logout (for authenticated users)

## Environment Variables

Create a `.env` file in the project root (see `.env.example`):

```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Important**: Never commit the `.env` file to version control. It's already in `.gitignore`.

## Developers

👥 **Development Team:**
- **Emmaculate Achieng**
- **Saline Akinyi**
- **Brilliant Kimari**

## Project Structure

```
Python_django/
├── config/              # Django project configuration
│   ├── settings.py      # Project settings
│   ├── urls.py          # Main URL routing
│   └── wsgi.py          # WSGI configuration
├── main/                # Main Django app
│   ├── views.py         # View logic
│   ├── urls.py          # App URL routing
│   ├── models.py        # Database models
│   ├── forms.py         # Django forms
│   ├── admin.py         # Admin configuration
│   └── templates/       # HTML templates
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (git ignored)
├── .env.example         # Environment template
├── .gitignore           # Git ignore rules
└── db.sqlite3           # Database file
```

## Security Features

✅ SECRET_KEY protected via environment variables  
✅ DEBUG mode configurable per environment  
✅ Password hashing with Django's built-in system  
✅ CSRF protection on all forms  
✅ Email validation on registration  
✅ Secure logout functionality  
✅ User authentication required for sensitive operations  

## Future Enhancements

- Add more animals to the gallery
- Implement animal filtering and search
- Add user profiles and preferences
- Integrate with wildlife databases
- Add conservation tips and articles
- Implement image uploads for animals

## License

This project is created for educational purposes.

---

**Made with ❤️ for Wildlife Conservation**
