CREATE DATABASE  IF NOT EXISTS `examen_timbox_db` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `examen_timbox_db`;
-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: examen_timbox_db
-- ------------------------------------------------------
-- Server version	5.6.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `companies`
--

DROP TABLE IF EXISTS `companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `companies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_empresa_usuarios1_idx` (`user_id`),
  CONSTRAINT `fk_empresa_usuarios1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companies`
--

LOCK TABLES `companies` WRITE;
/*!40000 ALTER TABLE `companies` DISABLE KEYS */;
INSERT INTO `companies` VALUES (1,'Mega Wow.inc',4),(2,'Tuxapps',5),(3,'Moscovapps',6),(4,'Deutschapps',7),(5,'USAPPS',8);
/*!40000 ALTER TABLE `companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employees` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(128) NOT NULL,
  `pw_hash` varchar(192) NOT NULL,
  `name` varchar(60) NOT NULL,
  `second_name` varchar(45) DEFAULT NULL,
  `lastname` varchar(45) NOT NULL,
  `second_lastname` varchar(45) DEFAULT NULL,
  `date_created` varchar(45) NOT NULL,
  `date_modified` varchar(45) NOT NULL COMMENT 'adminisrador o empleado',
  `rfc` varchar(45) NOT NULL,
  `job_name` varchar(60) NOT NULL,
  `subsidiary_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `correo_UNIQUE` (`email`),
  KEY `fk_employees_subsidiaries1_idx` (`subsidiary_id`),
  CONSTRAINT `fk_employees_subsidiaries1` FOREIGN KEY (`subsidiary_id`) REFERENCES `subsidiaries` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'employee@tuna.com','pbkdf2:sha1:1000$GYahXgfR$add2ffa40a23048f47bbc5a4fc27f822a15ad08a','Empleado1',NULL,'Bien',NULL,'2016-05-03 13:01:04','2016-05-03 13:01:04','EMP4897','Bartender',4),(3,'employee3@tuna.com','pbkdf2:sha1:1000$RzA5Fnpu$8cf45da22f79c5febea12cdda2658ef2b8baa978','Empleado Z',NULL,'Malisimo',NULL,'2016-05-03 13:46:03','2016-05-03 14:07:47','EMP159405','Manager',1);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subsidiaries`
--

DROP TABLE IF EXISTS `subsidiaries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subsidiaries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `street` varchar(80) NOT NULL,
  `suburb` varchar(45) NOT NULL,
  `ext_number` int(11) NOT NULL,
  `interior_number` int(11) DEFAULT NULL,
  `postal_code` int(10) NOT NULL,
  `city` varchar(60) NOT NULL,
  `country` varchar(50) NOT NULL,
  `company_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  UNIQUE KEY `interior_number_UNIQUE` (`interior_number`),
  KEY `fk_sucursales_empresa1_idx` (`company_id`),
  CONSTRAINT `fk_sucursales_empresa1` FOREIGN KEY (`company_id`) REFERENCES `companies` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subsidiaries`
--

LOCK TABLES `subsidiaries` WRITE;
/*!40000 ALTER TABLE `subsidiaries` DISABLE KEYS */;
INSERT INTO `subsidiaries` VALUES (1,'Torres','Torres Av.','Tores del Sur',568745,487,32589,'Juarez','Mexico',1),(4,'Centro','16 de Septiembre St.','Centro',55897,50,32589,'Juarez','Mexico',1);
/*!40000 ALTER TABLE `subsidiaries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(128) NOT NULL,
  `pw_hash` varchar(192) NOT NULL,
  `name` varchar(60) NOT NULL,
  `second_name` varchar(45) DEFAULT NULL,
  `lastname` varchar(45) NOT NULL,
  `second_lastname` varchar(45) DEFAULT NULL,
  `date_created` varchar(45) NOT NULL,
  `date_modified` varchar(45) NOT NULL COMMENT 'adminisrador o empleado',
  `rfc` varchar(45) NOT NULL,
  `authenticated` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `correo_UNIQUE` (`email`),
  UNIQUE KEY `rfc_UNIQUE` (`rfc`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (4,'tuna3@tuna.net','pbkdf2:sha1:1000$meqyTwFM$e39abb4b1286bb0a174c1f4ac9df54b9006a7da7','Angel',NULL,'Munoz',NULL,'2016-04-29 12:16:08','2016-05-03 14:08:29','RFC4657463',0),(5,'tuna@tuna.io','pbkdf2:sha1:1000$bmnNgdSx$11d93d942743beb5cc477f68bf010c04e817c82b','Angel',NULL,'Jornario',NULL,'2016-04-30 15:15:52','2016-04-30 15:15:52','RFC7890',0),(6,'tuna@tuna.ru','pbkdf2:sha1:1000$LvJPxUBv$1f6eda8817613d82319aeb5080b05c705473e040','Korsh',NULL,'Maxima',NULL,'2016-04-30 23:34:45','2016-05-03 01:02:18','RFC1578ED',0),(7,'tuna@tuna.de','pbkdf2:sha1:1000$dGUxNVL9$3101e20b0fbc45d6441919a71e9dfa61b4e90972','Franz',NULL,'Wehr',NULL,'2016-05-01 00:16:29','2016-05-03 15:26:39','RFC486DE',0),(8,'tuna@tuna.us','pbkdf2:sha1:1000$K3OpuumX$671c8b7d1f131cad6541901b0a225dacb1c5a960','Tuna',NULL,'Smitherson',NULL,'2016-05-01 00:17:21','2016-05-01 00:17:21','RFC1234US',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'examen_timbox_db'
--

--
-- Dumping routines for database 'examen_timbox_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-03 17:11:52
