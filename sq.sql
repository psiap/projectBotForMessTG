SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydbsubs
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydbsubs
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydbsubs` DEFAULT CHARACTER SET utf8 ;
USE `mydbsubs` ;

-- -----------------------------------------------------
-- Table `mydbsubs`.`tbsubs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydbsubs`.`tbsubs` (
  `keyid` INT NOT NULL AUTO_INCREMENT,
  `userid` VARCHAR(45) CHARACTER SET 'utf8' NULL DEFAULT NULL,
  `apitoken` VARCHAR(100) CHARACTER SET 'utf8' NULL DEFAULT NULL,
  `botname` VARCHAR(45) CHARACTER SET 'utf8' NULL DEFAULT NULL,
  `username` VARCHAR(45) CHARACTER SET 'utf8' NULL DEFAULT NULL,
  `pid` VARCHAR(45) CHARACTER SET 'utf8' NULL DEFAULT NULL,
  PRIMARY KEY (`keyid`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4 
COLLATE = utf8mb4_general_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
