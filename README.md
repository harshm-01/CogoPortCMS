# FASTAPI - Configuration Management System (CMS)

## About Project
The API provides endpoints to manage configurations for different countries. It allows creating, retrieving, updating, and deleting configuration settings. Each endpoint is designed to handle specific CRUD operations related to configurations stored in the database.

### Technologies Used
+ FastAPI: FastAPI is used to create the RESTful API endpoints.
+ SQLAlchemy: SQLAlchemy ORM is utilized for database interaction.
+ Python: Python language is used for writing application logic and defining schemas.


## Before we Start
+ To run this project, you need some packages and dependencies listed in the requirements.txt file along with their versions.
+ The project was originally created in a directory named harshCMS. If you're running this project on your system and the directory name is different, it could cause errors. Therefore, before running the project, please double-check all imports in the files.
+ Since we are only submitting an API due to time constraints, creating a dedicated frontend for testing the API is not possible. To verify, you can use the Swagger UI built-in provided by FastAPI for checking our API calls, or you can use any other API platform.
+ Please define all necessary key-value pairs in the .env files wherever required.

## API Documentation for Country-Specific Configurations

**Endpoints:**

**1. `/`**
   - This is the starting point of my API, representing details about me.

**2. `POST /create_configuration`**
   - This endpoint will create different configurations for various countries using a POST request.
   - **Request Body:**
     - `country_code` (string): A unique and non-nullable string representing the country code. While country codes are usually two characters, for simplicity, it is stored as a string.
     - `business_name` (string, optional): The business name of the company, which can be considered a string. Typically, this is required for any country.
     - `registration_numbers` (object): This stores the required configurations such as SSN, PAN numbers, GSTIN, etc., specific to each country as keys. Each key has a Boolean value indicating whether it is mandatory for users to provide these details.
     - `additional_data` (object): Similar to `registration_numbers`, this stores required configurations such as address, owner details, etc., specific to each country as keys. Each key has a Boolean value indicating whether it is mandatory for users to provide these details.
   - You can pass as many fields as needed.
   - These data are stored in JSON format in the table.

**3. `GET /get_all_configurations`**
   - This endpoint retrieves all the created configurations present in the table.

**4. `GET /get_configuration/{country}`**
   - This endpoint retrieves the configuration for a specific country. The country code must be provided in the endpoint.

**5. `DELETE /configuration/{country}`**
   - This endpoint deletes the configuration for a country upon providing the country code.

**6. `POST /update_configuration/{country}`**
   - This endpoint updates parameters such as the business name, and adds or deletes fields in `registration_numbers` and `additional_data` for a country. The country code must be provided.
   - If the country code is accidentally changed, it will not be updated in the database. Only other fields will be changed, keeping the country code intact.


**The solution focuses on:**
1. Utilizing PostgreSQL as the relational database management system.
2. Employing SQLAlchemy as the Object-Relational Mapper (ORM) to interact with the database in a Pythonic way.
3. Defining SQLAlchemy models for above requirements
4. Designing FastAPI endpoints for CRUD operations on both Book and Category entities
5. Employing Pydantic data models (schemas) to define the request and response data structures for each endpoint, ensuring data validation and type safety.
6. Implementing comprehensive error handling using FastAPI's built-in exception handling mechanisms. This should include handling potential database errors, validation errors, and other application-specific exceptions.

