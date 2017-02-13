/*
Navicat MySQL Data Transfer

Source Server         : 198Mysql
Source Server Version : 50628
Source Host           : 192.168.1.198:3306
Source Database       : featuretemp

Target Server Type    : MYSQL
Target Server Version : 50628
File Encoding         : 65001

Date: 2017-02-13 19:23:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add ', '7', 'add_clientoverview');
INSERT INTO `auth_permission` VALUES ('20', 'Can change ', '7', 'change_clientoverview');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete ', '7', 'delete_clientoverview');
INSERT INTO `auth_permission` VALUES ('22', 'Can add 数据源基本信息表', '8', 'add_datasourceinfo');
INSERT INTO `auth_permission` VALUES ('23', 'Can change 数据源基本信息表', '8', 'change_datasourceinfo');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete 数据源基本信息表', '8', 'delete_datasourceinfo');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 接口表', '9', 'add_dsinterfaceinfo');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 接口表', '9', 'change_dsinterfaceinfo');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 接口表', '9', 'delete_dsinterfaceinfo');
INSERT INTO `auth_permission` VALUES ('28', 'Can add 特征-参数映射表', '10', 'add_featurefieldrel');
INSERT INTO `auth_permission` VALUES ('29', 'Can change 特征-参数映射表', '10', 'change_featurefieldrel');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete 特征-参数映射表', '10', 'delete_featurefieldrel');
INSERT INTO `auth_permission` VALUES ('31', 'Can add 特征与计算参数对照表', '11', 'add_featureprocessinfo');
INSERT INTO `auth_permission` VALUES ('32', 'Can change 特征与计算参数对照表', '11', 'change_featureprocessinfo');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete 特征与计算参数对照表', '11', 'delete_featureprocessinfo');
INSERT INTO `auth_permission` VALUES ('34', 'Can add task state', '12', 'add_taskmeta');
INSERT INTO `auth_permission` VALUES ('35', 'Can change task state', '12', 'change_taskmeta');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete task state', '12', 'delete_taskmeta');
INSERT INTO `auth_permission` VALUES ('37', 'Can add saved group result', '13', 'add_tasksetmeta');
INSERT INTO `auth_permission` VALUES ('38', 'Can change saved group result', '13', 'change_tasksetmeta');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete saved group result', '13', 'delete_tasksetmeta');
INSERT INTO `auth_permission` VALUES ('40', 'Can add interval', '14', 'add_intervalschedule');
INSERT INTO `auth_permission` VALUES ('41', 'Can change interval', '14', 'change_intervalschedule');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete interval', '14', 'delete_intervalschedule');
INSERT INTO `auth_permission` VALUES ('43', 'Can add crontab', '15', 'add_crontabschedule');
INSERT INTO `auth_permission` VALUES ('44', 'Can change crontab', '15', 'change_crontabschedule');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete crontab', '15', 'delete_crontabschedule');
INSERT INTO `auth_permission` VALUES ('46', 'Can add periodic tasks', '16', 'add_periodictasks');
INSERT INTO `auth_permission` VALUES ('47', 'Can change periodic tasks', '16', 'change_periodictasks');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete periodic tasks', '16', 'delete_periodictasks');
INSERT INTO `auth_permission` VALUES ('49', 'Can add periodic task', '17', 'add_periodictask');
INSERT INTO `auth_permission` VALUES ('50', 'Can change periodic task', '17', 'change_periodictask');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete periodic task', '17', 'delete_periodictask');
INSERT INTO `auth_permission` VALUES ('52', 'Can add worker', '18', 'add_workerstate');
INSERT INTO `auth_permission` VALUES ('53', 'Can change worker', '18', 'change_workerstate');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete worker', '18', 'delete_workerstate');
INSERT INTO `auth_permission` VALUES ('55', 'Can add task', '19', 'add_taskstate');
INSERT INTO `auth_permission` VALUES ('56', 'Can change task', '19', 'change_taskstate');
INSERT INTO `auth_permission` VALUES ('57', 'Can delete task', '19', 'delete_taskstate');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `celery_taskmeta`
-- ----------------------------
DROP TABLE IF EXISTS `celery_taskmeta`;
CREATE TABLE `celery_taskmeta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` varchar(255) NOT NULL,
  `status` varchar(50) NOT NULL,
  `result` longtext,
  `date_done` datetime NOT NULL,
  `traceback` longtext,
  `hidden` tinyint(1) NOT NULL,
  `meta` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  KEY `celery_taskmeta_662f707d` (`hidden`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of celery_taskmeta
-- ----------------------------
INSERT INTO `celery_taskmeta` VALUES ('1', '8ac6fa50-bd8e-4c8b-96dd-9d226ef40298', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpUeXBlRXJyb3IKcQFVKWF1ZGl0X3Rhc2soKSB0YWtlcyBubyBhcmd1bWVudHMgKDEgZ2l2ZW4pcQKFcQNScQQu', '2017-01-24 15:16:33', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\nTypeError: audit_task() takes no arguments (1 given)\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('2', 'a7e805c8-3f85-49d6-82f8-aa3a49aacf1f', 'SUCCESS', null, '2017-01-24 15:17:29', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('3', 'ea1445d6-9041-442e-aedc-f8dd3344aed7', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpBdHRyaWJ1dGVFcnJvcgpxAVUjJ2ludCcgb2JqZWN0IGhhcyBubyBhdHRyaWJ1dGUgJ2dldCdxAoVxA1JxBC4=', '2017-01-24 15:46:46', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 29, in audit_task\n    original_data_list = data_get_dispatch(base_data)\n  File \"F:/featurefactory\\apps\\common\\dispatcher.py\", line 61, in data_get_dispatch\n    apply_id = base_data.get(\'apply_id\', None)\nAttributeError: \'int\' object has no attribute \'get\'\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('4', '0a311ab9-1002-425b-b432-a000da9bb4c8', 'SUCCESS', null, '2017-01-24 15:47:46', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('5', 'a68e2ff3-dbab-46bb-97ca-e4b5ce7873b3', 'SUCCESS', null, '2017-01-24 15:48:13', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('6', 'f0424bed-f22c-4b3f-878f-923374316d26', 'SUCCESS', null, '2017-01-24 17:26:37', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('7', 'd025e889-f034-4069-93a5-8307bddf6d81', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpUeXBlRXJyb3IKcQFVJydpbnN0YW5jZW1ldGhvZCcgb2JqZWN0IGlzIG5vdCBpdGVyYWJsZXEChXEDUnEELg==', '2017-02-09 16:17:42', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 31, in audit_task\n    ret_data = process_dispatch(original_data_list)\n  File \"F:/featurefactory\\apps\\common\\dispatcher.py\", line 110, in process_dispatch\n    ret_data.update(ret)\nTypeError: \'instancemethod\' object is not iterable\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('8', '7703da94-0d0f-4b11-8a5d-630901ef8093', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpUeXBlRXJyb3IKcQFVJydpbnN0YW5jZW1ldGhvZCcgb2JqZWN0IGlzIG5vdCBpdGVyYWJsZXEChXEDUnEELg==', '2017-02-09 16:18:49', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 31, in audit_task\n    ret_data = process_dispatch(original_data_list)\n  File \"F:/featurefactory\\apps\\common\\dispatcher.py\", line 110, in process_dispatch\n    ret_data.update(ret)\nTypeError: \'instancemethod\' object is not iterable\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('9', '51fcf816-fd8f-4bc2-89db-cf53cf7d6134', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpUeXBlRXJyb3IKcQFVJydpbnN0YW5jZW1ldGhvZCcgb2JqZWN0IGlzIG5vdCBpdGVyYWJsZXEChXEDUnEELg==', '2017-02-09 16:19:00', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 31, in audit_task\n    ret_data = process_dispatch(original_data_list)\n  File \"F:/featurefactory\\apps\\common\\dispatcher.py\", line 110, in process_dispatch\n    ret_data.update(ret)\nTypeError: \'instancemethod\' object is not iterable\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('10', 'c01cd4c3-2804-435f-8121-674edcb4c135', 'SUCCESS', null, '2017-02-09 16:19:56', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('11', '97deb84c-74eb-48d4-bcdd-04798b621162', 'SUCCESS', null, '2017-02-09 16:59:09', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('12', '57f3653b-6061-40b6-93f6-edba0200fe1e', 'SUCCESS', null, '2017-02-09 16:59:22', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('13', '71af445c-453f-4b14-be4d-ebf97d1cca7a', 'SUCCESS', null, '2017-02-13 10:55:17', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('14', '831abb50-60f5-40e6-b6ac-0682dff293f6', 'SUCCESS', null, '2017-02-13 12:01:28', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('15', '3c361ca1-04ee-4ee2-8c96-9a8e90445e94', 'SUCCESS', null, '2017-02-13 12:49:55', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('16', 'd3e7f3f3-2107-46e6-a73f-d065ba5266ed', 'SUCCESS', null, '2017-02-13 15:19:36', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('17', '970af867-2b1a-4573-814c-2bd4fc133800', 'SUCCESS', null, '2017-02-13 15:27:01', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('18', '4fb7e077-06b3-4e11-b2a1-f63df0aec7ee', 'SUCCESS', null, '2017-02-13 16:08:06', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('19', 'a2d26236-7a50-4bec-9c6c-e6314a761b5d', 'SUCCESS', null, '2017-02-13 17:06:02', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('20', 'b6a77899-37b1-4749-8f43-1b4d12c49889', 'SUCCESS', null, '2017-02-13 18:18:23', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('21', '0407a5d8-df38-4e90-ae72-899577ffde8c', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpUeXBlRXJyb3IKcQFVH3N0cmluZyBpbmRpY2VzIG11c3QgYmUgaW50ZWdlcnNxAoVxA1JxBC4=', '2017-02-13 18:21:22', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 31, in audit_task\n    target_field_list = [data[\'target_field_name\'] for data in base_data]\nTypeError: string indices must be integers\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('22', 'd17c4751-bea1-4a42-a16b-eb76c538c619', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpUeXBlRXJyb3IKcQFVH3N0cmluZyBpbmRpY2VzIG11c3QgYmUgaW50ZWdlcnNxAoVxA1JxBC4=', '2017-02-13 18:22:13', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 31, in audit_task\n    target_field_list = [data[\'target_field_name\'] for data in base_data]\nTypeError: string indices must be integers\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('23', '948453a9-6644-482c-ab5e-a2755fbebf1e', 'SUCCESS', null, '2017-02-13 19:11:27', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');

-- ----------------------------
-- Table structure for `celery_tasksetmeta`
-- ----------------------------
DROP TABLE IF EXISTS `celery_tasksetmeta`;
CREATE TABLE `celery_tasksetmeta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `taskset_id` varchar(255) NOT NULL,
  `result` longtext NOT NULL,
  `date_done` datetime NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `taskset_id` (`taskset_id`),
  KEY `celery_tasksetmeta_662f707d` (`hidden`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of celery_tasksetmeta
-- ----------------------------

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'log entry', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'permission', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('3', 'group', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('4', 'user', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'content type', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'session', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('7', '', 'common', 'clientoverview');
INSERT INTO `django_content_type` VALUES ('8', '数据源基本信息表', 'datasource', 'datasourceinfo');
INSERT INTO `django_content_type` VALUES ('9', '接口表', 'datasource', 'dsinterfaceinfo');
INSERT INTO `django_content_type` VALUES ('10', '特征-参数映射表', 'remote', 'featurefieldrel');
INSERT INTO `django_content_type` VALUES ('11', '特征与计算参数对照表', 'etl', 'featureprocessinfo');
INSERT INTO `django_content_type` VALUES ('12', 'task state', 'djcelery', 'taskmeta');
INSERT INTO `django_content_type` VALUES ('13', 'saved group result', 'djcelery', 'tasksetmeta');
INSERT INTO `django_content_type` VALUES ('14', 'interval', 'djcelery', 'intervalschedule');
INSERT INTO `django_content_type` VALUES ('15', 'crontab', 'djcelery', 'crontabschedule');
INSERT INTO `django_content_type` VALUES ('16', 'periodic tasks', 'djcelery', 'periodictasks');
INSERT INTO `django_content_type` VALUES ('17', 'periodic task', 'djcelery', 'periodictask');
INSERT INTO `django_content_type` VALUES ('18', 'worker', 'djcelery', 'workerstate');
INSERT INTO `django_content_type` VALUES ('19', 'task', 'djcelery', 'taskstate');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2017-01-20 14:37:27');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2017-01-20 14:37:33');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2017-01-20 14:37:35');
INSERT INTO `django_migrations` VALUES ('4', 'common', '0001_initial', '2017-01-20 14:37:35');
INSERT INTO `django_migrations` VALUES ('7', 'sessions', '0001_initial', '2017-01-20 14:37:37');
INSERT INTO `django_migrations` VALUES ('8', 'datasource', '0001_initial', '2017-01-20 18:12:30');
INSERT INTO `django_migrations` VALUES ('9', 'djcelery', '0001_initial', '2017-01-24 14:13:35');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for `djcelery_crontabschedule`
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_crontabschedule`;
CREATE TABLE `djcelery_crontabschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `minute` varchar(64) NOT NULL,
  `hour` varchar(64) NOT NULL,
  `day_of_week` varchar(64) NOT NULL,
  `day_of_month` varchar(64) NOT NULL,
  `month_of_year` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of djcelery_crontabschedule
-- ----------------------------

-- ----------------------------
-- Table structure for `djcelery_intervalschedule`
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_intervalschedule`;
CREATE TABLE `djcelery_intervalschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `every` int(11) NOT NULL,
  `period` varchar(24) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of djcelery_intervalschedule
-- ----------------------------

-- ----------------------------
-- Table structure for `djcelery_periodictask`
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_periodictask`;
CREATE TABLE `djcelery_periodictask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `task` varchar(200) NOT NULL,
  `args` longtext NOT NULL,
  `kwargs` longtext NOT NULL,
  `queue` varchar(200) DEFAULT NULL,
  `exchange` varchar(200) DEFAULT NULL,
  `routing_key` varchar(200) DEFAULT NULL,
  `expires` datetime DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime DEFAULT NULL,
  `total_run_count` int(10) unsigned NOT NULL,
  `date_changed` datetime NOT NULL,
  `description` longtext NOT NULL,
  `crontab_id` int(11) DEFAULT NULL,
  `interval_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `djcelery_periodictask_f3f0d72a` (`crontab_id`),
  KEY `djcelery_periodictask_1dcd7040` (`interval_id`),
  CONSTRAINT `djcelery_pe_interval_id_2f9f2053_fk_djcelery_intervalschedule_id` FOREIGN KEY (`interval_id`) REFERENCES `djcelery_intervalschedule` (`id`),
  CONSTRAINT `djcelery_peri_crontab_id_4bb497f6_fk_djcelery_crontabschedule_id` FOREIGN KEY (`crontab_id`) REFERENCES `djcelery_crontabschedule` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of djcelery_periodictask
-- ----------------------------

-- ----------------------------
-- Table structure for `djcelery_periodictasks`
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_periodictasks`;
CREATE TABLE `djcelery_periodictasks` (
  `ident` smallint(6) NOT NULL,
  `last_update` datetime NOT NULL,
  PRIMARY KEY (`ident`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of djcelery_periodictasks
-- ----------------------------

-- ----------------------------
-- Table structure for `djcelery_taskstate`
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_taskstate`;
CREATE TABLE `djcelery_taskstate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state` varchar(64) NOT NULL,
  `task_id` varchar(36) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `tstamp` datetime NOT NULL,
  `args` longtext,
  `kwargs` longtext,
  `eta` datetime DEFAULT NULL,
  `expires` datetime DEFAULT NULL,
  `result` longtext,
  `traceback` longtext,
  `runtime` double DEFAULT NULL,
  `retries` int(11) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `worker_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  KEY `djcelery_taskstate_9ed39e2e` (`state`),
  KEY `djcelery_taskstate_b068931c` (`name`),
  KEY `djcelery_taskstate_863bb2ee` (`tstamp`),
  KEY `djcelery_taskstate_662f707d` (`hidden`),
  KEY `djcelery_taskstate_ce77e6ef` (`worker_id`),
  CONSTRAINT `djcelery_taskstate_worker_id_4e3c2c27_fk_djcelery_workerstate_id` FOREIGN KEY (`worker_id`) REFERENCES `djcelery_workerstate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of djcelery_taskstate
-- ----------------------------

-- ----------------------------
-- Table structure for `djcelery_workerstate`
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_workerstate`;
CREATE TABLE `djcelery_workerstate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(255) NOT NULL,
  `last_heartbeat` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname` (`hostname`),
  KEY `djcelery_workerstate_f129901a` (`last_heartbeat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of djcelery_workerstate
-- ----------------------------

-- ----------------------------
-- Table structure for `fic_client_overview`
-- ----------------------------
DROP TABLE IF EXISTS `fic_client_overview`;
CREATE TABLE `fic_client_overview` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime NOT NULL,
  `client_code` varchar(128) NOT NULL,
  `client_id` varchar(128) NOT NULL,
  `client_secret` varchar(256) NOT NULL,
  `des_key` varchar(128) NOT NULL,
  `manage_type` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of fic_client_overview
-- ----------------------------
INSERT INTO `fic_client_overview` VALUES ('1', '0', '2017-01-20 14:47:38', '2017-01-20 14:47:38', 'dataocean_test', 'eezqKVwe3Fzc72m3K6LzfK4CbJDb7hbtoJThzsBo', '5yr2oMcUQSzld9JifoMvkN8tmyiwIB9Ra9IxUDDlmDmlPx3V8uJRkiTpSvVUdRVHLA1F91iyxgP4riz4fWVMbbyfq3ovo1c9kzwHtDrtMqVpMd2vZPFXGAkh7IjuBDQT', 'yyyyyyuuuuoooooo', 'procuratorate.dataocean_judger.Judger');
INSERT INTO `fic_client_overview` VALUES ('2', '0', '2017-01-20 14:47:38', '2017-01-20 14:47:38', 'lp_test', '', '', '', 'procuratorate.lp_judger.Judger');

-- ----------------------------
-- Table structure for `fic_data_source_info`
-- ----------------------------
DROP TABLE IF EXISTS `fic_data_source_info`;
CREATE TABLE `fic_data_source_info` (
  `is_delete` tinyint(1) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `data_source_identity` varchar(64) NOT NULL,
  `desc` varchar(512) DEFAULT NULL,
  `protocol_type` varchar(15) NOT NULL,
  `backend_url` varchar(64) NOT NULL,
  `api_manager` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of fic_data_source_info
-- ----------------------------
INSERT INTO `fic_data_source_info` VALUES ('0', '2017-01-20 18:13:45', '2017-01-20 18:13:45', '1', 'data_ocean测试接口', 'data_ocean_test', 'data_ocean测试接口', 'HTTP', 'http://apitest.digcredit.com', '');
INSERT INTO `fic_data_source_info` VALUES ('0', '2017-01-20 18:13:45', '2017-01-20 18:13:45', '2', 'data_ocean生产接口', 'data_ocean_prod', 'data_ocean生产接口', 'HTTP', 'http://api.digcredit.com', '');
INSERT INTO `fic_data_source_info` VALUES ('0', '2017-01-20 18:13:45', '2017-01-20 18:13:45', '3', 'lp集成接口', 'lp_integration', '猎聘集成接口', 'HTTP', 'http://127.0.0.1:8070', 'slumdog.lp_junkman');

-- ----------------------------
-- Table structure for `fic_feature_field_rel`
-- ----------------------------
DROP TABLE IF EXISTS `fic_feature_field_rel`;
CREATE TABLE `fic_feature_field_rel` (
  `is_delete` tinyint(1) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feature_name` varchar(64) NOT NULL,
  `raw_field_name` varchar(64) NOT NULL,
  `data_identity` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of fic_feature_field_rel
-- ----------------------------
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:05', '2017-01-20 17:08:05', '1', 'age', 'name', 'personal_info');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:06', '2017-01-20 17:08:06', '2', 'age', 'card_id', 'personal_info');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:06', '2017-01-20 17:08:06', '3', 'is_loan_agency', 'mobile', 'loan_agency');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:06', '2017-01-20 17:08:06', '4', 'is_organization_g_black', 'name', 'agentg_black');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:06', '2017-01-20 17:08:06', '5', 'is_organization_g_black', 'card_id', 'agentg_black');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:06', '2017-01-20 17:08:06', '6', 'is_organization_g_black', 'mobile', 'agentg_black');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:06', '2017-01-20 17:08:06', '7', 'is_netsky_black', 'mobile', 'tianwang_black');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:06', '2017-01-20 17:08:06', '8', 'is_netsky_longloan', 'mobile', 'tianwang_multi_loan');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:06', '2017-01-20 17:08:06', '9', 'is_skyeye_black', 'card_id', 'tianyan_black');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:06', '2017-01-20 17:08:06', '10', 'is_skyeye_black', 'mobile', 'tianyan_black');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:06', '2017-01-20 17:08:06', '11', 'is_skyeye_black', 'email', 'tianyan_black');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:06', '2017-01-20 17:08:06', '12', 'is_court_shixin', 'name', 'court_shixin_a_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:06', '2017-01-20 17:08:06', '13', 'is_court_shixin', 'card_id', 'court_shixin_a_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:06', '2017-01-20 17:08:06', '14', 'is_net_black', 'name', 'net_black_a_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:06', '2017-01-20 17:08:06', '15', 'is_net_black', 'card_id', 'net_black_a_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:06', '2017-01-20 17:08:06', '16', 'is_owner_mobile', 'name', 'telecom_mobile_identity_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:07', '2017-01-20 17:08:07', '17', 'is_owner_mobile', 'card_id', 'telecom_mobile_identity_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:07', '2017-01-20 17:08:07', '18', 'is_owner_mobile', 'mobile', 'telecom_mobile_identity_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:07', '2017-01-20 17:08:07', '19', 'is_owner_mobile', 'name', 'unicom_mobile_identity_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:07', '2017-01-20 17:08:07', '20', 'is_owner_mobile', 'card_id', 'unicom_mobile_identity_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:07', '2017-01-20 17:08:07', '21', 'is_owner_mobile', 'mobile', 'unicom_mobile_identity_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:07', '2017-01-20 17:08:07', '22', 'is_owner_mobile', 'name', 'yd_mobile_identity_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:07', '2017-01-20 17:08:07', '23', 'is_owner_mobile', 'card_id', 'yd_mobile_identity_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:07', '2017-01-20 17:08:07', '24', 'is_owner_mobile', 'mobile', 'yd_mobile_identity_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:07', '2017-01-20 17:08:07', '25', 'personal_income_ratio', 'mobile', 'china_mobile_ability');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:07', '2017-01-20 17:08:07', '26', 'has_negative_info', 'name', 'negative_info_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:07', '2017-01-20 17:08:07', '27', 'has_negative_info', 'card_id', 'negative_info_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:07', '2017-01-20 17:08:07', '28', 'is_netsky_gray', 'mobile', 'tianwang_gray');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:07', '2017-01-20 17:08:07', '29', 'is_court_zhixing', 'name', 'court_zhixing_a_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:07', '2017-01-20 17:08:07', '30', 'is_court_zhixing', 'card_id', 'court_zhixing_a_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:08', '2017-01-20 17:08:08', '31', 'mobile_local', 'mobile', 'mobile_locale');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:08', '2017-01-20 17:08:08', '32', 'mobile_online_time', 'mobile', 'yd_mobile_online_time_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:08', '2017-01-20 17:08:08', '33', 'mobile_online_time', 'mobile', 'unicome_mobile_online_time_s');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:08', '2017-01-20 17:08:08', '34', 'mobile_online_time', 'mobile', 'telecom_mobile_online');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:08', '2017-01-20 17:08:08', '35', 'gps_location', 'gps_longitude', 'geo_location');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-01-20 17:08:08', '2017-01-20 17:08:08', '36', 'gps_location', 'gps_latitude', 'geo_location');

-- ----------------------------
-- Table structure for `fic_feature_process_info`
-- ----------------------------
DROP TABLE IF EXISTS `fic_feature_process_info`;
CREATE TABLE `fic_feature_process_info` (
  `is_delete` tinyint(1) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feature_name` varchar(64) NOT NULL,
  `process_type` varchar(256) NOT NULL,
  `data_identity` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of fic_feature_process_info
-- ----------------------------
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:45', '2017-01-21 16:38:45', '1', 'age', 'studio.lp_dataocean_handle.lp_personal_info.Handle', 'personal_info');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:45', '2017-01-21 16:38:45', '2', 'is_loan_agency', 'studio.lp_dataocean_handle.lp_loan_agency.Handle', 'loan_agency');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:45', '2017-01-21 16:38:45', '3', 'is_organization_g_black', 'studio.lp_dataocean_handle.lp_agentg_black.Handle', 'agentg_black');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:45', '2017-01-21 16:38:45', '4', 'is_netsky_black', 'studio.lp_dataocean_handle.lp_tianwang_black.Handle', 'tianwang_black');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:45', '2017-01-21 16:38:45', '5', 'is_netsky_longloan', 'studio.lp_dataocean_handle.lp_tianwang_multi_loan.Handle', 'tianwang_multi_loan');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:45', '2017-01-21 16:38:45', '6', 'is_skyeye_black', 'studio.lp_dataocean_handle.lp_tianyan_black.Handle', 'tianyan_black');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:45', '2017-01-21 16:38:45', '7', 'is_court_shixin', 'studio.lp_dataocean_handle.lp_court_shixin_a_s.Handle', 'court_shixin_a_s');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:45', '2017-01-21 16:38:45', '8', 'is_net_black', 'studio.lp_dataocean_handle.lp_net_black_a_s.Handle', 'net_black_a_s');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:45', '2017-01-21 16:38:45', '9', 'is_owner_mobile', 'studio.lp_dataocean_handle.lp_telecom_mobile_identity_s.Handle', 'telecom_mobile_identity_s');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:45', '2017-01-21 16:38:45', '10', 'is_owner_mobile', 'studio.lp_dataocean_handle.lp_unicom_mobile_identity_s.Handle', 'unicom_mobile_identity_s');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:45', '2017-01-21 16:38:45', '11', 'is_owner_mobile', 'studio.lp_dataocean_handle.lp_yd_mobile_identity_s.Handle', 'yd_mobile_identity_s');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:45', '2017-01-21 16:38:45', '12', 'personal_income_ratio', 'studio.lp_dataocean_handle.lp_china_mobile_ability.Handle', 'china_mobile_ability');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:46', '2017-01-21 16:38:46', '13', 'has_negative_info', 'studio.lp_dataocean_handle.lp_negative_info_s.Handle', 'negative_info_s');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:46', '2017-01-21 16:38:46', '14', 'is_netsky_gray', 'studio.lp_dataocean_handle.lp_tianwang_gray.Handle', 'tianwang_gray');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:46', '2017-01-21 16:38:46', '15', 'is_court_zhixing', 'studio.lp_dataocean_handle.lp_court_zhixing_a_s.Handle', 'court_zhixing_a_s');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:46', '2017-01-21 16:38:46', '16', 'mobile_local', 'studio.lp_dataocean_handle.lp_mobile_locale.Handle', 'mobile_locale');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:46', '2017-01-21 16:38:46', '17', 'mobile_online_time', 'studio.lp_dataocean_handle.lp_yd_mobile_online_time_s.Handle', 'yd_mobile_online_time_s');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:46', '2017-01-21 16:38:46', '18', 'mobile_online_time', 'studio.lp_dataocean_handle.lp_unicome_mobile_online_time_s.Handle', 'unicome_mobile_online_time_s');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:46', '2017-01-21 16:38:46', '19', 'mobile_online_time', 'studio.lp_dataocean_handle.lp_telecom_mobile_online.Handle', 'telecom_mobile_online');
INSERT INTO `fic_feature_process_info` VALUES ('0', '2017-01-21 16:38:46', '2017-01-21 16:38:46', '20', 'gps_location', 'studio.lp_dataocean_handle.lp_geo_location.Handle', 'geo_location');

-- ----------------------------
-- Table structure for `fic_interface_info`
-- ----------------------------
DROP TABLE IF EXISTS `fic_interface_info`;
CREATE TABLE `fic_interface_info` (
  `is_delete` tinyint(1) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `data_identity` varchar(64) NOT NULL,
  `route` varchar(128) NOT NULL,
  `method` varchar(32) NOT NULL,
  `comment` varchar(512) DEFAULT NULL,
  `common_data` varchar(1024) DEFAULT NULL,
  `must_data` varchar(1024) NOT NULL,
  `is_need_token` tinyint(1) NOT NULL,
  `is_need_encrypt` tinyint(1) NOT NULL,
  `is_async` tinyint(1) NOT NULL,
  `encrypt_type` varchar(32) DEFAULT NULL,
  `data_source_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fic_interface_info_15a32e4a` (`data_source_id`),
  CONSTRAINT `fic_interface__data_source_id_28f7006_fk_fic_data_source_info_id` FOREIGN KEY (`data_source_id`) REFERENCES `fic_data_source_info` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of fic_interface_info
-- ----------------------------
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:53', '2017-01-24 09:36:53', '1', '个人基本信息查询', 'personal_info', '/api/rule/gateway/personal_info/', 'REMOTE', 'Courier', '{\'data_identity\': \'personal_info\'}', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:53', '2017-01-24 09:36:53', '2', '贷款中介查询', 'loan_agency', '/api/rule/gateway/loan_agency/', 'REMOTE', 'Courier', '{\'data_identity\': \'loan_agency\'}', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:53', '2017-01-24 09:36:53', '3', '机构G黑名单查询', 'agentg_black', '/api/rule/gateway/agentg_black/', 'REMOTE', 'Courier', '{\'data_identity\': \'agentg_black\'}', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\', \'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:53', '2017-01-24 09:36:53', '4', '天网黑名单查询', 'tianwang_black', '/api/rule/gateway/tianwang_black/', 'REMOTE', 'Courier', '{\'data_identity\': \'tianwang_black\'}', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:53', '2017-01-24 09:36:53', '5', '天网多头贷款查询', 'tianwang_multi_loan', '/api/rule/gateway/tianwang_multi_loan/', 'REMOTE', 'Courier', '{\'data_identity\': \'tianwang_multi_loan\'}', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:53', '2017-01-24 09:36:53', '6', '天眼黑名单查询', 'tianyan_black', '/api/rule/gateway/tianyan_black/', 'REMOTE', 'Courier', '{\'data_identity\': \'tianyan_black\'}', '{\'id_card_code\': \'%(card_id)s\', \'mobile\': \'%(mobile)s\', \'email\': \'\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:53', '2017-01-24 09:36:53', '7', '法院失信被执行人查询', 'court_shixin_a_s', '/api/rule/gateway/court_shixin_a_s/', 'REMOTE', 'Courier', '{\'data_identity\': \'court_shixin_a_s\'}', '{\'entity_name\': \'%(name)s\', \'entity_id\': \'%(card_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:54', '2017-01-24 09:36:54', '8', '网贷黑名单查询', 'net_black_a_s', '/api/rule/gateway/net_black_a_s/', 'REMOTE', 'Courier', '{\'data_identity\': \'net_black_a_s\'}', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:54', '2017-01-24 09:36:54', '9', '电信手机号三元素认证', 'telecom_mobile_identity_s', '/api/rule/gateway/telecom_mobile_identity_s/', 'REMOTE', 'Courier', '{\'data_identity\': \'telecom_mobile_identity_s\'}', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\', \'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:54', '2017-01-24 09:36:54', '10', '联通手机号三元素认证', 'unicom_mobile_identity_s', '/api/rule/gateway/unicom_mobile_identity_s/', 'REMOTE', 'Courier', '{\'data_identity\': \'unicom_mobile_identity_s\'}', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\', \'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:54', '2017-01-24 09:36:54', '11', '移动手机号三元素认证', 'yd_mobile_identity_s', '/api/rule/gateway/yd_mobile_identity_s/', 'REMOTE', 'Courier', '{\'data_identity\': \'yd_mobile_identity_s\'}', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\', \'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:54', '2017-01-24 09:36:54', '12', '移动手机信用查询', 'china_mobile_ability', '/api/rule/gateway/china_mobile_ability/', 'REMOTE', 'Courier', '{\'data_identity\': \'china_mobile_ability\'}', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:54', '2017-01-24 09:36:54', '13', '个人不良信息查询', 'negative_info_s', '/api/rule/gateway/negative_info_s/', 'REMOTE', 'Courier', '{\'data_identity\': \'negative_info_s\'}', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:54', '2017-01-24 09:36:54', '14', '天网灰名单查询', 'tianwang_gray', '/api/rule/gateway/tianwang_gray/', 'REMOTE', 'Courier', '{\'data_identity\': \'tianwang_gray\'}', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:54', '2017-01-24 09:36:54', '15', '法院被执行人查询', 'court_zhixing_a_s', '/api/rule/gateway/court_zhixing_a_s/', 'REMOTE', 'Courier', '{\'data_identity\': \'court_zhixing_a_s\'}', '{\'entity_name\': \'%(name)s\', \'entity_id\': \'%(card_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:54', '2017-01-24 09:36:54', '16', '手机号码归属地查询', 'mobile_locale', '/api/rule/gateway/mobile_locale/', 'REMOTE', 'Courier', '{\'data_identity\': \'mobile_locale\'}', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:54', '2017-01-24 09:36:54', '17', '移动号码在网时长查询', 'yd_mobile_online_time_s', '/api/rule/gateway/yd_mobile_online_time_s/', 'REMOTE', 'Courier', '{\'data_identity\': \'yd_mobile_online_time_s\'}', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:54', '2017-01-24 09:36:54', '18', '联通号码在网时长查询', 'unicome_mobile_online_time_s', '/api/rule/gateway/unicome_mobile_online_time_s/', 'REMOTE', 'Courier', '{\'data_identity\': \'\'}', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:54', '2017-01-24 09:36:54', '19', '电信号码在网时长查询', 'telecom_mobile_online', '/api/rule/gateway/telecom_mobile_online/', 'REMOTE', 'Courier', '{\'data_identity\': \'\'}', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-01-24 09:36:54', '2017-01-24 09:36:54', '20', '经纬度获取地理位置', 'geo_location', '/api/rule/gateway/geo_location/', 'REMOTE', 'Courier', '{\'data_identity\': \'\'}', '{\'gps_longitude\': \'%(longitude)s\', \'gps_latitude\': \'%(latitude)s\'}', '0', '0', '0', '', '3');
