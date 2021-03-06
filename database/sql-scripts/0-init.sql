CREATE DATABASE fifa CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

USE fifa;

-- fifa.players definition

CREATE TABLE `players` (
  `id` bigint NOT NULL,
  `name` varchar(25) NOT NULL,
  `age` int NOT NULL,
  `photo` varchar(50) NOT NULL,
  `photo_id` varchar(10) NOT NULL,
  `nationality` varchar(25) DEFAULT NULL,
  `flag` varchar(40) NOT NULL,
  `overall` int NOT NULL,
  `potential` int NOT NULL,
  `club` varchar(40) DEFAULT NULL,
  `club_logo` varchar(50) NOT NULL,
  `value` bigint NOT NULL,
  `wage` bigint NOT NULL,
  `special` int NOT NULL,
  `preferred_foot` varchar(5) DEFAULT NULL,
  `international_reputation` int DEFAULT NULL,
  `weak_foot` int DEFAULT NULL,
  `skill_moves` int DEFAULT NULL,
  `work_rate` varchar(15) DEFAULT NULL,
  `body_type` varchar(20) DEFAULT NULL,
  `real_face` tinyint(1) DEFAULT NULL,
  `position` varchar(3) DEFAULT NULL,
  `jersey_number` int DEFAULT NULL,
  `joined` date DEFAULT NULL,
  `loaned_from` varchar(40) DEFAULT NULL,
  `contract_valid_until` varchar(15) DEFAULT NULL,
  `height` varchar(5) DEFAULT NULL,
  `weight` varchar(6) DEFAULT NULL,
  `ls` int DEFAULT NULL,
  `st` int DEFAULT NULL,
  `rs` int DEFAULT NULL,
  `lw` int DEFAULT NULL,
  `lf` int DEFAULT NULL,
  `cf` int DEFAULT NULL,
  `rf` int DEFAULT NULL,
  `rw` int DEFAULT NULL,
  `lam` int DEFAULT NULL,
  `cam` int DEFAULT NULL,
  `ram` int DEFAULT NULL,
  `lm` int DEFAULT NULL,
  `lcm` int DEFAULT NULL,
  `cm` int DEFAULT NULL,
  `rcm` int DEFAULT NULL,
  `rm` int DEFAULT NULL,
  `lwb` int DEFAULT NULL,
  `ldm` int DEFAULT NULL,
  `cdm` int DEFAULT NULL,
  `rdm` int DEFAULT NULL,
  `rwb` int DEFAULT NULL,
  `lb` int DEFAULT NULL,
  `lcb` int DEFAULT NULL,
  `cb` int DEFAULT NULL,
  `rcb` int DEFAULT NULL,
  `rb` int DEFAULT NULL,
  `gk` int DEFAULT NULL,
  `crossing` int DEFAULT NULL,
  `finishing` int DEFAULT NULL,
  `heading_accuracy` int DEFAULT NULL,
  `short_passing` int DEFAULT NULL,
  `volleys` int DEFAULT NULL,
  `dribbling` int DEFAULT NULL,
  `curve` int DEFAULT NULL,
  `fk_accuracy` int DEFAULT NULL,
  `long_passing` int DEFAULT NULL,
  `ball_control` int DEFAULT NULL,
  `acceleration` int DEFAULT NULL,
  `sprint_speed` int DEFAULT NULL,
  `agility` int DEFAULT NULL,
  `reactions` int DEFAULT NULL,
  `balance` int DEFAULT NULL,
  `shot_power` int DEFAULT NULL,
  `jumping` int DEFAULT NULL,
  `stamina` int DEFAULT NULL,
  `strength` int DEFAULT NULL,
  `long_shots` int DEFAULT NULL,
  `aggression` int DEFAULT NULL,
  `interceptions` int DEFAULT NULL,
  `positioning` int DEFAULT NULL,
  `vision` int DEFAULT NULL,
  `penalties` int DEFAULT NULL,
  `composure` int DEFAULT NULL,
  `marking` int DEFAULT NULL,
  `standing_tackle` int DEFAULT NULL,
  `sliding_tackle` int DEFAULT NULL,
  `gk_diving` int DEFAULT NULL,
  `gk_handling` int DEFAULT NULL,
  `gk_kicking` int DEFAULT NULL,
  `gk_positioning` int DEFAULT NULL,
  `gk_reflexes` int DEFAULT NULL,
  `release_clause` bigint DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
