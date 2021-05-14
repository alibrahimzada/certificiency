CREATE TABLE customers(
   customer_id serial PRIMARY KEY,
   customer_name VARCHAR (255) UNIQUE NOT NULL,
   is_active BOOLEAN NOT NULL,
   created_on TIMESTAMP NOT NULL,
   company_permissions JSON NOT NULL,
   is_deleted BOOLEAN NOT NULL
);

CREATE TABLE roles(
   role_id serial PRIMARY KEY,
   role_name VARCHAR (255) UNIQUE NOT NULL,
   role_permissions JSON NOT NULL,
   customer_id INT NOT NULL,
   FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
   is_deleted BOOLEAN NOT NULL
);

CREATE TABLE users (
   user_id serial PRIMARY KEY,
   username VARCHAR ( 50 ) UNIQUE NOT NULL,
   password VARCHAR ( 100 ) NOT NULL,
   first_name VARCHAR ( 500 ) NOT NULL,
   last_name VARCHAR ( 500 ) NOT NULL,
   customer_id INT NOT NULL,
   role_id INT NOT NULL,
   is_active BOOLEAN NOT NULL,
   email VARCHAR ( 255 ) UNIQUE NOT NULL,
   created_on TIMESTAMP NOT NULL,
   last_login TIMESTAMP,
   FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
   FOREIGN KEY (role_id) REFERENCES roles (role_id),
   is_deleted BOOLEAN NOT NULL
);

CREATE TABLE event_categories (
   event_category_id serial PRIMARY KEY,
   event_category_name VARCHAR (100) NOT NULL,
   is_deleted BOOLEAN NOT NULL
 );

CREATE TABLE events (
   event_id serial PRIMARY KEY,
   event_name VARCHAR ( 100 ) NOT NULL,
   event_category_id INT NOT NULL,
   event_location VARCHAR ( 100 ),
   event_thumbnail VARCHAR ( 500 ),
   event_link VARCHAR ( 100 ),
   FOREIGN KEY (event_category_id) REFERENCES event_categories (event_category_id),
   is_deleted BOOLEAN NOT NULL
);


CREATE TABLE applications (
   application_id serial PRIMARY KEY,
   event_id INT NOT NULL,
   user_id INT NOT NULL,
   applied_on TIMESTAMP NOT NULL,
   application_status INT NOT NULL,
   is_deleted BOOLEAN NOT NULL,
   FOREIGN KEY (event_id) REFERENCES events (event_id),
   FOREIGN KEY (user_id) REFERENCES users (user_id)
);

CREATE TABLE certificates (
   certificate_id serial PRIMARY KEY,
   certified_on TIMESTAMP NOT NULL,
   application_id INT NOT NULL,
   certificate_link VARCHAR ( 255 ) NOT NULL,
   certificate_properties JSON NOT NULL,
   is_public BOOLEAN NOT NULL,
   is_deleted BOOLEAN NOT NULL,
   FOREIGN KEY (application_id) REFERENCES applications (application_id)	
);