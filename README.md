## 🔧 Selenium Test Automation for "E-Commerce Website" ##

# 🌐 Project Overview

This repository contains **automated UI and functional test scripts** developed using **Python, Selenium WebDriver**, and the **Page Object Model (POM)** for:

🔗 [E-Commerce Website](https://www.automationexercise.com)

> This E-Commerce demo site is designed for practicing web automation. It simulates a real-world shopping experience with user registration, login, product browsing, cart management, and contact forms — making it ideal for learning and showcasing UI automation skills.

---

## ✅ What This Project Covers

I created **modular, reusable test scripts for each main page and functionality** of the website. Each script focuses on:

- ✅ Functional testing of forms, buttons, and cart features  
- ✅ UI element presence and validation  
- ✅ Modal popups and alert handling  
- ✅ Positive and negative user flows  
- ✅ Page navigation and redirection testing  
- ✅ Full test coverage of user registration and login process  

Test scripts are structured using the **Page Object Model (POM)** design pattern for easy maintenance and code reuse.

---

## 📄 Pages and Features Tested

Scripts were written individually for the following pages and components:

- 🏠 **Home Page** — Page load, logo, header, and navigation  
- 🛍 **Products Page** — Add to cart, product visibility, modal behavior  
- 🛒 **Cart Page** — Product verification, quantity, removal, checkout modal  
- 📝 **Signup Page** — Registration with valid and invalid data  
- 🔐 **Login Page** — Login with valid/invalid credentials  
- 📤 **Contact Us Page** — Form submission and validation  
---

## 🧾 Test Case Documentation

All **manual test cases** are well-organized in the file below:

📄 [`Test_cases.md`](./Test_cases.md)

This document includes:

- Input field validations  
- Modal handling and redirections  
- Button behavior and link testing  
- Positive/negative test cases  
- Page-specific test scenarios  
- Cart and form interaction flows  

---

## 🧰 Tech Stack Used

| Tool/Library         | Description                             |
|----------------------|-----------------------------------------|
| 🐍 Python 3.x         | Main programming language               |
| 🧪 Selenium WebDriver | Browser automation framework            |
| 🧱 POM Pattern        | Structured and scalable automation      |
| 🧪 Pytest             | Test execution framework                |
| 🌐 ChromeDriver       | For automated testing in Chrome         |
| 🧩 GitHub             | Version control and collaboration       |

---

## 📁 Project Structure

Ecommerce-UI-Testing/
│
├── tests/                            # ✅ Test scripts (test_*.py)
│   ├── home_test.py
│   ├── products_test.py
│   ├── cart_test.py
│   ├── signup_test.py
│   ├── login_test.py
│   └── contact_us_test.py
│
├── pages/                            # 📄 Page Object classes (one per page)
│   ├── home_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── signup_page.py
│   ├── login_page.py
│   └── contact_us_page.py
│
├── Test_cases.md                     # 🧪 Manual test case documentation
├── requirements.txt                  # 📦 Python dependencies
├── README.md                         # 📘 Project overview and usage guide
└── .gitignore                        # 🚫 Ignored files and folders

---

## 🚀 How to Run the Tests

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ecommerce-ui-testing.git
   cd ecommerce-ui-testing
