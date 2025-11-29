# E-commerce Order Manager

A comprehensive Python application for managing e-commerce operations, including Order Management, Inventory Tracking, Customer Management, and Revenue Reporting. Built with **Streamlit** (GUI) and **MySQL** (Database).

## 🚀 Features
* **Dashboard:** Real-time KPIs, revenue charts, and sales trends.
* **Order Management:** Search, view, and delete orders.
* **New Order Creation:** Create orders with automatic stock deduction (Trigger-based).
* **Master Data:** Manage (Add/Update) Products and Customers.
* **Reports:** Export detailed sales data to CSV.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **GUI Framework:** Streamlit
* **Database:** MySQL
* **Libraries:** pandas, mysql-connector-python, matplotlib, python-dotenv

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
1.  Open **MySQL Workbench**.
2.  Open and run the SQL files located in `app/db/` in the following order:
    * 1️⃣ **`schema.sql`**: Creates the database `ecommerce_db` and tables.
    * 2️⃣ **`seed.sql`**: Inserts sample data (Products, Customers, Orders).
    * *(Note: Stored Procedures and Triggers are included in `schema.sql` or `part_c.sql` if separated).*
3.  Verify that the database `ecommerce_db` is created and has data.

### 3. Clone the Repository
```bash
git clone <your-repo-url>
cd ecommerce-order-manager