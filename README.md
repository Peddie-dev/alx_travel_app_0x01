# ALX Travel App 0x00

A Django-based travel application that allows users to browse listings, make bookings, and leave reviews. This project includes API endpoints using Django REST Framework (DRF) and a seeder to populate the database with sample data.

---

## **Project Structure**

alx_travel_app_0x00/
├── alx_travel_app/
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── listings/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── management/
│ └── commands/
│ └── seed.py
└── manage.py

yaml
Copy code

---

## **Features**

- **Listings**: Create and view travel listings with title, description, price per night, and location.
- **Bookings**: Users can book listings with specified check-in and check-out dates.
- **Reviews**: Users can leave ratings and comments on listings.
- **API Support**: REST API endpoints with serializers for data representation.
- **Database Seeder**: Management command to populate the database with sample listings.

---

## **Installation**

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd alx_travel_app_0x00
Create a virtual environment and activate it
