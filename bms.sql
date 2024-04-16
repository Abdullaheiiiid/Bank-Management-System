-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 17, 2022 at 02:22 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bms`
--

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `FName` varchar(600) NOT NULL,
  `LName` varchar(600) NOT NULL,
  `UName` varchar(600) NOT NULL,
  `Gender` varchar(600) NOT NULL,
  `NID` int(255) NOT NULL,
  `BDate` varchar(600) NOT NULL,
  `Pass` varchar(600) NOT NULL,
  `BANumber` int(255) NOT NULL,
  `Money` varchar(600) NOT NULL,
  `Type` varchar(600) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`FName`, `LName`, `UName`, `Gender`, `NID`, `BDate`, `Pass`, `BANumber`, `Money`, `Type`) VALUES
('amr', 'hossam', 'amrhossam', 'Male', 1, '2022-08-16', 'pas', 2000000000, '10000', 'admin'),
('omar', 'elsayed', 'omarelsayed', 'Male', 2, '2022-08-17', 'pa', 2000000001, '5230980.0', 'user'),
('ahmed', 'sad', 'adsas', 'Male', 5, '2002-02-09', 'fsd', 2000000002, 'NULL', 'admin'),
('Amr', 'Hossam', 'amr28', 'male', 5, '2022-09-28', 'eqw', 2000000003, 'NULL', 'user'),
('Ahmed', 'Mohamed', 'am2', 'male', 6, '2022-19-01', 'efew', 2000000004, '3000.0', 'user'),
('Ahmed', 'Hossam', 'ahmedhossam', 'male', 9, '2002-10-2', 'weqfd', 2000000005, '1800.0', 'user'),
('sad', 'dsf', 'sads', 'male', 10, '2022-08-12', 'wdasd', 2000000006, '1900', 'user'),
('dsa', 'sad', '', 'male', 3242, '2020-21-21', 'dsafdg', 2000000007, '1900', 'user'),
('ahmed', 'mohamed', 'am', 'male', 11, '2022-10-14', 'wpqeo', 2000000008, '1900', 'user'),
('sad', 'dsf', 'gfdg', 'male', 31, '231', 'ardq', 2000000009, '1900', 'user'),
('ahmed', 'mohamed', 'ada', 'male', 100, '2202-21-1', 'asdaq', 2000000010, '1200', 'user'),
('ale', 'eqq', 'ada', 'male', 14, '20212', 'qeq', 2000000012, '11111', 'user'),
('ewq', 'qew', 'fds', 'male', 3333, '1231', 'dasqew', 2000000013, '341', 'user'),
('adf', 'asdf', 'adfa', 'male', 1111, '231', 'adfr', 2000000014, '1750.0', 'user'),
('da', 'adsa', 'sfok', 'user', 2222, '2022', 'rkpew', 2000000015, '2150.0', 'user'),
('amr', 'hossam', 'eoew', 'male', 22220, '21313', 'owewqok', 2000000016, '20003', 'user'),
('amr', 'hossam', 'wqd', 'male', 220011, '2022-19-21', 'dafsa', 2000000017, 'NULL', 'admin'),
('ahmed', 'mohamed', 'sda', 'male', 201003, '2022-19-21', 'dawdq', 2000000018, 'NULL', 'admin'),
('ahmed', 'mohamed', 'ahmo22', 'male', 213, '2002/10/21', 'pass', 2000000019, '1650', 'user'),
('amr', 'hossam', 'amrhossam22', 'male', 211, '2022/09/27', 'amr32', 2000000020, 'NULL', 'admin'),
('amr', 'hossam', 'amr333', 'Male', 1231, '2022/19/29', 'ada', 2000000021, 'NULL', 'Admin'),
('Amr', 'Hossam', 'amr221a', 'Male', 2131, '2022-08-12', 'asda', 2000000022, 'NULL', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`BANumber`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `BANumber` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2000000023;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
