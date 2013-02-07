CREATE DATABASE  IF NOT EXISTS `emailtoolsystem` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `emailtoolsystem`;
-- MySQL dump 10.13  Distrib 5.5.16, for Win32 (x86)
--
-- Host: localhost    Database: db_email
-- ------------------------------------------------------
-- Server version	5.5.28

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
-- Table structure for table `anuncios`
--

DROP TABLE IF EXISTS `anuncios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `anuncios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) DEFAULT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `url_id` varchar(110) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `html` longtext,
  `tags` text,
  `cidade` varchar(110) DEFAULT NULL,
  `estado` varchar(110) DEFAULT NULL,
  `regiao` varchar(110) DEFAULT NULL,
  `sessao` varchar(110) DEFAULT NULL,
  `emails_type` tinyint(1) DEFAULT '-1' COMMENT 'Emails Type - 0: Only Externals; 1: Only Craigslist; 2: Both.',
  `has_phone` tinyint(1) DEFAULT '0',
  `post_date` datetime DEFAULT NULL,
  `insert_date` datetime DEFAULT NULL,
  `status` tinyint(1) DEFAULT '1' COMMENT '0: Unactive; 1: Active; 2: Deleted; 3: Waiting',
  `newsletters_id` int(11) DEFAULT NULL,
  `access_date` datetime DEFAULT '1900-01-01 00:00:00',
  PRIMARY KEY (`id`),
  UNIQUE KEY `k` (`k`),
  UNIQUE KEY `url_id` (`url_id`),
  UNIQUE KEY `url` (`url`),
  KEY `cidade` (`cidade`) USING BTREE,
  KEY `estado` (`estado`) USING BTREE,
  KEY `regiao` (`regiao`) USING BTREE,
  KEY `sessao` (`sessao`) USING BTREE,
  KEY `email_type` (`emails_type`) USING BTREE,
  KEY `has_phone` (`has_phone`) USING BTREE,
  KEY `post_date` (`post_date`) USING BTREE,
  KEY `status` (`status`) USING BTREE,
  KEY `insert_date` (`insert_date`) USING BTREE,
  KEY `in_anuncios_url_id` (`url_id`),
  KEY `in_anuncios_post_date` (`post_date`),
  KEY `in_anuncios_regiao` (`regiao`),
  KEY `fk_anuncios_newsletters1_idx` (`newsletters_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2146350 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `anuncios_emails`
--

DROP TABLE IF EXISTS `anuncios_emails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `anuncios_emails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) NOT NULL,
  `nome` varchar(245) NOT NULL,
  `url_id` varchar(255) NOT NULL,
  `tipo` varchar(20) NOT NULL,
  `anuncio` varchar(110) NOT NULL,
  `regiao` varchar(110) NOT NULL,
  `insert_date` datetime NOT NULL,
  `send_date` datetime DEFAULT NULL,
  `send_key` varchar(32) DEFAULT NULL,
  `first_read` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `k` (`k`),
  UNIQUE KEY `url_id` (`url_id`,`anuncio`),
  UNIQUE KEY `nome` (`nome`),
  UNIQUE KEY `send_key` (`send_key`)
) ENGINE=InnoDB AUTO_INCREMENT=427049 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `anuncios_telefones`
--

DROP TABLE IF EXISTS `anuncios_telefones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `anuncios_telefones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) NOT NULL,
  `nome` varchar(12) NOT NULL,
  `url_id` varchar(12) NOT NULL,
  `anuncio` varchar(110) NOT NULL,
  `insert_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `k` (`k`),
  UNIQUE KEY `url_id` (`url_id`,`anuncio`)
) ENGINE=InnoDB AUTO_INCREMENT=28727 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `blacklist`
--

DROP TABLE IF EXISTS `blacklist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blacklist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `url_id` varchar(110) NOT NULL,
  `insert_date` datetime NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `k` (`k`),
  UNIQUE KEY `url_id` (`url_id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cidades`
--

DROP TABLE IF EXISTS `cidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cidades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `url_id` varchar(110) DEFAULT NULL,
  `abreviacao` varchar(50) NOT NULL,
  `estado` varchar(110) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  `url` varchar(200) DEFAULT NULL,
  `dhinclusao` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `k_UNIQUE` (`k`),
  UNIQUE KEY `url_id_UNIQUE` (`url_id`)
) ENGINE=InnoDB AUTO_INCREMENT=517 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `envios`
--

