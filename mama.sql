-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: mysql-14549d38-blackv.b.aivencloud.com    Database: MH
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'aa6098ef-5c79-11ef-9a21-02dc90450ad3:1-985';

--
-- Table structure for table `articles`
--

DROP TABLE IF EXISTS `articles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `articles` (
  `title` varchar(256) NOT NULL,
  `author` varchar(128) DEFAULT NULL,
  `description` text,
  `content` text NOT NULL,
  `published_at` datetime DEFAULT NULL,
  `source` varchar(128) DEFAULT NULL,
  `url` varchar(256) DEFAULT NULL,
  `url_to_image` varchar(256) DEFAULT NULL,
  `is_featured` tinyint(1) DEFAULT NULL,
  `topic` varchar(128) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` varchar(60) NOT NULL,
  `updated_at` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `articles`
--

LOCK TABLES `articles` WRITE;
/*!40000 ALTER TABLE `articles` DISABLE KEYS */;
INSERT INTO `articles` VALUES ('How to Manage Time as a New Parent','Jane Doe','Tips for new parents to manage time effectively.','This article discusses time management strategies for new parents...','2024-09-20 14:00:00','Parenting Weekly','https://example.com/articles/time-management','https://example.com/images/time-management.jpg',1,'parenting','012c8b01-499f-4cdb-ab18-b58b2be7cd23','2024-10-25 06:41:12.986117','2024-10-25 06:44:02.136118'),('Parenting in the Digital Age','John Doe','Balancing screen time and real-world interactions for your children.','This article explores how parents can guide their children in managing screen time...','2024-10-01 10:00:00','Parenting Magazine','https://example.com/articles/digital-age-parenting','https://example.com/images/digital-age-parenting.jpg',1,'parenting','4d551809-0456-4f73-98b7-a08fec9752c1','2024-10-25 06:41:12.987470','2024-10-25 06:52:06.769237'),('Managing Stress in a Busy World','Emily Johnson','Tips and strategies for managing stress and maintaining mental health.','This article provides practical advice on how to manage stress in a fast-paced world...','2024-09-22 08:00:00','Mental Health Today','https://example.com/articles/managing-stress','https://example.com/images/managing-stress.jpg',1,'mental-health','4fd09c2b-8ab4-47b9-a626-c78058d09afd','2024-10-25 06:41:12.986117','2024-10-25 06:48:28.678064'),('Nutrition for a Strong Immune System','Dr. Anna Green','Key foods and nutrients that boost immunity.','This article provides insights into how a balanced diet rich in vitamins and minerals can strengthen the immune system...','2024-09-15 10:30:00','Health Magazine','https://example.com/articles/immune-nutrition','https://example.com/images/immune-nutrition.jpg',1,'health','5159ec21-95a6-4465-97ac-03b56221098e','2024-10-25 06:41:12.986117','2024-10-25 06:53:31.567170'),('Understanding Heart Health','Dr. William Carter','Tips on maintaining a healthy heart through diet and lifestyle.','This article covers essential tips to keep your heart healthy, from diet to regular exercise...','2024-09-30 08:00:00','Heart Foundation','https://example.com/articles/heart-health','https://example.com/images/heart-health.jpg',1,'health','5b6bd218-fa4f-4243-ae58-e6b373e1db1a','2024-10-25 06:41:12.987470','2024-10-25 06:53:39.216624'),('Mindfulness for Beginners','Samantha Lee','An introduction to mindfulness and how it can improve mental clarity.','This article explains the basics of mindfulness and how to get started with simple techniques...','2024-09-19 14:00:00','Mental Health Today','https://example.com/articles/mindfulness-beginners','https://example.com/images/mindfulness-beginners.jpg',1,'mental-health','6f98d76c-690d-4ca4-ace3-ae02186ed669','2024-10-25 06:41:12.988051','2024-10-25 06:53:52.355130'),('Positive Discipline Techniques','Dr. Lisa Brown','Effective discipline strategies that foster respect and cooperation.','This article outlines various positive discipline techniques that encourage good behavior...','2024-09-28 14:00:00','Parenting Resources','https://example.com/articles/positive-discipline','https://example.com/images/positive-discipline.jpg',1,'parenting','7961ca16-87b4-4c8b-83ce-4648235e7ebe','2024-10-25 06:41:12.987470','2024-10-25 06:52:28.151900'),('The Importance of Regular Exercise','John Smith','An article discussing the benefits of regular physical activity.','This article explores various health benefits associated with regular exercise...','2024-09-21 10:00:00','Health Daily','https://example.com/articles/regular-exercise','https://example.com/images/regular-exercise.jpg',1,'health','9f1b0b5f-6c8a-4ba9-91ee-56baa3ca86dd','2024-10-25 06:41:12.988051','2024-10-25 06:46:34.201772'),('The Importance of Regular Exercise','Michael Roberts','Why staying active is crucial for maintaining overall health.','This article discusses the numerous health benefits of regular physical activity...','2024-09-20 12:00:00','Healthline','https://example.com/articles/importance-exercise','https://example.com/images/regular-exercise.jpg',1,'health','a4c05338-a14b-45f2-ba7d-678df40e69ad','2024-10-25 06:41:12.986117','2024-10-25 06:53:21.979285'),('Overcoming Burnout','Emma Stone','How to recognize and recover from burnout in a demanding world.','This article provides readers with strategies to prevent and overcome burnout while maintaining balance in life...','2024-10-02 10:00:00','Mental Wellness Journal','https://example.com/articles/overcoming-burnout','https://example.com/images/overcoming-burnout.jpg',1,'mental-health','a4fc1d3b-d284-4147-8fba-4d2a70bdbaf6','2024-10-25 06:41:12.986117','2024-10-25 06:54:13.842247'),('Building Healthy Routines for Kids','Sarah Lee','A guide to creating consistent routines that promote healthy development.','Learn the importance of establishing healthy routines for children in their early years...','2024-09-18 09:00:00','Child Development Journal','https://example.com/articles/healthy-routines-kids','https://example.com/images/healthy-routines.jpg',1,'parenting','b2eb94c2-5e09-4c8f-b926-7785b462a9c4','2024-10-25 06:41:12.987470','2024-10-25 06:52:18.611076'),('Managing Diabetes with Diet','Nutritionist Karen Smith','A dietary guide to managing Type 2 diabetes effectively.','This article offers advice on how to control diabetes through diet, focusing on low-carb and high-fiber foods...','2024-10-02 11:00:00','Diabetes Journal','https://example.com/articles/diabetes-diet','https://example.com/images/diabetes-diet.jpg',1,'health','b3686ae8-bdf6-401c-962d-d6214301d3b3','2024-10-25 06:41:12.986117','2024-10-25 06:53:45.795775'),('How to Cope with Anxiety','Dr. James Wilson','Effective coping strategies for managing anxiety in daily life.','This article offers practical tips and exercises for those who struggle with anxiety...','2024-09-26 12:00:00','Anxiety Journal','https://example.com/articles/cope-anxiety','https://example.com/images/cope-anxiety.jpg',1,'mental-health','bb6f760a-8ea1-4712-b9dd-1d84cf11da07','2024-10-25 06:41:12.986117','2024-10-25 06:53:59.150301'),('The Benefits of Therapy','Dr. Linda Harris','An exploration of the positive impacts of therapy on mental well-being.','This article covers the key benefits of therapy for individuals dealing with mental health challenges...','2024-09-25 09:30:00','Therapy Weekly','https://example.com/articles/benefits-of-therapy','https://example.com/images/therapy-benefits.jpg',1,'mental-health','dbdde511-3676-43ca-b5f5-106683426528','2024-10-25 06:41:12.986117','2024-10-25 06:54:07.378149'),('Positive Discipline Techniques','Dr. Lisa Brown','Effective discipline strategies that foster respect and cooperation.','This article outlines various positive discipline techniques that encourage good behavior...','2024-09-28 14:00:00','Parenting Resources','https://example.com/articles/positive-discipline','https://example.com/images/positive-discipline.jpg',1,'parenting','f38d2687-63b6-4582-93a8-7a798435e1c6','2024-10-25 06:41:12.986117','2024-10-25 06:52:43.399185'),('Dealing with Toddler Tantrums','Jane Wilson','Strategies for calming down and preventing toddler tantrums.','This article provides parents with effective techniques for handling toddler tantrums in a calm manner...','2024-10-05 11:00:00','Parenthood Today','https://example.com/articles/toddler-tantrums','https://example.com/images/toddler-tantrums.jpg',1,'parenting','fc606609-8fc3-420c-a3c4-5bf5c7cf806d','2024-10-25 06:41:12.986117','2024-10-25 06:52:51.821498');
/*!40000 ALTER TABLE `articles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conversations`
--

DROP TABLE IF EXISTS `conversations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conversations` (
  `sender` varchar(60) NOT NULL,
  `receiver` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` varchar(60) NOT NULL,
  `updated_at` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `sender` (`sender`),
  KEY `receiver` (`receiver`),
  CONSTRAINT `conversations_ibfk_1` FOREIGN KEY (`sender`) REFERENCES `users` (`id`),
  CONSTRAINT `conversations_ibfk_2` FOREIGN KEY (`receiver`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conversations`
--

LOCK TABLES `conversations` WRITE;
/*!40000 ALTER TABLE `conversations` DISABLE KEYS */;
/*!40000 ALTER TABLE `conversations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_attendees`
--

DROP TABLE IF EXISTS `event_attendees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_attendees` (
  `user_id` varchar(60) NOT NULL,
  `event_id` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` varchar(60) NOT NULL,
  `updated_at` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`),
  KEY `event_id` (`event_id`),
  CONSTRAINT `event_attendees_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `event_attendees_ibfk_2` FOREIGN KEY (`event_id`) REFERENCES `events` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_attendees`
--

LOCK TABLES `event_attendees` WRITE;
/*!40000 ALTER TABLE `event_attendees` DISABLE KEYS */;
/*!40000 ALTER TABLE `event_attendees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events` (
  `name` varchar(128) NOT NULL,
  `description` varchar(256) DEFAULT NULL,
  `date` datetime NOT NULL,
  `location` varchar(128) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` varchar(60) NOT NULL,
  `updated_at` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES ('breast cancer talk','Come let us talk on how to to identify the signs of cancer','2024-10-29 00:00:00','Nakuru gardens','3d761746-6415-46a1-b9f8-13f0de44cd67','2024-10-24 10:12:36.773903','2024-10-24 10:57:11.025709'),('Mwanamke bomba','investment is the way. ','2024-10-31 00:00:00','Nakuru city mall','66567ddc-3b53-41a1-85ea-22ff73125e6a','2024-10-24 10:12:36.773903','2024-10-24 10:58:25.571197');
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group_messages`
--

DROP TABLE IF EXISTS `group_messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `group_messages` (
  `sender_id` varchar(60) NOT NULL,
  `group_id` varchar(60) NOT NULL,
  `content` varchar(1024) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` varchar(60) NOT NULL,
  `updated_at` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `sender_id` (`sender_id`),
  KEY `group_id` (`group_id`),
  CONSTRAINT `group_messages_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `users` (`id`),
  CONSTRAINT `group_messages_ibfk_2` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group_messages`
--

LOCK TABLES `group_messages` WRITE;
/*!40000 ALTER TABLE `group_messages` DISABLE KEYS */;
/*!40000 ALTER TABLE `group_messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groupmembers`
--

DROP TABLE IF EXISTS `groupmembers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `groupmembers` (
  `group_id` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  `is_admin` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` varchar(60) NOT NULL,
  `updated_at` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `group_id` (`group_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `groupmembers_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`),
  CONSTRAINT `groupmembers_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groupmembers`
--

LOCK TABLES `groupmembers` WRITE;
/*!40000 ALTER TABLE `groupmembers` DISABLE KEYS */;
INSERT INTO `groupmembers` VALUES ('84df3ea1-8d1e-474d-b21a-ddc01fcd4b70','3760d620-a92f-4823-ab3e-c08f1d9c8ca6','0','0551282f-cde2-44b7-83f6-7b603ec0c9be','2024-11-21 00:55:22.978081','2024-11-21 07:39:35.729515'),('99973629-86a1-4e65-9227-8943e23a0f88','e28a14ae-1d4b-4c4d-b92f-552079f49f09','0','24ced60e-3cad-4174-beaa-08d23828a61b','2024-10-24 10:12:36.776247','2024-10-24 11:22:02.752833'),('99973629-86a1-4e65-9227-8943e23a0f88','a49f350d-c5e8-4998-88fd-e37bf6068bcd','1','2c93b431-a8e5-4028-a4bc-1a1c1995247c','2024-10-24 10:12:36.773903','2024-10-24 10:36:52.221407'),('84df3ea1-8d1e-474d-b21a-ddc01fcd4b70','e28a14ae-1d4b-4c4d-b92f-552079f49f09','1','b10c6681-6a2c-4f96-b73a-82307f190ee1','2024-10-24 10:12:36.774670','2024-10-24 13:13:00.848710'),('30ede329-2b5d-4255-ac0b-f17c014d8db3','3760d620-a92f-4823-ab3e-c08f1d9c8ca6','0','b4bd5bb6-9a62-41c4-b1a7-b2f9699a79e9','2024-11-21 00:55:22.978081','2024-11-21 07:39:32.934235'),('30ede329-2b5d-4255-ac0b-f17c014d8db3','e28a14ae-1d4b-4c4d-b92f-552079f49f09','0','c3731ea5-b31e-472e-ad0f-a9a20da322dd','2024-11-21 11:38:15.307099','2024-11-21 12:30:38.693181'),('30ede329-2b5d-4255-ac0b-f17c014d8db3','a49f350d-c5e8-4998-88fd-e37bf6068bcd','1','ed85a242-4415-4081-a8f4-d128a27eedb9','2024-10-24 10:12:36.773903','2024-10-24 10:43:01.618516');
/*!40000 ALTER TABLE `groupmembers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groups`
--

DROP TABLE IF EXISTS `groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `groups` (
  `name` varchar(60) NOT NULL,
  `description` varchar(257) DEFAULT NULL,
  `created_by` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` varchar(60) NOT NULL,
  `updated_at` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `created_by` (`created_by`),
  CONSTRAINT `groups_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups`
--

LOCK TABLES `groups` WRITE;
/*!40000 ALTER TABLE `groups` DISABLE KEYS */;
INSERT INTO `groups` VALUES ('Child care','Join and get  more info on how to take care of your younglin','a49f350d-c5e8-4998-88fd-e37bf6068bcd','30ede329-2b5d-4255-ac0b-f17c014d8db3','2024-10-24 10:12:36.773903','2024-10-24 10:43:00.877686'),('Autism kids','meet parents with Autistic kids','e28a14ae-1d4b-4c4d-b92f-552079f49f09','84df3ea1-8d1e-474d-b21a-ddc01fcd4b70','2024-10-24 10:12:36.774670','2024-10-24 13:13:00.074536'),('Tea Group','Join the group and get the most tantalizing tea','a49f350d-c5e8-4998-88fd-e37bf6068bcd','99973629-86a1-4e65-9227-8943e23a0f88','2024-10-24 10:12:36.773903','2024-10-24 10:36:51.445649'),('Psychology','Help you understand any mental issue','a49f350d-c5e8-4998-88fd-e37bf6068bcd','b9bd56bf-9671-45cb-b788-9d02c3410e57','2024-10-24 10:12:36.776247','2024-10-24 10:39:03.126856');
/*!40000 ALTER TABLE `groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menteesessions`
--

DROP TABLE IF EXISTS `menteesessions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menteesessions` (
  `mentor_id` varchar(60) NOT NULL,
  `mentee_id` varchar(60) NOT NULL,
  `session_type` varchar(128) NOT NULL,
  `scheduled_time` datetime DEFAULT NULL,
  `message_thread_id` varchar(60) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` varchar(60) NOT NULL,
  `updated_at` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `mentor_id` (`mentor_id`),
  KEY `mentee_id` (`mentee_id`),
  KEY `message_thread_id` (`message_thread_id`),
  CONSTRAINT `menteesessions_ibfk_1` FOREIGN KEY (`mentor_id`) REFERENCES `users` (`id`),
  CONSTRAINT `menteesessions_ibfk_2` FOREIGN KEY (`mentee_id`) REFERENCES `users` (`id`),
  CONSTRAINT `menteesessions_ibfk_3` FOREIGN KEY (`message_thread_id`) REFERENCES `messages` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menteesessions`
--

LOCK TABLES `menteesessions` WRITE;
/*!40000 ALTER TABLE `menteesessions` DISABLE KEYS */;
/*!40000 ALTER TABLE `menteesessions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mentorship`
--

DROP TABLE IF EXISTS `mentorship`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mentorship` (
  `mentor_id` varchar(60) NOT NULL,
  `mentee_id` varchar(60) NOT NULL,
  `status` varchar(128) DEFAULT NULL,
  `start_date` datetime DEFAULT NULL,
  `end_date` datetime DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` varchar(60) NOT NULL,
  `updated_at` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `mentor_id` (`mentor_id`),
  KEY `mentee_id` (`mentee_id`),
  CONSTRAINT `mentorship_ibfk_1` FOREIGN KEY (`mentor_id`) REFERENCES `users` (`id`),
  CONSTRAINT `mentorship_ibfk_2` FOREIGN KEY (`mentee_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mentorship`
--

LOCK TABLES `mentorship` WRITE;
/*!40000 ALTER TABLE `mentorship` DISABLE KEYS */;
/*!40000 ALTER TABLE `mentorship` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `sender_id` varchar(60) NOT NULL,
  `recipient_id` varchar(60) NOT NULL,
  `content` varchar(1024) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `read` tinyint(1) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` varchar(60) NOT NULL,
  `updated_at` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `sender_id` (`sender_id`),
  KEY `recipient_id` (`recipient_id`),
  CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `users` (`id`),
  CONSTRAINT `messages_ibfk_2` FOREIGN KEY (`recipient_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES ('3760d620-a92f-4823-ab3e-c08f1d9c8ca6','a49f350d-c5e8-4998-88fd-e37bf6068bcd','what\'s up bro','2024-11-21 08:25:00',0,'2b7a29b4-5de4-417f-b7c5-73a95c309996','2024-11-21 07:55:15.985800','2024-11-21 08:25:00.152679'),('fd6327e0-2a50-458b-86ed-cf562bad0913','a49f350d-c5e8-4998-88fd-e37bf6068bcd','hello ','2024-10-25 15:10:54',0,'34041754-99d5-4161-a1de-97fa25775e0a','2024-10-25 06:41:12.988051','2024-10-25 15:10:54.243258'),('3760d620-a92f-4823-ab3e-c08f1d9c8ca6','a49f350d-c5e8-4998-88fd-e37bf6068bcd','hello','2024-11-21 08:24:46',0,'bf07c4cc-2126-4efd-93ce-8da7dbd18322','2024-11-21 07:55:15.985800','2024-11-21 08:24:45.345328');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `first_name` varchar(128) NOT NULL,
  `second_name` varchar(128) NOT NULL,
  `bio` text,
  `email` varchar(128) NOT NULL,
  `phone_number` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_mentor` tinyint(1) DEFAULT NULL,
  `expertise` text,
  `is_mentee` tinyint(1) DEFAULT NULL,
  `help_needed` text,
  `id` varchar(60) NOT NULL,
  `created_at` varchar(60) NOT NULL,
  `updated_at` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone_number` (`phone_number`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Kimarhi','brian','Mother.\nParent with Autistic kids','brian@gmail.com','06060040440','$2b$12$UPanyygKlB1OCWRxzaqrW.AfBmvBmWDXmvmKNWr76GnRRQHU/7sQW',0,NULL,0,NULL,'3760d620-a92f-4823-ab3e-c08f1d9c8ca6','2024-11-21 00:55:22.978081','2024-11-21 07:37:24.428422'),('kima','bki','Mother of 3 healthy boys and 2 baby girlsncnxnxn','b@gmail.com','0796699969','$2b$12$of6YNxORSf6j.CAKnChEbeEWaeDAwW2Y1ApEWzJGIgum2QMqU2ELq',0,NULL,0,NULL,'a49f350d-c5e8-4998-88fd-e37bf6068bcd','2024-10-24 10:12:36.776247','2024-10-24 10:15:10.845366'),('Jerono','Rhodah','Mum of two\n\n','rhodahjerono@gmail.com','0708847933','$2b$12$iUbARsKPtcFbvmCFiZuRNOHhfWUcTdY2qEh7YiKm77nT7U58hyG7K',0,NULL,0,NULL,'e28a14ae-1d4b-4c4d-b92f-552079f49f09','2024-10-24 10:12:36.776247','2024-10-24 11:17:13.879624'),('Ogero ','Brian ',NULL,'brianogero7910@gmail.com','0759776864','$2b$12$NII/iQPey9uADHId3g5RbOaqo44m2Zwx4Yl3t.FAiOxLwSmRdHtLi',0,NULL,0,NULL,'fd6327e0-2a50-458b-86ed-cf562bad0913','2024-10-25 06:41:12.988051','2024-10-25 15:09:46.241072');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-30 11:46:53
