# 🌆 CityServe

A full-stack web platform built using **Django** that connects users with local city services like shops, products, and service providers. The platform allows users to browse, order, and interact with multiple city-based services in one place.

---

## 🚀 Features

* 👤 User Authentication (Login / Register)
* 🛍️ Browse Products & Shops
* 🧾 Order Management System
* 🏙️ City-based service organization
* 📦 Product listing and categorization
* 🧑‍💼 Admin panel for management
* 🎨 Responsive UI using templates & static files

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite (for development)
* **Other:** Django Templates, Static Files

---

## 📂 Project Structure

```
CityServe/
│── cities/          # Handles city-related data
│── users/           # Authentication & user management
│── products/        # Product listing
│── orders/          # Order functionality
│── services/        # Services provided
│── shops/           # Shop management
│── templates/       # HTML templates
│── static/          # CSS, JS, images
│── manage.py        # Django entry point
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cityserve.git
cd cityserve
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

*(If requirements.txt not available, install Django manually: `pip install django`)*

---

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Run the server

```bash
python manage.py runserver
```

---

### 6. Open in browser

```
http://127.0.0.1:8000/
```

---

## 🔐 Admin Access

To access admin panel:

```bash
python manage.py createsuperuser
```

Then go to:

```
http://127.0.0.1:8000/admin/
```

---

## 📸 Screenshots (Add if possible)

* Home Page
* Product Listing
* Order Page
* Admin Dashboard

---

## 💡 Future Improvements

* Payment integration 💳
* REST API using Django REST Framework
* Deployment (AWS / Vercel / Render)
* Improved UI/UX

---

## 👩‍💻 Author

**Ishika M.**

* GitHub: https://github.com/ishikamokati30

---
