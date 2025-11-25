USE ecommerce_db;

-- 1. Chèn STAFF
INSERT INTO STAFF (full_name, role, phone_number, email, assigned_task) VALUES 
('Nguyen Van Quan', 'Logistics', '0901111111', 'quan.logistics@shop.com', 'Manage warehouse outbound'),
('Tran Thi Mai', 'Customer Support', '0902222222', 'mai.support@shop.com', 'Handle returns'),
('Le Van Hung', 'Shipper', '0903333333', 'hung.ship@shop.com', 'District 1 Delivery'),
('Pham Thu Ha', 'Finance', '0904444444', 'ha.finance@shop.com', 'Audit payments'),
('Hoang Van Nam', 'Manager', '0905555555', 'nam.manager@shop.com', 'General operations');

-- 2. Chèn CUSTOMERS
INSERT INTO CUSTOMERS (full_name, email, phone_number, address) VALUES 
('Nguyen Van A', 'vana@gmail.com', '0912345678', '123 Le Loi, HCM'),
('Tran Thi B', 'thib@gmail.com', '0987654321', '456 Nguyen Hue, HCM'),
('Le Van C', 'vanc@gmail.com', '0909090909', '789 Hai Ba Trung, Hanoi'),
('Pham Thi D', 'thid@gmail.com', '0911111111', '12 Tran Hung Dao, Danang'),
('Hoang Van E', 'vane@gmail.com', '0922222222', '34 Le Duan, Hue'),
('Do Thi F', 'thif@gmail.com', '0933333333', '56 Pasteur, HCM'),
('Bui Van G', 'vang@gmail.com', '0944444444', '78 Cach Mang Thang 8, Can Tho'),
('Dang Thi H', 'thih@gmail.com', '0955555555', '90 Vo Van Kiet, HCM'),
('Vu Van I', 'vani@gmail.com', '0966666666', '11 Dien Bien Phu, Hanoi'),
('Ngo Thi K', 'thik@gmail.com', '0977777777', '22 Ly Tu Trong, HCM');

-- 3. Chèn PRODUCTS
INSERT INTO PRODUCTS (product_name, category, unit_price, stock_quantity) VALUES 
('iPhone 15 Pro', 'Electronics', 25000000, 50),
('Samsung Galaxy S24', 'Electronics', 20000000, 40),
('MacBook Air M2', 'Electronics', 28000000, 30),
('Dell XPS 13', 'Electronics', 30000000, 20),
('Sony WH-1000XM5', 'Accessories', 8000000, 100),
('Logitech MX Master 3', 'Accessories', 2500000, 150),
('Mechanical Keyboard', 'Accessories', 1500000, 200),
('Gaming Monitor 27"', 'Electronics', 7000000, 25),
('Office Chair', 'Furniture', 3000000, 15),
('Wooden Desk', 'Furniture', 2000000, 10),
('Men T-Shirt', 'Fashion', 200000, 500),
('Women Dress', 'Fashion', 500000, 300),
('Running Shoes', 'Fashion', 1200000, 100),
('Backpack', 'Fashion', 800000, 80),
('Smart Watch', 'Electronics', 5000000, 60);

