CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100)
);

INSERT INTO employees (name, position) VALUES 
('John Doe', 'Developer'),
('Jane Smith', 'Manager'),
('Bob Johnson', 'HR');