DROP TABLE IF EXISTS `envios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `envios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) NOT NULL,
  `anuncio` varchar(110) NOT NULL,
  `tags` text,
  `email` varchar(245) NOT NULL,
  `email_type` varchar(50) NOT NULL,
  `cidade` varchar(110) NOT NULL,
  `estado` varchar(110) NOT NULL,
  `sessao` varchar(110) NOT NULL,
  `carta` varchar(110) NOT NULL,
  `email_envio` varchar(110) NOT NULL,
  `smtp` varchar(110) NOT NULL,
  `has_phone` tinyint(4) DEFAULT NULL,
  `num_reads` int(11) NOT NULL DEFAULT '0',
  `first_read` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `send_date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `post_date` datetime DEFAULT NULL,
  `contacted` char(1) DEFAULT '0',
  `comentario` char(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `k` (`k`),
  UNIQUE KEY `email` (`email`),
  KEY `anuncio` (`anuncio`) USING BTREE,
  KEY `has_phone` (`has_phone`) USING BTREE,
  KEY `send_date` (`send_date`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=349131 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `envios_comentario`
--

DROP TABLE IF EXISTS `envios_comentario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `envios_comentario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_envio` int(11) NOT NULL,
  `comentario` blob,
  `data_agenda` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `error_log`
--

DROP TABLE IF EXISTS `error_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `error_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) DEFAULT NULL,
  `description` text,
  `insert_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `k_UNIQUE` (`k`)
) ENGINE=InnoDB AUTO_INCREMENT=1439792 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `estado`
--

DROP TABLE IF EXISTS `estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) DEFAULT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `url_id` varchar(110) DEFAULT NULL,
  `regiao` varchar(110) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `estados`
--

DROP TABLE IF EXISTS `estados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `url_id` varchar(110) NOT NULL,
  `regiao` varchar(110) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `k_UNIQUE` (`k`),
  UNIQUE KEY `url_id_UNIQUE` (`url_id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `newsletters`
--

DROP TABLE IF EXISTS `newsletters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `newsletters` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(255) NOT NULL,
  `texto` text NOT NULL,
  `insert_date` datetime NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  `usuarios_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_newsletters_usuarios1_idx` (`usuarios_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `newsletters_imagens`
--

DROP TABLE IF EXISTS `newsletters_imagens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `newsletters_imagens` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `imagem` varchar(255) NOT NULL,
  `carta` varchar(255) NOT NULL,
  `newsletters_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_newsletters_imagens_newsletters1_idx` (`newsletters_id`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pagamentos`
--

