# Sabordo Project - Phone Repair Service Management System

A modern web application for managing phone repair services, built with Django and Bootstrap. This system allows customers to schedule repair appointments and administrators to manage service requests efficiently.

## Features

- 📱 Comprehensive phone repair service management
- 📅 Easy appointment scheduling system
- 🎨 Modern, responsive UI with Bootstrap
- 🔒 Secure user authentication
- 📊 Admin dashboard for service management
- 📧 Email notifications for appointments
- 📱 Mobile-friendly design

## Services Offered

- Screen Repair
- Battery Replacement
- Water Damage Repair
- Malware Removal
- Board Repair
- Data Recovery
- Phone Check Up
- Hardware Upgrade
- Hardware Replacement

## Tech Stack

- **Backend**: Django 5.2
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Database**: SQLite (default)
- **Python Version**: 3.13+

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sabordo-project.git
cd sabordo-project
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure

```
sabordo-project/
├── myproject/
│   ├── core/
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── static/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── forms.py
│   ├── manage.py
│   └── settings.py
├── requirements.txt
└── README.md
```

## Usage

1. **Customer View**
   - Browse available services
   - Schedule appointments
   - View appointment status
   - Receive email confirmations

2. **Admin View**
   - Manage appointments
   - Update service status
   - View customer information
   - Generate reports

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Acknowledgments

- Bootstrap for the UI components
- Django for the web framework
- All contributors who have helped shape this project
