/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.8.8-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: bmcaving
-- ------------------------------------------------------
-- Server version	11.8.8-MariaDB-1 from Debian

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `cave`
--

DROP TABLE IF EXISTS `cave`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `cave` (
  `system_id` int(11) NOT NULL,
  `cave_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `depth_ft` int(11) DEFAULT NULL,
  `length_ft` int(11) DEFAULT NULL,
  `years_surveyed` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`system_id`,`cave_id`),
  CONSTRAINT `cave_ibfk_1` FOREIGN KEY (`system_id`) REFERENCES `cave_system` (`system_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cave`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `cave` WRITE;
/*!40000 ALTER TABLE `cave` DISABLE KEYS */;
INSERT INTO `cave` VALUES
(1,1,'Icy Breath',NULL,NULL,NULL),
(3,1,'Tears of the Turtle',NULL,NULL,NULL);
/*!40000 ALTER TABLE `cave` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `cave_system`
--

DROP TABLE IF EXISTS `cave_system`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `cave_system` (
  `system_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `wilderness_unit` varchar(100) NOT NULL,
  `length_ft` int(11) DEFAULT NULL,
  `num_caves` int(11) DEFAULT NULL,
  PRIMARY KEY (`system_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cave_system`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `cave_system` WRITE;
/*!40000 ALTER TABLE `cave_system` DISABLE KEYS */;
INSERT INTO `cave_system` VALUES
(1,'Silvertip','Bob Marshall Wilderness',NULL,NULL),
(2,'Scapegoat','Scapegoat Wilderness',NULL,NULL),
(3,'Tears of the Turtle','Bob Marshall Wilderness',NULL,1);
/*!40000 ALTER TABLE `cave_system` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `expedition`
--

DROP TABLE IF EXISTS `expedition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `expedition` (
  `expedition_id` int(11) NOT NULL AUTO_INCREMENT,
  `label` varchar(150) NOT NULL,
  `year` year(4) NOT NULL,
  `objectives` varchar(255) DEFAULT NULL,
  `organization` varchar(100) DEFAULT NULL,
  `lead_person_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`expedition_id`),
  KEY `lead_person_id` (`lead_person_id`),
  CONSTRAINT `expedition_ibfk_1` FOREIGN KEY (`lead_person_id`) REFERENCES `person` (`person_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expedition`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `expedition` WRITE;
/*!40000 ALTER TABLE `expedition` DISABLE KEYS */;
INSERT INTO `expedition` VALUES
(1,'2024 Silvertip expedition',2024,NULL,NULL,2);
/*!40000 ALTER TABLE `expedition` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `expedition_cave`
--

DROP TABLE IF EXISTS `expedition_cave`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `expedition_cave` (
  `expedition_id` int(11) NOT NULL,
  `system_id` int(11) NOT NULL,
  `cave_id` int(11) NOT NULL,
  PRIMARY KEY (`expedition_id`,`system_id`,`cave_id`),
  KEY `system_id` (`system_id`,`cave_id`),
  CONSTRAINT `expedition_cave_ibfk_1` FOREIGN KEY (`expedition_id`) REFERENCES `expedition` (`expedition_id`),
  CONSTRAINT `expedition_cave_ibfk_2` FOREIGN KEY (`system_id`, `cave_id`) REFERENCES `cave` (`system_id`, `cave_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expedition_cave`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `expedition_cave` WRITE;
/*!40000 ALTER TABLE `expedition_cave` DISABLE KEYS */;
INSERT INTO `expedition_cave` VALUES
(1,1,1);
/*!40000 ALTER TABLE `expedition_cave` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `expedition_person`
--

DROP TABLE IF EXISTS `expedition_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `expedition_person` (
  `expedition_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`expedition_id`,`person_id`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `expedition_person_ibfk_1` FOREIGN KEY (`expedition_id`) REFERENCES `expedition` (`expedition_id`),
  CONSTRAINT `expedition_person_ibfk_2` FOREIGN KEY (`person_id`) REFERENCES `person` (`person_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expedition_person`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `expedition_person` WRITE;
/*!40000 ALTER TABLE `expedition_person` DISABLE KEYS */;
INSERT INTO `expedition_person` VALUES
(1,2);
/*!40000 ALTER TABLE `expedition_person` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `person_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `role` varchar(100) DEFAULT NULL,
  `years_active` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`person_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES
(1,'Newell','Campbell','Scientist/author','1970s'),
(2,'Dustin','K.','Expedition leader',NULL);
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2026-09-24 20:13:57
