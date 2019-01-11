CREATE TABLE IF NOT EXISTS `batter` (
      `id` INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
      `year` INTEGER,
      `name` VARCHAR(255) ,
      `team` VARCHAR(255) ,
      `bat` VARCHAR(255) ,
      `games` INTEGER ,
      `pa` INTEGER ,
      `ab` INTEGER ,
      `r` INTEGER ,
      `h` INTEGER ,
      `double` INTEGER ,
      `triple` INTEGER ,
      `hr` INTEGER ,
      `tb` INTEGER ,
      `rbi` INTEGER ,
      `so` INTEGER ,
      `bb` INTEGER ,
      `ibb` INTEGER ,
      `hbp` INTEGER ,
      `sh` INTEGER ,
      `sf` INTEGER ,
      `sb` INTEGER ,
      `cs` INTEGER ,
      `dp` INTEGER ,
      `ba` FLOAT ,
      `slg` FLOAT ,
      `obp` FLOAT,
      `create_date` DATETIME NOT NULL ,
      `update_date` DATETIME DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;