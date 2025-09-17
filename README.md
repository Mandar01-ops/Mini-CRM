#  Customer Relationship Management (CRM) Project

This project is a **Customer Relationship Management (CRM) system** built with **Python Django**.  
It helps businesses manage customers, contacts, and tasks efficiently.

---

##  Overview

This CRM project streamlines customer management by offering:  
- **User authentication**  
- **Customer & contact management**  
- **Task tracking**  
- **Dashboard for key metrics**

 Deployed Version: [Mini CRM on Render](https://mini-crm-8fli.onrender.com/login/)

---

##  Features

- **User Authentication** – Secure login/logout system.  
  - Superuser credentials:  
    - **Username:** `admin`  
    - **Password:** `admin`  

- **Customer Management** – Add, edit, delete customer records.  
- **Contact Management** – Track customer contacts and interactions.  
- **Task Management** – Assign and monitor tasks.  
- **Analytics Dashboard** – Visualize customer-related metrics.  

---

##  Technologies Used

### Backend
- Python  
- Django  
- Django ORM (SQLite / PostgreSQL)  

### Deployment
- Render (for hosting)  
- Gunicorn (for WSGI server)  

---

##  Getting Started

You can either use the deployed version or run the project locally.

### Option 1: Use the Deployed Version
 [Mini CRM on Render](https://mini-crm-8fli.onrender.com/login/)  
Login with:  
- **Username:** `admin`  
- **Password:** `admin`  

---

### Option 2: Run Locally on Your Machine

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Mandar01-ops/Mini-CRM.git
   cd Mini-CRM
2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
4. **Apply Migrations**
   ```bash
   python manage.py migrate
5. **Create Superuser (if needed)**
   ```bash
   python manage.py createsuperuser
6. **Run Development Server**
   ```bash
   python manage.py runserver
7. **Access the App**
Open http://localhost:8000 in your browser.

##  Contributing
Contributions are welcome! To contribute:
1. Fork the repo
2. Create a new branch (git checkout -b feature/new-feature)
3. Commit changes (git commit -am 'Add new feature')
4. Push branch (git push origin feature/new-feature)
5. Open a Pull Request

##  License
This project is licensed under the MIT License – see the [MIT License](./LICENSE). file for details.
