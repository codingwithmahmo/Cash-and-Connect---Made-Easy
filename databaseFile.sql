-- Create database
CREATE DATABASE BankManagement;

USE BankManagement;

-- Users table
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    cnic VARCHAR(15) UNIQUE NOT NULL,
    account_balance DECIMAL(15, 2) DEFAULT 0.00,
    role ENUM('customer', 'admin') NOT NULL
);

-- Transactions table
CREATE TABLE Transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    transaction_type ENUM('deposit', 'withdrawal', 'transfer') NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    target_account INT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- Loans table
CREATE TABLE Loans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    loan_amount DECIMAL(15, 2) NOT NULL,
    status ENUM('approved', 'pending', 'declined') DEFAULT 'pending',
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

