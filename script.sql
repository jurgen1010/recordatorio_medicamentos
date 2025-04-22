CREATE DATABASE IF NOT EXISTS recordatorio_salud;
USE recordatorio_salud;

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    contraseña VARCHAR(255) NOT NULL
);

--Tabla medicamentos con clave foranea dentro de Medicamentos
CREATE TABLE IF NOT EXISTS categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);


-- Tabla de medicamentos con clave foránea a usuarios
CREATE TABLE IF NOT EXISTS medicamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    dosis VARCHAR(50),
    duracion INT NOT NULL, -- duración del tratamiento en días
    usuario_id INT,
    categoria_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE SET NULL
);

--Tabla recordatorios con clave foranea a Medicamentos
CREATE TABLE IF NOT EXISTS recordatorios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    medicamento_id INT NOT NULL,
    fecha_hora DATETIME NOT NULL,
    estado ENUM('pendiente', 'completado') DEFAULT 'pendiente',
    FOREIGN KEY (medicamento_id) REFERENCES medicamentos(id) ON DELETE CASCADE
);

--Tabla notificaciones con clave foranea a Usuarios
CREATE TABLE IF NOT EXISTS notificaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    mensaje TEXT NOT NULL,
    fecha_hora DATETIME NOT NULL,
    leido BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

--Tabla Historial medicamentos con clave foranea a Medicamentos y Usuarios
CREATE TABLE IF NOT EXISTS historial_medicamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    medicamento_id INT NOT NULL,
    fecha_hora DATETIME NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (medicamento_id) REFERENCES medicamentos(id) ON DELETE CASCADE
);

--Tabla doctores con clave foranea a Usuarios
CREATE TABLE IF NOT EXISTS doctores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100),
    telefono VARCHAR(15),
    correo VARCHAR(100) UNIQUE
);

--Tabla recetas con clave foranea a Doctores y Usuarios
CREATE TABLE IF NOT EXISTS recetas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    doctor_id INT NOT NULL,
    fecha DATETIME NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctores(id) ON DELETE CASCADE
);

--Tabla medicamentos recetas, relacion entre Recetas y Medicamentos
CREATE TABLE IF NOT EXISTS medicamentos_recetas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    receta_id INT NOT NULL,
    medicamento_id INT NOT NULL,
    FOREIGN KEY (receta_id) REFERENCES recetas(id) ON DELETE CASCADE,
    FOREIGN KEY (medicamento_id) REFERENCES medicamentos(id) ON DELETE CASCADE
);

--Tabla farmacias
CREATE TABLE IF NOT EXISTS farmacias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(15)
);

--Tabla medicamentos en farmacias, relacion entre Farmacias y Medicamentos
CREATE TABLE IF NOT EXISTS medicamentos_farmacias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    farmacia_id INT NOT NULL,
    medicamento_id INT NOT NULL,
    precio DECIMAL(10, 2),
    stock INT DEFAULT 0,
    FOREIGN KEY (farmacia_id) REFERENCES farmacias(id) ON DELETE CASCADE,
    FOREIGN KEY (medicamento_id) REFERENCES medicamentos(id) ON DELETE CASCADE
);

--Tabla configuraciones de usuarios con clave foranea a Usarios
CREATE TABLE IF NOT EXISTS configuraciones_usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    recibir_notificaciones BOOLEAN DEFAULT TRUE,
    zona_horaria VARCHAR(50) DEFAULT 'UTC',
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

--Tabla horarios medicamentos con clave foranea a Medicamentos
CREATE TABLE IF NOT EXISTS horarios_medicamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    medicamento_id INT NOT NULL,
    hora TIME NOT NULL,
    FOREIGN KEY (medicamento_id) REFERENCES medicamentos(id) ON DELETE CASCADE
);

--Tabla Contactos emergencia con clave foranea a Usuarios
CREATE TABLE IF NOT EXISTS contactos_emergencia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    relacion VARCHAR(50),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

INSERT INTO usuarios (nombre, correo, contraseña) VALUES
('Ana López', 'ana.lopez@example.com', 'clave123'),
('Carlos Ruiz', 'carlos.ruiz@example.com', '1234segura'),
('María Torres', 'maria.torres@example.com', 'passmaria')
('Jurgen Perez', 'jurgen.perez@example.com', 'yuyo123');

INSERT INTO categorias (nombre) VALUES
('Analgésicos'),       -- Medicamentos para aliviar el dolor
('Antibióticos'),      -- Medicamentos para tratar infecciones bacterianas
('Antiinflamatorios'), -- Medicamentos para reducir la inflamación
('Vitaminas'),         -- Suplementos vitamínicos
('Antihistamínicos'),  -- Medicamentos para tratar alergias
('Antidepresivos'),    -- Medicamentos para tratar la depresión
('Antipiréticos'),     -- Medicamentos para reducir la fiebre
('Antidiabéticos'),    -- Medicamentos para controlar la diabetes
('Antihipertensivos'), -- Medicamentos para controlar la presión arterial
('Anticoagulantes'),   -- Medicamentos para prevenir coágulos sanguíneos
('Anticonvulsivos'),   -- Medicamentos para tratar convulsiones
('Relajantes musculares'); -- Medicamentos para aliviar espasmos musculares

INSERT INTO medicamentos (nombre, dosis, duracion, usuario_id, categoria_id) VALUES
('Paracetamol', '500mg', 5, 2, 1),
('Ibuprofeno', '400mg', 3, 2, 3),
('Amoxicilina', '250mg', 7, 2, 2),
('Vitamina C', '1000mg', 10, 3, 4);

