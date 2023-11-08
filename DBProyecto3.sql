-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf16 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para proyecto
CREATE DATABASE IF NOT EXISTS `proyecto` /*!40100 DEFAULT CHARACTER SET utf16 COLLATE utf16_spanish_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `proyecto`;

-- Volcando estructura para tabla proyecto.alumnos
CREATE TABLE IF NOT EXISTS `alumnos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `ap` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `correo` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `estado` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `fechanacimiento` date DEFAULT NULL,
  `carrera_id` int DEFAULT NULL,
  `grupo_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `carrera_id` (`carrera_id`),
  KEY `grupo_id` (`grupo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla proyecto.carrera
CREATE TABLE IF NOT EXISTS `carrera` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `semestres` int DEFAULT NULL,
  `grupo_id` int DEFAULT NULL,
  `alumno_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `alumno_id` (`alumno_id`),
  KEY `materia_id` (`grupo_id`) USING BTREE,
  CONSTRAINT `FK_carrera_alumnos` FOREIGN KEY (`alumno_id`) REFERENCES `alumnos` (`carrera_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla proyecto.grupos
CREATE TABLE IF NOT EXISTS `grupos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `carrera_id` int DEFAULT NULL,
  `materia_id` int DEFAULT NULL,
  `maestro_id` int DEFAULT NULL,
  `salon_id` int DEFAULT NULL,
  `horario_id` int DEFAULT NULL,
  `semestre` varchar(255) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `maxalumnos` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_grupos_carrera` (`carrera_id`),
  KEY `materia_id` (`materia_id`),
  KEY `maestro_id` (`maestro_id`),
  KEY `salon_id` (`salon_id`),
  KEY `horario_id` (`horario_id`),
  CONSTRAINT `FK_grupos_carrera` FOREIGN KEY (`carrera_id`) REFERENCES `carrera` (`grupo_id`),
  CONSTRAINT `FK_grupos_horario` FOREIGN KEY (`horario_id`) REFERENCES `horario` (`grupo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla proyecto.grupos_salon
CREATE TABLE IF NOT EXISTS `grupos_salon` (
  `id` int NOT NULL AUTO_INCREMENT,
  `grupos_salon_id` int DEFAULT NULL,
  `salon_grupos_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_grupos_salon_grupos` (`grupos_salon_id`),
  KEY `FK_grupos_salon_salon` (`salon_grupos_id`),
  CONSTRAINT `FK_grupos_salon_grupos` FOREIGN KEY (`grupos_salon_id`) REFERENCES `grupos` (`salon_id`),
  CONSTRAINT `FK_grupos_salon_salon` FOREIGN KEY (`salon_grupos_id`) REFERENCES `salon` (`grupo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla proyecto.horario
CREATE TABLE IF NOT EXISTS `horario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `turno` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `grupo_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `grupo_id` (`grupo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla proyecto.maestros
CREATE TABLE IF NOT EXISTS `maestros` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `ap` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `am` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `correo` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `carrera` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `estudios` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `grupo_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_maestros_grupos` (`grupo_id`),
  CONSTRAINT `FK_maestros_grupos` FOREIGN KEY (`grupo_id`) REFERENCES `grupos` (`maestro_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla proyecto.materias
CREATE TABLE IF NOT EXISTS `materias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `creditos` int DEFAULT NULL,
  `semestre` int DEFAULT NULL,
  `carrera_id` int DEFAULT NULL,
  `grupo_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `carrera_id` (`carrera_id`),
  KEY `FK_materias_grupos` (`grupo_id`),
  CONSTRAINT `FK_materias_grupos` FOREIGN KEY (`grupo_id`) REFERENCES `grupos` (`materia_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla proyecto.materias_carrera
CREATE TABLE IF NOT EXISTS `materias_carrera` (
  `id` int NOT NULL AUTO_INCREMENT,
  `materias_carrera_id` int DEFAULT NULL,
  `carrera_materia_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_materias_carrera_materias` (`materias_carrera_id`),
  KEY `FK_materias_carrera_carrera` (`carrera_materia_id`),
  CONSTRAINT `FK_materias_carrera_carrera` FOREIGN KEY (`carrera_materia_id`) REFERENCES `carrera` (`grupo_id`),
  CONSTRAINT `FK_materias_carrera_materias` FOREIGN KEY (`materias_carrera_id`) REFERENCES `materias` (`carrera_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla proyecto.salon
CREATE TABLE IF NOT EXISTS `salon` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(10) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `edificio` char(1) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `grupo_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `grupo_id` (`grupo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla proyecto.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `idusuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `ap` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `am` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `usuario` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `password` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `perfil` varchar(15) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`idusuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

-- La exportación de datos fue deseleccionada.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
