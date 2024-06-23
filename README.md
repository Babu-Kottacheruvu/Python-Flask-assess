### Project Name: Task Manager

### Description:
The Task Manager is a web application built using Flask that allows users to manage their tasks. Users can view a list of tasks, add new tasks, mark tasks as complete, and delete tasks.

### Installation:
1. Install Python 3.x on your machine.
2. Install Flask using pip: `pip install flask`.
3. Install MySQL and set up a local database.

### Database Setup:
1. Create a MySQL database named "user".
2. Create a table named "user" with the following columns:
   - id (int, primary key)
   - title (varchar)
   - description (text)
   - due_date (date)
   - status (varchar)
3. Sample SQL queries:
   - Create table:
   `
     CREATE TABLE user (
         id INT AUTO_INCREMENT PRIMARY KEY,
         title VARCHAR(255) NOT NULL,
         description TEXT,
         due_date DATE,
         status VARCHAR(50)
     );
     `
   - Insert sample data:
    `
     INSERT INTO user (title, description, due_date, status)
     VALUES
         ('id 1', 'Description for Task 1', '2024-06-30', 'Incomplete'),
         ('id 2', 'Description for Task 2', '2024-07-05', 'Complete'),
         ('id 3', 'Description for Task 3', '2024-07-10', 'Incomplete');
     `

### Running the Application:
1. Set up the Flask application:
   - Initialize a new Flask application.
   - Define routes for managing tasks (e.g., list tasks, add task, mark task as complete, delete task).
2. Run the Flask application:
   - Use `flask run` to start the Flask development server.

### Routes:
1. `/hello` (GET): Retrun string saying "Hello, World!".
   - Example: `http://localhost:5000/hello`
2. `/users`(GET):Retrives all the details preseint is database called "usersdb"
    -Example: `http://localhost:5000/users`
2. `/tasks/new` (POST): Add a new task.
   - Example: `POST http://localhost:5000/new_user`
3. `/users/<id>` (GET): Retrieve details of a specific task by ID.
   - Example: `http://localhost:5000/users/<id>`


### Contributing:
1. Git Workflow:
   - Initialize a new Git repository for the project.
   - Create a branch for your changes (e.g., `task-manager-feature`).
   - Make commits to your branch as you implement new features or fix bugs.
   - Push your branch to the remote repository.
   - Create a pull request from your branch to the main branch for review.
2. How to Contribute:
   - Fork the repository.
   - Clone the forked repository to your local machine.
   - Create a new branch for your changes.
   - Make your changes and commit them to your branch.
   - Push your branch to your fork on GitHub.
   - Create a pull request from your branch to the main repository's branch.

### License:
This project is released under the MIT License.