INSERT INTO recordatorios (medicamento_id, fecha_hora, estado) VALUES
(13, '2025-04-15 08:00:00', 'pendiente'), 
(13, '2025-04-15 20:00:00', 'pendiente'), 
(16, '2025-04-16 09:00:00', 'pendiente'), 
(15, '2025-04-17 07:30:00', 'completado'), 
(14, '2025-04-18 10:00:00', 'pendiente');

INSERT INTO notificaciones (usuario_id, mensaje, fecha_hora, leido) VALUES
(8, 'Recordatorio: Tomar Paracetamol a las 8:00 AM', '2025-04-15 08:00:00', FALSE),
(2, 'Recordatorio: Tomar Ibuprofeno a las 9:00 AM', '2025-04-16 09:00:00', FALSE),
(3, 'Recordatorio: Tomar Amoxicilina a las 7:30 AM', '2025-04-17 07:30:00', TRUE),
(3, 'Recordatorio: Tomar Vitamina C a las 10:00 AM', '2025-04-18 10:00:00', FALSE),
(2, 'Recordatorio: Consulta médica programada para el 20 de abril', '2025-04-20 15:00:00', FALSE);

INSERT INTO historial_medicamentos (usuario_id, medicamento_id, fecha_hora) VALUES
(8, 13, '2025-04-15 08:00:00'), 
(2, 13, '2025-04-16 09:00:00'), 
(3, 16, '2025-04-17 07:30:00'), 
(8, 14, '2025-04-18 10:00:00'), 
(2, 15, '2025-04-19 08:00:00');

INSERT INTO doctores (nombre, especialidad, telefono, correo) VALUES
('Dr. Juan Pérez', 'Cardiología', '3001234567', 'juan.perez@hospital.com'),
('Dra. Ana Gómez', 'Pediatría', '3012345678', 'ana.gomez@hospital.com'),
('Dr. Carlos Ruiz', 'Neurología', '3023456789', 'carlos.ruiz@hospital.com'),
('Dra. María Torres', 'Dermatología', '3034567890', 'maria.torres@hospital.com'),
('Dr. Jorge Ramírez', 'Medicina General', '3045678901', 'jorge.ramirez@hospital.com');

INSERT INTO recetas (usuario_id, doctor_id, fecha) VALUES (1, 1, '2025-04-01 09:00:00');
INSERT INTO recetas (usuario_id, doctor_id, fecha) VALUES (2, 2, '2025-04-02 10:30:00');
INSERT INTO recetas (usuario_id, doctor_id, fecha) VALUES (3, 3, '2025-04-03 11:45:00');
INSERT INTO recetas (usuario_id, doctor_id, fecha) VALUES (8, 4, '2025-04-04 08:15:00');

INSERT INTO medicamentos_recetas (receta_id, medicamento_id) VALUES (1, 1);
INSERT INTO medicamentos_recetas (receta_id, medicamento_id) VALUES (1, 2);
INSERT INTO medicamentos_recetas (receta_id, medicamento_id) VALUES (2, 3);
INSERT INTO medicamentos_recetas (receta_id, medicamento_id) VALUES (3, 4);

INSERT INTO farmacias (nombre, direccion, telefono) VALUES ('Farmacia Central', 'Calle 10 #45-23', '3011234567');
INSERT INTO farmacias (nombre, direccion, telefono) VALUES ('Salud Total', 'Carrera 15 #33-90', '3027654321');
INSERT INTO farmacias (nombre, direccion, telefono) VALUES ('Botica Popular', 'Av. 80 #50-10', '3031122334');
INSERT INTO farmacias (nombre, direccion, telefono) VALUES ('Droguería Medellín', 'Calle 30 #70-50', '3049988776');

INSERT INTO medicamentos_farmacias (farmacia_id, medicamento_id, precio, stock) VALUES (1, 1, 12000.50, 10);
INSERT INTO medicamentos_farmacias (farmacia_id, medicamento_id, precio, stock) VALUES (2, 2, 8500.00, 25);
INSERT INTO medicamentos_farmacias (farmacia_id, medicamento_id, precio, stock) VALUES (3, 3, 15300.75, 15);
INSERT INTO medicamentos_farmacias (farmacia_id, medicamento_id, precio, stock) VALUES (4, 4, 6400.00, 8);

INSERT INTO configuraciones_usuarios (usuario_id, recibir_notificaciones, zona_horaria) VALUES (1, TRUE, 'America/Bogota');
INSERT INTO configuraciones_usuarios (usuario_id, recibir_notificaciones, zona_horaria) VALUES (2, FALSE, 'UTC');
INSERT INTO configuraciones_usuarios (usuario_id, recibir_notificaciones, zona_horaria) VALUES (3, TRUE, 'America/New_York');
INSERT INTO configuraciones_usuarios (usuario_id, recibir_notificaciones, zona_horaria) VALUES (4, TRUE, 'Europe/Madrid');

INSERT INTO horarios_medicamentos (medicamento_id, hora) VALUES (1, '08:00:00');
INSERT INTO horarios_medicamentos (medicamento_id, hora) VALUES (2, '12:00:00');
INSERT INTO horarios_medicamentos (medicamento_id, hora) VALUES (3, '18:00:00');
INSERT INTO horarios_medicamentos (medicamento_id, hora) VALUES (4, '20:30:00');

INSERT INTO contactos_emergencia (usuario_id, nombre, telefono, relacion) VALUES (1, 'Laura Gómez', '3112233445', 'Hermana');
INSERT INTO contactos_emergencia (usuario_id, nombre, telefono, relacion) VALUES (2, 'Carlos Pérez', '3123344556', 'Padre');
INSERT INTO contactos_emergencia (usuario_id, nombre, telefono, relacion) VALUES (3, 'María Torres', '3134455667', 'Esposa');
INSERT INTO contactos_emergencia (usuario_id, nombre, telefono, relacion) VALUES (4, 'Jorge Ramírez', '3145566778', 'Amigo');
