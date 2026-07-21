# Happy Journey

A travel and tourism website for exploring destinations, planning trips, retreats, and treks — built with Django.

## Tech Stack (planned)

- **Backend:** Django (Python)
- **Frontend:** Django templates + HTML/CSS (React planned as a future upgrade)
- **Database:** SQLite (development) → PostgreSQL via Neon (production)
- **Media storage:** Cloudinary (planned)
- **Deployment:** Render (backend) + Neon (database)
- **Payments:** eSewa / Khalti integration (planned)

## Features Completed So Far

- Django project (`happyjourney`) and app (`core`) set up
- Sidebar + top-bar navbar layout with logo, search bar, and navigation links:
  - Home, About us, Retreats, Trekking package, Gallery, Reviews, Blogs, Contact
- Active link highlighting based on current page
- All 8 navbar pages created with placeholder content
- Custom user model (`CustomUser`) extending Django's `AbstractUser`, with a `phone_number` field for future use
- Authentication backend allowing login via **either username or email**
- Login page with:
  - Email/Username + Password fields
  - "Forgot password?" link (not yet functional)
  - Error message on invalid login
- Profile dropdown menu (shown after login instead of Login/Sign up buttons):
  - Displays "Hi, [First name]"
  - My profile, My bookings, My history, Logout
- Logout with confirmation popup before logging out

## Not Yet Built

- Signup page
- Forgot password functionality
- "My profile", "My bookings", "My history" pages (currently placeholder links)
- Actual content/models for Retreats, Trekking package, Gallery, Reviews, Blogs, Contact
- Booking flow
- Payment integration (eSewa/Khalti)
- Image uploads via Cloudinary
- Deployment (Render + Neon)

## Project Structure

```
happy-journey/
├── core/
│   ├── migrations/
│   ├── static/core/
│   │   ├── css/style.css
│   │   └── images/logo.png
│   ├── templates/core/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── retreats.html
│   │   ├── trekking.html
│   │   ├── gallery.html
│   │   ├── reviews.html
│   │   ├── blogs.html
│   │   ├── contact.html
│   │   └── login.html
│   ├── admin.py
│   ├── backends.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── happyjourney/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── db.sqlite3
```

## Local Setup

1. Clone the repo and enter the project folder:
   ```bash
   git clone https://github.com/purnimapant77/happy-journey.git
   cd happy-journey
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
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

5. Create a superuser (for admin access and testing login):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000` in your browser.

## Contributors

- Purnima Pant ([@purnimapant77](https://github.com/purnimapant77))
- Sushana Dahal ([@Shusanaa](https://github.com/Shusanaa))
