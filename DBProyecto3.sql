CREATE DATABASE IF NOT EXISTS `proyecto`;
USE `proyecto`;

CREATE TABLE IF NOT EXISTS `alumnos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `ap` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `am` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `correo` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `estado` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT "Jalisco",
  `fechanacimiento` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `carrera_id` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `grupo_id` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT "grupo 1",
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

CREATE TABLE IF NOT EXISTS `usuarios` (
  `idusuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `ap` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `am` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `usuario` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `password` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `correo` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `estatus` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT "0",
  `perfil` varchar(15) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT "Alumno",
  PRIMARY KEY (`idusuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

CREATE TABLE IF NOT EXISTS `horario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `turno` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `hora` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `grupo_id` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT "grupo 1",
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

CREATE TABLE IF NOT EXISTS `salon` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(10) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `edificio` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT "Edificio 1",
  `aula` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT "1",
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

CREATE TABLE IF NOT EXISTS `carrera` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `semestres` int DEFAULT NULL,
  `materias` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `grupo_id` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT "grupo 1",
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

CREATE TABLE IF NOT EXISTS `grupos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `fecha` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `carrera` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `materia` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `maestro` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `salon` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `horario` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `semestre` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `maxalumnos` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

CREATE TABLE IF NOT EXISTS `maestros` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `ap` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `am` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `correo` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `carrera` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `materia` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `grupo_id` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT "grupo 1",
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

CREATE TABLE IF NOT EXISTS `materias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `creditos` int DEFAULT NULL,
  `semestre` int DEFAULT NULL,
  `carrera_id` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `grupo_id` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT "grupo 1",
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

INSERT INTO `usuarios` (`idusuario`, `nombre`, `ap`, `am`, `usuario`, `password`, `perfil`) 
VALUES ('1', 'Admin', NULL, NULL, 'Admin', 'AdminP', 'Admin'), 
('2', 'Maestro', NULL, NULL, 'Maestro', 'MaestroP', 'Maestro'),
('3', 'Alumno', NULL, NULL, 'Alumno', 'AlumnoP', 'Alumno');
INSERT INTO `alumnos` (`id`, `nombre`, `ap`, `am`, `correo`, `estado`, `fechanacimiento`, `carrera_id`, `grupo_id`) 
VALUES (NULL, 'Joan', 'Sebastian', NULL, 'joasbas@gmail.com', 'Jalisco', '12/07/1968', 'Computacion', 'grupo 1');
INSERT INTO `carrera` (`id`, `nombre`, `semestres`, `materias`, `grupo_id`) VALUES (NULL, 'Computacion', '8', 'Corridos tumbados 1', 'grupo1');
INSERT INTO `grupos` (`id`, `nombre`, `fecha`, `carrera`, `materia`, `maestro`, `salon`, `horario`, `semestre`, `maxalumnos`) 
VALUES (NULL, 'grupo 1', 'I - J', 'Computacion', 'corridos tumbados 1', 'Valentin', 'salon 1', '7:00:00', '1', '30');
INSERT INTO `horario` (`id`, `turno`, `hora`, `grupo_id`) 
VALUES (NULL, 'L - I', '7:00:00', 'grupo 1');
INSERT INTO `maestros` (`id`, `nombre`, `ap`, `am`, `correo`, `carrera`, `materia`, `grupo_id`) 
VALUES (NULL, 'Valentin', 'Elizalde', NULL, NULL, 'Computacion', 'Corridos tumbados 1', 'grupo 1');
INSERT INTO `materias` (`id`, `nombre`, `creditos`, `semestre`, `carrera_id`, `grupo_id`) 
VALUES (NULL, 'Corridos tumbados 1', '8', '1', 'Computacion', 'grupo 1');
INSERT INTO `salon` (`id`, `nombre`, `edificio`, `aula`) VALUES (NULL, 'salon 1', 'Edificio 1', '1');

