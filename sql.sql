-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: fuprox
-- ------------------------------------------------------
-- Server version	5.7.31-0ubuntu0.16.04.1

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
-- Table structure for table `account_status`
--

DROP TABLE IF EXISTS `account_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` int(11) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `code` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user` (`user`),
  CONSTRAINT `account_status_ibfk_1` FOREIGN KEY (`user`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_status`
--

LOCK TABLES `account_status` WRITE;
/*!40000 ALTER TABLE `account_status` DISABLE KEYS */;
INSERT INTO `account_status` VALUES (1,12,1,'14284347'),(2,13,0,'3431213'),(3,14,0,'10173835'),(4,15,0,'6984409'),(5,16,1,'16679259'),(6,17,0,'12044769'),(7,18,0,'13916303'),(8,19,0,'16122519'),(9,20,0,'13676137'),(10,21,0,'10348473'),(11,22,0,'16715848'),(12,23,0,'7286183'),(13,24,0,'12876952'),(14,25,0,'7465740'),(15,26,0,'9383679'),(16,27,1,'1509293'),(17,28,0,'15848426'),(18,29,0,'12499922'),(19,30,0,'8902850');
/*!40000 ALTER TABLE `account_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `service_name` varchar(250) DEFAULT NULL,
  `start` varchar(200) DEFAULT NULL,
  `branch_id` int(11) DEFAULT NULL,
  `ticket` varchar(6) NOT NULL,
  `date_added` datetime DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  `nxt` int(11) NOT NULL,
  `serviced` tinyint(1) NOT NULL,
  `teller` varchar(200) NOT NULL,
  `kind` int(11) NOT NULL,
  `user` int(11) DEFAULT NULL,
  `is_instant` tinyint(1) DEFAULT NULL,
  `forwarded` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `date_added` (`date_added`)
) ENGINE=InnoDB AUTO_INCREMENT=175 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES (1,'Loans Services','2020-07-22 00:00:28.401590',3,'1','2020-07-21 20:59:45',0,1001,1,'0',1,0,0,NULL),(3,'Loans Services','2020-07-22 00:03:11.791570',3,'2','2020-07-21 21:02:28',0,1001,1,'0',2,0,0,NULL),(5,'Loans Services','2020-07-22 00:21:41.725501',3,'3','2020-07-21 21:20:58',0,1001,1,'0',3,0,0,NULL),(7,'Loans Services','2020-07-22 00:21:50.095163',3,'4','2020-07-21 21:21:06',0,1001,1,'0',4,0,0,NULL),(9,'Loans Services','2020-07-22 00:22:15.795178',3,'5','2020-07-21 21:21:32',0,1001,1,'0',5,0,0,NULL),(11,'Loans Services','2020-07-22 00:26:03.381134',3,'6','2020-07-21 21:25:20',0,1001,1,'0',6,0,0,NULL),(13,'Loans Services','2020-07-22 00:26:07.700472',3,'7','2020-07-21 21:25:24',0,1001,1,'0',7,0,0,NULL),(15,'Loans Services','2020-07-22 00:26:13.407145',3,'8','2020-07-21 21:25:30',0,1001,1,'0',8,0,0,NULL),(17,'Loans Services','2020-07-22 00:26:27.498217',3,'9','2020-07-21 21:25:44',0,1001,1,'0',9,0,0,NULL),(18,'Loans Services','2020-07-22 00:26:27.498217',3,'9','2020-07-21 21:25:46',0,1001,0,'0',9,0,0,NULL),(19,'Loans Services','2020-02-10 08:44:31',3,'10','2020-07-21 21:57:33',0,1001,1,'0',1,2,0,NULL),(20,'Loans Services','2020-02-10 08:44:31',3,'11','2020-07-21 21:58:40',0,1001,1,'0',1,2,0,NULL),(21,'Loans Services','2020-02-10 08:44:31',3,'12','2020-07-21 21:58:46',0,1001,1,'0',1,2,0,NULL),(22,'Loans Services','2020-02-10 08:44:31',3,'13','2020-07-21 21:58:56',0,1001,0,'0',1,2,0,NULL),(23,'Loans Services','2020-02-10 08:44:31',3,'14','2020-07-21 21:59:07',0,1001,0,'0',1,2,0,NULL),(24,'Loans Services','2020-02-10 08:44:31',3,'15','2020-07-21 21:59:17',0,1001,0,'0',1,2,0,NULL),(25,'Loans Services','2020-02-10 08:44:31',3,'16','2020-07-21 22:00:30',0,1001,0,'0',1,2,1,NULL),(26,'Loans Services','2020-07-22 00:00:28.401590',3,'17','2020-07-25 19:22:24',0,1001,0,'0',1,0,0,NULL),(30,'Loans Services','2020-07-22 00:21:41.725501',3,'18','2020-07-25 19:22:25',0,1001,0,'0',3,0,0,NULL),(34,'Loans Services','2020-07-22 00:22:15.795178',3,'19','2020-07-25 19:22:26',0,1001,0,'0',5,0,0,NULL),(38,'Loans Services','2020-07-22 00:26:07.700472',3,'20','2020-07-25 19:22:27',0,1001,0,'0',7,0,0,NULL),(40,'Loans Services','2020-07-22 00:26:13.407145',3,'21','2020-07-25 19:22:28',0,1001,0,'0',8,0,0,NULL),(44,'Loans Services','2020-02-10 08:44:31',3,'22','2020-07-25 19:22:29',0,1001,0,'0',10,2,0,NULL),(48,'Loans Services','2020-02-10 08:44:31',3,'23','2020-07-25 19:22:30',0,1001,0,'0',12,2,0,NULL),(52,'Loans Services','2020-02-10 08:44:31',3,'24','2020-07-25 19:22:31',0,1001,0,'0',14,2,0,NULL),(54,'Loans Services','2020-02-10 08:44:31',3,'25','2020-07-25 19:22:32',0,1001,0,'0',15,2,0,NULL),(58,'Loans Services','2020-07-22 00:00:28.401590',3,'26','2020-07-25 19:23:24',0,1001,0,'0',1,0,0,NULL),(62,'Loans Services','2020-07-22 00:21:41.725501',3,'27','2020-07-25 19:23:25',0,1001,0,'0',3,0,0,NULL),(66,'Loans Services','2020-07-22 00:22:15.795178',3,'28','2020-07-25 19:23:26',0,1001,0,'0',5,0,0,NULL),(70,'Loans Services','2020-07-22 00:26:07.700472',3,'29','2020-07-25 19:23:27',0,1001,0,'0',7,0,0,NULL),(74,'Loans Services','2020-07-22 00:26:27.498217',3,'30','2020-07-25 19:23:28',0,1001,0,'0',9,0,0,NULL),(76,'Loans Services','2020-02-10 08:44:31',3,'31','2020-07-25 19:23:29',0,1001,0,'0',10,2,0,NULL),(80,'Loans Services','2020-02-10 08:44:31',3,'32','2020-07-25 19:23:30',0,1001,0,'0',12,2,0,NULL),(84,'Loans Services','2020-02-10 08:44:31',3,'33','2020-07-25 19:23:31',0,1001,0,'0',14,2,0,NULL),(88,'Loans Services','2020-02-10 08:44:31',3,'34','2020-07-25 19:23:32',0,1001,0,'0',16,2,1,NULL),(90,'Loans Services','2020-07-22 00:00:28.401590',3,'35','2020-07-25 19:23:33',0,1001,0,'0',17,0,0,NULL),(94,'Loans Services','2020-07-22 00:03:11.791570',3,'36','2020-07-25 19:23:34',0,1001,0,'0',19,0,0,NULL),(98,'Loans Services','2020-07-22 00:00:28.401590',3,'37','2020-07-25 19:24:24',0,1001,0,'0',1,0,0,NULL),(100,'Loans Services','2020-07-22 00:03:11.791570',3,'38','2020-07-25 19:24:25',0,1001,0,'0',2,0,0,NULL),(104,'Loans Services','2020-07-22 00:21:50.095163',3,'39','2020-07-25 19:24:26',0,1001,0,'0',4,0,0,NULL),(108,'Loans Services','2020-07-22 00:26:03.381134',3,'40','2020-07-25 19:24:27',0,1001,0,'0',6,0,0,NULL),(112,'Loans Services','2020-07-22 00:26:13.407145',3,'41','2020-07-25 19:24:28',0,1001,0,'0',8,0,0,NULL),(114,'Loans Services','2020-07-22 00:26:27.498217',3,'42','2020-07-25 19:24:29',0,1001,0,'0',9,0,0,NULL),(118,'Loans Services','2020-02-10 08:44:31',3,'43','2020-07-25 19:24:30',0,1001,0,'0',11,2,0,NULL),(122,'Loans Services','2020-02-10 08:44:31',3,'44','2020-07-25 19:24:31',0,1001,0,'0',13,2,0,NULL),(126,'Loans Services','2020-02-10 08:44:31',3,'45','2020-07-25 19:24:32',0,1001,0,'0',15,2,0,NULL),(128,'Loans Services','2020-02-10 08:44:31',3,'46','2020-07-25 19:24:33',0,1001,0,'0',16,2,1,NULL),(132,'Loans Services','2020-07-22 00:03:11.791570',3,'47','2020-07-25 19:24:34',0,1001,0,'0',18,0,0,NULL),(136,'Loans Services','2020-07-22 00:21:41.725501',3,'48','2020-07-25 19:24:35',0,1001,0,'0',20,0,0,NULL),(138,'Loans Services','2020-07-22 00:00:28.401590',3,'49','2020-07-25 19:25:24',0,1001,0,'0',1,0,0,NULL),(140,'Loans Services','2020-07-22 00:03:11.791570',3,'50','2020-07-25 19:25:25',0,1001,0,'0',2,0,0,NULL),(144,'Loans Services','2020-07-22 00:21:50.095163',3,'51','2020-07-25 19:25:26',0,1001,0,'0',4,0,0,NULL),(148,'Loans Services','2020-07-22 00:26:03.381134',3,'52','2020-07-25 19:25:27',0,1001,0,'0',6,0,0,NULL),(152,'Loans Services','2020-07-22 00:26:13.407145',3,'53','2020-07-25 19:25:28',0,1001,0,'0',8,0,0,NULL),(156,'Loans Services','2020-02-10 08:44:31',3,'54','2020-07-25 19:25:29',0,1001,0,'0',10,2,0,NULL),(160,'Loans Services','2020-02-10 08:44:31',3,'55','2020-07-25 19:25:30',0,1001,0,'0',12,2,0,NULL),(162,'Loans Services','2020-02-10 08:44:31',3,'56','2020-07-25 19:25:31',0,1001,0,'0',13,2,0,NULL),(166,'Loans Services','2020-02-10 08:44:31',3,'57','2020-07-25 19:25:32',0,1001,0,'0',15,2,0,NULL),(170,'Loans Services','2020-07-22 00:00:28.401590',3,'58','2020-07-25 19:25:33',0,1001,0,'0',17,0,0,NULL),(174,'Loans Services','2020-07-22 00:03:11.791570',3,'59','2020-07-25 19:25:34',0,1001,0,'0',19,0,0,NULL);
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking_times`
--

DROP TABLE IF EXISTS `booking_times`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booking_times` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) NOT NULL,
  `date_added` datetime DEFAULT NULL,
  `service` varchar(250) NOT NULL,
  `start` datetime DEFAULT NULL,
  `end` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `booking_id` (`booking_id`),
  KEY `service` (`service`),
  CONSTRAINT `booking_times_ibfk_1` FOREIGN KEY (`service`) REFERENCES `service_offered` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking_times`
--

LOCK TABLES `booking_times` WRITE;
/*!40000 ALTER TABLE `booking_times` DISABLE KEYS */;
/*!40000 ALTER TABLE `booking_times` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branch`
--

DROP TABLE IF EXISTS `branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `branch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) DEFAULT NULL,
  `company` varchar(100) NOT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `opens` varchar(50) DEFAULT NULL,
  `closes` varchar(50) DEFAULT NULL,
  `service` varchar(100) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `key_` text,
  `valid_till` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `company` (`company`),
  KEY `service` (`service`),
  CONSTRAINT `branch_ibfk_1` FOREIGN KEY (`company`) REFERENCES `company` (`name`),
  CONSTRAINT `branch_ibfk_2` FOREIGN KEY (`service`) REFERENCES `service` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch`
--

LOCK TABLES `branch` WRITE;
/*!40000 ALTER TABLE `branch` DISABLE KEYS */;
INSERT INTO `branch` VALUES (2,'Hubei, China','Equity Bank','112.87832224656','31.15172525','0800','1700','Finance','abdulhafidhadan400@gmail.com','38035ac5d88c202d02949427b3dcb3ab48c6d54103b2b7c88bca536cf0e6d086',NULL),(3,'Equit Bank UniCity Mall, Thika Road, Thika District, Central, Kenya','Equity Bank','36.940418','-1.176823','0800','1700','Finance','abdulhafidhadan400@gmail.com','00694b024702d29719276233b7e9d49373ec16491497ddf31529d496d619d8cc',NULL),(4,'Equity Bank, Moi Avenue, Central Business District, Ngara, Nairobi, 00101, Kenya','Equity Bank','36.8262017','-1.2872908','08:00','17:00','Finance','abdulhafidhadan400@gmail.com','3446e08ef90e6537aec39d3930df7a3780e267f2c6254339f9745d48c7e349da',NULL),(5,'Equity Bank Ruiru, Ruiru Kamiti Road, Thika District, Central, Kenya','Equity Bank','36.959238','-1.148854','08:00','17:00','Finance','abdulhafidhadan400@gmail.com','b2772eac0db0e7c97b50b9b249b71fbe069ce336f79aa46b4d81e4c655ac9111',NULL);
/*!40000 ALTER TABLE `branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `service` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,'Equity Bank','2'),(2,'Tester','1');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(48) NOT NULL,
  `phoneNumber` varchar(12) NOT NULL,
  `image_file` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phoneNumber` (`phoneNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'abdulhafidhadan400@gmail.com','6f667f08','default.jpg','$2b$12$YcdcllCAtg8HmL1SYhX4NudyO/5YjP7Mq6jqk8Yh0WWZepWQu1oIu'),(2,'boos@gmail.com','3cee0b9f','default.jpg','$2b$12$zkVpKwbwWKzW4I89QD1UTu5eDSvIUcO9/x/u9KLdX6oXWDVllNNYy'),(3,'admin@gmail.com','cb428fbe','default.jpg','$2b$12$7hOUIYs7gLxk.cnX2JjQ9e.TPqfu7UJ/dx9/D6dSLb2FeWwzNvvki'),(4,'guyoabdihafid@gmail.com','396dd5cf','default.jpg','$2b$12$8d93TLn0pwKcrr7lhUQhM.wtGyuMXqkAbO/QTyyV0ReY5dN811dk.'),(5,'e6d398e6@gmail.com','e02a0dee','default.jpg','$2b$12$8dspA3HWYjoeCV.1O9OnrOIGnkM1FF.FFYL0mHMWWxwYDC3eMSPKa'),(6,'nniteric@gmail.com','dad3bf5d','default.jpg','$2b$12$Vw4Cf1R8qBa1Uyu1Rc0uRO8rCewzhbtVjdvmTQ1CTgBxQAivhIc1.'),(7,'breezy@gmail.com','67603704','default.jpg','$2b$12$2FnZJyRdcMYVNkm2gqAPSeavxsgAY9Azavthj6PknvDSVEUJcBieO'),(8,'denniskiruku@gmail.com','87','default.jpg','$2b$12$8UPK/Z1ejSMTzGG7fQZHk.H5cr0V8pWKjOmTiKdn8Tw3gNmqSBOdy'),(9,'hhhjeeeqqwe@gmail.com','4071','default.jpg','$2b$12$4RO8d9FidndW8Njghs7L6./09.LWR7Hf7YHQPdQTtbNEmu19AtF66'),(10,'abdulhusseinduo@gmail.com','807','default.jpg','$2b$12$57F6J9lQD4bhFno2yMOMLOOb6OItaYHdGowrumRaH56ubgsEcmnSC'),(11,'nddjjajaAA@GMAIL.COM','3791','default.jpg','$2b$12$sr6r4Dx7qqe/TKVUEI9a3.VfR0JBZmg52sX2DcD7yx3.T24UehgWi'),(12,'erickmaina29@students.ku.ac.ke','1422','default.jpg','$2b$12$8scpMawqgR68SBgOqYOcQOtqiouwHBO/TJUBv190zAG6tYH7ZrFgG'),(13,'email@abdul.com','4028','default.jpg','$2b$12$2oEzWcHavPZoGUiJtVv4VuDM1nqlNuHrAbtgczqF1czU5lC8gqrq2'),(14,'c174e837@gmail.com','3524','default.jpg','$2b$12$omsIwL2bETqZD7rlawr0t.f8sOtWjNyFC/ung49zeuN6im5JQWhmO'),(15,'kirukuwambui@gmail.com','1687','default.jpg','$2b$12$20TMUM/n4yWJfFOp3E8Vy.LnIJjDE5qYN5iria/wkMk6Aw4nuxxfW'),(16,'niteric@gmail.com','3261','default.jpg','$2b$12$elybvCzBwoJ0y9UiDOFVge0iJVL.4z1qGDg72RzBUEEmd0Q96X0Ny'),(17,'g.abdihafidh@students.ku.ac.ke','270','default.jpg','$2b$12$KKsveydMVbjoa0EVjy8thuYlnJx/KGwUY1UbhhLd.f5ySK7rUkrHe'),(18,'ericmaina29@students.ku.ac.ke','251','default.jpg','$2b$12$Y/AO9yeTEeW08JddzI5C/ed7F0vO2aHuVzfKAzxbYZsurHqSrfRvW'),(19,'tlepvdcltioesljlr@awdrt.net','299','default.jpg','$2b$12$MjQJhHsfdFm0BD9Y8TeNqObBWlPdIeAKLooWokmaAwml8/THpLzQW'),(20,'erickmaina@students.ku.ac.ke','356','default.jpg','$2b$12$gy5RkRuz7dVSgkzaPOS6QO43roJg9LnpL9KH5qMoR9coCv25bCEoe'),(21,'kirukduwambui@gmail.com','3922','default.jpg','$2b$12$UiG98JlsxwMC.pE/pZv3POMAjZP4xhdhSx.svyyJEpAEqgtGLx2vS'),(22,'kirukduwambuier@gmail.com','1461','default.jpg','$2b$12$bqK6BeYgrpygubmJfb9oYeH8a6xaaBrkh0JoOaS3IET3H3Ccu1YrG'),(23,'deniskiruku@gmail.com','3723','default.jpg','$2b$12$mqwu4LZKRoA8aoTJUyp41u3eRB976PQUr1iW2Q73A7Yo37hhjo4Pa'),(24,'niter@gmail.com','2808','default.jpg','$2b$12$62G52vEmQ7LPs1EyqkDqEe2P/3iesRjD/R4bW964sy.YYAg7GyLj2'),(25,'deniswambui@icloud.com','2195','default.jpg','$2b$12$vmZorzx0HO5DFJjsgzu4Su9XAe3XyXN7fwqBwXldwsmdyKGweC3M2'),(26,'annwanjikun05@gmail.com','1960','default.jpg','$2b$12$tM4TLZvVdWj9Bf.5h5qHs.t695/H0XB/6DKwFyLhgdkHHJH13r80a'),(27,'Ngimaalex@gmail.com','2319','default.jpg','$2b$12$9fLKp93BeJpWaZlaK8Z7COWaWdcQiUMhAMHtmquuiqWj43/2oSnBq'),(28,'niteriic@gmail.com','158','default.jpg','$2b$12$XaDgt1mtYMRzN2xUI6u7FeesA6nuGMvYK7KI9vRCKBIohMtSQX0Mm'),(29,'niteriiic@gmail.com','2067','default.jpg','$2b$12$6VeE0ksxcMl0aUiZytb7gO1JQzy0vWQ9JZrLKkZBIszYsnP3IxBAi'),(30,'nite@gmail.com','2324','default.jpg','$2b$12$fw6JOAhx1eoje9CkmqHfP.Q6HAWgZ.oLCZiA3xmXvWFopLKOv1FvC');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `help`
--

DROP TABLE IF EXISTS `help`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `help` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(100) NOT NULL,
  `title` varchar(250) NOT NULL,
  `solution` text NOT NULL,
  `date_added` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `help`
--

LOCK TABLES `help` WRITE;
/*!40000 ALTER TABLE `help` DISABLE KEYS */;
INSERT INTO `help` VALUES (1,'Random help test','Help for tests','The decorated ceilings of the Natural History Museum in South Kensington, London, were designed by the museum\'s architect Alfred Waterhouse, and were unveiled at the building\'s opening in 1881. The ceiling of the large Central Hall (pictured) consists of 162 panels, 108 of which depict plants considered significant to the history of the museum, to the British Empire or to the museum\'s visitors. The remaining 54 are highly stylised decorative botanical paintings. The ceiling of the smaller North Hall consists of 36 panels, 18 of which depict plants growing in the British Isles. Both ceilings make extensive use of gilding for visual effect. Built of lath and plaster to save costs, the ceilings are unusually fragile and require extensive maintenance and restoration. Since 2016 the skeleton of a blue whale has been suspended from the ceiling of the Central Hall. (Full article...)\r\n\r\nRecently featured:\r\nEris (dwarf planet) Elasmosaurus Osbert Lancaster\r\nArchive By email More featured articles\r\nDid you know ...\r\nFakhreddine Mosque\r\nFakhreddine Mosque\r\n... that the Druze emir Fakhr al-Din built a mosque (pictured) in Mount Lebanon despite the non-use of mosques by the Druze?\r\n... that none of the 17 anchor projects put forward for recovery from the 2011 Christchurch earthquake in New Zealand have been delivered on time?\r\n... that Stuart Bergsma, a medical missionary in Ethiopia and India, connected speaking in tongues with emotional stress?\r\n... that the 1994 video game Kajko i Kokosz, the first based on the Polish comic book series of the same name, was not playtested, and the initial release had to be recalled and replaced?\r\n... that Sarah Chapone compares the legal situation of married women in 18th-century England to slavery in her legal treatise?\r\n... that the J. N. Petit Library in Mumbai is considered to be one of the finest examples of Neo-Gothic architecture in the city?\r\n... that the transmitter used to start Nashville radio station WSIX was purchased in exchange for five barrels of oil?\r\n... that during the women\'s marathon at the 1983 World Championships in Athletics, one runner fell out of medal contention when she stopped for a toilet break?\r\nArchive Start a new article Nominate an article\r\nIn the news\r\nCOVID-19 pandemic\r\nDisease Virus Testing Timeline By location Impact Notable deaths Portal\r\nNajib Razak in 2008\r\nNajib Razak\r\nFormer Malaysian prime minister Najib Razak (pictured) is found guilty on all seven charges in the first trial related to the 1MDB scandal.\r\nA series of attacks over disputed farmland in Darfur, Sudan, leaves more than eighty people dead and several villages destroyed.\r\nA security breach in the administration system of Twitter results in many prominent accounts promoting a bitcoin scam.','2020-07-30 18:12:07');
/*!40000 ALTER TABLE `help` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `icon`
--

DROP TABLE IF EXISTS `icon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `icon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `date_added` datetime DEFAULT NULL,
  `branch` int(11) NOT NULL,
  `icon` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `icon`
--

LOCK TABLES `icon` WRITE;
/*!40000 ALTER TABLE `icon` DISABLE KEYS */;
/*!40000 ALTER TABLE `icon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `image_company`
--

DROP TABLE IF EXISTS `image_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `image_company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company` int(11) NOT NULL,
  `image` varchar(250) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `company` (`company`),
  CONSTRAINT `image_company_ibfk_1` FOREIGN KEY (`company`) REFERENCES `company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `image_company`
--

LOCK TABLES `image_company` WRITE;
/*!40000 ALTER TABLE `image_company` DISABLE KEYS */;
INSERT INTO `image_company` VALUES (1,2,'3f0ab13b13a93140.png');
/*!40000 ALTER TABLE `image_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mpesa`
--

DROP TABLE IF EXISTS `mpesa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mpesa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` float DEFAULT NULL,
  `receipt_number` varchar(255) DEFAULT NULL,
  `transaction_date` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `checkout_request_id` varchar(255) DEFAULT NULL,
  `merchant_request_id` varchar(255) DEFAULT NULL,
  `result_code` int(11) NOT NULL,
  `result_desc` text,
  `date_added` datetime DEFAULT NULL,
  `local_transactional_key` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mpesa`
--

LOCK TABLES `mpesa` WRITE;
/*!40000 ALTER TABLE `mpesa` DISABLE KEYS */;
INSERT INTO `mpesa` VALUES (1,NULL,NULL,NULL,'0','ws_CO_230720201509565921','3468-14243299-1',1032,'Request cancelled by user','2020-07-23 12:10:13','79641687c566a75c2771');
/*!40000 ALTER TABLE `mpesa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `online_booking`
--

DROP TABLE IF EXISTS `online_booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `online_booking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `service_name` varchar(100) DEFAULT NULL,
  `start` varchar(200) DEFAULT NULL,
  `branch_id` int(11) DEFAULT NULL,
  `ticket` varchar(6) NOT NULL,
  `date_added` datetime DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  `next` tinyint(1) NOT NULL,
  `serviced` tinyint(1) NOT NULL,
  `teller` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `online_booking`
--

LOCK TABLES `online_booking` WRITE;
/*!40000 ALTER TABLE `online_booking` DISABLE KEYS */;
/*!40000 ALTER TABLE `online_booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `body` text NOT NULL,
  `token` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (1,'{\"Body\":{\"stkCallback\":{\"MerchantRequestID\":\"23856-29202510-1\",\"CheckoutRequestID\":\"ws_CO_220720200038503405\",\"ResultCode\":0,\"ResultDesc\":\"The service request is processed successfully.\",\"CallbackMetadata\":{\"Item\":[{\"Name\":\"Amount\",\"Value\":5.00},{\"Name\":\"MpesaReceiptNumber\",\"Value\":\"OGM1XQGKTR\"},{\"Name\":\"Balance\"},{\"Name\":\"TransactionDate\",\"Value\":20200722003900},{\"Name\":\"PhoneNumber\",\"Value\":254719573310}]}}}}','33e02e2915611eeb7e2e'),(2,'{\"Body\":{\"stkCallback\":{\"MerchantRequestID\":\"23854-29222959-1\",\"CheckoutRequestID\":\"ws_CO_220720200100095633\",\"ResultCode\":0,\"ResultDesc\":\"The service request is processed successfully.\",\"CallbackMetadata\":{\"Item\":[{\"Name\":\"Amount\",\"Value\":10.00},{\"Name\":\"MpesaReceiptNumber\",\"Value\":\"OGM5XQI1S9\"},{\"Name\":\"Balance\"},{\"Name\":\"TransactionDate\",\"Value\":20200722010017},{\"Name\":\"PhoneNumber\",\"Value\":254719573310}]}}}}','5d430e76d5b2f9c78980'),(3,'{\"Body\":{\"stkCallback\":{\"MerchantRequestID\":\"3468-14243299-1\",\"CheckoutRequestID\":\"ws_CO_230720201509565921\",\"ResultCode\":1032,\"ResultDesc\":\"Request cancelled by user\"}}}','79641687c566a75c2771'),(4,'{\"Body\":{\"stkCallback\":{\"MerchantRequestID\":\"15593-12821390-1\",\"CheckoutRequestID\":\"ws_CO_310720201743387493\",\"ResultCode\":1037,\"ResultDesc\":\"DS timeout.\"}}}','d7bee7df38daacaf809c'),(5,'{\"Body\":{\"stkCallback\":{\"MerchantRequestID\":\"30521-13307640-1\",\"CheckoutRequestID\":\"ws_CO_310720201824371607\",\"ResultCode\":1037,\"ResultDesc\":\"DS timeout.\"}}}','2a8d0ca83a5d0bd884a6'),(6,'{\"Body\":{\"stkCallback\":{\"MerchantRequestID\":\"15589-12925763-1\",\"CheckoutRequestID\":\"ws_CO_310720201827488897\",\"ResultCode\":1037,\"ResultDesc\":\"DS timeout.\"}}}','777355cc15103c222803'),(7,'{\"Body\":{\"stkCallback\":{\"MerchantRequestID\":\"30857-12933524-1\",\"CheckoutRequestID\":\"ws_CO_310720201831199400\",\"ResultCode\":1037,\"ResultDesc\":\"DS timeout.\"}}}','6f5e6a4cd4135aef5de9'),(8,'{\"Body\":{\"stkCallback\":{\"MerchantRequestID\":\"15581-15890385-1\",\"CheckoutRequestID\":\"ws_CO_010820201745442726\",\"ResultCode\":0,\"ResultDesc\":\"The service request is processed successfully.\",\"CallbackMetadata\":{\"Item\":[{\"Name\":\"Amount\",\"Value\":5.00},{\"Name\":\"MpesaReceiptNumber\",\"Value\":\"OH1090HEI2\"},{\"Name\":\"Balance\"},{\"Name\":\"TransactionDate\",\"Value\":20200801174550},{\"Name\":\"PhoneNumber\",\"Value\":254701811299}]}}}}','41b5b210c84462dbe785'),(9,'{\"Body\":{\"stkCallback\":{\"MerchantRequestID\":\"30519-17099271-1\",\"CheckoutRequestID\":\"ws_CO_010820202141404889\",\"ResultCode\":0,\"ResultDesc\":\"The service request is processed successfully.\",\"CallbackMetadata\":{\"Item\":[{\"Name\":\"Amount\",\"Value\":5.00},{\"Name\":\"MpesaReceiptNumber\",\"Value\":\"OH149BJF82\"},{\"Name\":\"Balance\"},{\"Name\":\"TransactionDate\",\"Value\":20200801214155},{\"Name\":\"PhoneNumber\",\"Value\":254721657647}]}}}}','fb12932f505fd070f458'),(10,'{\"Body\":{\"stkCallback\":{\"MerchantRequestID\":\"19835-17192260-1\",\"CheckoutRequestID\":\"ws_CO_010820202208266369\",\"ResultCode\":0,\"ResultDesc\":\"The service request is processed successfully.\",\"CallbackMetadata\":{\"Item\":[{\"Name\":\"Amount\",\"Value\":10.00},{\"Name\":\"MpesaReceiptNumber\",\"Value\":\"OH179C58WL\"},{\"Name\":\"Balance\"},{\"Name\":\"TransactionDate\",\"Value\":20200801220851},{\"Name\":\"PhoneNumber\",\"Value\":254721657647}]}}}}','062c0713ce707959e500');
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recovery`
--

DROP TABLE IF EXISTS `recovery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recovery` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` int(11) NOT NULL,
  `code` varchar(50) NOT NULL,
  `used` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user` (`user`),
  CONSTRAINT `recovery_ibfk_1` FOREIGN KEY (`user`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recovery`
--

LOCK TABLES `recovery` WRITE;
/*!40000 ALTER TABLE `recovery` DISABLE KEYS */;
INSERT INTO `recovery` VALUES (1,8,'1998-0612',0),(2,5,'3421-0560',1),(3,5,'1012-5371',0),(4,5,'1801-9845',0),(5,5,'7932-6933',1),(6,8,'8953-3946',0),(7,5,'7325-3302',1),(8,5,'7704-8247',1),(9,4,'7353-9038',1);
/*!40000 ALTER TABLE `recovery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service`
--

DROP TABLE IF EXISTS `service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `service` varchar(250) DEFAULT NULL,
  `is_medical` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service`
--

LOCK TABLES `service` WRITE;
/*!40000 ALTER TABLE `service` DISABLE KEYS */;
INSERT INTO `service` VALUES (1,'Banking','Banking and Finance',0),(2,'Finance','Testing',0);
/*!40000 ALTER TABLE `service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service_offered`
--

DROP TABLE IF EXISTS `service_offered`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `service_offered` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `branch_id` int(11) NOT NULL,
  `name` varchar(250) DEFAULT NULL,
  `teller` varchar(100) DEFAULT NULL,
  `date_added` datetime DEFAULT NULL,
  `code` varchar(10) NOT NULL,
  `icon` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service_offered`
--

LOCK TABLES `service_offered` WRITE;
/*!40000 ALTER TABLE `service_offered` DISABLE KEYS */;
INSERT INTO `service_offered` VALUES (1,3,'Loans Services','','2020-07-21 20:48:44','LNS','1'),(2,5,'Deposits','','2020-07-24 23:54:04','DPT','1'),(4,5,'Withdrawals and Deposits','','2020-07-24 23:58:16','WND','1');
/*!40000 ALTER TABLE `service_offered` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teller`
--

DROP TABLE IF EXISTS `teller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teller` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `date_added` datetime DEFAULT NULL,
  `branch` int(11) DEFAULT NULL,
  `service` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `number` (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teller`
--

LOCK TABLES `teller` WRITE;
/*!40000 ALTER TABLE `teller` DISABLE KEYS */;
INSERT INTO `teller` VALUES (1,1,'2020-07-24 08:36:03',5,'Info'),(3,2,'2020-07-24 08:36:03',5,'Super'),(4,3,'2020-07-24 08:36:04',5,'Merger'),(5,5,'2020-07-25 19:24:08',1,'Loans Services');
/*!40000 ALTER TABLE `teller` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teller_booking`
--

DROP TABLE IF EXISTS `teller_booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teller_booking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teller_to` int(11) NOT NULL,
  `booking_id` int(11) NOT NULL,
  `teller_from` int(11) DEFAULT NULL,
  `remarks` text NOT NULL,
  `active` tinyint(1) NOT NULL,
  `date_added` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teller_booking`
--

LOCK TABLES `teller_booking` WRITE;
/*!40000 ALTER TABLE `teller_booking` DISABLE KEYS */;
/*!40000 ALTER TABLE `teller_booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(12) NOT NULL,
  `email` varchar(48) NOT NULL,
  `image_file` varchar(20) NOT NULL,
  `password` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','admin@gmail.com','default.jpg','$2b$12$BXXQc5RIGZvymRHuvK1Eju99Uh6.FRn10BejYN8HgIQWtytE2jf1W');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `video`
--

DROP TABLE IF EXISTS `video`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) DEFAULT NULL,
  `active` int(11) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `video`
--

LOCK TABLES `video` WRITE;
/*!40000 ALTER TABLE `video` DISABLE KEYS */;
/*!40000 ALTER TABLE `video` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-02  8:53:17
