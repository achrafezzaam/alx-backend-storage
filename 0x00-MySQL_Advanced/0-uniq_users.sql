-- Create the users table with the id, email and name columns
CREATE TABLE IF NOT EXISTS `users` (
  id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
);
