# E-commerce Order Manager

A comprehensive Python application for managing e-commerce operations, including Order Management, Inventory Tracking, Customer Management, and Revenue Reporting. Built with **Streamlit** (GUI) and **MySQL** (Database).
## 🛠️ Tech Stack
* **Language:** Python 3.12.6
* **GUI Framework:** Streamlit
* **Database:** MySQL
* **Libraries:** pandas, mysql-connector-python, matplotlib, python-dotenv

## 🚀 Features
* **Dashboard:** Real-time KPIs, revenue charts, and sales trends.
* **Order Management:** Search, view, and delete orders.
* **New Order Creation:** Create orders with automatic stock deduction (Trigger-based).
* **Master Data:** Manage (Add/Update) Products and Customers.
* **Reports:** Export detailed sales data to CSV.

---

## ⚙️ Installation & Setup Guide

Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites
Ensure you have the following installed:
* [Python 3.8+](https://www.python.org/downloads/)
* [MySQL Server](https://dev.mysql.com/downloads/mysql/) (and MySQL Workbench)
* [Git](https://git-scm.com/) (Optional)

### 2. Database Setup (Important!)
Before running the Python app, you must set up the database.
1. Clone the **Repository** by using this line (make sure you have Git):
```bash
git clone https://github.com/Dangtooo/ecommerce-project.git
```
2.  Open **MySQL Workbench**.
3.  Open and run the SQL files located in `app/db/` in the following order:
```bash
schema.sql
seed.sql
queries.sql
```
4.  Remember to replace the password by **your MySQL password** in `.env` file:
```bash
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=<your-password>
DB_NAME=ecommerce_db
```
### 3. Library Setup
You need to download appropriate libraries to run the program, using this line of command:
```bash
pip install -r requirements.txt
```
### 4. Run the program
After MySQL and Library setup, you can now run the program by using this line of command (make sure you in the `/app` folder):
```bash
streamlit run main.py
```