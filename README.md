# Online Store Inventory and Supplier Management API

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Run the server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Swagger-Ui Documentation

- **/api/schema/docs/**: Get comprehensive documentation and Testing of the APIs

### Employee Management

- **POST /api/v1/auth/register/**: Register an Employee
- **POST /api/v1/auth/login/**: Login an Employee
- **POST /api/v1/auth/logout/**: Logout an Employee
- **POST /api/v1/auth/profile/employee/{id}**: Get Employee Details

### Inventory Items

- **GET /api/v1/inventory/item/list/**: List all inventory items.
- **POST /api/v1/inventory/item/create/**: Create a new inventory item.
- **GET /api/v1/inventory/item/{id}/**: Retrieve a specific inventory item.
- **PUT /api/v1/inventory/item/{id}/**: Update a specific inventory item.
- **DELETE /api/v1/inventory/item/{id}/**: Delete a specific inventory item.

### Suppliers

- **GET /api/v1/supplier/list/**: List all suppliers.
- **POST /api/v1/supplier/create/**: Create a new supplier.
- **GET /api/v1/supplier/{id}/**: Retrieve a specific supplier.
- **PUT /api/v1/supplier/{id}/**: Update a specific supplier.
- **DELETE /api/v1/supplier/{id}/**: Delete a specific supplier.
