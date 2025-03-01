# **FastAPI Microservices Hub 🚀**

A **FastAPI-based microservices architecture** for managing **customers, invoices, and products** using **SQLite, SQLAlchemy, and Docker**. The project is fully **Dockerized** and supports **asynchronous testing** with `pytest`.

## **Project Overview**
This project consists of **three microservices**:
- **Customer Service** (`port 80`) - Manages customers
- **Invoice Service** (`port 81`) - Handles invoices
- **Product Service** (`port 82`) - Manages products

Each service is **containerized with Docker**, has **independent SQLite databases**, and exposes **REST APIs**.

---

## **Installation**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/fastapi-microservices-hub.git
cd fastapi-microservices-hub
```

### **2️⃣ Set Up Virtual Environment**
```sh
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### **3️⃣ Running Services Locally (Without Docker)**
#### **Customer Service**
```sh
cd microservices/customer_service
uvicorn main:app --reload --port 80
```

#### **Invoice Service**
```sh
cd microservices/invoice_service
uvicorn main:app --reload --port 81
```

#### **Product Service**
```sh
cd microservices/product_service
uvicorn main:app --reload --port 82
```

---

## **Running with Docker 🐳**
Each microservice has its own **Dockerfile**.

### **Building and Running Services**
Navigate into each microservice folder and run:

#### **Customer Service**
```sh
cd microservices/customer_service
docker build -t service1 .
docker run -d --name service1 -p 80:80 service1
```

#### **Invoice Service**
```sh
cd microservices/invoice_service
docker build -t service2 .
docker run -d --name service2 -p 81:81 service2
```

#### **Product Service**
```sh
cd microservices/product_service
docker build -t service3 .
docker run -d --name service3 -p 82:82 service3
```

---

## **Database Migration**
Since we are using SQLite, database tables are **automatically created** when the FastAPI app starts.

However, if you need to reset the database:
```sh
rm -f microservices/customer_service/database.db
rm -f microservices/invoice_service/database.db
rm -f microservices/product_service/database.db
```

Then restart the services.

---

## **API Documentation (Swagger UI)**
Once the services are running, access Swagger Docs:

- [Customer Service](http://localhost:80/docs)
- [Invoice Service](http://localhost:81/docs)
- [Product Service](http://localhost:82/docs)

---

## **CRUD Endpoints**
Each microservice exposes RESTful CRUD endpoints.

### **Customer Service (`/customers`)**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/customers/` | Create a customer |
| `GET` | `/customers/` | List all customers |
| `GET` | `/customers/{customer_id}` | Get a customer by ID |
| `PATCH` | `/customers/{customer_id}` | Update customer info |
| `DELETE` | `/customers/{customer_id}` | Delete a customer |

### **Invoice Service (`/invoices`)**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/invoices/` | Create an invoice |
| `GET` | `/invoices/` | List all invoices |
| `GET` | `/invoices/{invoice_id}` | Get an invoice by ID |
| `PATCH` | `/invoices/{invoice_id}` | Update invoice info |
| `DELETE` | `/invoices/{invoice_id}` | Delete an invoice |

### **Product Service (`/products`)**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/products/` | Create a product |
| `GET` | `/products/` | List all products |
| `GET` | `/products/{product_id}` | Get a product by ID |
| `PATCH` | `/products/{product_id}` | Update product info |
| `DELETE` | `/products/{product_id}` | Delete a product |

---

## **Contributing**
All contributions are welcome.
---

## **License**
📝 MIT License. Feel free to use and modify this project!

---

