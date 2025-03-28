---
## 🛒 QuickCart – Django E-commerce Website

QuickCart is a fully functional e-commerce website built using Django. It allows users to browse products, add them to a cart, and securely place orders — all with a clean Bootstrap frontend.

---

### 🔥 Features

- User registration and login  
- Product listing with categories  
- Add to cart / remove from cart  
- Checkout system  
- Order summary  
- Responsive UI using Bootstrap 5  
- Admin panel to manage products and orders  

---

### 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** MySQL
- **Other:** Font Awesome, Django admin

---

### 🚀 Getting Started

#### 1. Clone the repository

```bash
git clone https://github.com/yourusername/quickcart.git
cd quickcart
```

#### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure environment variables

Create a `.env` file in the root directory and add the following:

```env
DB_NAME=your_database_name
DB_USER=your_database_username
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
```

> 🔐 **Note:** Do not commit your `.env` file to version control.

#### 5. Apply migrations and run the server

```bash
python manage.py migrate
python manage.py runserver
```

#### 6. Access the site

Open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 🔐 Admin Access

- Create a superuser:
```bash
python manage.py createsuperuser
```

- Then go to: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

### 📁 Project Structure

```
quickcart/
│
├── static/              # CSS, JS, images
├── templates/           # HTML templates
├── shop/                # Main app (views, models, urls)
├── media/               # Uploaded product images
├── mysql/               # MySQL-related files (if any)
└── manage.py
```

---

