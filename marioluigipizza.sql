-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Gegenereerd op: 02 nov 2022 om 22:00
-- Serverversie: 5.7.36
-- PHP-versie: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `marioluigipizza`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `tbl_menu`
--

DROP TABLE IF EXISTS `tbl_menu`;
CREATE TABLE IF NOT EXISTS `tbl_menu` (
  `menu_id` int(250) NOT NULL AUTO_INCREMENT,
  `name` varchar(400) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `ingredients` varchar(250) NOT NULL,
  `pic` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`menu_id`)
) ENGINE=InnoDB AUTO_INCREMENT=332 DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `tbl_menu`
--

INSERT INTO `tbl_menu` (`menu_id`, `name`, `price`, `ingredients`, `pic`, `type`) VALUES
(279, 'Margherita', '8.90', 'flour, tomato sauce, mozzarella', 'pizza1.png', 'pizza'),
(280, 'Marinara', '9.90', 'flour, tomato sauce, extra virgin olive oil, oregano and garlic', 'pizza2.png', 'pizza'),
(281, 'Prosciutto e funghi', '11.90', 'tomato sauce, mozzarella, prosciutto cotto, and mushrooms', 'pizza3.png', 'pizza'),
(282, 'Quattro Stagioni', '11.90', 'flour, tomato sauce, mozzarella, artichokes, olives, mushrooms, prosciutto cotto', 'pizza4.png', 'pizza'),
(283, 'Capricciosa', '12.90', 'flour, tomato sauce, mozzarella,  Italian baked ham, mushroom, artichoke and tomato', 'pizza5.png', 'pizza'),
(284, 'Quattro Formaggi', '12.90', 'flour, tomato sauce, mozzarella, gorgonzola, parmesan, Emmental, oregano, basil', 'pizza6.png', 'pizza'),
(285, 'Ortolana', '11.90', 'flour, tomato sauce, mozzarella, tomatoes, garlic, bell pepper, courgettes, eggplant,oregano, olives', 'pizza7.png', 'pizza'),
(286, 'Diavola', '13.90', 'flour, tomato sauce, mozzarella, spianata romana salami, red peppers', 'pizza8.png', 'pizza'),
(287, 'Carbonara', '13.90', 'flour, Crème frache, mozzarella, onion, mini mozzarella balls, bacon & black pepper', 'pizza9.png', 'pizza'),
(288, 'Frutti di Mare', '15.90', 'flour, tomato sauce,  scampi, squid, mussels', 'pizza10.png', 'pizza'),
(289, 'Caprese', '13.50', 'Tomato sauce, mozzarella, fresh spinach, fresh tomato, mini mozzarella balls, pizza herbs & a swirl of pesto', 'pizza11.png', 'pizza'),
(290, 'Pizza porchetta', '13.90', 'flour, tomato sauce, mozzarella, rosemary, porchetta', 'pizza12.png', 'pizza'),
(291, 'Tiramisu', '4.95', 'Mascarpone, lady fingers, liqueur, espresso', 'dessert1.png', 'dessert'),
(292, 'Crema di fragola', '4.95', 'Mascarpone cream, strawberries', 'dessert2.png', 'dessert'),
(293, 'Cannoli', '5.95', 'cannoli filling, cannoli shells', 'dessert3.png', 'dessert'),
(294, 'Pasta pomodoro', '11.45', 'Tomato sauce, onion, cherry tomatoes', 'pasta2.png', 'pasta'),
(295, 'Pasta tonno e pomodori', '13.95', 'Tomato sauce, cherry tomatoes, tuna, spring onion, garlic', 'pasta4.png', 'pasta'),
(297, 'Pasta chicken alfredo', '16.45', 'Chicken, cream, Grana Padano DOP, nutmeg, parsley, mushroom', 'pasta6.png', 'pasta'),
(298, 'Pasta pesto basil', '11.95', 'Basil pesto with pine nuts, Grana Padano DOP, pine nuts', 'pasta7.png', 'pasta'),
(300, 'Coca cola', '4.95', '', 'cola.png', 'drinks'),
(301, 'Fanta', '4.95', '', 'fanta.png', 'drinks'),
(302, 'Sprite', '4.95', '', 'sprite.png', 'drinks'),
(303, 'Wine', '4.95', '', 'wine.png', 'drinks'),
(304, 'Water', '3.20', '', 'water.png', 'drinks'),
(322, 'Panettone', '6.95', 'milk, butter, eggs, vanilla extract, zest lemon, raisins, rum extractlt', 'dessert4.png', 'dessert'),
(323, 'Pasta arrabbiata', '11.45', 'Tomato sauce, garlic, onion, chili', 'pasta1.png', 'pasta'),
(325, 'Pasta crema di funghi', '13.45', 'Cream, mushrooms, white wine, onion', 'pasta3.png', 'pasta'),
(327, 'Pasta carbonara', '13.45', 'Cream, bacon, onion, fresh egg, Grana Padano DOP, parsley', 'pasta5.png', 'pasta'),
(330, 'Pasta bolognese', '12.95', 'Tomato sauce, minced beef, onion, carrot', 'pasta8.png', 'pasta');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `tbl_order`
--

