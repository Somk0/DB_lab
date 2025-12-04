CREATE DATABASE IF NOT EXISTS flixbus
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;

USE flixbus;

DROP TABLE IF EXISTS route_stops;
DROP TABLE IF EXISTS stops;
DROP TABLE IF EXISTS routes;
DROP TABLE IF EXISTS buses;
DROP TABLE IF EXISTS bus_types;

CREATE TABLE bus_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE buses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    plate_number VARCHAR(20) NOT NULL UNIQUE,
    capacity INT NOT NULL,
    bus_type_id INT NOT NULL,
    CONSTRAINT fk_buses_bus_types
      FOREIGN KEY (bus_type_id) REFERENCES bus_types(id)
);

CREATE TABLE routes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    from_city VARCHAR(50) NOT NULL,
    to_city VARCHAR(50) NOT NULL
);

CREATE TABLE stops (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city_name VARCHAR(50) NOT NULL
);

CREATE TABLE route_stops (
    route_id INT NOT NULL,
    stop_id INT NOT NULL,
    sequence INT NOT NULL,
    PRIMARY KEY (route_id, stop_id),
    CONSTRAINT fk_route_stops_route
      FOREIGN KEY (route_id) REFERENCES routes(id)
      ON DELETE CASCADE,
    CONSTRAINT fk_route_stops_stop
      FOREIGN KEY (stop_id) REFERENCES stops(id)
      ON DELETE CASCADE
);

INSERT INTO bus_types (name) VALUES
  ('Standard'),
  ('Comfort'),
  ('Premium');

INSERT INTO buses (plate_number, capacity, bus_type_id) VALUES
  ('AA1234AA', 50, 1),
  ('BB5678BB', 60, 2),
  ('CC9012CC', 55, 3);

INSERT INTO routes (name, from_city, to_city) VALUES
  ('Київ — Львів', 'Київ', 'Львів'),
  ('Львів — Варшава', 'Львів', 'Варшава');

INSERT INTO stops (city_name) VALUES
  ('Київ'),
  ('Житомир'),
  ('Рівне'),
  ('Львів'),
  ('Луцьк'),
  ('Варшава');


INSERT INTO route_stops (route_id, stop_id, sequence) VALUES
  (1, 1, 1), 
  (1, 2, 2), 
  (1, 3, 3), 
  (1, 4, 4); 


INSERT INTO route_stops (route_id, stop_id, sequence) VALUES
  (2, 4, 1), 
  (2, 5, 2), 
  (2, 6, 3); 
