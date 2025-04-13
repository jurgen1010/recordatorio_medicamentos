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

-- Eliminar las columnas relacionadas con horarios
ALTER TABLE medicamentos DROP COLUMN frecuencia;
ALTER TABLE medicamentos DROP COLUMN horario_inicio;

-- Agregar la columna para la relación con categorías
ALTER TABLE medicamentos ADD COLUMN categoria_id INT;

-- Agregar la clave foránea para la relación con la tabla categorias
ALTER TABLE medicamentos ADD CONSTRAINT fk_categoria FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE SET NULL;

--Tabla recordatorios con clave foranea a Medicamentos
CREATE TABLE IF NOT EXISTS recordatorios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    medicamento_id INT NOT NULL,
    fecha_hora DATETIME NOT NULL,
    estado ENUM('pendiente', 'completado') DEFAULT 'pendiente',
    FOREIGN KEY (medicamento_id) REFERENCES medicamentos(id) ON DELETE CASCADE
);

--Tabla medicamentos con clave foranea dentro de Medicamentos
CREATE TABLE IF NOT EXISTS categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
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
    FOREIGN KEY (doctor_id) REFERENCES doctores(id) ON DELETE SET NULL
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
('María Torres', 'maria.torres@example.com', 'passmaria');

INSERT INTO medicamentos (nombre, dosis, duracion, usuario_id, categoria_id) VALUES
('Paracetamol', '500mg', 5, 1, 1),
('Ibuprofeno', '400mg', 3, 1, 3),
('Amoxicilina', '250mg', 7, 2, 2),
('Vitamina C', '1000mg', 10, 3, 4);

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