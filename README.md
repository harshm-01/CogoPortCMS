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


**The solution focuses on:**
1. Utilizing PostgreSQL as the relational database management system.
2. Employing SQLAlchemy as the Object-Relational Mapper (ORM) to interact with the database in a Pythonic way.
3. Defining SQLAlchemy models for above requirements
4. Designing FastAPI endpoints for CRUD operations on both Book and Category entities
5. Employing Pydantic data models (schemas) to define the request and response data structures for each endpoint, ensuring data validation and type safety.
6. Implementing comprehensive error handling using FastAPI's built-in exception handling mechanisms. This should include handling potential database errors, validation errors, and other application-specific exceptions.

