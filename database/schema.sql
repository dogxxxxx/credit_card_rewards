CREATE TABLE `banks` (
  `bank_id` integer PRIMARY KEY AUTO_INCREMENT,
  `bank_name` VARCHAR(32) NOT NULL
);

CREATE TABLE `cards` (
  `card_id` integer PRIMARY KEY AUTO_INCREMENT,
  `card_name` VARCHAR(64),
  `bank_id` integer NOT NULL
);

CREATE TABLE `store_types` (
  `store_type_id` integer PRIMARY KEY AUTO_INCREMENT,
  `store_type_name` varchar(64) UNIQUE NOT NULL
);

CREATE TABLE `stores` (
  `store_id` integer PRIMARY KEY AUTO_INCREMENT,
  `store_name` varchar(64) UNIQUE NOT NULL,
  `store_type_id` integer NOT NULL
);

CREATE TABLE `rewards` (
  `reward_id` integer PRIMARY KEY AUTO_INCREMENT,
  `card_id` integer NOT NULL,
  `store_id` integer NOT NULL,
  `reward_amount` decimal(5,2) NOT NULL,
  `ts_epoch_ms` bigint NOT NULL
);

ALTER TABLE `cards` ADD FOREIGN KEY (`bank_id`) REFERENCES `banks` (`bank_id`);

ALTER TABLE `stores` ADD FOREIGN KEY (`store_type_id`) REFERENCES `store_types` (`store_type_id`);

ALTER TABLE `rewards` ADD FOREIGN KEY (`card_id`) REFERENCES `cards` (`card_id`);

ALTER TABLE `rewards` ADD FOREIGN KEY (`store_id`) REFERENCES `stores` (`store_id`);
