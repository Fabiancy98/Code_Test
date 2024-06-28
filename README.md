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

### Authentication

- The API uses JWT (JSON Web Token) for authentication. Include the token in the Authorization header as Bearer TOKEN.

### Swagger-Ui Documentation

- **/api/schema/docs/**: Get comprehensive documentation and Testing of the APIs

### Employee Management

#### Endpoints

##### POST /api/v1/auth/login/:

    Description: Endpoint for Employee login.
    Request Body: JSON, x-www-form-urlencoded, multipart/form-data

```bash
      {
      "email": "string",
      "password": "string"
      }
```

Response:

```bash
   {
   "email": "string",
   "access_token": "string",
   "refresh_token": "string",
   "id": "string"
   }
```

##### POST /api/v1/auth/logout/:

    Description: Endpoint for user logout.
    Request Body: JSON, x-www-form-urlencoded, multipart/form-data

```bash
   {
   "refresh_token": "string"
   }
```

Response:

```bash
   {
   "message": "logged out succesfully"
   }
```

##### POST /api/v1/auth/register/:

    Description: Endpoint for user registration.
    Request Body: JSON, x-www-form-urlencoded, multipart/form-data

```bash
      {
      "email": "string",
      "password": "string",
      "password2": "string",
      "first_name": "string",
      "last_name": "string",
      "branch": "string",
      "country": "string",
      "state": "string",
      "phone_number": "string|max10chars"
      }
```

Response:

```bash
   {
      "message": "hi {first_name} thanks for signing up"
   }
```

##### GET /api/v1/auth/profile/employee/{id}:

    Description: Retrieve employee profile by ID.
    Path Parameters:

       id (string): Employee ID

Response:

```bash
      {
         "email": "string",
         "password": "string",
         "password2": "string",
         "first_name": "string",
         "last_name": "string",
         "branch": "string",
         "country": "string",
         "state": "string",
         "phone_number": "string|max10chars"
      }
```

##### PUT /api/v1/auth/profile/employee/{id}

    Description: Update employee profile by ID.
    Path Parameters:
        id (string): Employee ID
    Request Body: JSON, x-www-form-urlencoded, multipart/form-data

```bash
      {
         "email": "string",
         "password": "string",
         "password2": "string",
         "first_name": "string",
         "last_name": "string",
         "branch": "string",
         "country": "string",
         "state": "string",
         "phone_number": "string"
      }
```

Response:

```bash
   {
      "message": "Employee profile sucessfully updated"
   }
```

### Inventory Items

##### GET /api/v1/inventory/item/list/:

Description: Retrieve list of all items along with all the suppliers that supply the item
Response:

```bash
   [
      {
      "id": "integer",
      "name": "string",
      "description": "string",
      "price": "string"
      }
   ]
```

##### POST /api/v1/inventory/item/create/:

Description: Create a new item.
Request Body: JSON, x-www-form-urlencoded, multipart/form-data

```bash
   {
      "name": "string",
      "description": "string",
      "price": "string",
      "suppliers": []
   }
```

Response:

```bash
   {
   "message": "Item <item_name> created successfully"
   }
```

##### GET /api/v1/inventory/item/{id}/:

Description: Retrieve supplier details by ID.
Path Parameters:

      id (integer): Supplier ID

Response:

```bash
[
   {
      "id": "integer",
      "name": "string",
      "description": "string",
      "price": "string",
      "created_at": "date",
      "updated_at": "date",
      "suppliers": []
   }
]
```

##### PUT /api/v1/inventory/item/{id}/:

Description: Update item details by ID.
Path Parameters:

            id (integer): Item ID

Request Body: JSON, x-www-form-urlencoded, multipart/form-data

      ```bash
      {
         "id": "integer",
         "name": "string",
         "description": "string",
         "price": "string",
         "suppliers": []
      }

      ```

Response:

```bash
{
"msg": "Item <item_name> successfully updated"
}
```

##### DELETE /api/v1/inventory/item/{id}/:

    Description: Delete item by ID.
    Path Parameters:
        id (integer): Item ID

    Response:
    ```bash
      {
         "msg": "Item <item_name> successfully deleted"
      }```

### Suppliers

##### GET /api/v1/supplier/list/:

#### POST /api/v1/supplier/create/\*\*: Create a new supplier.

Description: Update supplier details by ID.

Request Body: JSON, x-www-form-urlencoded, multipart/form-data

      ```bash
      {
         "name": "string",
         "email": "string",
         "phone_number": "string",
         "address": "string"
      }```

Response:

#### GET /api/v1/supplier/{id}/\*\*: Retrieve a specific supplier.

Description: Retrieve supplier details by ID.
Path Parameters:

      id (integer): Supplier ID

Response:

```bash
{
"id": "integer",
"name": "string",
"email": "string",
"phone_number": "string",
"address": "string",
"items": []
}
```

#### PUT /api/v1/supplier/{id}/:

      Description: Update supplier details by ID.
      Path Parameters:

         id (integer): Supplier ID

      Request Body: JSON, x-www-form-urlencoded, multipart/form-data

      ```bash
      {
         "name": "string",
         "email": "string",
         "phone_number": "string",
         "address": "string"
      }

````

Response:

```bash{
   "message": Supplier {instance.n sucessfully updated
   }
````

- **DELETE /api/v1/supplier/{id}/**: Delete a specific supplier.
  Description: Delete item by ID.
  Path Parameters:
  id (integer): Item ID
  Response:

```bash{
   "message": Supplier {instance.name} sucessfully deleted
   }

```
