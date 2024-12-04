-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 24, 2024 at 08:02 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `premier_league_db`
--
CREATE DATABASE IF NOT EXISTS `premier_league_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `premier_league_db`;

-- --------------------------------------------------------

--
-- Table structure for table `Admin`
--

DROP TABLE IF EXISTS `Admin`;
CREATE TABLE IF NOT EXISTS `Admin` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `rights_id` bigint(20) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `rights_id` (`rights_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Admin`
--

INSERT INTO `Admin` (`id`, `name`, `email`, `rights_id`) VALUES
(1, 'Victor', 'vicotr322@gmail.com', 0);

-- --------------------------------------------------------

--
-- Table structure for table `Analyst`
--

DROP TABLE IF EXISTS `Analyst`;
CREATE TABLE IF NOT EXISTS `Analyst` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `rights_id` bigint(20) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `rights_id` (`rights_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Analyst`
--

INSERT INTO `Analyst` (`id`, `name`, `email`, `rights_id`) VALUES
(1, 'John', 'john44@ukr.net', 1);

-- --------------------------------------------------------

--
-- Table structure for table `Comments`
--

DROP TABLE IF EXISTS `Comments`;
CREATE TABLE IF NOT EXISTS `Comments` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) UNSIGNED NOT NULL,
  `post_id` bigint(20) UNSIGNED NOT NULL,
  `created_at` datetime NOT NULL,
  `comment_text` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `post_id` (`post_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Comments`
--

INSERT INTO `Comments` (`id`, `user_id`, `post_id`, `created_at`, `comment_text`) VALUES
(1, 1, 1, '2024-11-24 19:43:32', 'Comment!!!'),
(2, 4, 1, '2024-11-24 19:45:50', 'Nice post!\r\n'),
(3, 2, 1, '2024-11-24 19:46:07', 'Bad post!\r\n'),
(4, 3, 4, '2024-11-24 19:58:29', 'text... your advert could be here...'),
(5, 3, 3, '2024-11-24 19:59:20', 'Lorem ipsum dolom sit amet...'),
(6, 1, 2, '2024-11-24 19:59:55', 'New comment text!!');

-- --------------------------------------------------------

--
-- Table structure for table `Data`
--

DROP TABLE IF EXISTS `Data`;
CREATE TABLE IF NOT EXISTS `Data` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `media_paths` varchar(255) DEFAULT NULL,
  `creation_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Data`
--

INSERT INTO `Data` (`id`, `title`, `description`, `media_paths`, `creation_time`) VALUES
(1, 'New title#1', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eleifend egestas tellus at tristique. Suspendisse neque odio, dictum ullamcorper vehicula sed, bibendum sit amet libero. Curabitur vestibulum nisi eget est pretium, at pretium augue feugiat. Suspendisse nec ipsum dolor. In et consectetur urna, eu sollicitudin odio. Nullam egestas eros et ipsum dapibus, et volutpat enim lobortis. Proin sed commodo felis. Morbi sed est in justo elementum dapibus. Praesent viverra venenatis ante, vel lobortis arcu cursus sed. Duis id ornare nunc. Etiam malesuada elit in ipsum interdum, ut congue est ornare. Integer eget lorem et sem sollicitudin aliquam. Aliquam vitae elit et diam vulputate euismod. ', NULL, '2024-10-27 22:10:17'),
(2, 'Post title#2', 'Nulla ornare turpis velit, et tincidunt ipsum viverra in. Curabitur eget rhoncus mi. Etiam quis convallis eros. Phasellus laoreet egestas vehicula. Duis sit amet malesuada odio. Fusce dignissim enim at tellus finibus scelerisque. Ut efficitur fringilla est eu condimentum. Sed ut lacinia felis. Praesent metus neque, congue ornare arcu in, pulvinar viverra nibh. Ut porta vulputate leo, a consectetur nisi tincidunt eget. Nulla non rutrum justo, tempus dictum quam. Fusce sed bibendum libero, sit amet scelerisque metus. ', NULL, '2024-10-27 22:11:17'),
(3, 'Post #3', 'descritption, some text...', NULL, '2024-11-24 19:54:24'),
(4, 'Post #4', 'new description for post #4', NULL, '2024-11-24 19:54:57');

-- --------------------------------------------------------

--
-- Table structure for table `issue_ticket`
--

DROP TABLE IF EXISTS `issue_ticket`;
CREATE TABLE IF NOT EXISTS `issue_ticket` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) UNSIGNED NOT NULL,
  `admin_id` bigint(20) UNSIGNED DEFAULT NULL,
  `issue_description` varchar(255) NOT NULL,
  UNIQUE KEY `id` (`id`),
  KEY `issue_id` (`user_id`,`admin_id`),
  KEY `user_id` (`user_id`),
  KEY `admin_id` (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `issue_ticket`
--

INSERT INTO `issue_ticket` (`id`, `user_id`, `admin_id`, `issue_description`) VALUES
(1, 3, NULL, 'Lorem ipsum...'),
(2, 1, 1, '*some issue description...*'),
(3, 2, NULL, 'Issue with post #1!!!\r\n'),
(4, 3, 1, 'A lot if issues with post #2!'),
(5, 3, 1, 'Website lagging!');

-- --------------------------------------------------------

--
-- Table structure for table `push_data_request`
--

DROP TABLE IF EXISTS `push_data_request`;
CREATE TABLE IF NOT EXISTS `push_data_request` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) UNSIGNED NOT NULL,
  `data_id` bigint(20) UNSIGNED NOT NULL,
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`,`data_id`),
  KEY `data_id` (`data_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `rights`
--

DROP TABLE IF EXISTS `rights`;
CREATE TABLE IF NOT EXISTS `rights` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rights`
--

INSERT INTO `rights` (`id`, `title`, `description`) VALUES
(0, 'Admin', 'Some description of what admin can do...'),
(1, 'Analyst', 'Also some description of what analyst can do...'),
(2, 'User', 'User abilites...\r\n\r\nYour ad could be here...');

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
CREATE TABLE IF NOT EXISTS `User` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `rights_id` bigint(20) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `rights_id` (`rights_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `User`
--

INSERT INTO `User` (`id`, `name`, `email`, `rights_id`) VALUES
(1, 'Andrew', 'andw@outlook.com', 2),
(2, 'Marva', 'marvaFL@gmail.com', 2),
(3, 'Joyce', 'joyceMerril@gmail.com', 2),
(4, 'Kelly', 'kelly_bowers1@gmail.com', 2);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Admin`
--
ALTER TABLE `Admin`
  ADD CONSTRAINT `Admin_ibfk_1` FOREIGN KEY (`rights_id`) REFERENCES `rights` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Analyst`
--
ALTER TABLE `Analyst`
  ADD CONSTRAINT `Analyst_ibfk_1` FOREIGN KEY (`rights_id`) REFERENCES `rights` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Comments`
--
ALTER TABLE `Comments`
  ADD CONSTRAINT `Comments_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Comments_ibfk_2` FOREIGN KEY (`post_id`) REFERENCES `Data` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `issue_ticket`
--
ALTER TABLE `issue_ticket`
  ADD CONSTRAINT `issue_ticket_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `User` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `issue_ticket_ibfk_3` FOREIGN KEY (`admin_id`) REFERENCES `Admin` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `push_data_request`
--
ALTER TABLE `push_data_request`
  ADD CONSTRAINT `push_data_request_ibfk_1` FOREIGN KEY (`data_id`) REFERENCES `Data` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `push_data_request_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `User` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `User`
--
ALTER TABLE `User`
  ADD CONSTRAINT `User_ibfk_1` FOREIGN KEY (`rights_id`) REFERENCES `rights` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
