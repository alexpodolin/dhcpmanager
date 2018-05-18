-- MySQL dump 10.14  Distrib 5.5.56-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: dhcpd
-- ------------------------------------------------------
-- Server version	5.5.56-MariaDB

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
-- Table structure for table `dhcp_srv`
--

DROP TABLE IF EXISTS `dhcp_srv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dhcp_srv` (
  `id` tinyint(3) NOT NULL AUTO_INCREMENT,
  `srv_hostname` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `srv_hostname_UNIQUE` (`srv_hostname`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='dhcp servers list';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `hosts_allow`
--

DROP TABLE IF EXISTS `hosts_allow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_allow` (
  `id` smallint(5) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(32) NOT NULL,
  `mac_addr` varchar(18) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `mac_addr_UNIQUE` (`mac_addr`)
) ENGINE=InnoDB AUTO_INCREMENT=5036 DEFAULT CHARSET=utf8 COMMENT='hosts allow to get ip address and parameters via dhcpd server';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `interfaces_ipv4`
--

DROP TABLE IF EXISTS `interfaces_ipv4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `interfaces_ipv4` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_srv` tinyint(3) NOT NULL,
  `vlan` smallint(4) NOT NULL,
  `phys_dev_srv` varchar(15) NOT NULL DEFAULT 'enp4s0f0',
  `onboot` varchar(3) NOT NULL DEFAULT 'yes',
  `subnet_ipv4` int(15) unsigned NOT NULL,
  `prefix` tinyint(2) NOT NULL,
  `int_ipv4` int(15) unsigned NOT NULL,
  `dns_srv_01` int(15) unsigned NOT NULL,
  `dns_srv_02` int(15) unsigned NOT NULL,
  `dns_domain` varchar(25) DEFAULT 'NR.LOCAL',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `int_ipv4_UNIQUE` (`int_ipv4`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8 COMMENT='network sub_interfaces for dhcpd server`s';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `net_ipv4`
--

DROP TABLE IF EXISTS `net_ipv4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `net_ipv4` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `interface` varchar(15) NOT NULL,
  `subnet_ipv4` int(15) unsigned NOT NULL,
  `netmask` int(15) unsigned NOT NULL,
  `default_gw` int(15) unsigned NOT NULL,
  `broadcast` int(15) unsigned NOT NULL,
  `ip_range_start` int(15) unsigned NOT NULL,
  `ip_range_end` int(15) unsigned NOT NULL,
  `failover_peer` varchar(20) NOT NULL DEFAULT 'nr-dhcpd-failover',
  `opt_242` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `reserved_ipv4`
--

DROP TABLE IF EXISTS `reserved_ipv4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reserved_ipv4` (
  `id` smallint(5) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(32) NOT NULL,
  `mac_addr` varchar(18) NOT NULL,
  `res_ipv4` int(15) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mac_addr_UNIQUE` (`mac_addr`),
  UNIQUE KEY `res_ipv4_UNIQUE` (`res_ipv4`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-18 10:03:28
