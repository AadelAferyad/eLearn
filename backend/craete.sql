DROP DATABASE IF EXISTS ELEARN;
CREATE DATABASE IF NOT EXISTS ELEARN;

-- CREATE USER IF NOT EXISTS 'elearn'@'localhost';
-- SET PASSWORD FOR 'elearn'@'localhost' = 'Elearn@mysQl21_TEST321321';
-- GRANT ALL ON ELEARN.* TO 'elearn'@'localhost';
-- GRANT SELECT ON performance_schema.* TO 'elearn'@'localhost';
-- FLUSH PRIVILEGES;
USE ELEARN;

CREATE TABLE `files` (
    `name` varchar(80) DEFAULT NULL,
    `path` varchar(256) NOT NULL,
    `id` varchar(60) NOT NULL,
    `created_at` datetime DEFAULT NULL,
    `updated_at` datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

LOCK TABLES `files` WRITE;
INSERT INTO `files`(`name`,`path`,`id`,`created_at`,`updated_at`) VALUES ('director','director.png','017ec502-e84a-4a0f-92d6-d97e27bb6bdf','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('teacher_back_end_1','teacher_back_end_1.png','0d375b05-5ef9-4d43-aaca-436762bb25bf','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('teacher_back_end_2','teacher_back_end_2.png','58705a31-5e9d-45d8-8c56-d04e96b43003','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('teacher_front_end_1','teacher_front_end_1.png','24574f4f-9593-486c-84d4-22e9ccf28d1d','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('teacher_front_end_2','teacher_front_end_2.png','12e9ccb4-03e4-4f82-ac3d-4fc7e3ebfbfe','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('student','Desktop/student_1.png','1e0f976d-beef-497b-b29c-b4a25d1c071a','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('student','Desktop/student_2.png','28ff856a-2cfb-44df-91b8-1285914553c8','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('student','Desktop/student_3.png','17f5323c-6bff-33fd-72c1-1396823342b7','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('student','Desktop/student_4.png','28cc746b-2ccb-22df-01c8-0215487984a8','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('student','Desktop/student_5.png','ead9d3d8-7940-4295-a636-34ab0edad8ee','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('student','Desktop/student_6.png','451771c0-1a15-4c55-a1bd-627814d6f249','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('student','Desktop/student_7.png','ce6257f4-9e57-4f90-ab3c-299de7dd6be1','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('php','php.pdf','11021b97-cd2a-47e8-b079-62e5626c9a2f','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('javascript','javascript.pdf','09d0c930-baf2-4bc8-9df8-cfb44558eb08','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('git','git.png','cdea2645-f50b-4c90-86e7-170fbe440b4c','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('convocation','convocation.png','d669f673-6ee4-42ec-85f7-0c978c71c856','2024-05-19 00:00:00','2024-05-19 00:00:00'),
('keybord','keybord.pdf','f6af522b-ad29-4351-ad86-873ac852d44d','2024-05-19 00:00:00','2024-05-19 00:00:00');

UNLOCK TABLES;
CREATE TABLE `persons` (
    `first_name` varchar(60) NOT NULL,
    `last_name` varchar(60) NOT NULL,
    `email` varchar(256) DEFAULT NULL,
    `phone` varchar(20) DEFAULT NULL,
    `username` varchar(60) NOT NULL,
    `password` varchar(256) NOT NULL,
    `birthday` date DEFAULT NULL,
    `image_id` varchar(256) DEFAULT NULL,
    `id` varchar(60) NOT NULL,
    `created_at` datetime DEFAULT NULL,
    `updated_at` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `image_id` (`image_id`),
    CONSTRAINT `persons_ibfk_1` FOREIGN KEY (`image_id`) REFERENCES `files` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
LOCK TABLES `persons` WRITE;
INSERT INTO `persons`(`first_name`,`email`,`username`,`birthday`,`id`,`last_name`,`phone`,`password`,`image_id`,`created_at`,`updated_at`) VALUES
#director
('Hamid','hamid@gmail.com','hamidChokri','1982-09-19','cfec441d-049f-4d7e-ab62-53d4a5194494','Chokri','0624212451','123456789','017ec502-e84a-4a0f-92d6-d97e27bb6bdf','2024-05-07 00:00:00','2024-05-21 00:00:00'),
#teacher
('Rdwan','rdwan@gmail.com','rdawnBorbouh','1988-08-10','d45dc1ff-8b50-4ab0-907b-fa32b7da6c75','Borboh','0653213461','sda75f321','0d375b05-5ef9-4d43-aaca-436762bb25bf','2024-05-07 00:00:00','2024-05-21 00:00:00'),
('malik','Baha@gmail.com','Baha2','1978-03-29','e636423f-19ae-4ced-b384-ca23919ed957','Baha','0655321311','dsad2d321','58705a31-5e9d-45d8-8c56-d04e96b43003','2024-05-07 00:00:00','2024-05-21 00:00:00'),
('moha','sbay@gmail.com','mohasbauy','1938-02-19','69e22c69-d857-4cae-9fd9-c42cebdf922d','Sibay','0652321461','dsadl2d,2','24574f4f-9593-486c-84d4-22e9ccf28d1d','2024-05-07 00:00:00','2024-05-21 00:00:00'),
('Abd lkarim','khtabi@gmail.com','abdkarim2','1990-07-19','eb2696e6-36ef-41fc-afc0-72623479a110','Khtabi','0685411461','qwertyuio','12e9ccb4-03e4-4f82-ac3d-4fc7e3ebfbfe','2024-05-07 00:00:00','2024-05-21 00:00:00'),
#student
('Aadel','aadel@gmail.com','haruma','2002-01-19','18d5a34c-b712-463e-8527-2f4ae4e9a960','Aferyad','0675531471','oiuytrewq','1e0f976d-beef-497b-b29c-b4a25d1c071a','2024-05-07 00:00:00','2024-05-21 00:00:00'),
('Ismail','ismail@gmail.com','liams','2004-06-19','1f913dc8-f6f2-4b29-b0e4-87c9d11eeb49','Melali','0665641481','asdfghjkl','28ff856a-2cfb-44df-91b8-1285914553c8','2024-05-07 00:00:00','2024-05-21 00:00:00'),
('Asmae','aasmae@gmail.com','mofe','2003-02-19','d128a3bf-2fa2-46d0-bef1-96d6aa74e700','Moftar','0655751491','lkjhgfdsa','17f5323c-6bff-33fd-72c1-1396823342b7','2024-05-07 00:00:00','2024-05-21 00:00:00'),
('Siali','sialal@gmail.com','aalla','2001-10-19','8cac01c8-f518-4e25-98a5-e38ff870c7e9','baja','0645881451','dasdasdsd','28cc746b-2ccb-22df-01c8-0215487984a8','2024-05-07 00:00:00','2024-05-21 00:00:00'),
('Houda','houda@gmail.com','foxy','2003-09-10','4d74e609-e737-4113-9e61-f1e77e2f2c09','belhaj','0635971441','12321dsad','ead9d3d8-7940-4295-a636-34ab0edad8ee','2024-05-07 00:00:00','2024-05-21 00:00:00'),
('Hanane','hanane@gmail.com','hanane','2003-02-14','a5a68f57-c6d4-4ced-b759-5d06379860c2','sabir','0640561431','dsad2123d','451771c0-1a15-4c55-a1bd-627814d6f249','2024-05-07 00:00:00','2024-05-21 00:00:00'),
('Oumaima','oumaima@gmail.com','oumaima','2002-03-09','4c27ff3f-ec80-469e-a192-e8158ca05669','moghamir','0645431221','dksadjsaj','ce6257f4-9e57-4f90-ab3c-299de7dd6be1','2024-05-07 00:00:00','2024-05-21 00:00:00');
UNLOCK TABLES;

CREATE TABLE `directors` (
    `person_id` varchar(60) DEFAULT NULL,
    `id` varchar(60) NOT NULL,
    `created_at` datetime DEFAULT NULL,
    `updated_at` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `person_id` (`person_id`),
    CONSTRAINT `directors_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `persons` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

LOCK TABLES `directors` WRITE;
INSERT INTO `directors`(`person_id`,`id`,`created_at`,`updated_at`) VALUES
('cfec441d-049f-4d7e-ab62-53d4a5194494','05426a2f-d4dd-4e4b-9a42-4964b9f9f769','2024-05-19 16:27:35','2024-05-19 16:27:37');
UNLOCK TABLES;

CREATE TABLE `courses` (
    `name` varchar(60) NOT NULL,
    `year` int NOT NULL,
    `id` varchar(60) NOT NULL,
    `created_at` datetime DEFAULT NULL,
    `updated_at` datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
LOCK TABLES `courses` WRITE;
INSERT INTO `courses`(`name`,`id`,`year`,`updated_at`,`created_at`) VALUES
('Backend','ca9aa3c0-6c0b-4764-9f3a-e1693b9a6c57',1,'2024-05-19 16:27:37','2024-05-19 16:27:35'),
('Frontend','88873def-7169-4e99-844c-62abfeed2e61',1,'2024-05-19 16:27:37','2024-05-19 16:27:35'),
('Backend','d4ef0705-a9ae-4494-a21d-c719d0a706f1',2,'2024-05-19 16:27:37','2024-05-19 16:27:35'),
('Frontend','45b5148c-54ac-45c5-94f0-b958d7abaed3',2,'2024-05-19 16:27:37','2024-05-19 16:27:35');
UNLOCK TABLES;
CREATE TABLE `teachers` (
    `person_id` varchar(60) DEFAULT NULL,
    `course_id` varchar(60) DEFAULT NULL,
    `id` varchar(60) NOT NULL,
    `created_at` datetime DEFAULT NULL,
    `updated_at` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `person_id` (`person_id`),
    KEY `course_id` (`course_id`),
    CONSTRAINT `teachers_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `persons` (`id`),
    CONSTRAINT `teachers_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
LOCK TABLES `teachers` WRITE;
INSERT INTO `teachers`(`person_id`,`id`,`course_id`,`updated_at`,`created_at`) VALUES
('d45dc1ff-8b50-4ab0-907b-fa32b7da6c75','61f7266b-ab49-4036-9d3d-27198799d8d9','ca9aa3c0-6c0b-4764-9f3a-e1693b9a6c57','2024-05-19 17:08:18','2024-05-19 17:08:21'),
('e636423f-19ae-4ced-b384-ca23919ed957','4696469b-f762-41e9-9f0e-363984246e56','88873def-7169-4e99-844c-62abfeed2e61','2024-05-19 17:08:18','2024-05-19 17:08:21'),
('69e22c69-d857-4cae-9fd9-c42cebdf922d','12cdb3ef-9fa2-46dc-8264-ce5d6698883a','d4ef0705-a9ae-4494-a21d-c719d0a706f1','2024-05-19 17:08:18','2024-05-19 17:08:21'),
('eb2696e6-36ef-41fc-afc0-72623479a110','6031b978-1ecb-4ee1-8b1c-1a549d3b1e3d','45b5148c-54ac-45c5-94f0-b958d7abaed3','2024-05-19 17:08:18','2024-05-19 17:08:21');
UNLOCK TABLES;
CREATE TABLE `students` (
    `person_id` varchar(60) DEFAULT NULL,
    `course_id` varchar(60) DEFAULT NULL,
    `id` varchar(60) NOT NULL,
    `created_at` datetime DEFAULT NULL,
    `updated_at` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `person_id` (`person_id`),
    KEY `course_id` (`course_id`),
    CONSTRAINT `students_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `persons` (`id`),
    CONSTRAINT `students_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
LOCK TABLES `students` WRITE;
INSERT INTO `students`(`person_id`,`id`,`course_id`,`updated_at`,`created_at`) VALUES
('18d5a34c-b712-463e-8527-2f4ae4e9a960','12706cb4-273f-473c-b6d4-34320d466ab5','ca9aa3c0-6c0b-4764-9f3a-e1693b9a6c57','2024-05-19 17:15:16','2024-05-19 17:15:18'),
('1f913dc8-f6f2-4b29-b0e4-87c9d11eeb49','a59f6b3f-fc7d-484e-9e93-58c0935a63bd','d4ef0705-a9ae-4494-a21d-c719d0a706f1','2024-05-19 17:15:16','2024-05-19 17:15:18'),
('d128a3bf-2fa2-46d0-bef1-96d6aa74e700','61214fdb-a4e8-454d-a5d3-343f1d411425','88873def-7169-4e99-844c-62abfeed2e61','2024-05-19 17:15:16','2024-05-19 17:15:18'),
('8cac01c8-f518-4e25-98a5-e38ff870c7e9','02a1b5bd-def9-4f54-b33f-a12d3a1719ca','d4ef0705-a9ae-4494-a21d-c719d0a706f1','2024-05-19 17:15:16','2024-05-19 17:15:18'),
('4d74e609-e737-4113-9e61-f1e77e2f2c09','9e41f2c9-323c-4e0c-8ad1-56e15167d132','ca9aa3c0-6c0b-4764-9f3a-e1693b9a6c57','2024-05-19 17:15:16','2024-05-19 17:15:18'),
('a5a68f57-c6d4-4ced-b759-5d06379860c2','803296b2-562d-418c-8749-2712b335ed8c','45b5148c-54ac-45c5-94f0-b958d7abaed3','2024-05-19 17:15:16','2024-05-19 17:15:18'),
('4c27ff3f-ec80-469e-a192-e8158ca05669','24e6ca13-8ec8-4ab6-aabf-14e1ca7bdcd7','88873def-7169-4e99-844c-62abfeed2e61','2024-05-19 17:15:16','2024-05-19 17:15:18');
UNLOCK TABLES;

CREATE TABLE `events` (
    `name` varchar(60) NOT NULL,
    `description` varchar(1024) DEFAULT NULL,
    `image_id` varchar(60) DEFAULT NULL,
    `target` varchar(60) DEFAULT NULL,
    `deadline` datetime DEFAULT NULL,
    `id` varchar(60) NOT NULL,
    `created_at` datetime DEFAULT NULL,
    `updated_at` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `image_id` (`image_id`),
    KEY `target` (`target`),
    CONSTRAINT `events_ibfk_1` FOREIGN KEY (`image_id`) REFERENCES `files` (`id`),
    CONSTRAINT `events_ibfk_2` FOREIGN KEY (`target`) REFERENCES `courses` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE `resources` (
    `name` varchar(60) NOT NULL,
    `description` varchar(1024) NOT NULL,
    `file_id` varchar(60) DEFAULT NULL,
    `target` varchar(60) NOT NULL,
    `id` varchar(60) NOT NULL,
    `created_at` datetime DEFAULT NULL,
    `updated_at` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `file_id` (`file_id`),
    KEY `target` (`target`),
    CONSTRAINT `resources_ibfk_1` FOREIGN KEY (`file_id`) REFERENCES `files` (`id`),
    CONSTRAINT `resources_ibfk_2` FOREIGN KEY (`target`) REFERENCES `courses` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
CREATE TABLE `lessons` (
    `name` varchar(60) NOT NULL,
    `description` varchar(1024) NOT NULL,
    `file_id` varchar(60) DEFAULT NULL,
    `target` varchar(60) NOT NULL,
    `deadline` datetime NOT NULL,
    `id` varchar(60) NOT NULL,
    `created_at` datetime DEFAULT NULL,
    `updated_at` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `file_id` (`file_id`),
    KEY `target` (`target`),
    CONSTRAINT `lessons_ibfk_1` FOREIGN KEY (`file_id`) REFERENCES `files` (`id`),
    CONSTRAINT `lessons_ibfk_2` FOREIGN KEY (`target`) REFERENCES `courses` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