DROP TABLE IF EXISTS `pagamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pagamentos` (
  `idpagamento` int(11) NOT NULL AUTO_INCREMENT,
  `data_pagamento` datetime NOT NULL,
  `idplano` int(11) NOT NULL,
  `iduser` int(11) NOT NULL,
  PRIMARY KEY (`idpagamento`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `planos`
--

DROP TABLE IF EXISTS `planos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `planos` (
  `idplano` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `preco` decimal(10,0) NOT NULL,
  `tempo` int(11) NOT NULL,
  `ativo` char(1) NOT NULL DEFAULT '1',
  `descricao` blob,
  PRIMARY KEY (`idplano`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `regiao`
--

DROP TABLE IF EXISTS `regiao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `regiao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) DEFAULT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `url_id` varchar(110) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `regioes`
--

DROP TABLE IF EXISTS `regioes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `regioes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `url_id` varchar(110) NOT NULL,
  `inicio` time NOT NULL,
  `fim` time NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `k` (`k`),
  UNIQUE KEY `url_id` (`url_id`),
  KEY `in_regioes_inicio` (`inicio`),
  KEY `in_regioes_fim` (`fim`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `remetentes`
--

DROP TABLE IF EXISTS `remetentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `remetentes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `url_id` varchar(110) NOT NULL,
  `email` varchar(100) NOT NULL,
  `quantidade` int(5) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `k` (`k`),
  UNIQUE KEY `url_id` (`url_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sessoes`
--

DROP TABLE IF EXISTS `sessoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sessoes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `url_id` varchar(110) NOT NULL,
  `abreviacao` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `k` (`k`),
  UNIQUE KEY `url_id` (`url_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sessoes_whitelist`
--

DROP TABLE IF EXISTS `sessoes_whitelist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sessoes_whitelist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `url_id` varchar(110) NOT NULL,
  `sessao` varchar(110) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `k` (`k`),
  UNIQUE KEY `url_id` (`url_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `smtp`
--

DROP TABLE IF EXISTS `smtp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `smtp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuarios_id` int(11) NOT NULL,
  `usuario` varchar(100) NOT NULL,
  `senha` varchar(30) NOT NULL,
  `porta` int(11) NOT NULL DEFAULT '25',
  `host` varchar(250) NOT NULL,
  `seguro` tinyint(1) NOT NULL DEFAULT '0',
  `status` tinyint(1) NOT NULL DEFAULT '1',
  `dta_proximo_envio` timestamp NULL DEFAULT NULL COMMENT ' /* comment truncated */',
  `limite_envio` int(11) NOT NULL DEFAULT '0' COMMENT 'limite diario de envio',
  `qtde_enviada` int(11) NOT NULL DEFAULT '0' COMMENT 'Qtde de email enviada no dia, com referencia a dhultimo_envio',
  `qtde_max_envio` int(11) NOT NULL DEFAULT '5' COMMENT ' /* comment truncated */',
  `qtde_seg_envio` int(11) NOT NULL DEFAULT '5' COMMENT ' /* comment truncated */',

  PRIMARY KEY (`id`),
  KEY `fk_smtp_usuarios_idx` (`usuarios_id`),
  CONSTRAINT `fk_smtp_usuarios` FOREIGN KEY (`usuarios_id`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sys_privileges`
--

DROP TABLE IF EXISTS `sys_privileges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sys_privileges` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) NOT NULL,
  `name` varchar(100) NOT NULL,
  `url_id` varchar(110) NOT NULL,
  `group` varchar(110) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url_id_UNIQUE` (`url_id`),
  UNIQUE KEY `k_UNIQUE` (`k`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sys_privileges_group`
--

DROP TABLE IF EXISTS `sys_privileges_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sys_privileges_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) NOT NULL,
  `name` varchar(100) NOT NULL,
  `url_id` varchar(110) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url_id_UNIQUE` (`url_id`),
  UNIQUE KEY `k_UNIQUE` (`k`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sys_privileges_users`
--

DROP TABLE IF EXISTS `sys_privileges_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sys_privileges_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sys_privilege` varchar(110) NOT NULL,
  `user` varchar(110) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `url`
--

DROP TABLE IF EXISTS `url`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `url` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `url_id` varchar(110) NOT NULL,
  `sessao` varchar(110) NOT NULL,
  `cidade` varchar(110) NOT NULL,
  `estado` varchar(110) NOT NULL,
  `bloq_sessao` tinyint(1) NOT NULL DEFAULT '0',
  `bloq_cidade` tinyint(1) NOT NULL DEFAULT '0',
  `insert_date` datetime NOT NULL,
  `last_access` datetime NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `k` (`k`),
  UNIQUE KEY `url_id` (`url_id`),
  UNIQUE KEY `nome` (`nome`)
) ENGINE=InnoDB AUTO_INCREMENT=3498 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `used_emails`
--

DROP TABLE IF EXISTS `used_emails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `used_emails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=77384 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` varchar(32) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `url_id` varchar(110) NOT NULL,
  `sexo` char(1) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(32) NOT NULL,
  `ac_crawler` tinyint(1) DEFAULT '0',
  `ac_sender` tinyint(1) DEFAULT '0',
  `insert_date` datetime NOT NULL,
  `last_login` datetime NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`,`status`),
  UNIQUE KEY `url_id_UNIQUE` (`url_id`),
  UNIQUE KEY `k_UNIQUE` (`k`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-12-24 12:22:17
