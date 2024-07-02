-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: hackerthon
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `problems`
--

DROP TABLE IF EXISTS `problems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `problems` (
  `id` int NOT NULL AUTO_INCREMENT,
  `submissions` int DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `content` text,
  `accepted` int DEFAULT NULL,
  `exampleCase` text,
  `constraints` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problems`
--

LOCK TABLES `problems` WRITE;
/*!40000 ALTER TABLE `problems` DISABLE KEYS */;
INSERT INTO `problems` VALUES (1,0,'Grumpy Bookstore Owner','There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.\n\nOn some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.\n\nWhen the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.\n\nThe bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.\n\nReturn the maximum number of customers that can be satisfied throughout the day.',0,'Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3\nOutput: 16\nExplanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. \nThe maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.','The first line is a positive integer N in the range 2 &leq; N &leq; 2 &times; 10<sup>4</sup><br>\nThe second line is a sequence of N positive integers customers with 0 &leq; customer[i] &leq; 1000<br>\nThe third line is a sequence of N positive integers grumpy<br>\nThe fourth line is an integer minutes in the range 1 &leq; minutes &leq; n &leq; 2 &times; 10<sup>4</sup><br>\n<br>\n<strong>Input:</strong> customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3<br>\n<strong>Output:</strong> 16<br>\n<strong>Explanation:</strong> The bookstore owner keeps themselves not grumpy for the last 3 minutes. The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.'),(3,0,'Frog Jump','A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.\n\nGiven a list of stones positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.\n\nIf the frogs last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.',0,'Example 1:\nInput: stones = [0,1,3,5,6,8,12,17]\nOutput: true\nExplanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.','<p>\n    Constraints:\n</p>\n<p>\n    2 &le; stones.length &le; 2000<br>\n    0 &le; stones[i] &le; 2<sup>31</sup> - 1<br>\n    stones[0] == 0<br>\n    stones is sorted in a strictly increasing order.\n</p>\n'),(4,0,'Reducing Dishes','A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.\n\nLike-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].\n\nReturn the maximum sum of like-time coefficient that the chef can obtain after preparing some amount of dishes.\n\nDishes can be prepared in any order and the chef can discard some dishes to get this maximum value.',0,'Example 1:\n\nInput: satisfaction = [-1,-8,0,5,-9]\nOutput: 14\nExplanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).\nEach dish is prepared in one unit of time.','<h3>Constraints:</h3>\n<p>\n    <code>n == satisfaction.length</code><br>\n    <code>1 &le; n &le; 500</code><br>\n    <code>-1000 &le; satisfaction[i] &le; 1000</code>\n</p>\n');
/*!40000 ALTER TABLE `problems` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-02  9:51:37