-- 4. Chèn ORDERS
INSERT INTO ORDERS (customer_id, order_date, order_status) VALUES 
(1, '2023-10-01 08:00:00', 'Delivered'), (2, '2023-10-02 09:00:00', 'Delivered'), 
(3, '2023-10-03 10:00:00', 'Shipped'), (4, '2023-10-04 11:00:00', 'Pending'),
(5, '2023-10-05 12:00:00', 'Cancelled'), (1, '2023-10-06 13:00:00', 'Delivered'),
(2, '2023-10-07 14:00:00', 'Delivered'), (3, '2023-10-08 15:00:00', 'Shipped'),
(4, '2023-10-09 16:00:00', 'Pending'), (5, '2023-10-10 17:00:00', 'Cancelled'),
(6, '2023-10-11 08:30:00', 'Delivered'), (7, '2023-10-12 09:30:00', 'Delivered'),
(8, '2023-10-13 10:30:00', 'Shipped'), (9, '2023-10-14 11:30:00', 'Pending'),
(10, '2023-10-15 12:30:00', 'Delivered'), (1, '2023-10-16 13:30:00', 'Delivered'),
(2, '2023-10-17 14:30:00', 'Shipped'), (3, '2023-10-18 15:30:00', 'Pending'),
(4, '2023-10-19 16:30:00', 'Delivered'), (5, '2023-10-20 17:30:00', 'Cancelled'),
(6, '2023-10-21 08:15:00', 'Delivered'), (7, '2023-10-22 09:15:00', 'Delivered'),
(8, '2023-10-23 10:15:00', 'Shipped'), (9, '2023-10-24 11:15:00', 'Pending'),
(10, '2023-10-25 12:15:00', 'Delivered'), (1, '2023-10-26 13:15:00', 'Delivered'),
(2, '2023-10-27 14:15:00', 'Shipped'), (3, '2023-10-28 15:15:00', 'Pending'),
(4, '2023-10-29 16:15:00', 'Delivered'), (5, '2023-10-30 17:15:00', 'Cancelled');

-- 5. Chèn ORDER_DETAILS
INSERT INTO ORDER_DETAILS (order_id, product_id, quantity, unit_price) VALUES 
(1, 1, 1, 25000000), (1, 5, 2, 8000000),
(2, 2, 1, 20000000), (2, 6, 1, 2500000),
(3, 11, 5, 200000), (3, 13, 1, 1200000),
(4, 15, 1, 5000000), (5, 3, 1, 28000000),
(6, 7, 10, 1500000), (6, 8, 1, 7000000),
(7, 4, 1, 30000000), (7, 6, 2, 2500000),
(8, 9, 2, 3000000), (8, 10, 1, 2000000),
(9, 12, 3, 500000), (10, 1, 1, 25000000),
(11, 14, 2, 800000), (11, 11, 2, 200000),
(12, 2, 1, 20000000), (12, 5, 1, 8000000),
(13, 15, 2, 5000000), (14, 3, 1, 28000000), (14, 6, 1, 2500000),
(15, 7, 5, 1500000), (16, 8, 2, 7000000), (16, 1, 1, 25000000),
(17, 4, 1, 30000000), (18, 9, 1, 3000000), (18, 10, 1, 2000000), (18, 5, 1, 8000000),
(19, 12, 2, 500000), (19, 13, 1, 1200000),
(20, 2, 1, 20000000), (21, 11, 10, 200000),
(22, 14, 1, 800000), (22, 15, 1, 5000000),
(23, 6, 5, 2500000),
(24, 1, 1, 25000000), (24, 5, 1, 8000000), (24, 7, 1, 1500000),
(25, 3, 1, 28000000), (26, 4, 1, 30000000), (26, 6, 2, 2500000),
(27, 8, 1, 7000000), (28, 9, 4, 3000000),
(29, 10, 2, 2000000), (29, 11, 5, 200000),
(30, 1, 2, 25000000);

-- Tính tổng tiền
UPDATE ORDERS o
SET total_amount = (
    SELECT IFNULL(SUM(subtotal), 0) 
    FROM ORDER_DETAILS od 
    WHERE od.order_id = o.order_id
);