DROP TABLE IF EXISTS `tbl_order`;
CREATE TABLE IF NOT EXISTS `tbl_order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_nr` int(55) NOT NULL,
  `terminal_id` int(11) NOT NULL,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_id`),
  KEY `terminal_id` (`terminal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `tbl_order`
--

INSERT INTO `tbl_order` (`order_id`, `order_nr`, `terminal_id`, `datetime`) VALUES
(4, 491, 1, '2022-10-26 11:52:30'),
(6, 436, 1, '2022-10-26 11:54:28'),
(7, 129, 1, '2022-10-26 11:56:51'),
(8, 952, 1, '2022-10-26 11:57:09'),
(17, 915, 1, '2022-10-28 13:40:37'),
(18, 638, 1, '2022-10-29 14:15:21'),
(22, 359, 1, '2022-11-02 21:53:08');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `tbl_orderrow`
--

DROP TABLE IF EXISTS `tbl_orderrow`;
CREATE TABLE IF NOT EXISTS `tbl_orderrow` (
  `row_id` int(11) NOT NULL AUTO_INCREMENT,
  `menu_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `quantity` int(40) NOT NULL,
  PRIMARY KEY (`row_id`),
  KEY `orderid` (`order_id`),
  KEY `menuid` (`menu_id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `tbl_orderrow`
--

INSERT INTO `tbl_orderrow` (`row_id`, `menu_id`, `order_id`, `quantity`) VALUES
(9, 300, 4, 1),
(10, 301, 4, 1),
(11, 302, 4, 1),
(15, 300, 6, 1),
(16, 301, 6, 1),
(17, 302, 6, 1),
(18, 300, 7, 1),
(19, 301, 7, 1),
(20, 302, 7, 1),
(21, 300, 8, 1),
(22, 301, 8, 1),
(23, 302, 8, 1),
(39, 291, 17, 2),
(40, 292, 17, 1),
(41, 293, 17, 2),
(42, 322, 17, 1),
(43, 291, 18, 5),
(44, 292, 18, 2),
(45, 293, 18, 2),
(46, 322, 18, 1),
(56, 294, 22, 1),
(57, 295, 22, 1),
(58, 297, 22, 2);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `tbl_restaurant`
--

DROP TABLE IF EXISTS `tbl_restaurant`;
CREATE TABLE IF NOT EXISTS `tbl_restaurant` (
  `rest_id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(40) NOT NULL,
  `street` varchar(40) NOT NULL,
  `number` int(55) DEFAULT NULL,
  PRIMARY KEY (`rest_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `tbl_restaurant`
--

INSERT INTO `tbl_restaurant` (`rest_id`, `city`, `street`, `number`) VALUES
(1, 'eindhoven', 'rachelsmolen', 1),
(2, 'test', 'teststr', NULL),
(3, 'test', 'teststr', NULL);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `tbl_terminal`
--

DROP TABLE IF EXISTS `tbl_terminal`;
CREATE TABLE IF NOT EXISTS `tbl_terminal` (
  `terminal_id` int(11) NOT NULL AUTO_INCREMENT,
  `restaurant_id` int(55) NOT NULL,
  PRIMARY KEY (`terminal_id`),
  KEY `restid` (`restaurant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `tbl_terminal`
--

INSERT INTO `tbl_terminal` (`terminal_id`, `restaurant_id`) VALUES
(1, 1);

--
-- Beperkingen voor geëxporteerde tabellen
--

--
-- Beperkingen voor tabel `tbl_order`
--
ALTER TABLE `tbl_order`
  ADD CONSTRAINT `terminal_id` FOREIGN KEY (`terminal_id`) REFERENCES `tbl_terminal` (`terminal_id`) ON DELETE CASCADE;

--
-- Beperkingen voor tabel `tbl_orderrow`
--
ALTER TABLE `tbl_orderrow`
  ADD CONSTRAINT `menuid` FOREIGN KEY (`menu_id`) REFERENCES `tbl_menu` (`menu_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `orderid` FOREIGN KEY (`order_id`) REFERENCES `tbl_order` (`order_id`) ON DELETE CASCADE;

--
-- Beperkingen voor tabel `tbl_terminal`
--
ALTER TABLE `tbl_terminal`
  ADD CONSTRAINT `restid` FOREIGN KEY (`restaurant_id`) REFERENCES `tbl_restaurant` (`rest_id`) ON DELETE NO ACTION ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
