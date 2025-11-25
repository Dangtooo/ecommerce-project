DROP DATABASE IF EXISTS ecommerce_db;
CREATE DATABASE ecommerce_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ecommerce_db;

-- 1. Bảng CUSTOMERS (Khách hàng)
CREATE TABLE CUSTOMERS (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address TEXT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 2. Bảng PRODUCTS (Sản phẩm)
CREATE TABLE PRODUCTS (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category VARCHAR(50),
    description TEXT,
    unit_price DECIMAL(10, 2) NOT NULL CHECK (unit_price >= 0),
    stock_quantity INT NOT NULL CHECK (stock_quantity >= 0)
);

-- 3. Bảng STAFF (Nhân viên)
CREATE TABLE STAFF (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    assigned_task TEXT
);

-- 4. Bảng ORDERS (Đơn hàng)
CREATE TABLE ORDERS (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) DEFAULT 0.00,
    order_status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES CUSTOMERS(customer_id)
);

-- 5. Bảng ORDER_DETAILS (Chi tiết đơn hàng)
CREATE TABLE ORDER_DETAILS (
    detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL, 
    subtotal DECIMAL(10, 2) GENERATED ALWAYS AS (quantity * unit_price) STORED,
    FOREIGN KEY (order_id) REFERENCES ORDERS(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES PRODUCTS(product_id)
);

-- 6. Bảng PAYMENTS (Thanh toán)
CREATE TABLE PAYMENTS (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('Card', 'Transfer', 'COD') NOT NULL,
    payment_status ENUM('Pending', 'Completed', 'Refunded') DEFAULT 'Pending',
    FOREIGN KEY (order_id) REFERENCES ORDERS(order_id)
);

-- 7. Bảng SHIPMENTS (Vận chuyển)
CREATE TABLE SHIPMENTS (
    shipment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    staff_id INT, 
    shipment_date DATETIME,
    delivery_date DATETIME,
    courier_name VARCHAR(50), 
    tracking_number VARCHAR(50),
    shipment_status ENUM('Pending', 'In Transit', 'Delivered', 'Returned') DEFAULT 'Pending',
    FOREIGN KEY (order_id) REFERENCES ORDERS(order_id),
    FOREIGN KEY (staff_id) REFERENCES STAFF(staff_id)
);