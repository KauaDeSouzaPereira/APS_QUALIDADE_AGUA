-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: aps_qualidade_agua
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `resultadosia`
--

DROP TABLE IF EXISTS `resultadosia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resultadosia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `datahora` datetime NOT NULL,
  `resultado` bit(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resultadosia`
--

LOCK TABLES `resultadosia` WRITE;
/*!40000 ALTER TABLE `resultadosia` DISABLE KEYS */;
INSERT INTO `resultadosia` VALUES (1,'2024-05-27 23:36:19',_binary '\0'),(2,'2024-05-27 23:36:19',_binary '\0'),(3,'2024-05-27 23:36:19',_binary '\0'),(4,'2024-05-27 23:36:19',_binary '\0'),(5,'2024-05-27 23:36:19',_binary '\0'),(6,'2024-05-27 23:36:19',_binary '\0'),(7,'2024-05-27 23:36:19',_binary '\0'),(8,'2024-05-27 23:36:19',_binary '\0'),(9,'2024-05-27 23:36:19',_binary '\0'),(10,'2024-05-27 23:36:19',_binary '\0'),(11,'2024-05-27 23:36:20',_binary '\0'),(12,'2024-05-27 23:36:20',_binary '\0'),(13,'2024-05-27 23:36:20',_binary '\0'),(14,'2024-05-27 23:36:20',_binary '\0'),(15,'2024-05-27 23:36:20',_binary '\0'),(16,'2024-05-27 23:36:20',_binary '\0'),(17,'2024-05-27 23:36:20',_binary '\0'),(18,'2024-05-27 23:36:20',_binary '\0'),(19,'2024-05-27 23:36:20',_binary '\0'),(20,'2024-05-27 23:36:20',_binary '\0'),(21,'2024-05-27 23:36:20',_binary '\0'),(22,'2024-05-27 23:36:20',_binary '\0'),(23,'2024-05-27 23:36:20',_binary '\0'),(24,'2024-05-27 23:36:20',_binary '\0'),(25,'2024-05-27 23:36:20',_binary '\0'),(26,'2024-05-27 23:36:20',_binary '\0'),(27,'2024-05-27 23:36:20',_binary '\0'),(28,'2024-05-27 23:36:20',_binary '\0'),(29,'2024-05-27 23:36:20',_binary '\0'),(30,'2024-05-27 23:36:20',_binary '\0'),(31,'2024-05-27 23:36:20',_binary '\0'),(32,'2024-05-27 23:36:20',_binary '\0'),(33,'2024-05-27 23:36:20',_binary ''),(34,'2024-05-27 23:36:20',_binary '\0'),(35,'2024-05-27 23:36:20',_binary '\0'),(36,'2024-05-27 23:36:20',_binary '\0'),(37,'2024-05-27 23:36:20',_binary '\0'),(38,'2024-05-27 23:36:20',_binary '\0'),(39,'2024-05-27 23:36:20',_binary '\0');
/*!40000 ALTER TABLE `resultadosia` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-28  0:32:16
