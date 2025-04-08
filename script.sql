CREATE DATABASE IF NOT EXISTS recordatorio_salud;
USE recordatorio_salud;

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    contraseña VARCHAR(255) NOT NULL
);

-- Tabla de medicamentos con clave foránea a usuarios
CREATE TABLE IF NOT EXISTS medicamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    dosis VARCHAR(50),
    frecuencia INT NOT NULL, -- cada cuántas horas se toma
    horario_inicio DATETIME NOT NULL,
    duracion INT NOT NULL, -- duración del tratamiento en días
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

INSERT INTO usuarios (nombre, correo, contraseña) VALUES
('Ana López', 'ana.lopez@example.com', 'clave123'),
('Carlos Ruiz', 'carlos.ruiz@example.com', '1234segura'),
('María Torres', 'maria.torres@example.com', 'passmaria');

INSERT INTO medicamentos (nombre, dosis, frecuencia, horario_inicio, duracion, usuario_id) VALUES
('Paracetamol', '500mg', 8, '2025-03-03 08:00:00', 5, 1),
('Ibuprofeno', '400mg', 6, '2025-03-03 07:30:00', 3, 1),
('Amoxicilina', '250mg', 12, '2025-03-03 09:00:00', 7, 2),
('Vitamina C', '1000mg', 24, '2025-03-03 10:00:00', 10, 3);
