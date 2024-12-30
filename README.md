# CODTECH-PP-Task2
---

# Inventory Management System  

## Internship Details  
- **Name:** Aditya Kumar  
- **Company:** CODTECH IT SOLUTIONS  
- **Intern ID:** CT6WDS2357  
- **Domain:** Python Programming  
- **Duration:** NOV 15th, 2024 to DEC 30th, 2024  
- **Mentor:** Neela Santhosh Kumar

---

## About the Project  
The **Inventory Management System** is a Python-based desktop application developed using `Tkinter`, `MySQL`, and the `smtplib` library. This system is designed to streamline inventory management processes, featuring dual user roles—**Admin** and **Employee**—to ensure efficient handling of operations.  

---

## Features  

### Admin Features  
1. **Supplier Management:**  
   - Add new suppliers.  
   - Activate or deactivate suppliers.  

2. **Product Management:**  
   - Add new products.  
   - Activate or deactivate products.  

3. **Sales Monitoring:**  
   - View and analyze sales charts.  

4. **User Management:**
   - Add New User (Admin/Employee)
   - Reset passwords for admin and employees using the SMTP mail feature.
   

### Employee Features  
1. **Cart and Sales Management:**  
   - Add items to a cart for customers.  
   - Enter customer details (name and mobile number).  
   - Generate and print/save the bill.  

---

## Highlights  
- **Dual User Roles:**  
  - **Admin**: Focused on inventory and supplier management, and monitoring overall sales performance.  
  - **Employee**: Handles customer transactions and billing.  

- **Secure Login and Password Reset:**  
  - Integrated `smtplib` for email-based password recovery.  

- **Database Integration:**  
  - Powered by `MySQL` for efficient data storage and retrieval.  

- **Sales Analysis:**  
  - Admins can visualize sales trends with integrated charts.  

- **Interactive GUI:**  
  - Built with `Tkinter`, providing a clean and user-friendly interface.  

- **Billing System:**  
  - Employees can generate and save printable bills for customers.  

---

## Tech Stack  
- **Frontend:** Tkinter (Python GUI Library)  
- **Backend:** MySQL for database operations  
- **Additional Libraries:**  
  - `smtplib` for email integration  
  - `matplotlib` (if used for sales chart visualization)  

---

## How to Run  

### Prerequisites  
1. **Install Python**: Ensure Python is installed on your system.  
2. **Install Required Libraries**:  
   ```bash
   pip install mysql-connector-python
   pip install matplotlib  # If sales charts are included
   ```

3. **Set Up MySQL Database**:  
   - Create a MySQL database for the system.  
   - Run the provided `.sql` script to set up tables and initial data (if provided).  

4. **Email Configuration**:  
   - Update the SMTP settings in the code with your email credentials for password recovery.

---

### Steps to Run  
1. Clone the repository:  
   ```bash
   git clone https://github.com/aditya-kr86/CODTECH-PP-Task2.git
   cd CODTECH-PP-Task1
   ```

2. Launch the application:  
   ```bash
   python dashboard.py
   ```

3. Log in as **Admin** or **Employee** to access respective features.  

---

## Screenshots  
![10](https://github.com/user-attachments/assets/3cb96b0e-571f-464b-b1ab-a63954fbdc92)
![11](https://github.com/user-attachments/assets/aa2c3a55-aaba-4206-99f5-fa6ca4ad4d27)
![12](https://github.com/user-attachments/assets/c2705c29-b247-4190-8cee-c63fa19b5b21)
![13](https://github.com/user-attachments/assets/3360ba0b-67c1-404a-8281-f884044de16a)
![14](https://github.com/user-attachments/assets/5a357f01-08ba-472a-8441-e5b656387ccc)
![15](https://github.com/user-attachments/assets/77e2d5ce-c809-42da-9883-6feedbdc7ec0)
![16](https://github.com/user-attachments/assets/a7473775-dc08-43dc-8cb6-38eac94c715b)
![17](https://github.com/user-attachments/assets/e981d4de-51e4-4303-930c-31743720e9f4)







---

### Thank You!  
This project was an incredible learning experience in managing roles, integrating databases, and developing feature-rich applications. I’m looking forward to feedback and suggestions for improvements!  

---