-- 6. Chèn PAYMENTS
INSERT INTO PAYMENTS (order_id, amount, payment_method, payment_status) VALUES 
(1, 41000000, 'Card', 'Completed'), (2, 22500000, 'Transfer', 'Completed'),
(3, 2200000, 'COD', 'Completed'), (4, 5000000, 'Card', 'Pending'),
(5, 28000000, 'Card', 'Refunded'), (6, 22000000, 'Transfer', 'Completed'),
(7, 35000000, 'Card', 'Completed'), (8, 8000000, 'COD', 'Completed'),
(9, 1500000, 'Card', 'Pending'), (10, 25000000, 'Transfer', 'Refunded'),
(11, 2000000, 'COD', 'Completed'), (12, 28000000, 'Card', 'Completed'),
(13, 10000000, 'Transfer', 'Completed'), (14, 30500000, 'Card', 'Pending'),
(15, 7500000, 'COD', 'Completed'), (16, 39000000, 'Card', 'Completed'),
(17, 30000000, 'Transfer', 'Completed'), (18, 13000000, 'Card', 'Pending'),
(19, 2200000, 'COD', 'Completed'), (20, 20000000, 'Transfer', 'Refunded'),
(21, 2000000, 'Card', 'Completed'), (22, 5800000, 'COD', 'Completed'),
(23, 12500000, 'Transfer', 'Completed'), (24, 34500000, 'Card', 'Pending'),
(25, 28000000, 'Card', 'Completed'), (26, 35000000, 'Transfer', 'Completed'),
(27, 7000000, 'COD', 'Completed'), (28, 12000000, 'Card', 'Pending'),
(29, 5000000, 'Transfer', 'Completed'), (30, 50000000, 'Card', 'Refunded');

-- 7. Chèn SHIPMENTS
INSERT INTO SHIPMENTS (order_id, staff_id, shipment_date, delivery_date, courier_name, tracking_number, shipment_status) VALUES 
(1, 3, '2023-10-01 10:00:00', '2023-10-03 10:00:00', 'GiaoHangNhanh', 'GHN001', 'Delivered'),
(2, 3, '2023-10-02 10:00:00', '2023-10-04 10:00:00', 'ViettelPost', 'VT002', 'Delivered'),
(3, 1, '2023-10-03 12:00:00', NULL, 'GrabExpress', 'GRB003', 'In Transit'),
(6, 3, '2023-10-06 14:00:00', '2023-10-08 14:00:00', 'GiaoHangNhanh', 'GHN004', 'Delivered'),
(7, 3, '2023-10-07 14:00:00', '2023-10-09 14:00:00', 'ViettelPost', 'VT005', 'Delivered'),
(8, 1, '2023-10-08 16:00:00', NULL, 'GiaoHangTietKiem', 'GHTK006', 'In Transit'),
(11, 3, '2023-10-11 09:00:00', '2023-10-13 09:00:00', 'GiaoHangNhanh', 'GHN007', 'Delivered'),
(12, 3, '2023-10-12 10:00:00', '2023-10-14 10:00:00', 'ViettelPost', 'VT008', 'Delivered'),
(13, 1, '2023-10-13 11:00:00', NULL, 'GrabExpress', 'GRB009', 'In Transit'),
(15, 3, '2023-10-15 13:00:00', '2023-10-17 13:00:00', 'GiaoHangNhanh', 'GHN010', 'Delivered'),
(16, 3, '2023-10-16 14:00:00', '2023-10-18 14:00:00', 'ViettelPost', 'VT011', 'Delivered'),
(17, 1, '2023-10-17 15:00:00', NULL, 'GiaoHangTietKiem', 'GHTK012', 'In Transit'),
(19, 3, '2023-10-19 17:00:00', '2023-10-21 17:00:00', 'GiaoHangNhanh', 'GHN013', 'Delivered'),
(21, 3, '2023-10-21 09:00:00', '2023-10-23 09:00:00', 'ViettelPost', 'VT014', 'Delivered'),
(22, 3, '2023-10-22 10:00:00', '2023-10-24 10:00:00', 'GrabExpress', 'GRB015', 'Delivered'),
(23, 1, '2023-10-23 11:00:00', NULL, 'GiaoHangNhanh', 'GHN016', 'In Transit'),
(25, 3, '2023-10-25 13:00:00', '2023-10-27 13:00:00', 'ViettelPost', 'VT017', 'Delivered'),
(26, 3, '2023-10-26 14:00:00', '2023-10-28 14:00:00', 'GiaoHangTietKiem', 'GHTK018', 'Delivered'),
(27, 1, '2023-10-27 15:00:00', NULL, 'GiaoHangNhanh', 'GHN019', 'In Transit'),
(29, 3, '2023-10-29 17:00:00', '2023-10-31 17:00:00', 'ViettelPost', 'VT020', 'Delivered');