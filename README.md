# Estintori 🔥

**Estintori** is a simple and functional Django-based web application to manage fire extinguishers, emergency doors, and fire sensor data — built by a technician, for technicians.  
The goal is to keep everything organized and ready for inspections.

It supports PostgreSQL, Docker, and basic user authentication. No REST API. No overengineering.

---

## 🔧 What You Can Do

- Register and update **fire extinguishers**
- Manage **emergency doors** with notes and inspections
- Track **fire sensors** and their status
- Post **news or updates** for your team
- Log in/out with user authentication
- Use it locally on your own network

---

## 🧱 Tech Overview

- Django + Python 3
- PostgreSQL
- Docker support
- No external APIs
- UI is simple — built for function, not beauty

---

## 🚀 Quick Start (Manual)

```bash
git clone https://github.com/your-username/estintori.git
cd estintori
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# make sure PostgreSQL is running and configured
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🐳 Quick Start with Docker

Make sure you have Docker and Docker Compose installed.

```bash
docker compose up --build
```

Access the app at [http://localhost:8000](http://localhost:8000)

---

## 🔐 User Access

- Admin panel: `/admin`
- You can create users and assign roles
- Basic permissions only (not role-based yet)

---

## 🌐 Languages

- English 🇬🇧  
- Italian 🇮🇹  
(Default is Italian, switchable via settings)

---

## 📄 License

MIT — do whatever you want, just don't remove the author's name.

---

## 👷 Author

Developed by **Viktor Holovin**, technician with a passion for open tools.  
If it helps someone — the mission is complete.

---

## 📝 Notes

- This is not a commercial product. It's built for internal use.
- Contributions are welcome, but keep it simple.
