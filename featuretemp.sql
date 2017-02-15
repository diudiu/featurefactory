/*
Navicat MySQL Data Transfer

Source Server         : 198Mysql
Source Server Version : 50628
Source Host           : 192.168.1.198:3306
Source Database       : featuretemp

Target Server Type    : MYSQL
Target Server Version : 50628
File Encoding         : 65001

Date: 2017-02-15 11:58:08
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
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;

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
INSERT INTO `auth_permission` VALUES ('58', 'Can add ', '20', 'add_citycodefield');
INSERT INTO `auth_permission` VALUES ('59', 'Can change ', '20', 'change_citycodefield');
INSERT INTO `auth_permission` VALUES ('60', 'Can delete ', '20', 'delete_citycodefield');
INSERT INTO `auth_permission` VALUES ('61', 'Can add 接口-参数映射表', '21', 'add_interfacefieldrel');
INSERT INTO `auth_permission` VALUES ('62', 'Can change 接口-参数映射表', '21', 'change_interfacefieldrel');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete 接口-参数映射表', '21', 'delete_interfacefieldrel');

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
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;

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
INSERT INTO `celery_taskmeta` VALUES ('24', '711b8377-8c67-41d1-9515-b4cf3c7a8630', 'SUCCESS', null, '2017-02-14 16:09:38', null, '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('25', '44b04ce8-ba6d-4d6f-af6e-b1cd03ea84c5', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpLZXlFcnJvcgpxAVURdGFyZ2V0X2ZpZWxkX25hbWVxAoVxA1JxBC4=', '2017-02-14 17:06:49', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 31, in audit_task\n    target_field_list = [data[\'target_field_name\'] for data in base_data[\'useful_args\']]\nKeyError: \'target_field_name\'\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('26', '48f8b8fd-5403-413c-bfe7-27886d556220', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpLZXlFcnJvcgpxAVURdGFyZ2V0X2ZpZWxkX25hbWVxAoVxA1JxBC4=', '2017-02-14 17:29:23', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 31, in audit_task\n    target_field_list = [data[\'target_field_name\'] for data in base_data[\'useful_args\']]\nKeyError: \'target_field_name\'\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('27', '6e28454f-5cd7-428c-bfd8-1914e0be295d', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpLZXlFcnJvcgpxAVURdGFyZ2V0X2ZpZWxkX25hbWVxAoVxA1JxBC4=', '2017-02-14 17:30:56', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 31, in audit_task\n    target_field_list = [data[\'target_field_name\'] for data in base_data[\'useful_args\']]\nKeyError: \'target_field_name\'\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('28', '423bfa73-c8b5-45ff-a5c9-7b0c2d37d1ad', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpLZXlFcnJvcgpxAVURdGFyZ2V0X2ZpZWxkX25hbWVxAoVxA1JxBC4=', '2017-02-14 17:36:30', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 31, in audit_task\n    target_field_list = [data[\'target_field_name\'] for data in base_data[\'useful_args\']]\nKeyError: \'target_field_name\'\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('29', '094ced72-c9c5-489f-9ea5-acfc0ea7f80d', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpJbXBvcnRFcnJvcgpxAVUZTm8gbW9kdWxlIG5hbWVkIHN0YWNrbGVzc3EChXEDUnEELg==', '2017-02-14 17:38:47', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 29, in audit_task\n    original_data_list = data_get_dispatch(base_data)\n  File \"D:\\PyCharm 2016.1.4\\helpers\\pydev\\pydevd.py\", line 1485, in <module>\n    from _pydevd_bundle import pydevd_stackless\n  File \"D:\\PyCharm 2016.1.4\\helpers\\pydev\\_pydevd_bundle\\pydevd_stackless.py\", line 13, in <module>\n    import stackless  # @UnresolvedImport\nImportError: No module named stackless\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('30', '3b41f43f-d62c-489d-bc4e-5bf794763234', 'FAILURE', 'gAJjUXVldWUKRW1wdHkKcQEpUnECLg==', '2017-02-14 17:56:47', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 29, in audit_task\n    original_data_list = data_get_dispatch(base_data)\n  File \"D:\\Python\\lib\\site-packages\\kombu\\transport\\virtual\\__init__.py\", line 830, in drain_events\n    item, channel = get(timeout=timeout)\n  File \"D:\\Python\\lib\\site-packages\\kombu\\transport\\redis.py\", line 352, in get\n    ret = self.handle_event(fileno, event)\n  File \"D:\\Python\\lib\\site-packages\\kombu\\transport\\redis.py\", line 335, in handle_event\n    return self.on_readable(fileno), self\n  File \"D:\\Python\\lib\\site-packages\\kombu\\transport\\redis.py\", line 331, in on_readable\n    return chan.handlers[type]()\n  File \"D:\\Python\\lib\\site-packages\\kombu\\transport\\redis.py\", line 660, in _brpop_read\n    raise Empty()\nEmpty\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('31', '9038471e-20d7-47db-b35e-560595467adb', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpTeW50YXhFcnJvcgpxAVUOaW52YWxpZCBzeW50YXhxAihVJ0Y6L2ZlYXR1cmVmYWN0b3J5XHNsdW1kb2dcbHBfanVua21hbi5weXEDS3NLGlUaICAgICAgICAgICAgaWYgaW50ZXJmYWNlLgpxBHSGcQVScQYu', '2017-02-14 17:57:04', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 29, in audit_task\n    original_data_list = data_get_dispatch(base_data)\n  File \"F:/featurefactory\\apps\\common\\dispatcher.py\", line 86, in data_get_dispatch\n    obj = import_string(api_manager)\n  File \"D:\\Python\\lib\\site-packages\\django\\utils\\module_loading.py\", line 26, in import_string\n    module = import_module(module_path)\n  File \"D:\\Python\\lib\\importlib\\__init__.py\", line 37, in import_module\n    __import__(name)\n  File \"F:/featurefactory\\slumdog\\lp_junkman.py\", line 115\n    if interface.\n                ^\nSyntaxError: invalid syntax\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('32', 'bf80272c-17b6-4e96-8c96-470c7e66324f', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpLZXlFcnJvcgpxAVURdGFyZ2V0X2ZpZWxkX25hbWVxAoVxA1JxBC4=', '2017-02-14 17:58:59', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 31, in audit_task\n    target_field_list = [data[\'target_field_name\'] for data in base_data[\'useful_args\']]\nKeyError: \'target_field_name\'\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('33', '0dfe6957-e6e4-4288-bd4d-f2fdd3ac89da', 'FAILURE', 'gAJjUXVldWUKRW1wdHkKcQEpUnECLg==', '2017-02-14 17:59:54', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 29, in audit_task\n    original_data_list = data_get_dispatch(base_data)\n  File \"D:\\Python\\lib\\site-packages\\kombu\\transport\\virtual\\__init__.py\", line 830, in drain_events\n    item, channel = get(timeout=timeout)\n  File \"D:\\Python\\lib\\site-packages\\kombu\\transport\\redis.py\", line 352, in get\n    ret = self.handle_event(fileno, event)\n  File \"D:\\Python\\lib\\site-packages\\kombu\\transport\\redis.py\", line 335, in handle_event\n    return self.on_readable(fileno), self\n  File \"D:\\Python\\lib\\site-packages\\kombu\\transport\\redis.py\", line 331, in on_readable\n    return chan.handlers[type]()\n  File \"D:\\Python\\lib\\site-packages\\kombu\\transport\\redis.py\", line 660, in _brpop_read\n    raise Empty()\nEmpty\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('34', '36dd8129-2b8b-46f2-9392-3d063c38e857', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpLZXlFcnJvcgpxAVURdGFyZ2V0X2ZpZWxkX25hbWVxAoVxA1JxBC4=', '2017-02-14 18:02:58', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 31, in audit_task\n    target_field_list = [data[\'target_field_name\'] for data in base_data[\'useful_args\']]\nKeyError: \'target_field_name\'\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('35', 'bba48adc-2826-4c15-8467-9264d829afcf', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpLZXlFcnJvcgpxAVURdGFyZ2V0X2ZpZWxkX25hbWVxAoVxA1JxBC4=', '2017-02-14 18:04:16', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 31, in audit_task\n    target_field_list = [data[\'target_field_name\'] for data in base_data[\'useful_args\']]\nKeyError: \'target_field_name\'\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('36', '42b160d8-e4a7-4557-bdad-02d0283fd131', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpBdHRyaWJ1dGVFcnJvcgpxAVUkJ2xpc3QnIG9iamVjdCBoYXMgbm8gYXR0cmlidXRlICdnZXQncQKFcQNScQQu', '2017-02-14 18:04:30', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 31, in audit_task\n    target_field_list = original_data_list.get(\'feature_list\', None)\nAttributeError: \'list\' object has no attribute \'get\'\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('37', 'a4cb2310-f484-4aa8-b539-9996f97e3499', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpBdHRyaWJ1dGVFcnJvcgpxAVUkJ2xpc3QnIG9iamVjdCBoYXMgbm8gYXR0cmlidXRlICdnZXQncQKFcQNScQQu', '2017-02-14 18:05:33', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 31, in audit_task\n    target_field_list = original_data_list.get(\'feature_list\', None)\nAttributeError: \'list\' object has no attribute \'get\'\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('38', '8997c064-35f5-4fc0-9d8f-d90aadfa6a6b', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpJbXBvcnRFcnJvcgpxAVUZTm8gbW9kdWxlIG5hbWVkIHN0YWNrbGVzc3EChXEDUnEELg==', '2017-02-14 18:24:20', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"D:\\PyCharm 2016.1.4\\helpers\\pydev\\pydevd.py\", line 1485, in <module>\n    from _pydevd_bundle import pydevd_stackless\n  File \"D:\\PyCharm 2016.1.4\\helpers\\pydev\\_pydevd_bundle\\pydevd_stackless.py\", line 13, in <module>\n    import stackless  # @UnresolvedImport\nImportError: No module named stackless\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('39', '3441ac2a-e63c-4996-8c6c-fb8c6a031701', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpJbXBvcnRFcnJvcgpxAVUbTm8gbW9kdWxlIG5hbWVkIG9ubGluZV90aW1lcQKFcQNScQQu', '2017-02-14 18:40:01', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 47, in audit_task\n    ret_data = process_dispatch(original_data_list, base_data[\'feature_list\'])\n  File \"F:/featurefactory\\apps\\common\\dispatcher.py\", line 110, in process_dispatch\n    obj = import_string(obj_string)\n  File \"D:\\Python\\lib\\site-packages\\django\\utils\\module_loading.py\", line 26, in import_string\n    module = import_module(module_path)\n  File \"D:\\Python\\lib\\importlib\\__init__.py\", line 37, in import_module\n    __import__(name)\nImportError: No module named online_time\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('40', '1eed1c0f-1b43-40e2-b525-52fc57504a2c', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpJbXBvcnRFcnJvcgpxAVUbTm8gbW9kdWxlIG5hbWVkIG9ubGluZV90aW1lcQKFcQNScQQu', '2017-02-14 18:51:19', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 47, in audit_task\n    ret_data = process_dispatch(original_data_list, base_data[\'feature_list\'], collect_type_list)\n  File \"F:/featurefactory\\apps\\common\\dispatcher.py\", line 110, in process_dispatch\n    feature_name + cons.HANDLE_COMBINE + cons.HANDLE_CLASS\n  File \"D:\\Python\\lib\\site-packages\\django\\utils\\module_loading.py\", line 26, in import_string\n    module = import_module(module_path)\n  File \"D:\\Python\\lib\\importlib\\__init__.py\", line 37, in import_module\n    __import__(name)\nImportError: No module named online_time\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('41', 'a3c138f0-790e-426b-acc8-70f7d7a6f81a', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpJbXBvcnRFcnJvcgpxAVUeTm8gbW9kdWxlIG5hbWVkIGxwX29ubGluZV90aW1lcQKFcQNScQQu', '2017-02-14 18:53:50', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 47, in audit_task\n    ret_data = process_dispatch(original_data_list, base_data[\'feature_list\'], collect_type_list)\n  File \"F:/featurefactory\\apps\\common\\dispatcher.py\", line 111, in process_dispatch\n    feature_name + cons.HANDLE_COMBINE + cons.HANDLE_CLASS\n  File \"D:\\Python\\lib\\site-packages\\django\\utils\\module_loading.py\", line 26, in import_string\n    module = import_module(module_path)\n  File \"D:\\Python\\lib\\importlib\\__init__.py\", line 37, in import_module\n    __import__(name)\nImportError: No module named lp_online_time\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('42', '9fca49e1-d7fd-4a65-abee-c3df0588b9d4', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpJbXBvcnRFcnJvcgpxAVUeTm8gbW9kdWxlIG5hbWVkIGxwX29ubGluZV90aW1lcQKFcQNScQQu', '2017-02-14 18:54:19', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 47, in audit_task\n    ret_data = process_dispatch(original_data_list, base_data[\'feature_list\'], collect_type_list)\n  File \"F:/featurefactory\\apps\\common\\dispatcher.py\", line 112, in process_dispatch\n    obj = import_string(obj_string)\n  File \"D:\\Python\\lib\\site-packages\\django\\utils\\module_loading.py\", line 26, in import_string\n    module = import_module(module_path)\n  File \"D:\\Python\\lib\\importlib\\__init__.py\", line 37, in import_module\n    __import__(name)\nImportError: No module named lp_online_time\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('43', '66d7a90d-e936-41c1-b9dd-353d31cd7137', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpJbXBvcnRFcnJvcgpxAVUeTm8gbW9kdWxlIG5hbWVkIGxwX29ubGluZV90aW1lcQKFcQNScQQu', '2017-02-15 09:18:01', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 47, in audit_task\n    ret_data = process_dispatch(original_data_list, base_data[\'feature_list\'], collect_type_list)\n  File \"F:/featurefactory\\apps\\common\\dispatcher.py\", line 112, in process_dispatch\n    obj = import_string(obj_string)\n  File \"D:\\Python\\lib\\site-packages\\django\\utils\\module_loading.py\", line 26, in import_string\n    module = import_module(module_path)\n  File \"D:\\Python\\lib\\importlib\\__init__.py\", line 37, in import_module\n    __import__(name)\nImportError: No module named lp_online_time\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('44', '63d5eebb-269f-42ec-a886-c3dbb64f2bd0', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpJbXBvcnRFcnJvcgpxAVUeTm8gbW9kdWxlIG5hbWVkIGxwX29ubGluZV90aW1lcQKFcQNScQQu', '2017-02-15 11:01:58', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 51, in audit_task\n    ret_data = process_dispatch(original_data_list, base_data[\'feature_list\'], collect_type_list)\n  File \"F:/featurefactory\\apps\\common\\dispatcher.py\", line 113, in process_dispatch\n    obj = import_string(obj_string)\n  File \"D:\\Python\\lib\\site-packages\\django\\utils\\module_loading.py\", line 26, in import_string\n    module = import_module(module_path)\n  File \"D:\\Python\\lib\\importlib\\__init__.py\", line 37, in import_module\n    __import__(name)\nImportError: No module named lp_online_time\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');
INSERT INTO `celery_taskmeta` VALUES ('45', '0ffce1cc-96df-4b4e-b3b0-a4ef9811eee2', 'FAILURE', 'gAJjZXhjZXB0aW9ucwpJbXBvcnRFcnJvcgpxAVUeTm8gbW9kdWxlIG5hbWVkIGxwX29ubGluZV90aW1lcQKFcQNScQQu', '2017-02-15 11:14:51', 'Traceback (most recent call last):\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 240, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"D:\\Python\\lib\\site-packages\\celery\\app\\trace.py\", line 438, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"F:/featurefactory\\apps\\async\\tasks.py\", line 51, in audit_task\n    ret_data = process_dispatch(original_data_list, base_data[\'feature_list\'], collect_type_list)\n  File \"F:/featurefactory\\apps\\common\\dispatcher.py\", line 113, in process_dispatch\n    obj = import_string(obj_string)\n  File \"D:\\Python\\lib\\site-packages\\django\\utils\\module_loading.py\", line 26, in import_string\n    module = import_module(module_path)\n  File \"D:\\Python\\lib\\importlib\\__init__.py\", line 37, in import_module\n    __import__(name)\nImportError: No module named lp_online_time\n', '0', 'eJxrYKotZIzgYGBgSM7IzEkpSs0rZIotZC7WAwBWuwcA');

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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

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
INSERT INTO `django_content_type` VALUES ('20', '', 'common', 'citycodefield');
INSERT INTO `django_content_type` VALUES ('21', '接口-参数映射表', 'datasource', 'interfacefieldrel');

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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2017-01-20 14:37:27');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2017-01-20 14:37:33');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2017-01-20 14:37:35');
INSERT INTO `django_migrations` VALUES ('4', 'common', '0001_initial', '2017-01-20 14:37:35');
INSERT INTO `django_migrations` VALUES ('7', 'sessions', '0001_initial', '2017-01-20 14:37:37');
INSERT INTO `django_migrations` VALUES ('9', 'djcelery', '0001_initial', '2017-01-24 14:13:35');
INSERT INTO `django_migrations` VALUES ('11', 'common', '0002_citycodefield', '2017-02-14 11:50:26');
INSERT INTO `django_migrations` VALUES ('12', 'remote', '0001_initial', '2017-02-14 14:37:33');
INSERT INTO `django_migrations` VALUES ('13', 'datasource', '0001_initial', '2017-02-14 14:41:16');
INSERT INTO `django_migrations` VALUES ('14', 'remote', '0002_featurefieldrel_collect_type', '2017-02-14 17:07:46');
INSERT INTO `django_migrations` VALUES ('15', 'remote', '0003_auto_20170214_1710', '2017-02-14 17:10:42');

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
-- Table structure for `fic_city_code_field`
-- ----------------------------
DROP TABLE IF EXISTS `fic_city_code_field`;
CREATE TABLE `fic_city_code_field` (
  `is_delete` tinyint(1) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city_name_cn` varchar(256) NOT NULL,
  `city_name_en` varchar(256) NOT NULL,
  `father_tip` varchar(256) NOT NULL,
  `father_code` varchar(256) DEFAULT NULL,
  `city_code` varchar(256) NOT NULL,
  `seouri` varchar(256) NOT NULL,
  `abbreviation` varchar(256) DEFAULT NULL,
  `city_level` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1610 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of fic_city_code_field
-- ----------------------------
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:47', '2017-02-14 12:14:47', '1', ' 不限 ', ' Open ', '0', '', '0', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:50', '2017-02-14 12:14:50', '2', ' 北京 ', ' BeiJing ', '0', '', '10', ' beijing ', ' 北京 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:51', '2017-02-14 12:14:51', '3', ' 东城区 ', ' DongChengQu ', '1', '10', '10010010', ' dongcheng ', ' 东城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:51', '2017-02-14 12:14:51', '4', ' 西城区 ', ' XiChengQu ', '1', '10', '10010020', ' xicheng ', ' 西城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:51', '2017-02-14 12:14:51', '5', ' 朝阳区 ', ' ChaoYangQu ', '1', '10', '10010030', ' chaoyang ', ' 朝阳区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:52', '2017-02-14 12:14:52', '6', ' 海淀区 ', ' HaiDianQu ', '1', '10', '10010050', ' haidian ', ' 海淀区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:52', '2017-02-14 12:14:52', '7', ' 石景山 ', ' ShiJingShan ', '1', '10', '10010070', ' shijingshan ', ' 石景山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:52', '2017-02-14 12:14:52', '8', ' 门头沟 ', ' MenTouGou ', '1', '10', '10010080', ' mentougou ', ' 门头沟 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:53', '2017-02-14 12:14:53', '9', ' 丰台区 ', ' FengTaiQu ', '1', '10', '10010090', ' fengtai ', ' 丰台区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:53', '2017-02-14 12:14:53', '10', ' 房山区 ', ' FangShanQu ', '1', '10', '10010100', ' fangshan ', ' 房山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:53', '2017-02-14 12:14:53', '11', ' 大兴区 ', ' DaXingQu ', '1', '10', '10010110', ' daxing ', ' 大兴区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:54', '2017-02-14 12:14:54', '12', ' 通州区 ', ' TongZhouQu ', '1', '10', '10010120', ' tongzhou ', ' 通州区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:54', '2017-02-14 12:14:54', '13', ' 顺义区 ', ' ShunYiQu ', '1', '10', '10010130', ' shunyi ', ' 顺义区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:57', '2017-02-14 12:14:57', '14', ' 平谷区 ', ' PingGuQu ', '1', '10', '10010140', ' pinggu ', ' 平谷区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:57', '2017-02-14 12:14:57', '15', ' 昌平区 ', ' ChangPingQu ', '1', '10', '10010150', ' changping ', ' 昌平区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:57', '2017-02-14 12:14:57', '16', ' 怀柔区 ', ' HuaiRouQu ', '1', '10', '10010160', ' huairou ', ' 怀柔区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:57', '2017-02-14 12:14:57', '17', ' 延庆县 ', ' YanQingXian ', '1', '10', '10010170', ' yanqing ', ' 延庆县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:57', '2017-02-14 12:14:57', '18', ' 密云县 ', ' MiYunXian ', '1', '10', '10010180', ' miyun ', ' 密云县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:57', '2017-02-14 12:14:57', '19', ' 上海 ', ' ShangHai ', '0', '', '20', ' shanghai ', ' 上海 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:57', '2017-02-14 12:14:57', '20', ' 浦东新区 ', ' PuDongXinQu ', '1', '20', '20010010', ' pudong ', ' 浦东区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:57', '2017-02-14 12:14:57', '21', ' 徐汇区 ', ' XuHuiQu ', '1', '20', '20010020', ' xuhui ', ' 徐汇区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:57', '2017-02-14 12:14:57', '22', ' 长宁区 ', ' ZhangNingQu ', '1', '20', '20010030', ' changning ', ' 长宁区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:57', '2017-02-14 12:14:57', '23', ' 普陀区 ', ' PuTuoQu ', '1', '20', '20010040', ' putuo ', ' 普陀区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:57', '2017-02-14 12:14:57', '24', ' 闸北区 ', ' ZhaBeiQu ', '1', '20', '20010050', ' zhabei ', ' 闸北区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:57', '2017-02-14 12:14:57', '25', ' 虹口区 ', ' HongKouQu ', '1', '20', '20010060', ' hongkou ', ' 虹口区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:57', '2017-02-14 12:14:57', '26', ' 杨浦区 ', ' YangPuQu ', '1', '20', '20010070', ' yangpu ', ' 杨浦区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:58', '2017-02-14 12:14:58', '27', ' 黄浦区 ', ' HuangPuQu ', '1', '20', '20010080', ' huangpu ', ' 黄浦区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:58', '2017-02-14 12:14:58', '28', ' 静安区 ', ' JingAnQu ', '1', '20', '20010100', ' jingan ', ' 静安区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:58', '2017-02-14 12:14:58', '29', ' 宝山区 ', ' BaoShanQu ', '1', '20', '20010110', ' baoshan ', ' 宝山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:58', '2017-02-14 12:14:58', '30', ' 闵行区 ', ' MinXingQu ', '1', '20', '20010120', ' minhang ', ' 闵行区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:58', '2017-02-14 12:14:58', '31', ' 嘉定区 ', ' JiaDingQu ', '1', '20', '20010130', ' jiading ', ' 嘉定区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:58', '2017-02-14 12:14:58', '32', ' 金山区 ', ' JinShanQu ', '1', '20', '20010140', ' jinshan ', ' 金山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:58', '2017-02-14 12:14:58', '33', ' 松江区 ', ' SongJiangQu ', '1', '20', '20010150', ' songjiang ', ' 松江区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:58', '2017-02-14 12:14:58', '34', ' 青浦区 ', ' QingPuQu ', '1', '20', '20010160', ' qingpu ', ' 青浦区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:58', '2017-02-14 12:14:58', '35', ' 奉贤区 ', ' FengXianQu ', '1', '20', '20010180', ' fengxian ', ' 奉贤区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:58', '2017-02-14 12:14:58', '36', ' 崇明县 ', ' ChongMingXian ', '1', '20', '20010190', ' chongming ', ' 崇明县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:58', '2017-02-14 12:14:58', '37', ' 天津 ', ' TianJin ', '0', '', '30', ' tianjin ', ' 天津 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:58', '2017-02-14 12:14:58', '38', ' 和平区 ', ' HePingQu ', '1', '30', '30010010', ' heping ', ' 和平区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:58', '2017-02-14 12:14:58', '39', ' 河东区 ', ' HeDongQu ', '1', '30', '30010020', ' hedong ', ' 河东区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:58', '2017-02-14 12:14:58', '40', ' 河西区 ', ' HeXiQu ', '1', '30', '30010030', ' hexi ', ' 河西区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:59', '2017-02-14 12:14:59', '41', ' 南开区 ', ' NanKaiQu ', '1', '30', '30010040', ' nankai ', ' 南开区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:59', '2017-02-14 12:14:59', '42', ' 河北区 ', ' HeBeiQu ', '1', '30', '30010050', ' hebei ', ' 河北区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:59', '2017-02-14 12:14:59', '43', ' 红桥区 ', ' HongQiaoQu ', '1', '30', '30010060', ' hongqiao ', ' 红桥区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:59', '2017-02-14 12:14:59', '44', ' 塘沽区 ', ' TangGuQu ', '1', '30', '30010070', ' tangku ', ' 塘沽区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:59', '2017-02-14 12:14:59', '45', ' 汉沽区 ', ' HanGuQu ', '1', '30', '30010080', ' hanku ', ' 汉沽区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:59', '2017-02-14 12:14:59', '46', ' 大港区 ', ' DaGangQu ', '1', '30', '30010090', ' dagang ', ' 大港区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:59', '2017-02-14 12:14:59', '47', ' 东丽区 ', ' DongLiQu ', '1', '30', '30010100', ' dongli ', ' 东丽区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:59', '2017-02-14 12:14:59', '48', ' 西青区 ', ' XiQingQu ', '1', '30', '30010110', ' xiqing ', ' 西青区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:59', '2017-02-14 12:14:59', '49', ' 津南区 ', ' JinNanQu ', '1', '30', '30010120', ' jinnan ', ' 津南区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:59', '2017-02-14 12:14:59', '50', ' 北辰区 ', ' BeiChenQu ', '1', '30', '30010130', ' beichen ', ' 北辰区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:59', '2017-02-14 12:14:59', '51', ' 武清区 ', ' WuQingQu ', '1', '30', '30010140', ' wuqing ', ' 武清区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:59', '2017-02-14 12:14:59', '52', ' 宝坻区 ', ' BaoChiQu ', '1', '30', '30010150', ' baodi ', ' 宝坻区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:14:59', '2017-02-14 12:14:59', '53', ' 宁河县 ', ' NingHeXian ', '1', '30', '30010160', ' ninghe ', ' 宁河县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:00', '2017-02-14 12:15:00', '54', ' 静海县 ', ' JingHaiXian ', '1', '30', '30010170', ' jinghai ', ' 静海县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:00', '2017-02-14 12:15:00', '55', ' 蓟　县 ', ' Ji　Xian ', '1', '30', '30010180', ' jixian ', ' 蓟　县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:00', '2017-02-14 12:15:00', '56', ' 开发区 ', ' KaiFaQu ', '1', '30', '30010200', ' kaifaqu ', ' 开发区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:00', '2017-02-14 12:15:00', '57', ' 滨海区 ', ' BinHaiQu ', '1', '30', '30010210', ' binhaiqu ', ' 滨海区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:00', '2017-02-14 12:15:00', '58', ' 重庆 ', ' ChongQing ', '0', '', '40', ' chongqing ', ' 重庆 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:00', '2017-02-14 12:15:00', '59', ' 渝中区 ', ' YuZhongQu ', '1', '40', '40010010', ' yuzhong ', ' 渝中区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:00', '2017-02-14 12:15:00', '60', ' 江北区 ', ' JiangBeiQu ', '1', '40', '40010020', ' jiangbei ', ' 江北区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:00', '2017-02-14 12:15:00', '61', ' 南岸区 ', ' NanAnQu ', '1', '40', '40010030', ' nanan ', ' 南岸区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:00', '2017-02-14 12:15:00', '62', ' 沙坪坝 ', ' ShaPingBa ', '1', '40', '40010040', ' shapingva ', ' 沙坪坝 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:00', '2017-02-14 12:15:00', '63', ' 九龙坡 ', ' JiuLongPo ', '1', '40', '40010050', ' jiulongpo ', ' 九龙坡 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:00', '2017-02-14 12:15:00', '64', ' 大渡口 ', ' DaDuKou ', '1', '40', '40010060', ' dadukou ', ' 大渡口 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:00', '2017-02-14 12:15:00', '65', ' 北碚区 ', ' BeiBeiQu ', '1', '40', '40010070', ' beibei ', ' 北碚区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:00', '2017-02-14 12:15:00', '66', ' 巴南区 ', ' BaNanQu ', '1', '40', '40010080', ' banan ', ' 巴南区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:01', '2017-02-14 12:15:01', '67', ' 渝北区 ', ' YuBeiQu ', '1', '40', '40010090', ' yubei ', ' 渝北区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:01', '2017-02-14 12:15:01', '68', ' 永川区 ', ' YongChuanQu ', '1', '40', '40010100', ' yongchuan ', ' 永川区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:01', '2017-02-14 12:15:01', '69', ' 涪陵区 ', ' FuLingQu ', '1', '40', '40010110', ' fuling ', ' 涪陵区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:01', '2017-02-14 12:15:01', '70', ' 合川区 ', ' HeChuanQu ', '1', '40', '40010120', ' hechuan ', ' 合川区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:01', '2017-02-14 12:15:01', '71', ' 江津区 ', ' JiangJinQu ', '1', '40', '40010130', ' jiangjin ', ' 江津区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:01', '2017-02-14 12:15:01', '72', ' 长寿区 ', ' ZhangShouQu ', '1', '40', '40010140', ' changshou ', ' 长寿区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:01', '2017-02-14 12:15:01', '73', ' 南川区 ', ' NanChuanQu ', '1', '40', '40010170', ' nanchuan ', ' 南川区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:01', '2017-02-14 12:15:01', '74', ' 万州区 ', ' WanZhouQu ', '1', '40', '40010180', ' wanzhou ', ' 万州区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:01', '2017-02-14 12:15:01', '75', ' 黔江区 ', ' QianJiangQu ', '1', '40', '40010190', ' qianjiang ', ' 黔江区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:01', '2017-02-14 12:15:01', '76', ' 綦江区 ', ' QiJiangQu ', '1', '40', '40010200', ' qijiang ', ' 綦江区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:01', '2017-02-14 12:15:01', '77', ' 潼南县 ', ' TongNanXian ', '1', '40', '40010210', ' tongnanxian ', ' 潼南县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:01', '2017-02-14 12:15:01', '78', ' 铜梁区 ', ' TongLiangQu ', '1', '40', '40010220', ' tongliang ', ' 铜梁区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:01', '2017-02-14 12:15:01', '79', ' 大足区 ', ' DaZuQu ', '1', '40', '40010230', ' dazu ', ' 大足区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:01', '2017-02-14 12:15:01', '80', ' 荣昌县 ', ' RongChangXian ', '1', '40', '40010240', ' rongchangxian ', ' 荣昌县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:02', '2017-02-14 12:15:02', '81', ' 璧山区 ', ' BiShanQu ', '1', '40', '40010250', ' bishan ', ' 璧山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:02', '2017-02-14 12:15:02', '82', ' 垫江县 ', ' DianJiangXian ', '1', '40', '40010260', ' dianjiangxian ', ' 垫江县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:02', '2017-02-14 12:15:02', '83', ' 武隆县 ', ' WuLongXian ', '1', '40', '40010270', ' wulongxian ', ' 武隆县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:02', '2017-02-14 12:15:02', '84', ' 丰都县 ', ' FengDouXian ', '1', '40', '40010280', ' fengdouxian ', ' 丰都县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:02', '2017-02-14 12:15:02', '85', ' 城口县 ', ' ChengKouXian ', '1', '40', '40010290', ' chengkouxian ', ' 城口县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:02', '2017-02-14 12:15:02', '86', ' 梁平县 ', ' LiangPingXian ', '1', '40', '40010300', ' liangpingxian ', ' 梁平县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:02', '2017-02-14 12:15:02', '87', ' 开县 ', ' KaiXian ', '1', '40', '40010310', ' kaixian ', ' 开县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:02', '2017-02-14 12:15:02', '88', ' 巫溪县 ', ' WuXiXian ', '1', '40', '40010320', ' wuxixian ', ' 巫溪县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:02', '2017-02-14 12:15:02', '89', ' 巫山县 ', ' WuShanXian ', '1', '40', '40010330', ' wushanxian ', ' 巫山县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:02', '2017-02-14 12:15:02', '90', ' 奉节县 ', ' FengJieXian ', '1', '40', '40010340', ' fengjiexian ', ' 奉节县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:02', '2017-02-14 12:15:02', '91', ' 云阳县 ', ' YunYangXian ', '1', '40', '40010350', ' yunyangxian ', ' 云阳县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:02', '2017-02-14 12:15:02', '92', ' 忠县 ', ' ZhongXian ', '1', '40', '40010360', ' zhongxian ', ' 忠县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:02', '2017-02-14 12:15:02', '93', ' 石柱 ', ' ShiZhu ', '1', '40', '40010370', ' shizhu ', ' 石柱 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:02', '2017-02-14 12:15:02', '94', ' 彭水县 ', ' PengShuiXian ', '1', '40', '40010380', ' pengshui ', ' 彭水 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '95', ' 酉阳县 ', ' YouYangXian ', '1', '40', '40010390', ' youyang ', ' 酉阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '96', ' 石柱县 ', ' ShiZhuXian ', '1', '40', '40010410', ' shizhuxian ', ' 石柱县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '97', ' 秀山县 ', ' XiuShanXian ', '1', '40', '40010420', ' xiushan ', ' 秀山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '98', ' 广东省 ', ' GuangDongSheng ', '0', '', '50', ' guangdong ', ' 广东省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '99', ' 广州 ', ' GuangZhou ', '1', '50', '50020', ' guangzhou ', ' 广州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '100', ' 白云区 ', ' BaiYunQu ', '1', '50020', '50020010', ' baiyun ', ' 白云区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '101', ' 天河区 ', ' TianHeQu ', '1', '50020', '50020020', ' tianhe ', ' 天河区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '102', ' 越秀区 ', ' YueXiuQu ', '1', '50020', '50020030', ' yuexiu ', ' 越秀区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '103', ' 海珠区 ', ' HaiZhuQu ', '1', '50020', '50020040', ' zhuhai ', ' 海珠区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '104', ' 黄埔区 ', ' HuangBuQu ', '1', '50020', '50020050', ' huangpu ', ' 黄埔区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '105', ' 荔湾区 ', ' LiWanQu ', '1', '50020', '50020060', ' xinliwan ', ' 荔湾区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '106', ' 番禺区 ', ' FanYuQu ', '1', '50020', '50020070', ' fanyu ', ' 番禺区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '107', ' 花都区 ', ' HuaDouQu ', '1', '50020', '50020080', ' huadu ', ' 花都区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '108', ' 萝岗区 ', ' LuoGangQu ', '1', '50020', '50020090', ' luogang ', ' 萝岗区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '109', ' 南沙区 ', ' NanShaQu ', '1', '50020', '50020100', ' nansha ', ' 南沙区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '110', ' 从化区 ', ' CongHuaQu ', '1', '50020', '50020110', ' conghua ', ' 从化市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:03', '2017-02-14 12:15:03', '111', ' 增城区 ', ' ZengChengQu ', '1', '50020', '50020120', ' zengcheng ', ' 增城市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '112', ' 潮州 ', ' ChaoZhou ', '1', '50', '50030', ' chaozhou ', ' 潮州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '113', ' 东莞 ', ' DongGuan ', '1', '50', '50040', ' dongguan ', ' 东莞 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '114', ' 南城区 ', ' NanChengQu ', '1', '50040', '50040010', ' nanchengqu ', ' 南城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '115', ' 东城区 ', ' DongChengQu ', '1', '50040', '50040020', ' dongchengqu ', ' 东城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '116', ' 万江区 ', ' WanJiangQu ', '1', '50040', '50040030', ' wanjiangqu ', ' 万江区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '117', ' 莞城区 ', ' GuanChengQu ', '1', '50040', '50040040', ' wanchengqu ', ' 莞城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '118', ' 石龙镇 ', ' ShiLongZhen ', '1', '50040', '50040050', ' shilongzhen ', ' 石龙镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '119', ' 虎门镇 ', ' HuMenZhen ', '1', '50040', '50040060', ' humenzhen ', ' 虎门镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '120', ' 麻涌镇 ', ' MaYongZhen ', '1', '50040', '50040070', ' mayongzhen ', ' 麻涌镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '121', ' 道滘镇 ', ' DaoJiaoZhen ', '1', '50040', '50040080', ' daojiaozhen ', ' 道滘镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '122', ' 石碣镇 ', ' ShiJieZhen ', '1', '50040', '50040090', ' shijiezhen ', ' 石碣镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '123', ' 沙田镇 ', ' ShaTianZhen ', '1', '50040', '50040100', ' shatianzhen ', ' 沙田镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '124', ' 望牛墩 ', ' WangNiuDun ', '1', '50040', '50040110', ' wangniudun ', ' 望牛墩 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '125', ' 洪梅镇 ', ' HongMeiZhen ', '1', '50040', '50040120', ' hongmeizhen ', ' 洪梅镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '126', ' 茶山镇 ', ' ChaShanZhen ', '1', '50040', '50040130', ' chashanzhen ', ' 茶山镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:04', '2017-02-14 12:15:04', '127', ' 寮步镇 ', ' LiaoBuZhen ', '1', '50040', '50040140', ' liaobuzhen ', ' 寮步镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:05', '2017-02-14 12:15:05', '128', ' 大岭山 ', ' DaLingShan ', '1', '50040', '50040150', ' dalingshan ', ' 大岭山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:05', '2017-02-14 12:15:05', '129', ' 大朗镇 ', ' DaLangZhen ', '1', '50040', '50040160', ' dalangzhen ', ' 大朗镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:05', '2017-02-14 12:15:05', '130', ' 黄江镇 ', ' HuangJiangZhen ', '1', '50040', '50040170', ' huangjiangzhen ', ' 黄江镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:05', '2017-02-14 12:15:05', '131', ' 樟木头 ', ' ZhangMuTou ', '1', '50040', '50040180', ' zhangmutou ', ' 樟木头 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:05', '2017-02-14 12:15:05', '132', ' 凤岗镇 ', ' FengGangZhen ', '1', '50040', '50040190', ' fenggangzhen ', ' 凤岗镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:05', '2017-02-14 12:15:05', '133', ' 塘厦镇 ', ' TangShaZhen ', '1', '50040', '50040200', ' tangxiazhen ', ' 塘厦镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:05', '2017-02-14 12:15:05', '134', ' 谢岗镇 ', ' XieGangZhen ', '1', '50040', '50040210', ' xiegangzhen ', ' 谢岗镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:05', '2017-02-14 12:15:05', '135', ' 厚街镇 ', ' HouJieZhen ', '1', '50040', '50040220', ' houjiezhen ', ' 厚街镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:05', '2017-02-14 12:15:05', '136', ' 清溪镇 ', ' QingXiZhen ', '1', '50040', '50040230', ' qingxizhen ', ' 清溪镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:05', '2017-02-14 12:15:05', '137', ' 常平镇 ', ' ChangPingZhen ', '1', '50040', '50040240', ' changpingzhen ', ' 常平镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:05', '2017-02-14 12:15:05', '138', ' 桥头镇 ', ' QiaoTouZhen ', '1', '50040', '50040250', ' qiaotouzhen ', ' 桥头镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:05', '2017-02-14 12:15:05', '139', ' 横沥镇 ', ' HengLiZhen ', '1', '50040', '50040260', ' henglizhen ', ' 横沥镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:05', '2017-02-14 12:15:05', '140', ' 东坑镇 ', ' DongKengZhen ', '1', '50040', '50040270', ' dongkengzhen ', ' 东坑镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:05', '2017-02-14 12:15:05', '141', ' 企石镇 ', ' QiShiZhen ', '1', '50040', '50040280', ' qishizhen ', ' 企石镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:06', '2017-02-14 12:15:06', '142', ' 石排镇 ', ' ShiPaiZhen ', '1', '50040', '50040290', ' shipaizhen ', ' 石排镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:06', '2017-02-14 12:15:06', '143', ' 长安镇 ', ' ZhangAnZhen ', '1', '50040', '50040300', ' changanzhen ', ' 长安镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:06', '2017-02-14 12:15:06', '144', ' 中堂镇 ', ' ZhongTangZhen ', '1', '50040', '50040310', ' zhongtangzhen ', ' 中堂镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:06', '2017-02-14 12:15:06', '145', ' 高埗镇 ', ' GaoBuZhen ', '1', '50040', '50040320', ' gaobuzhen ', ' 高埗镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:06', '2017-02-14 12:15:06', '146', ' 松山湖 ', ' SongShanHu ', '1', '50040', '50040330', ' songshanhu ', ' 松山湖 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:06', '2017-02-14 12:15:06', '147', ' 佛山 ', ' FoShan ', '1', '50', '50050', ' foshan ', ' 佛山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:06', '2017-02-14 12:15:06', '148', ' 禅城区 ', ' ChanChengQu ', '1', '50050', '50050010', ' chanchengqu ', ' 禅城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:06', '2017-02-14 12:15:06', '149', ' 南海区 ', ' NanHaiQu ', '1', '50050', '50050020', ' nanhaiqu ', ' 南海区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:06', '2017-02-14 12:15:06', '150', ' 顺德区 ', ' ShunDeQu ', '1', '50050', '50050030', ' shundequ ', ' 顺德区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:06', '2017-02-14 12:15:06', '151', ' 三水区 ', ' SanShuiQu ', '1', '50050', '50050040', ' sanshuiqu ', ' 三水区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:06', '2017-02-14 12:15:06', '152', ' 高明区 ', ' GaoMingQu ', '1', '50050', '50050050', ' gaomingqu ', ' 高明区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:06', '2017-02-14 12:15:06', '153', ' 新城区 ', ' XinChengQu ', '1', '50050', '50050060', ' xinchengqu ', ' 新城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:06', '2017-02-14 12:15:06', '154', ' 大沥 ', ' DaLi ', '1', '50050', '50050070', ' dali ', ' 大沥 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:07', '2017-02-14 12:15:07', '155', ' 黄岐 ', ' HuangQi ', '1', '50050', '50050080', ' huangqi ', ' 黄岐 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:07', '2017-02-14 12:15:07', '156', ' 西樵 ', ' XiQiao ', '1', '50050', '50050090', ' xiqiao ', ' 西樵 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:07', '2017-02-14 12:15:07', '157', ' 南庄 ', ' NanZhuang ', '1', '50050', '50050100', ' nanzhuang ', ' 南庄 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:07', '2017-02-14 12:15:07', '158', ' 惠州 ', ' HuiZhou ', '1', '50', '50060', ' huizhou ', ' 惠州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:07', '2017-02-14 12:15:07', '159', ' 清远 ', ' QingYuan ', '1', '50', '50070', ' qingyuan ', ' 清远 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:07', '2017-02-14 12:15:07', '160', ' 汕头 ', ' ShanTou ', '1', '50', '50080', ' shantou ', ' 汕头 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:07', '2017-02-14 12:15:07', '161', ' 深圳 ', ' ShenZhen ', '1', '50', '50090', ' shenzhen ', ' 深圳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:07', '2017-02-14 12:15:07', '162', ' 罗湖区 ', ' LuoHuQu ', '1', '50090', '50090010', ' luohu ', ' 罗湖区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:07', '2017-02-14 12:15:07', '163', ' 福田区 ', ' FuTianQu ', '1', '50090', '50090020', ' futian ', ' 福田区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:07', '2017-02-14 12:15:07', '164', ' 南山区 ', ' NanShanQu ', '1', '50090', '50090030', ' nanshan ', ' 南山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:07', '2017-02-14 12:15:07', '165', ' 宝安区 ', ' BaoAnQu ', '1', '50090', '50090040', ' anbao ', ' 宝安区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:07', '2017-02-14 12:15:07', '166', ' 龙岗区 ', ' LongGangQu ', '1', '50090', '50090050', ' longgang ', ' 龙岗区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:08', '2017-02-14 12:15:08', '167', ' 盐田区 ', ' YanTianQu ', '1', '50090', '50090060', ' yantian ', ' 盐田区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:08', '2017-02-14 12:15:08', '168', ' 光明新区 ', ' GuangMingXinQu ', '1', '50090', '50090070', ' guangmingxinqu ', ' 光明新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:08', '2017-02-14 12:15:08', '169', ' 坪山新区 ', ' PingShanXinQu ', '1', '50090', '50090080', ' pingshanxinqu ', ' 坪山新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:08', '2017-02-14 12:15:08', '170', ' 大鹏新区 ', ' DaPengXinQu ', '1', '50090', '50090090', ' dapengxinqu ', ' 大鹏新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:08', '2017-02-14 12:15:08', '171', ' 龙华新区 ', ' LongHuaXinQu ', '1', '50090', '50090100', ' longhuaxinqu ', ' 龙华新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:08', '2017-02-14 12:15:08', '172', ' 顺德 ', ' ShunDe ', '1', '50', '50100', ' shunde ', ' 顺德 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:08', '2017-02-14 12:15:08', '173', ' 湛江 ', ' ZhanJiang ', '1', '50', '50110', ' zhanjiang ', ' 湛江 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:08', '2017-02-14 12:15:08', '174', ' 肇庆 ', ' ZhaoQing ', '1', '50', '50120', ' zhaoqing ', ' 肇庆 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:08', '2017-02-14 12:15:08', '175', ' 中山 ', ' ZhongShan ', '1', '50', '50130', ' zhongshan ', ' 中山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:08', '2017-02-14 12:15:08', '176', ' 珠海 ', ' ZhuHai ', '1', '50', '50140', ' zhuhai ', ' 珠海 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:08', '2017-02-14 12:15:08', '177', ' 香洲区 ', ' XiangZhouQu ', '1', '50140', '50140010', ' xiangzhouqu ', ' 香洲区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:08', '2017-02-14 12:15:08', '178', ' 斗门区 ', ' DouMenQu ', '1', '50140', '50140020', ' doumenqu ', ' 斗门区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:08', '2017-02-14 12:15:08', '179', ' 金湾区 ', ' JinWanQu ', '1', '50140', '50140030', ' jinwanqu ', ' 金湾区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:09', '2017-02-14 12:15:09', '180', ' 横琴新区 ', ' HengQinXinQu ', '1', '50140', '50140040', ' hengqinxinqu ', ' 横琴新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:09', '2017-02-14 12:15:09', '181', ' 江门 ', ' JiangMen ', '1', '50', '50150', ' jiangmen ', ' 江门 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:09', '2017-02-14 12:15:09', '182', ' 阳江 ', ' YangJiang ', '1', '50', '50160', ' yangjiang ', ' 阳江 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:09', '2017-02-14 12:15:09', '183', ' 韶关 ', ' ShaoGuan ', '1', '50', '50170', ' shaoguan ', ' 韶关 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:09', '2017-02-14 12:15:09', '184', ' 茂名 ', ' MaoMing ', '1', '50', '50180', ' maoming ', ' 茂名 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:09', '2017-02-14 12:15:09', '185', ' 梅州 ', ' MeiZhou ', '1', '50', '50190', ' meizhou ', ' 梅州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:09', '2017-02-14 12:15:09', '186', ' 汕尾 ', ' ShanWei ', '1', '50', '50200', ' shanwei ', ' 汕尾 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:09', '2017-02-14 12:15:09', '187', ' 河源 ', ' HeYuan ', '1', '50', '50210', ' heyuan ', ' 河源 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:09', '2017-02-14 12:15:09', '188', ' 揭阳 ', ' JieYang ', '1', '50', '50220', ' jieyang ', ' 揭阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:09', '2017-02-14 12:15:09', '189', ' 云浮 ', ' YunFu ', '1', '50', '50230', ' yunfu ', ' 云浮 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:09', '2017-02-14 12:15:09', '190', ' 开平 ', ' KaiPing ', '1', '50', '50240', ' kaiping ', ' 开平 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:09', '2017-02-14 12:15:09', '191', ' 台山 ', ' TaiShan ', '1', '50', '50250', ' taishan ', ' 台山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:09', '2017-02-14 12:15:09', '192', ' 普宁 ', ' PuNing ', '1', '50', '50260', ' puning ', ' 普宁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:09', '2017-02-14 12:15:09', '193', ' 南沙 ', ' NanSha ', '1', '50', '50270', ' nansha ', ' 南沙 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '194', ' 龙川 ', ' LongChuan ', '1', '50', '50280', ' longchuan ', ' 龙川 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '195', ' 鹤山 ', ' HeShan ', '1', '50', '50290', ' heshan ', ' HESHAN ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '196', ' 江苏省 ', ' JiangSuSheng ', '0', '', '60', ' jiangsu ', ' 江苏省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '197', ' 南京 ', ' NanJing ', '1', '60', '60020', ' nanjing ', ' 南京 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '198', ' 玄武区 ', ' XuanWuQu ', '1', '60020', '60020010', ' xuanwu ', ' 玄武区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '199', ' 白下区 ', ' BaiXiaQu ', '1', '60020', '60020020', ' baixia ', ' 白下区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '200', ' 秦淮区 ', ' QinHuaiQu ', '1', '60020', '60020030', ' qinhuai ', ' 秦淮区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '201', ' 建邺区 ', ' JianYeQu ', '1', '60020', '60020040', ' jianye ', ' 建邺区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '202', ' 鼓楼区 ', ' GuLouQu ', '1', '60020', '60020050', ' gulou ', ' 鼓楼区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '203', ' 下关区 ', ' XiaGuanQu ', '1', '60020', '60020060', ' xiaguan ', ' 下关区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '204', ' 浦口区 ', ' PuKouQu ', '1', '60020', '60020070', ' pukou ', ' 浦口区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '205', ' 六合区 ', ' LiuHeQu ', '1', '60020', '60020080', ' liuhe ', ' 六合区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '206', ' 栖霞区 ', ' QiXiaQu ', '1', '60020', '60020090', ' qixia ', ' 栖霞区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '207', ' 雨花台 ', ' YuHuaTai ', '1', '60020', '60020100', ' yuhuatai ', ' 雨花台 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '208', ' 江宁区 ', ' JiangNingQu ', '1', '60020', '60020110', ' jiangning ', ' 江宁区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:10', '2017-02-14 12:15:10', '209', ' 溧水县 ', ' LiShuiXian ', '1', '60020', '60020120', ' lishui ', ' 溧水县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '210', ' 高淳县 ', ' GaoChunXian ', '1', '60020', '60020130', ' gaochun ', ' 高淳县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '211', ' 大厂区 ', ' DaChangQu ', '1', '60020', '60020140', ' dachangqu ', ' 大厂区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '212', ' 常熟 ', ' ChangShu ', '1', '60', '60030', ' changshu ', ' 常熟 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '213', ' 常州 ', ' ChangZhou ', '1', '60', '60040', ' changzhou ', ' 常州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '214', ' 天宁区 ', ' TianNingQu ', '1', '60040', '60040010', ' tianningqu ', ' 天宁区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '215', ' 钟楼区 ', ' ZhongLouQu ', '1', '60040', '60040020', ' zhonglouqu ', ' 钟楼区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '216', ' 戚墅堰 ', ' QiShuYan ', '1', '60040', '60040030', ' qishuyan ', ' 戚墅堰 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '217', ' 郊区 ', ' JiaoQu ', '1', '60040', '60040040', ' jiaoqu ', ' 郊区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '218', ' 新北区 ', ' XinBeiQu ', '1', '60040', '60040050', ' xinbeiqu ', ' 新北区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '219', ' 武进区 ', ' WuJinQu ', '1', '60040', '60040060', ' wujinqu ', ' 武进区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '220', ' 溧阳市 ', ' LiYangShi ', '1', '60040', '60040070', ' liyangshi ', ' 溧阳市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '221', ' 金坛市 ', ' JinTanShi ', '1', '60040', '60040080', ' jintanshi ', ' 金坛市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '222', ' 昆山 ', ' KunShan ', '1', '60', '60050', ' kunshan ', ' 昆山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '223', ' 连云港 ', ' LianYunGang ', '1', '60', '60060', ' lianyungang ', ' 连云港 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '224', ' 南通 ', ' NanTong ', '1', '60', '60070', ' nantong ', ' 南通 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:11', '2017-02-14 12:15:11', '225', ' 苏州 ', ' SuZhou ', '1', '60', '60080', ' suzhou ', ' 苏州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '226', ' 金阊区 ', ' JinChangQu ', '1', '60080', '60080010', ' jinchang ', ' 金阊区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '227', ' 沧浪区 ', ' CangLangQu ', '1', '60080', '60080020', ' canglang ', ' 沧浪区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '228', ' 平江区 ', ' PingJiangQu ', '1', '60080', '60080030', ' pingjiang ', ' 平江区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '229', ' 工业园 ', ' GongYeYuan ', '1', '60080', '60080040', ' gongyeyuan ', ' 工业园 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '230', ' 高新区 ', ' GaoXinQu ', '1', '60080', '60080050', ' gaoxin ', ' 高新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '231', ' 吴中区 ', ' WuZhongQu ', '1', '60080', '60080060', ' wuzhong ', ' 吴中区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '232', ' 相城区 ', ' XiangChengQu ', '1', '60080', '60080070', ' xiangcheng ', ' 相城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '233', ' 张家港 ', ' ZhangJiaGang ', '1', '60080', '60080080', ' zhangjiagang ', ' 张家港 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '234', ' 常熟市 ', ' ChangShuShi ', '1', '60080', '60080090', ' changshu ', ' 常熟市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '235', ' 太仓市 ', ' TaiCangShi ', '1', '60080', '60080100', ' taicang ', ' 太仓市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '236', ' 昆山市 ', ' KunShanShi ', '1', '60080', '60080110', ' kunshan ', ' 昆山市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '237', ' 吴江市 ', ' WuJiangShi ', '1', '60080', '60080120', ' wujiang ', ' 吴江市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '238', ' 虎丘区 ', ' HuQiuQu ', '1', '60080', '60080130', ' huqiuqu ', ' 虎丘区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '239', ' 玉山镇 ', ' YuShanZhen ', '1', '60080', '60080140', ' yushanzhen ', ' 玉山镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '240', ' 巴城镇 ', ' BaChengZhen ', '1', '60080', '60080150', ' bachengzhen ', ' 巴城镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:12', '2017-02-14 12:15:12', '241', ' 周市镇 ', ' ZhouShiZhen ', '1', '60080', '60080160', ' zhoushizhen ', ' 周市镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:13', '2017-02-14 12:15:13', '242', ' 陆家镇 ', ' LuJiaZhen ', '1', '60080', '60080170', ' lujiazhen ', ' 陆家镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:13', '2017-02-14 12:15:13', '243', ' 花桥镇 ', ' HuaQiaoZhen ', '1', '60080', '60080180', ' huaqiaozhen ', ' 花桥镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:13', '2017-02-14 12:15:13', '244', ' 淀山湖 ', ' DianShanHu ', '1', '60080', '60080190', ' dianshanhu ', ' 淀山湖 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:13', '2017-02-14 12:15:13', '245', ' 张浦镇 ', ' ZhangPuZhen ', '1', '60080', '60080200', ' zhangpuzhen ', ' 张浦镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:13', '2017-02-14 12:15:13', '246', ' 周庄镇 ', ' ZhouZhuangZhen ', '1', '60080', '60080210', ' zhouzhuangzhen ', ' 周庄镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:13', '2017-02-14 12:15:13', '247', ' 千灯镇 ', ' QianDengZhen ', '1', '60080', '60080220', ' qiandengzhen ', ' 千灯镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:13', '2017-02-14 12:15:13', '248', ' 锦溪镇 ', ' JinXiZhen ', '1', '60080', '60080230', ' jinxizhen ', ' 锦溪镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:13', '2017-02-14 12:15:13', '249', ' 开发区 ', ' KaiFaQu ', '1', '60080', '60080240', ' kaifaqu ', ' 开发区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:13', '2017-02-14 12:15:13', '250', ' 太仓 ', ' TaiCang ', '1', '60', '60090', ' taicang ', ' 太仓 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:13', '2017-02-14 12:15:13', '251', ' 无锡 ', ' WuXi ', '1', '60', '60100', ' wuxi ', ' 无锡 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:13', '2017-02-14 12:15:13', '252', ' 崇安区 ', ' ChongAnQu ', '1', '60100', '60100010', ' chonganqu ', ' 崇安区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:13', '2017-02-14 12:15:13', '253', ' 北塘区 ', ' BeiTangQu ', '1', '60100', '60100020', ' beitangqu ', ' 北塘区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:13', '2017-02-14 12:15:13', '254', ' 南长区 ', ' NanZhangQu ', '1', '60100', '60100030', ' nanchangqu ', ' 南长区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:14', '2017-02-14 12:15:14', '255', ' 锡山区 ', ' XiShanQu ', '1', '60100', '60100040', ' xishanqu ', ' 锡山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:14', '2017-02-14 12:15:14', '256', ' 惠山区 ', ' HuiShanQu ', '1', '60100', '60100050', ' huishanqu ', ' 惠山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:14', '2017-02-14 12:15:14', '257', ' 滨湖区 ', ' BinHuQu ', '1', '60100', '60100060', ' binhuqu ', ' 滨湖区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:14', '2017-02-14 12:15:14', '258', ' 新区 ', ' XinQu ', '1', '60100', '60100070', ' xinqu ', ' 新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:14', '2017-02-14 12:15:14', '259', ' 宜兴市 ', ' YiXingShi ', '1', '60100', '60100080', ' yixingshi ', ' 宜兴市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:14', '2017-02-14 12:15:14', '260', ' 江阴市 ', ' JiangYinShi ', '1', '60100', '60100090', ' jiangyinshi ', ' 江阴市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:14', '2017-02-14 12:15:14', '261', ' 徐州 ', ' XuZhou ', '1', '60', '60110', ' xuzhou ', ' 徐州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:14', '2017-02-14 12:15:14', '262', ' 扬州 ', ' YangZhou ', '1', '60', '60120', ' yangzhou ', ' 扬州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:14', '2017-02-14 12:15:14', '263', ' 镇江 ', ' ZhenJiang ', '1', '60', '60130', ' zhenjiang ', ' 镇江 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:14', '2017-02-14 12:15:14', '264', ' 淮安 ', ' HuaiAn ', '1', '60', '60140', ' huaian ', ' 淮安 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:14', '2017-02-14 12:15:14', '265', ' 盐城 ', ' YanCheng ', '1', '60', '60150', ' yancheng ', ' 盐城 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:14', '2017-02-14 12:15:14', '266', ' 泰州 ', ' TaiZhou ', '1', '60', '60160', ' taizhou0523 ', ' 泰州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:14', '2017-02-14 12:15:14', '267', ' 宿迁 ', ' SuQian ', '1', '60', '60170', ' suqian ', ' 宿迁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:15', '2017-02-14 12:15:15', '268', ' 张家港 ', ' ZhangJiaGang ', '1', '60', '60180', ' zhangjiagang ', ' 张家港 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:15', '2017-02-14 12:15:15', '269', ' 江阴 ', ' JiangYin ', '1', '60', '60190', ' jiangyin ', ' 江阴 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:15', '2017-02-14 12:15:15', '270', ' 丹阳 ', ' DanYang ', '1', '60', '60200', ' danyang ', ' 丹阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:15', '2017-02-14 12:15:15', '271', ' 溧阳 ', ' LiYang ', '1', '60', '60210', ' liyang ', ' 溧阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:15', '2017-02-14 12:15:15', '272', ' 泰兴 ', ' TaiXing ', '1', '60', '60220', ' taixing ', ' 泰兴 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:15', '2017-02-14 12:15:15', '273', ' 宜兴 ', ' YiXing ', '1', '60', '60230', ' yixing ', ' 宜兴 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:15', '2017-02-14 12:15:15', '274', ' 靖江 ', ' JingJiang ', '1', '60', '60240', ' jingjiang ', ' 靖江 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:15', '2017-02-14 12:15:15', '275', ' 句容 ', ' JuRong ', '1', '60', '60250', ' jurong ', ' 句容 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:15', '2017-02-14 12:15:15', '276', ' 如皋 ', ' RuGao ', '1', '60', '60260', ' rugao ', ' 如皋 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:15', '2017-02-14 12:15:15', '277', ' 扬中 ', ' YangZhong ', '1', '60', '60270', ' yangzhong ', ' 扬中 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:15', '2017-02-14 12:15:15', '278', ' 高邮 ', ' GaoYou ', '1', '60', '60280', ' gaoyou ', ' 高邮 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:15', '2017-02-14 12:15:15', '279', ' 启东 ', ' QiDong ', '1', '60', '60290', ' qidong ', ' 启东 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:16', '2017-02-14 12:15:16', '280', ' 盱眙 ', ' XuYi ', '1', '60', '60300', ' xuyi ', ' 盱眙 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:16', '2017-02-14 12:15:16', '281', ' 通州 ', ' TongZhou ', '1', '60', '60310', ' tongzhou ', ' 通州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:16', '2017-02-14 12:15:16', '282', ' 金湖 ', ' JinHu ', '1', '60', '60320', ' jinhu ', ' 金湖 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:16', '2017-02-14 12:15:16', '283', ' 浙江省 ', ' ZheJiangSheng ', '0', '', '70', ' zhejiang ', ' 浙江省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:16', '2017-02-14 12:15:16', '284', ' 杭州 ', ' HangZhou ', '1', '70', '70020', ' hangzhou ', ' 杭州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:16', '2017-02-14 12:15:16', '285', ' 上城区 ', ' ShangChengQu ', '1', '70020', '70020010', ' shangcheng ', ' 上城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:16', '2017-02-14 12:15:16', '286', ' 下城区 ', ' XiaChengQu ', '1', '70020', '70020020', ' xaicheng ', ' 下城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:16', '2017-02-14 12:15:16', '287', ' 拱墅区 ', ' GongShuQu ', '1', '70020', '70020030', ' gongshu ', ' 拱墅区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:16', '2017-02-14 12:15:16', '288', ' 西湖区 ', ' XiHuQu ', '1', '70020', '70020040', ' xihu ', ' 西湖区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:16', '2017-02-14 12:15:16', '289', ' 江干区 ', ' JiangGanQu ', '1', '70020', '70020050', ' jianggan ', ' 江干区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:16', '2017-02-14 12:15:16', '290', ' 滨江区 ', ' BinJiangQu ', '1', '70020', '70020060', ' binjiang ', ' 滨江区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:16', '2017-02-14 12:15:16', '291', ' 萧山区 ', ' XiaoShanQu ', '1', '70020', '70020070', ' xiaoshan ', ' 萧山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:16', '2017-02-14 12:15:16', '292', ' 余杭区 ', ' YuHangQu ', '1', '70020', '70020080', ' yuhang ', ' 余杭区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:16', '2017-02-14 12:15:16', '293', ' 临安市 ', ' LinAnShi ', '1', '70020', '70020090', ' linan ', ' 临安市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '294', ' 富阳区 ', ' FuYangQu ', '1', '70020', '70020100', ' fuyang ', ' 富阳区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '295', ' 建德市 ', ' JianDeShi ', '1', '70020', '70020110', ' jiande ', ' 建德市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '296', ' 桐庐县 ', ' TongLuXian ', '1', '70020', '70020120', ' tonglu ', ' 桐庐县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '297', ' 淳安县 ', ' ChunAnXian ', '1', '70020', '70020130', ' cunan ', ' 淳安县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '298', ' 市郊 ', ' ShiJiao ', '1', '70020', '70020140', ' shijiao ', ' 市郊 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '299', ' 宁波 ', ' NingBo ', '1', '70', '70030', ' ningbo ', ' 宁波 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '300', ' 海曙区 ', ' HaiShuQu ', '1', '70030', '70030010', ' haishuqu ', ' 海曙区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '301', ' 江东区 ', ' JiangDongQu ', '1', '70030', '70030020', ' jiangdongqu ', ' 江东区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '302', ' 江北区 ', ' JiangBeiQu ', '1', '70030', '70030030', ' jiangbeiqu ', ' 江北区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '303', ' 镇海区 ', ' ZhenHaiQu ', '1', '70030', '70030040', ' zhenhaiqu ', ' 镇海区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '304', ' 北仑区 ', ' BeiLunQu ', '1', '70030', '70030050', ' beilunqu ', ' 北仑区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '305', ' 鄞州区 ', ' YinZhouQu ', '1', '70030', '70030060', ' yinzhouqu ', ' 鄞州区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '306', ' 余姚市 ', ' YuYaoShi ', '1', '70030', '70030070', ' yuyaoshi ', ' 余姚市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '307', ' 慈溪市 ', ' CiXiShi ', '1', '70030', '70030080', ' cixishi ', ' 慈溪市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '308', ' 奉化市 ', ' FengHuaShi ', '1', '70030', '70030090', ' fenghuashi ', ' 奉化市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:17', '2017-02-14 12:15:17', '309', ' 象山县 ', ' XiangShanXian ', '1', '70030', '70030100', ' xiangshanxian ', ' 象山县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:18', '2017-02-14 12:15:18', '310', ' 宁海县 ', ' NingHaiXian ', '1', '70030', '70030110', ' ninghaixian ', ' 宁海县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:18', '2017-02-14 12:15:18', '311', ' 温州 ', ' WenZhou ', '1', '70', '70040', ' wenzhou ', ' 温州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:18', '2017-02-14 12:15:18', '312', ' 鹿城区 ', ' LuChengQu ', '1', '70040', '70040010', ' luchengqu ', ' 鹿城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:18', '2017-02-14 12:15:18', '313', ' 龙湾区 ', ' LongWanQu ', '1', '70040', '70040020', ' longwanqu ', ' 龙湾区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:18', '2017-02-14 12:15:18', '314', ' 瓯海区 ', ' OuHaiQu ', '1', '70040', '70040030', ' ouhaiqu ', ' 瓯海区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:18', '2017-02-14 12:15:18', '315', ' 瑞安市 ', ' RuiAnShi ', '1', '70040', '70040040', ' ruianshi ', ' 瑞安市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:18', '2017-02-14 12:15:18', '316', ' 乐清市 ', ' LeQingShi ', '1', '70040', '70040050', ' leqingshi ', ' 乐清市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:18', '2017-02-14 12:15:18', '317', ' 洞头县 ', ' DongTouXian ', '1', '70040', '70040060', ' dongtouxian ', ' 洞头县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:18', '2017-02-14 12:15:18', '318', ' 永嘉县 ', ' YongJiaXian ', '1', '70040', '70040070', ' yongjiaxian ', ' 永嘉县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:18', '2017-02-14 12:15:18', '319', ' 平阳县 ', ' PingYangXian ', '1', '70040', '70040080', ' pingyangxian ', ' 平阳县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:18', '2017-02-14 12:15:18', '320', ' 苍南县 ', ' CangNanXian ', '1', '70040', '70040090', ' cangnanxian ', ' 苍南县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:18', '2017-02-14 12:15:18', '321', ' 文成县 ', ' WenChengXian ', '1', '70040', '70040100', ' wenchengxian ', ' 文成县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:18', '2017-02-14 12:15:18', '322', ' 泰顺县 ', ' TaiShunXian ', '1', '70040', '70040110', ' taishunxian ', ' 泰顺县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:19', '2017-02-14 12:15:19', '323', ' 绍兴 ', ' ShaoXing ', '1', '70', '70050', ' shaoxing ', ' 绍兴 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:19', '2017-02-14 12:15:19', '324', ' 金华 ', ' JinHua ', '1', '70', '70060', ' jinhua ', ' 金华 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:19', '2017-02-14 12:15:19', '325', ' 台州 ', ' TaiZhou ', '1', '70', '70070', ' taizhou ', ' 台州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:19', '2017-02-14 12:15:19', '326', ' 湖州 ', ' HuZhou ', '1', '70', '70080', ' huzhou ', ' 湖州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:19', '2017-02-14 12:15:19', '327', ' 嘉兴 ', ' JiaXing ', '1', '70', '70090', ' jiaxing ', ' 嘉兴 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:19', '2017-02-14 12:15:19', '328', ' 衢州 ', ' QuZhou ', '1', '70', '70100', ' quzhou ', ' 衢州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:19', '2017-02-14 12:15:19', '329', ' 丽水 ', ' LiShui ', '1', '70', '70110', ' lishui ', ' 丽水 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:19', '2017-02-14 12:15:19', '330', ' 舟山 ', ' ZhouShan ', '1', '70', '70120', ' zhoushan ', ' 舟山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:19', '2017-02-14 12:15:19', '331', ' 义乌 ', ' YiWu ', '1', '70', '70130', ' yiwu ', ' 义乌 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:19', '2017-02-14 12:15:19', '332', ' 海宁 ', ' HaiNing ', '1', '70', '70140', ' haining ', ' 海宁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:19', '2017-02-14 12:15:19', '333', ' 玉环县 ', ' YuHuanXian ', '1', '70', '70150', ' yuhuanxian ', ' 玉环县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:19', '2017-02-14 12:15:19', '334', ' 平湖 ', ' PingHu ', '1', '70', '70160', ' pinghu ', ' 平湖 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:19', '2017-02-14 12:15:19', '335', ' 永康 ', ' YongKang ', '1', '70', '70170', ' yongkang ', ' 永康 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:19', '2017-02-14 12:15:19', '336', ' 东阳 ', ' DongYang ', '1', '70', '70180', ' dongyang ', ' 东阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:19', '2017-02-14 12:15:19', '337', ' 嘉善 ', ' JiaShan ', '1', '70', '70190', ' jiashan ', ' 嘉善 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:20', '2017-02-14 12:15:20', '338', ' 余姚 ', ' YuYao ', '1', '70', '70200', ' yuyao ', ' 余姚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:20', '2017-02-14 12:15:20', '339', ' 慈溪 ', ' CiXi ', '1', '70', '70210', ' cixi ', ' 慈溪 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:20', '2017-02-14 12:15:20', '340', ' 乐清 ', ' LeQing ', '1', '70', '70220', ' leqing ', ' 乐清 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:20', '2017-02-14 12:15:20', '341', ' 永嘉 ', ' YongJia ', '1', '70', '70230', ' yongjia ', ' 永嘉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:20', '2017-02-14 12:15:20', '342', ' 桐乡 ', ' TongXiang ', '1', '70', '70240', ' tongxiang ', ' 桐乡 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:20', '2017-02-14 12:15:20', '343', ' 瑞安 ', ' RuiAn ', '1', '70', '70250', ' ruian ', ' 瑞安 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:20', '2017-02-14 12:15:20', '344', ' 温岭 ', ' WenLing ', '1', '70', '70260', ' wenling ', ' 温岭 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:20', '2017-02-14 12:15:20', '345', ' 上虞 ', ' ShangYu ', '1', '70', '70270', ' shangyu ', ' 上虞 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:20', '2017-02-14 12:15:20', '346', ' 诸暨 ', ' ZhuJi ', '1', '70', '70280', ' zhuji ', ' 诸暨 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:20', '2017-02-14 12:15:20', '347', ' 宁海 ', ' NingHai ', '1', '70', '70290', ' ninghai ', ' 宁海 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:20', '2017-02-14 12:15:20', '348', ' 三门 ', ' SanMen ', '1', '70', '70300', ' sanmen ', ' 三门 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:20', '2017-02-14 12:15:20', '349', ' 德清 ', ' DeQing ', '1', '70', '70310', ' deqing ', ' 德清 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:20', '2017-02-14 12:15:20', '350', ' 象山 ', ' XiangShan ', '1', '70', '70320', ' xiangshan ', ' 象山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:21', '2017-02-14 12:15:21', '351', ' 方家山 ', ' FangJiaShan ', '1', '70', '70330', ' fangjiashan ', ' 方家山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:21', '2017-02-14 12:15:21', '352', ' 龙泉 ', ' LongQuan ', '1', '70', '70340', ' longquan ', ' 龙泉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:21', '2017-02-14 12:15:21', '353', ' 安徽省 ', ' AnHuiSheng ', '0', '', '80', ' anhui ', ' 安徽省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:21', '2017-02-14 12:15:21', '354', ' 合肥 ', ' HeFei ', '1', '80', '80020', ' hefei ', ' 合肥 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:21', '2017-02-14 12:15:21', '355', ' 庐阳区 ', ' LuYangQu ', '1', '80020', '80020010', ' luyangqu ', ' 庐阳区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:21', '2017-02-14 12:15:21', '356', ' 瑶海区 ', ' YaoHaiQu ', '1', '80020', '80020020', ' yaohaiqu ', ' 瑶海区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:21', '2017-02-14 12:15:21', '357', ' 蜀山区 ', ' ShuShanQu ', '1', '80020', '80020030', ' shushanqu ', ' 蜀山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:21', '2017-02-14 12:15:21', '358', ' 包河区 ', ' BaoHeQu ', '1', '80020', '80020040', ' baohequ ', ' 包河区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:21', '2017-02-14 12:15:21', '359', ' 长丰县 ', ' ZhangFengXian ', '1', '80020', '80020050', ' changfengxian ', ' 长丰县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:21', '2017-02-14 12:15:21', '360', ' 肥东县 ', ' FeiDongXian ', '1', '80020', '80020060', ' feidongxian ', ' 肥东县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:21', '2017-02-14 12:15:21', '361', ' 肥西县 ', ' FeiXiXian ', '1', '80020', '80020070', ' feixixian ', ' 肥西县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:21', '2017-02-14 12:15:21', '362', ' 新站区 ', ' XinZhanQu ', '1', '80020', '80020080', ' xinzhanqu ', ' 新站区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:21', '2017-02-14 12:15:21', '363', ' 经开区 ', ' JingKaiQu ', '1', '80020', '80020090', ' jingkaiqu ', ' 经开区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:22', '2017-02-14 12:15:22', '364', ' 高新区 ', ' GaoXinQu ', '1', '80020', '80020100', ' gaoxinqu ', ' 高新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:22', '2017-02-14 12:15:22', '365', ' 滨湖区 ', ' BinHuQu ', '1', '80020', '80020110', ' binhuxinqu ', ' 滨湖区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:22', '2017-02-14 12:15:22', '366', ' 北城区 ', ' BeiChengQu ', '1', '80020', '80020120', ' beichengxinqu ', ' 北城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:22', '2017-02-14 12:15:22', '367', ' 政务区 ', ' ZhengWuQu ', '1', '80020', '80020130', ' zhengwuxinqu ', ' 政务区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:22', '2017-02-14 12:15:22', '368', ' 安庆 ', ' AnQing ', '1', '80', '80030', ' anqing ', ' 安庆 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:22', '2017-02-14 12:15:22', '369', ' 蚌埠 ', ' BangBu ', '1', '80', '80040', ' bengbu ', ' 蚌埠 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:22', '2017-02-14 12:15:22', '370', ' 芜湖 ', ' WuHu ', '1', '80', '80050', ' wuhu ', ' 芜湖 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:22', '2017-02-14 12:15:22', '371', ' 淮南 ', ' HuaiNan ', '1', '80', '80060', ' huainan ', ' 淮南 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:22', '2017-02-14 12:15:22', '372', ' 马鞍山 ', ' MaAnShan ', '1', '80', '80070', ' maanshan ', ' 马鞍山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:22', '2017-02-14 12:15:22', '373', ' 淮北 ', ' HuaiBei ', '1', '80', '80080', ' huaibei ', ' 淮北 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:22', '2017-02-14 12:15:22', '374', ' 铜陵 ', ' TongLing ', '1', '80', '80090', ' tongling ', ' 铜陵 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:22', '2017-02-14 12:15:22', '375', ' 黄山 ', ' HuangShan ', '1', '80', '80100', ' huangshan ', ' 黄山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:22', '2017-02-14 12:15:22', '376', ' 滁州 ', ' ChuZhou ', '1', '80', '80110', ' chuzhou ', ' 滁州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:22', '2017-02-14 12:15:22', '377', ' 阜阳 ', ' FuYang ', '1', '80', '80120', ' fuyang ', ' 阜阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:23', '2017-02-14 12:15:23', '378', ' 宿州 ', ' SuZhou ', '1', '80', '80130', ' suzhou0557 ', ' 宿州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:23', '2017-02-14 12:15:23', '379', ' 六安 ', ' LiuAn ', '1', '80', '80140', ' liuan ', ' 六安 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:23', '2017-02-14 12:15:23', '380', ' 亳州 ', ' BoZhou ', '1', '80', '80150', ' bozhou ', ' 亳州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:23', '2017-02-14 12:15:23', '381', ' 池州 ', ' ChiZhou ', '1', '80', '80160', ' chizhou ', ' 池州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:23', '2017-02-14 12:15:23', '382', ' 宣城 ', ' XuanCheng ', '1', '80', '80170', ' xuancheng ', ' 宣城 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:23', '2017-02-14 12:15:23', '383', ' 巢湖 ', ' ChaoHu ', '1', '80', '80180', ' chaohu ', ' 巢湖 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:23', '2017-02-14 12:15:23', '384', ' 凤阳 ', ' FengYang ', '1', '80', '80190', ' fengyang ', ' 凤阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:23', '2017-02-14 12:15:23', '385', ' 广德 ', ' GuangDe ', '1', '80', '80200', ' guangde ', ' 广德 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:23', '2017-02-14 12:15:23', '386', ' 宿松 ', ' SuSong ', '1', '80', '80210', ' susong ', ' 宿松 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:23', '2017-02-14 12:15:23', '387', ' 福建省 ', ' FuJianSheng ', '0', '', '90', ' fujian ', ' 福建省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:23', '2017-02-14 12:15:23', '388', ' 福州 ', ' FuZhou ', '1', '90', '90020', ' fuzhou ', ' 福州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:23', '2017-02-14 12:15:23', '389', ' 鼓楼区 ', ' GuLouQu ', '1', '90020', '90020010', ' gulouqu ', ' 鼓楼区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '390', ' 台江区 ', ' TaiJiangQu ', '1', '90020', '90020020', ' taijiangqu ', ' 台江区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '391', ' 仓山区 ', ' CangShanQu ', '1', '90020', '90020030', ' cangshanqu ', ' 仓山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '392', ' 马尾区 ', ' MaWeiQu ', '1', '90020', '90020040', ' maweiqu ', ' 马尾区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '393', ' 晋安区 ', ' JinAnQu ', '1', '90020', '90020050', ' jinanqu ', ' 晋安区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '394', ' 福清市 ', ' FuQingShi ', '1', '90020', '90020060', ' fuqingshi ', ' 福清市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '395', ' 长乐市 ', ' ZhangLeShi ', '1', '90020', '90020070', ' changleshi ', ' 长乐市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '396', ' 闽侯县 ', ' MinHouXian ', '1', '90020', '90020080', ' minhouxian ', ' 闽侯县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '397', ' 连江县 ', ' LianJiangXian ', '1', '90020', '90020090', ' lianjiangxian ', ' 连江县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '398', ' 罗源县 ', ' LuoYuanXian ', '1', '90020', '90020100', ' luoyuanxian ', ' 罗源县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '399', ' 闽清县 ', ' MinQingXian ', '1', '90020', '90020110', ' minqingxian ', ' 闽清县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '400', ' 永泰县 ', ' YongTaiXian ', '1', '90020', '90020120', ' yongtaixian ', ' 永泰县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '401', ' 平潭县 ', ' PingTanXian ', '1', '90020', '90020130', ' pingtanxian ', ' 平潭县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '402', ' 泉州 ', ' QuanZhou ', '1', '90', '90030', ' quanzhou ', ' 泉州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '403', ' 厦门 ', ' ShaMen ', '1', '90', '90040', ' xiamen ', ' 厦门 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '404', ' 思明区 ', ' SiMingQu ', '1', '90040', '90040010', ' simingqu ', ' 思明区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '405', ' 海沧区 ', ' HaiCangQu ', '1', '90040', '90040020', ' haicangqu ', ' 海沧区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:24', '2017-02-14 12:15:24', '406', ' 湖里区 ', ' HuLiQu ', '1', '90040', '90040030', ' huliqu ', ' 湖里区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '407', ' 集美区 ', ' JiMeiQu ', '1', '90040', '90040040', ' jimeiqu ', ' 集美区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '408', ' 同安区 ', ' TongAnQu ', '1', '90040', '90040050', ' tonganqu ', ' 同安区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '409', ' 翔安区 ', ' XiangAnQu ', '1', '90040', '90040060', ' xianganqu ', ' 翔安区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '410', ' 漳州 ', ' ZhangZhou ', '1', '90', '90050', ' zhangzhou ', ' 漳州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '411', ' 莆田 ', ' PuTian ', '1', '90', '90060', ' putian ', ' 莆田 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '412', ' 三明 ', ' SanMing ', '1', '90', '90070', ' sanming ', ' 三明 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '413', ' 南平 ', ' NanPing ', '1', '90', '90080', ' nanping ', ' 南平 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '414', ' 龙岩 ', ' LongYan ', '1', '90', '90090', ' longyan ', ' 龙岩 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '415', ' 宁德 ', ' NingDe ', '1', '90', '90100', ' ningde ', ' 宁德 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '416', ' 泉港区 ', ' QuanGangQu ', '1', '90', '90110', ' quangangqu ', ' 泉港区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '417', ' 福安 ', ' FuAn ', '1', '90', '90120', ' fuan ', ' 福安 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '418', ' 晋江 ', ' JinJiang ', '1', '90', '90130', ' jinjiang ', ' 晋江 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '419', ' 甘肃省 ', ' GanSuSheng ', '0', '', '100', ' gansu ', ' 甘肃省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '420', ' 兰州 ', ' LanZhou ', '1', '100', '100020', ' lanzhou ', ' 兰州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '421', ' 皋兰县 ', ' GaoLanXian ', '1', '100020', '100020010', ' gaolanxian ', ' 皋兰县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:25', '2017-02-14 12:15:25', '422', ' 城关区 ', ' ChengGuanQu ', '1', '100020', '100020020', ' chengguanqu ', ' 城关区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:26', '2017-02-14 12:15:26', '423', ' 七里河 ', ' QiLiHe ', '1', '100020', '100020030', ' qilihe ', ' 七里河 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:26', '2017-02-14 12:15:26', '424', ' 西固区 ', ' XiGuQu ', '1', '100020', '100020040', ' xiguqu ', ' 西固区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:26', '2017-02-14 12:15:26', '425', ' 安宁区 ', ' AnNingQu ', '1', '100020', '100020050', ' anningqu ', ' 安宁区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:26', '2017-02-14 12:15:26', '426', ' 红古区 ', ' HongGuQu ', '1', '100020', '100020060', ' hongguqu ', ' 红古区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:26', '2017-02-14 12:15:26', '427', ' 永登县 ', ' YongDengXian ', '1', '100020', '100020070', ' yongdengxian ', ' 永登县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:26', '2017-02-14 12:15:26', '428', ' 榆中县 ', ' YuZhongXian ', '1', '100020', '100020080', ' yuzhongxian ', ' 榆中县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:26', '2017-02-14 12:15:26', '429', ' 嘉峪关 ', ' JiaYuGuan ', '1', '100', '100030', ' jiayuguan ', ' 嘉峪关 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:26', '2017-02-14 12:15:26', '430', ' 酒泉 ', ' JiuQuan ', '1', '100', '100040', ' jiuquan ', ' 酒泉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:26', '2017-02-14 12:15:26', '431', ' 金昌 ', ' JinChang ', '1', '100', '100050', ' jinchang ', ' 金昌 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:26', '2017-02-14 12:15:26', '432', ' 白银 ', ' BaiYin ', '1', '100', '100060', ' baiyin ', ' 白银 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:26', '2017-02-14 12:15:26', '433', ' 天水 ', ' TianShui ', '1', '100', '100070', ' tianshui ', ' 天水 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:26', '2017-02-14 12:15:26', '434', ' 张掖 ', ' ZhangYe ', '1', '100', '100080', ' zhangye ', ' 张掖 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:26', '2017-02-14 12:15:26', '435', ' 武威 ', ' WuWei ', '1', '100', '100090', ' wuwei ', ' 武威 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:26', '2017-02-14 12:15:26', '436', ' 定西 ', ' DingXi ', '1', '100', '100100', ' dingxi ', ' 定西 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:26', '2017-02-14 12:15:26', '437', ' 陇南 ', ' LongNan ', '1', '100', '100110', ' longnan ', ' 陇南 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:27', '2017-02-14 12:15:27', '438', ' 平凉 ', ' PingLiang ', '1', '100', '100120', ' pingliang ', ' 平凉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:27', '2017-02-14 12:15:27', '439', ' 庆阳 ', ' QingYang ', '1', '100', '100130', ' qingyang ', ' 庆阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:27', '2017-02-14 12:15:27', '440', ' 临夏 ', ' LinXia ', '1', '100', '100140', ' linxia ', ' 临夏 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:27', '2017-02-14 12:15:27', '441', ' 甘南 ', ' GanNan ', '1', '100', '100150', ' gannan ', ' 甘南 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:27', '2017-02-14 12:15:27', '442', ' 广西 ', ' GuangXi ', '0', '', '110', ' guangxi ', ' 广西 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:27', '2017-02-14 12:15:27', '443', ' 南宁 ', ' NanNing ', '1', '110', '110020', ' nanning ', ' 南宁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:27', '2017-02-14 12:15:27', '444', ' 邕宁区 ', ' YongNingQu ', '1', '110020', '110020010', ' yongningqu ', ' 邕宁区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:27', '2017-02-14 12:15:27', '445', ' 青秀区 ', ' QingXiuQu ', '1', '110020', '110020020', ' qingxiuqu ', ' 青秀区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:27', '2017-02-14 12:15:27', '446', ' 兴宁区 ', ' XingNingQu ', '1', '110020', '110020030', ' xingningqu ', ' 兴宁区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:27', '2017-02-14 12:15:27', '447', ' 良庆区 ', ' LiangQingQu ', '1', '110020', '110020040', ' liangqingqu ', ' 良庆区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:27', '2017-02-14 12:15:27', '448', ' 西乡塘 ', ' XiXiangTang ', '1', '110020', '110020050', ' xixiangtang ', ' 西乡塘 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:27', '2017-02-14 12:15:27', '449', ' 江南区 ', ' JiangNanQu ', '1', '110020', '110020060', ' jiangnanqu ', ' 江南区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:27', '2017-02-14 12:15:27', '450', ' 武鸣县 ', ' WuMingXian ', '1', '110020', '110020070', ' wumingxian ', ' 武鸣县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:28', '2017-02-14 12:15:28', '451', ' 隆安县 ', ' LongAnXian ', '1', '110020', '110020080', ' longanxian ', ' 隆安县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:28', '2017-02-14 12:15:28', '452', ' 马山县 ', ' MaShanXian ', '1', '110020', '110020090', ' mashanxian ', ' 马山县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:28', '2017-02-14 12:15:28', '453', ' 上林县 ', ' ShangLinXian ', '1', '110020', '110020100', ' shanglinxian ', ' 上林县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:28', '2017-02-14 12:15:28', '454', ' 宾阳县 ', ' BinYangXian ', '1', '110020', '110020110', ' binyangxian ', ' 宾阳县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:28', '2017-02-14 12:15:28', '455', ' 横县 ', ' HengXian ', '1', '110020', '110020120', ' hengxian ', ' 横县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:28', '2017-02-14 12:15:28', '456', ' 北海 ', ' BeiHai ', '1', '110', '110030', ' beihai ', ' 北海 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:28', '2017-02-14 12:15:28', '457', ' 桂林 ', ' GuiLin ', '1', '110', '110040', ' guilin ', ' 桂林 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:28', '2017-02-14 12:15:28', '458', ' 柳州 ', ' LiuZhou ', '1', '110', '110050', ' liuzhou ', ' 柳州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:28', '2017-02-14 12:15:28', '459', ' 玉林 ', ' YuLin ', '1', '110', '110060', ' yulin ', ' 玉林 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:28', '2017-02-14 12:15:28', '460', ' 梧州 ', ' WuZhou ', '1', '110', '110070', ' wuzhou ', ' 梧州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:28', '2017-02-14 12:15:28', '461', ' 崇左 ', ' ChongZuo ', '1', '110', '110080', ' chongzuo ', ' 崇左 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:28', '2017-02-14 12:15:28', '462', ' 来宾 ', ' LaiBin ', '1', '110', '110090', ' laibin ', ' 来宾 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:28', '2017-02-14 12:15:28', '463', ' 防城港 ', ' FangChengGang ', '1', '110', '110100', ' fangchenggang ', ' 防城港 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:29', '2017-02-14 12:15:29', '464', ' 百色 ', ' BaiSe ', '1', '110', '110110', ' baise ', ' 百色 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:29', '2017-02-14 12:15:29', '465', ' 钦州 ', ' QinZhou ', '1', '110', '110120', ' qinzhou ', ' 钦州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:29', '2017-02-14 12:15:29', '466', ' 贺州 ', ' HeZhou ', '1', '110', '110130', ' hezhou ', ' 贺州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:29', '2017-02-14 12:15:29', '467', ' 河池 ', ' HeChi ', '1', '110', '110140', ' hechi ', ' 河池 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:29', '2017-02-14 12:15:29', '468', ' 贵港 ', ' GuiGang ', '1', '110', '110150', ' guigang ', ' 贵港 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:29', '2017-02-14 12:15:29', '469', ' 贵州省 ', ' GuiZhouSheng ', '0', '', '120', ' guizhou ', ' 贵州省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:29', '2017-02-14 12:15:29', '470', ' 贵阳 ', ' GuiYang ', '1', '120', '120020', ' guiyang ', ' 贵阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:29', '2017-02-14 12:15:29', '471', ' 南明区 ', ' NanMingQu ', '1', '120020', '120020010', ' nanmingqu ', ' 南明区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:29', '2017-02-14 12:15:29', '472', ' 云岩区 ', ' YunYanQu ', '1', '120020', '120020020', ' yunyanqu ', ' 云岩区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:29', '2017-02-14 12:15:29', '473', ' 花溪区 ', ' HuaXiQu ', '1', '120020', '120020030', ' huaxiqu ', ' 花溪区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:29', '2017-02-14 12:15:29', '474', ' 乌当区 ', ' WuDangQu ', '1', '120020', '120020040', ' wudangqu ', ' 乌当区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:29', '2017-02-14 12:15:29', '475', ' 白云区 ', ' BaiYunQu ', '1', '120020', '120020050', ' baiyunqu ', ' 白云区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:29', '2017-02-14 12:15:29', '476', ' 小河区 ', ' XiaoHeQu ', '1', '120020', '120020060', ' xiaohequ ', ' 小河区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:29', '2017-02-14 12:15:29', '477', ' 金阳区 ', ' JinYangQu ', '1', '120020', '120020070', ' jinyangqu ', ' 金阳区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:30', '2017-02-14 12:15:30', '478', ' 新天园 ', ' XinTianYuan ', '1', '120020', '120020080', ' xintianyuan ', ' 新天园 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:30', '2017-02-14 12:15:30', '479', ' 清镇市 ', ' QingZhenShi ', '1', '120020', '120020090', ' qingzhenshi ', ' 清镇市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:30', '2017-02-14 12:15:30', '480', ' 开阳县 ', ' KaiYangXian ', '1', '120020', '120020100', ' kaiyangxian ', ' 开阳县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:30', '2017-02-14 12:15:30', '481', ' 修文县 ', ' XiuWenXian ', '1', '120020', '120020110', ' xiuwenxian ', ' 修文县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:30', '2017-02-14 12:15:30', '482', ' 息烽县 ', ' XiFengXian ', '1', '120020', '120020120', ' xifengxian ', ' 息烽县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:30', '2017-02-14 12:15:30', '483', ' 遵义 ', ' ZunYi ', '1', '120', '120030', ' zunyi ', ' 遵义 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:30', '2017-02-14 12:15:30', '484', ' 六盘水 ', ' LiuPanShui ', '1', '120', '120040', ' liupanshui ', ' 六盘水 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:30', '2017-02-14 12:15:30', '485', ' 安顺 ', ' AnShun ', '1', '120', '120050', ' anshun ', ' 安顺 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:30', '2017-02-14 12:15:30', '486', ' 毕节 ', ' BiJie ', '1', '120', '120060', ' bijie ', ' 毕节 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:30', '2017-02-14 12:15:30', '487', ' 铜仁 ', ' TongRen ', '1', '120', '120070', ' tongren ', ' 铜仁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:30', '2017-02-14 12:15:30', '488', ' 黔西南 ', ' QianXiNan ', '1', '120', '120080', ' qianxinan ', ' 黔西南 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:31', '2017-02-14 12:15:31', '489', ' 黔东南 ', ' QianDongNan ', '1', '120', '120090', ' qiandongnan ', ' 黔东南 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:31', '2017-02-14 12:15:31', '490', ' 黔南 ', ' QianNan ', '1', '120', '120100', ' qiannan ', ' 黔南 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:31', '2017-02-14 12:15:31', '491', ' 海南省 ', ' HaiNanSheng ', '0', '', '130', ' hainan ', ' 海南省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:31', '2017-02-14 12:15:31', '492', ' 海口 ', ' HaiKou ', '1', '130', '130020', ' haikou ', ' 海口 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:31', '2017-02-14 12:15:31', '493', ' 秀英区 ', ' XiuYingQu ', '1', '130020', '130020010', ' xiuyingqu ', ' 秀英区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:31', '2017-02-14 12:15:31', '494', ' 龙华区 ', ' LongHuaQu ', '1', '130020', '130020020', ' longhuaqu ', ' 龙华区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:31', '2017-02-14 12:15:31', '495', ' 琼山区 ', ' QiongShanQu ', '1', '130020', '130020030', ' qiongshanqu ', ' 琼山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:31', '2017-02-14 12:15:31', '496', ' 美兰区 ', ' MeiLanQu ', '1', '130020', '130020040', ' meilanqu ', ' 美兰区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:31', '2017-02-14 12:15:31', '497', ' 澄迈县 ', ' ChengMaiXian ', '1', '130020', '130020050', ' chengmaixian ', ' 澄迈县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:31', '2017-02-14 12:15:31', '498', ' 万宁市 ', ' WanNingShi ', '1', '130020', '130020060', ' wanningshi ', ' 万宁市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:31', '2017-02-14 12:15:31', '499', ' 文昌市 ', ' WenChangShi ', '1', '130020', '130020070', ' wenchangshi ', ' 文昌市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:31', '2017-02-14 12:15:31', '500', ' 儋州市 ', ' DanZhouShi ', '1', '130020', '130020080', ' danzhoushi ', ' 儋州市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:31', '2017-02-14 12:15:31', '501', ' 屯昌县 ', ' TunChangXian ', '1', '130020', '130020090', ' tunchangxian ', ' 屯昌县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:31', '2017-02-14 12:15:31', '502', ' 东方市 ', ' DongFangShi ', '1', '130020', '130020100', ' dongfangshi ', ' 东方市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:31', '2017-02-14 12:15:31', '503', ' 昌江县 ', ' ChangJiangXian ', '1', '130020', '130020110', ' changjiangxian ', ' 昌江县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '504', ' 乐东黎 ', ' LeDongLi ', '1', '130020', '130020120', ' ledongli ', ' 乐东黎 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '505', ' 临高县 ', ' LinGaoXian ', '1', '130020', '130020130', ' lingaoxian ', ' 临高县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '506', ' 琼海市 ', ' QiongHaiShi ', '1', '130020', '130020140', ' qionghaishi ', ' 琼海市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '507', ' 府城 ', ' FuCheng ', '1', '130020', '130020150', ' fucheng ', ' 府城 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '508', ' 三亚 ', ' SanYa ', '1', '130', '130030', ' sanya ', ' 三亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '509', ' 三沙 ', ' SanSha ', '1', '130', '130040', ' sansha ', ' 三沙 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '510', ' 文昌 ', ' WenChang ', '1', '130', '130060', ' wenchang ', ' 文昌 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '511', ' 琼海 ', ' QiongHai ', '1', '130', '130070', ' qionghai ', ' 琼海 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '512', ' 万宁 ', ' WanNing ', '1', '130', '130080', ' wanning ', ' 万宁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '513', ' 儋州 ', ' DanZhou ', '1', '130', '130090', ' danzhou ', ' 儋州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '514', ' 东方 ', ' DongFang ', '1', '130', '130100', ' dongfang ', ' 东方 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '515', ' 五指山 ', ' WuZhiShan ', '1', '130', '130110', ' wuzhishan ', ' 五指山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '516', ' 定安 ', ' DingAn ', '1', '130', '130120', ' dingan ', ' 定安 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '517', ' 屯昌 ', ' TunChang ', '1', '130', '130130', ' tunchang ', ' 屯昌 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '518', ' 澄迈 ', ' ChengMai ', '1', '130', '130140', ' chengmai ', ' 澄迈 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:32', '2017-02-14 12:15:32', '519', ' 临高 ', ' LinGao ', '1', '130', '130150', ' lingao ', ' 临高 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:33', '2017-02-14 12:15:33', '520', ' 琼中 ', ' QiongZhong ', '1', '130', '130160', ' qiongzhong ', ' 琼中 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:33', '2017-02-14 12:15:33', '521', ' 保亭 ', ' BaoTing ', '1', '130', '130170', ' baoting ', ' 保亭 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:33', '2017-02-14 12:15:33', '522', ' 白沙 ', ' BaiSha ', '1', '130', '130180', ' baisha ', ' 白沙 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:33', '2017-02-14 12:15:33', '523', ' 昌江 ', ' ChangJiang ', '1', '130', '130190', ' chengjiang ', ' 昌江 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:33', '2017-02-14 12:15:33', '524', ' 乐东 ', ' LeDong ', '1', '130', '130200', ' ledong ', ' 乐东 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:33', '2017-02-14 12:15:33', '525', ' 陵水 ', ' LingShui ', '1', '130', '130210', ' lingshui ', ' 陵水 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:33', '2017-02-14 12:15:33', '526', ' 河北省 ', ' HeBeiSheng ', '0', '', '140', ' hebei ', ' 河北省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:33', '2017-02-14 12:15:33', '527', ' 石家庄 ', ' ShiJiaZhuang ', '1', '140', '140020', ' shijiazhuang ', ' 石家庄 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:33', '2017-02-14 12:15:33', '528', ' 长安区 ', ' ZhangAnQu ', '1', '140020', '140020010', ' changanqu ', ' 长安区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:33', '2017-02-14 12:15:33', '529', ' 桥东区 ', ' QiaoDongQu ', '1', '140020', '140020020', ' qiaodongqu ', ' 桥东区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:33', '2017-02-14 12:15:33', '530', ' 桥西区 ', ' QiaoXiQu ', '1', '140020', '140020030', ' qiaoxiqu ', ' 桥西区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:33', '2017-02-14 12:15:33', '531', ' 新华区 ', ' XinHuaQu ', '1', '140020', '140020040', ' xinhuaqu ', ' 新华区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:33', '2017-02-14 12:15:33', '532', ' 裕华区 ', ' YuHuaQu ', '1', '140020', '140020050', ' yuhuaqu ', ' 裕华区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:33', '2017-02-14 12:15:33', '533', ' 井陉矿 ', ' JingXingKuang ', '1', '140020', '140020060', ' jingxingkuang ', ' 井陉矿 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:33', '2017-02-14 12:15:33', '534', ' 高新区 ', ' GaoXinQu ', '1', '140020', '140020070', ' gaoxinqu ', ' 高新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:34', '2017-02-14 12:15:34', '535', ' 辛集市 ', ' XinJiShi ', '1', '140020', '140020080', ' xinjishi ', ' 辛集市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:34', '2017-02-14 12:15:34', '536', ' 藁城市 ', ' GaoChengShi ', '1', '140020', '140020090', ' gaochengshi ', ' 藁城市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:34', '2017-02-14 12:15:34', '537', ' 晋州市 ', ' JinZhouShi ', '1', '140020', '140020100', ' jinzhoushi ', ' 晋州市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:34', '2017-02-14 12:15:34', '538', ' 新乐市 ', ' XinLeShi ', '1', '140020', '140020110', ' xinleshi ', ' 新乐市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:34', '2017-02-14 12:15:34', '539', ' 鹿泉市 ', ' LuQuanShi ', '1', '140020', '140020120', ' luquanshi ', ' 鹿泉市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:34', '2017-02-14 12:15:34', '540', ' 井陉县 ', ' JingXingXian ', '1', '140020', '140020130', ' jingxingxian ', ' 井陉县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:34', '2017-02-14 12:15:34', '541', ' 正定县 ', ' ZhengDingXian ', '1', '140020', '140020140', ' zhengdingxian ', ' 正定县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:34', '2017-02-14 12:15:34', '542', ' 栾城县 ', ' LuanChengXian ', '1', '140020', '140020150', ' luanchengxian ', ' 栾城县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:34', '2017-02-14 12:15:34', '543', ' 行唐县 ', ' XingTangXian ', '1', '140020', '140020160', ' xingtangxian ', ' 行唐县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:34', '2017-02-14 12:15:34', '544', ' 灵寿县 ', ' LingShouXian ', '1', '140020', '140020170', ' lingshouxian ', ' 灵寿县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:34', '2017-02-14 12:15:34', '545', ' 高邑县 ', ' GaoYiXian ', '1', '140020', '140020180', ' gaoyixian ', ' 高邑县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:34', '2017-02-14 12:15:34', '546', ' 深泽县 ', ' ShenZeXian ', '1', '140020', '140020190', ' shenzexian ', ' 深泽县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:34', '2017-02-14 12:15:34', '547', ' 赞皇县 ', ' ZanHuangXian ', '1', '140020', '140020200', ' zanhuangxian ', ' 赞皇县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:34', '2017-02-14 12:15:34', '548', ' 无极县 ', ' WuJiXian ', '1', '140020', '140020210', ' wujixian ', ' 无极县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:35', '2017-02-14 12:15:35', '549', ' 平山县 ', ' PingShanXian ', '1', '140020', '140020220', ' pingshanxian ', ' 平山县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:35', '2017-02-14 12:15:35', '550', ' 元氏县 ', ' YuanShiXian ', '1', '140020', '140020230', ' yuanshixian ', ' 元氏县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:35', '2017-02-14 12:15:35', '551', ' 赵县 ', ' ZhaoXian ', '1', '140020', '140020240', ' zhaoxian ', ' 赵县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:35', '2017-02-14 12:15:35', '552', ' 保定 ', ' BaoDing ', '1', '140', '140030', ' baoding ', ' 保定 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:35', '2017-02-14 12:15:35', '553', ' 承德 ', ' ChengDe ', '1', '140', '140040', ' chengde ', ' 承德 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:35', '2017-02-14 12:15:35', '554', ' 邯郸 ', ' HanDan ', '1', '140', '140050', ' handan ', ' 邯郸 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:35', '2017-02-14 12:15:35', '555', ' 廊坊 ', ' LangFang ', '1', '140', '140060', ' langfang ', ' 廊坊 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:35', '2017-02-14 12:15:35', '556', ' 秦皇岛 ', ' QinHuangDao ', '1', '140', '140070', ' qinhuangdao ', ' 秦皇岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:35', '2017-02-14 12:15:35', '557', ' 唐山 ', ' TangShan ', '1', '140', '140080', ' tangshan ', ' 唐山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:35', '2017-02-14 12:15:35', '558', ' 张家口 ', ' ZhangJiaKou ', '1', '140', '140090', ' zhangjiakou ', ' 张家口 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:35', '2017-02-14 12:15:35', '559', ' 邢台 ', ' XingTai ', '1', '140', '140100', ' xingtai ', ' 邢台 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:35', '2017-02-14 12:15:35', '560', ' 沧州 ', ' CangZhou ', '1', '140', '140110', ' cangzhou ', ' 沧州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:36', '2017-02-14 12:15:36', '561', ' 衡水 ', ' HengShui ', '1', '140', '140120', ' hengshui ', ' 衡水 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:36', '2017-02-14 12:15:36', '562', ' 燕郊 ', ' YanJiao ', '1', '140', '140130', ' yanjiao ', ' 燕郊 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:36', '2017-02-14 12:15:36', '563', ' 固安 ', ' GuAn ', '1', '140', '140140', ' guan ', ' 固安 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:36', '2017-02-14 12:15:36', '564', ' 遵化 ', ' ZunHua ', '1', '140', '140150', ' zunhua ', ' 遵化 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:36', '2017-02-14 12:15:36', '565', ' 香河 ', ' XiangHe ', '1', '140', '140160', ' xianghe ', ' 香河 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:36', '2017-02-14 12:15:36', '566', ' 三河 ', ' SanHe ', '1', '140', '140170', ' sanhe ', ' 三河 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:36', '2017-02-14 12:15:36', '567', ' 河南省 ', ' HeNanSheng ', '0', '', '150', ' henan ', ' 河南省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:36', '2017-02-14 12:15:36', '568', ' 郑州 ', ' ZhengZhou ', '1', '150', '150020', ' zhengzhou ', ' 郑州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:36', '2017-02-14 12:15:36', '569', ' 金水区 ', ' JinShuiQu ', '1', '150020', '150020010', ' jinshuiqu ', ' 金水区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:36', '2017-02-14 12:15:36', '570', ' 邙山区 ', ' MangShanQu ', '1', '150020', '150020020', ' mangshanqu ', ' 邙山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:36', '2017-02-14 12:15:36', '571', ' 二七区 ', ' ErQiQu ', '1', '150020', '150020030', ' erqiqu ', ' 二七区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:36', '2017-02-14 12:15:36', '572', ' 管城区 ', ' GuanChengQu ', '1', '150020', '150020040', ' guanchengqu ', ' 管城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:36', '2017-02-14 12:15:36', '573', ' 中原区 ', ' ZhongYuanQu ', '1', '150020', '150020050', ' zhongyuanqu ', ' 中原区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:37', '2017-02-14 12:15:37', '574', ' 上街区 ', ' ShangJieQu ', '1', '150020', '150020060', ' shangjiequ ', ' 上街区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:37', '2017-02-14 12:15:37', '575', ' 惠济区 ', ' HuiJiQu ', '1', '150020', '150020070', ' huijiqu ', ' 惠济区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:37', '2017-02-14 12:15:37', '576', ' 郑东区 ', ' ZhengDongQu ', '1', '150020', '150020080', ' zhengdongqu ', ' 郑东区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:37', '2017-02-14 12:15:37', '577', ' 经济技术 ', ' JingJiJiShu ', '1', '150020', '150020090', ' jingjijishu ', ' 经济技术 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:37', '2017-02-14 12:15:37', '578', ' 高新区 ', ' GaoXinQu ', '1', '150020', '150020100', ' gaoxinqu ', ' 高新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:37', '2017-02-14 12:15:37', '579', ' 加工区 ', ' JiaGongQu ', '1', '150020', '150020110', ' jiagongqu ', ' 加工区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:37', '2017-02-14 12:15:37', '580', ' 巩义市 ', ' GongYiShi ', '1', '150020', '150020120', ' gongyishi ', ' 巩义市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:37', '2017-02-14 12:15:37', '581', ' 荥阳市 ', ' XingYangShi ', '1', '150020', '150020130', ' yingyangshi ', ' 荥阳市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:37', '2017-02-14 12:15:37', '582', ' 新密市 ', ' XinMiShi ', '1', '150020', '150020140', ' xinmishi ', ' 新密市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:37', '2017-02-14 12:15:37', '583', ' 新郑市 ', ' XinZhengShi ', '1', '150020', '150020150', ' xinzhengshi ', ' 新郑市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:37', '2017-02-14 12:15:37', '584', ' 登封市 ', ' DengFengShi ', '1', '150020', '150020160', ' dengfengshi ', ' 登封市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:37', '2017-02-14 12:15:37', '585', ' 中牟县 ', ' ZhongMouXian ', '1', '150020', '150020170', ' zhongmouxian ', ' 中牟县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:37', '2017-02-14 12:15:37', '586', ' 开封 ', ' KaiFeng ', '1', '150', '150030', ' kaifeng ', ' 开封 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:37', '2017-02-14 12:15:37', '587', ' 洛阳 ', ' LuoYang ', '1', '150', '150040', ' luoyang ', ' 洛阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '588', ' 商丘 ', ' ShangQiu ', '1', '150', '150050', ' shangqiu ', ' 商丘 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '589', ' 安阳 ', ' AnYang ', '1', '150', '150060', ' anyang ', ' 安阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '590', ' 平顶山 ', ' PingDingShan ', '1', '150', '150070', ' pingdingshan ', ' 平顶山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '591', ' 新乡 ', ' XinXiang ', '1', '150', '150080', ' xinxiang ', ' 新乡 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '592', ' 焦作 ', ' JiaoZuo ', '1', '150', '150090', ' jiaozuo ', ' 焦作 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '593', ' 濮阳 ', ' PuYang ', '1', '150', '150100', ' puyang ', ' 濮阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '594', ' 许昌 ', ' XuChang ', '1', '150', '150110', ' xuchang ', ' 许昌 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '595', ' 漯河 ', ' TaHe ', '1', '150', '150120', ' luohe ', ' 漯河 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '596', ' 三门峡 ', ' SanMenXia ', '1', '150', '150130', ' shanmenxia ', ' 三门峡 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '597', ' 鹤壁 ', ' HeBi ', '1', '150', '150140', ' hebi ', ' 鹤壁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '598', ' 周口 ', ' ZhouKou ', '1', '150', '150150', ' zhoukou ', ' 周口 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '599', ' 驻马店 ', ' ZhuMaDian ', '1', '150', '150160', ' zhumadian ', ' 驻马店 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '600', ' 南阳 ', ' NanYang ', '1', '150', '150170', ' nanyang ', ' 南阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '601', ' 信阳 ', ' XinYang ', '1', '150', '150180', ' xinyang ', ' 信阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '602', ' 济源 ', ' JiYuan ', '1', '150', '150190', ' jiyuan ', ' 济源 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:38', '2017-02-14 12:15:38', '603', ' 西平 ', ' XiPing ', '1', '150', '150200', ' xiping ', ' 西平 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:39', '2017-02-14 12:15:39', '604', ' 长葛 ', ' ZhangGe ', '1', '150', '150210', ' changge ', ' 长葛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:39', '2017-02-14 12:15:39', '605', ' 黑龙江省 ', ' HeiLongJiangSheng ', '0', '', '160', ' heilongjiang ', ' 黑龙江省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:39', '2017-02-14 12:15:39', '606', ' 哈尔滨 ', ' HaErBin ', '1', '160', '160020', ' haerbin ', ' 哈尔滨 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:39', '2017-02-14 12:15:39', '607', ' 道里区 ', ' DaoLiQu ', '1', '160020', '160020010', ' daoliqu ', ' 道里区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:39', '2017-02-14 12:15:39', '608', ' 南岗区 ', ' NanGangQu ', '1', '160020', '160020020', ' nangangqu ', ' 南岗区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:39', '2017-02-14 12:15:39', '609', ' 动力区 ', ' DongLiQu ', '1', '160020', '160020030', ' dongliqu ', ' 动力区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:39', '2017-02-14 12:15:39', '610', ' 平房区 ', ' PingFangQu ', '1', '160020', '160020040', ' pingfangqu ', ' 平房区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:39', '2017-02-14 12:15:39', '611', ' 香坊区 ', ' XiangFangQu ', '1', '160020', '160020050', ' xiangfangqu ', ' 香坊区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:39', '2017-02-14 12:15:39', '612', ' 太平区 ', ' TaiPingQu ', '1', '160020', '160020060', ' taipingqu ', ' 太平区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:39', '2017-02-14 12:15:39', '613', ' 道外区 ', ' DaoWaiQu ', '1', '160020', '160020070', ' daowaiqu ', ' 道外区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:39', '2017-02-14 12:15:39', '614', ' 阿城市 ', ' AChengShi ', '1', '160020', '160020080', ' achengshi ', ' 阿城市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:39', '2017-02-14 12:15:39', '615', ' 呼兰区 ', ' HuLanQu ', '1', '160020', '160020090', ' hulanqu ', ' 呼兰区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:39', '2017-02-14 12:15:39', '616', ' 松北区 ', ' SongBeiQu ', '1', '160020', '160020100', ' songbeiqu ', ' 松北区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:39', '2017-02-14 12:15:39', '617', ' 尚志市 ', ' ShangZhiShi ', '1', '160020', '160020110', ' shangzhishi ', ' 尚志市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:40', '2017-02-14 12:15:40', '618', ' 双城市 ', ' ShuangChengShi ', '1', '160020', '160020120', ' shuangchengshi ', ' 双城市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:40', '2017-02-14 12:15:40', '619', ' 五常市 ', ' WuChangShi ', '1', '160020', '160020130', ' wuchangshi ', ' 五常市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:40', '2017-02-14 12:15:40', '620', ' 方正县 ', ' FangZhengXian ', '1', '160020', '160020140', ' fangzhengxian ', ' 方正县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:40', '2017-02-14 12:15:40', '621', ' 宾县 ', ' BinXian ', '1', '160020', '160020150', ' binxian ', ' 宾县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:40', '2017-02-14 12:15:40', '622', ' 依兰县 ', ' YiLanXian ', '1', '160020', '160020160', ' yilanxian ', ' 依兰县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:40', '2017-02-14 12:15:40', '623', ' 巴彦县 ', ' BaYanXian ', '1', '160020', '160020170', ' bayanxian ', ' 巴彦县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:40', '2017-02-14 12:15:40', '624', ' 通河县 ', ' TongHeXian ', '1', '160020', '160020180', ' tonghexian ', ' 通河县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:40', '2017-02-14 12:15:40', '625', ' 木兰县 ', ' MuLanXian ', '1', '160020', '160020190', ' mulanxian ', ' 木兰县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:40', '2017-02-14 12:15:40', '626', ' 延寿县 ', ' YanShouXian ', '1', '160020', '160020200', ' yanshouxian ', ' 延寿县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:40', '2017-02-14 12:15:40', '627', ' 大庆 ', ' DaQing ', '1', '160', '160030', ' daqing ', ' 大庆 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:40', '2017-02-14 12:15:40', '628', ' 佳木斯 ', ' JiaMuSi ', '1', '160', '160040', ' jiamusi ', ' 佳木斯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:40', '2017-02-14 12:15:40', '629', ' 牡丹江 ', ' MuDanJiang ', '1', '160', '160050', ' mudanjiang ', ' 牡丹江 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:40', '2017-02-14 12:15:40', '630', ' 齐齐哈尔 ', ' QiQiHaEr ', '1', '160', '160060', ' qiqihaer ', ' 齐齐哈尔 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:40', '2017-02-14 12:15:40', '631', ' 鸡西 ', ' JiXi ', '1', '160', '160070', ' jixi ', ' 鸡西 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:40', '2017-02-14 12:15:40', '632', ' 鹤岗 ', ' HeGang ', '1', '160', '160080', ' hegang ', ' 鹤岗 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:41', '2017-02-14 12:15:41', '633', ' 双鸭山 ', ' ShuangYaShan ', '1', '160', '160090', ' shuangyashan ', ' 双鸭山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:41', '2017-02-14 12:15:41', '634', ' 伊春 ', ' YiChun ', '1', '160', '160100', ' yichun ', ' 伊春 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:41', '2017-02-14 12:15:41', '635', ' 七台河 ', ' QiTaiHe ', '1', '160', '160110', ' qitaihe ', ' 七台河 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:41', '2017-02-14 12:15:41', '636', ' 黑河 ', ' HeiHe ', '1', '160', '160120', ' heihe ', ' 黑河 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:41', '2017-02-14 12:15:41', '637', ' 绥化 ', ' SuiHua ', '1', '160', '160130', ' suihua ', ' 绥化 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:41', '2017-02-14 12:15:41', '638', ' 大兴安岭 ', ' DaXingAnLing ', '1', '160', '160140', ' daxinganling ', ' 大兴安岭 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:41', '2017-02-14 12:15:41', '639', ' 安达 ', ' AnDa ', '1', '160', '160150', ' anda ', ' 安达 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:41', '2017-02-14 12:15:41', '640', ' 双城 ', ' ShuangCheng ', '1', '160', '160160', ' shuangcheng ', ' 双城 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:41', '2017-02-14 12:15:41', '641', ' 尚志 ', ' ShangZhi ', '1', '160', '160170', ' shangzhi ', ' 尚志 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:41', '2017-02-14 12:15:41', '642', ' 绥芬河 ', ' SuiFenHe ', '1', '160', '160180', ' suifenghe ', ' 绥芬河 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:41', '2017-02-14 12:15:41', '643', ' 肇东 ', ' ZhaoDong ', '1', '160', '160190', ' zhaodong ', ' 肇东 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:41', '2017-02-14 12:15:41', '644', ' 湖北省 ', ' HuBeiSheng ', '0', '', '170', ' hubei ', ' 湖北省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:41', '2017-02-14 12:15:41', '645', ' 武汉 ', ' WuHan ', '1', '170', '170020', ' wuhan ', ' 武汉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:42', '2017-02-14 12:15:42', '646', ' 江岸区 ', ' JiangAnQu ', '1', '170020', '170020010', ' jiangan ', ' 江岸区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:42', '2017-02-14 12:15:42', '647', ' 江汉区 ', ' JiangHanQu ', '1', '170020', '170020020', ' jianghan ', ' 江汉区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:42', '2017-02-14 12:15:42', '648', ' 硚口区 ', ' QiaoKouQu ', '1', '170020', '170020030', ' qiaokou ', ' 硚口区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:42', '2017-02-14 12:15:42', '649', ' 汉阳区 ', ' HanYangQu ', '1', '170020', '170020040', ' hanyang ', ' 汉阳区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:42', '2017-02-14 12:15:42', '650', ' 武昌区 ', ' WuChangQu ', '1', '170020', '170020050', ' wuchang ', ' 武昌区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:42', '2017-02-14 12:15:42', '651', ' 青山区 ', ' QingShanQu ', '1', '170020', '170020060', ' qingshan ', ' 青山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:42', '2017-02-14 12:15:42', '652', ' 洪山区 ', ' HongShanQu ', '1', '170020', '170020070', ' hongshan ', ' 洪山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:42', '2017-02-14 12:15:42', '653', ' 蔡甸区 ', ' CaiDianQu ', '1', '170020', '170020080', ' caidian ', ' 蔡甸区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:42', '2017-02-14 12:15:42', '654', ' 江夏区 ', ' JiangXiaQu ', '1', '170020', '170020090', ' jiangxia ', ' 江夏区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:42', '2017-02-14 12:15:42', '655', ' 黄陂区 ', ' HuangBeiQu ', '1', '170020', '170020100', ' huangpi ', ' 黄陂区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:42', '2017-02-14 12:15:42', '656', ' 新洲区 ', ' XinZhouQu ', '1', '170020', '170020110', ' xinzhou ', ' 新洲区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:42', '2017-02-14 12:15:42', '657', ' 东西湖 ', ' DongXiHu ', '1', '170020', '170020120', ' dongxihu ', ' 东西湖 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:42', '2017-02-14 12:15:42', '658', ' 汉南区 ', ' HanNanQu ', '1', '170020', '170020130', ' hannan ', ' 汉南区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:43', '2017-02-14 12:15:43', '659', ' 开发区 ', ' KaiFaQu ', '1', '170020', '170020140', ' kaifaqu ', ' 开发区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:43', '2017-02-14 12:15:43', '660', ' 十堰 ', ' ShiYan ', '1', '170', '170030', ' shiyan ', ' 十堰 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:43', '2017-02-14 12:15:43', '661', ' 襄阳 ', ' XiangYang ', '1', '170', '170040', ' xiangyang ', ' 襄阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:43', '2017-02-14 12:15:43', '662', ' 宜昌 ', ' YiChang ', '1', '170', '170050', ' yichang ', ' 宜昌 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:43', '2017-02-14 12:15:43', '663', ' 潜江 ', ' QianJiang ', '1', '170', '170060', ' qianjiang ', ' 潜江 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:43', '2017-02-14 12:15:43', '664', ' 荆门 ', ' JingMen ', '1', '170', '170070', ' jingmen ', ' 荆门 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:43', '2017-02-14 12:15:43', '665', ' 荆州 ', ' JingZhou ', '1', '170', '170080', ' jingzhou ', ' 荆州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:43', '2017-02-14 12:15:43', '666', ' 黄石 ', ' HuangShi ', '1', '170', '170090', ' huangshi ', ' 黄石 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:43', '2017-02-14 12:15:43', '667', ' 鄂州 ', ' EZhou ', '1', '170', '170100', ' ezhou ', ' 鄂州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:43', '2017-02-14 12:15:43', '668', ' 黄冈 ', ' HuangGang ', '1', '170', '170110', ' huanggang ', ' 黄冈 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:43', '2017-02-14 12:15:43', '669', ' 孝感 ', ' XiaoGan ', '1', '170', '170120', ' xiaogan ', ' 孝感 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:43', '2017-02-14 12:15:43', '670', ' 咸宁 ', ' XianNing ', '1', '170', '170130', ' xianning ', ' 咸宁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:43', '2017-02-14 12:15:43', '671', ' 随州 ', ' SuiZhou ', '1', '170', '170140', ' suizhou ', ' 随州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:44', '2017-02-14 12:15:44', '672', ' 仙桃 ', ' XianTao ', '1', '170', '170150', ' xiantao ', ' 仙桃 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:44', '2017-02-14 12:15:44', '673', ' 天门 ', ' TianMen ', '1', '170', '170160', ' tianmen ', ' 天门 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:44', '2017-02-14 12:15:44', '674', ' 神农架 ', ' ShenNongJia ', '1', '170', '170170', ' shennongjia ', ' 神农架 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:44', '2017-02-14 12:15:44', '675', ' 恩施 ', ' EnShi ', '1', '170', '170180', ' enshi ', ' 恩施 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:44', '2017-02-14 12:15:44', '676', ' 公安 ', ' GongAn ', '1', '170', '170190', ' gongan ', ' 公安 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:44', '2017-02-14 12:15:44', '677', ' 武穴 ', ' WuXue ', '1', '170', '170200', ' wuxue ', ' 武穴 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:44', '2017-02-14 12:15:44', '678', ' 宜城 ', ' YiCheng ', '1', '170', '170210', ' yicheng ', ' 宜城 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:44', '2017-02-14 12:15:44', '679', ' 湖南省 ', ' HuNanSheng ', '0', '', '180', ' hunan ', ' 湖南省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:44', '2017-02-14 12:15:44', '680', ' 长沙 ', ' ChangSha ', '1', '180', '180020', ' changsha ', ' 长沙 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:44', '2017-02-14 12:15:44', '681', ' 岳麓区 ', ' YueLuQu ', '1', '180020', '180020010', ' yueluqu ', ' 岳麓区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:44', '2017-02-14 12:15:44', '682', ' 芙蓉区 ', ' FuRongQu ', '1', '180020', '180020020', ' furongqu ', ' 芙蓉区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:44', '2017-02-14 12:15:44', '683', ' 天心区 ', ' TianXinQu ', '1', '180020', '180020030', ' tianxinqu ', ' 天心区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:44', '2017-02-14 12:15:44', '684', ' 开福区 ', ' KaiFuQu ', '1', '180020', '180020040', ' kaifuqu ', ' 开福区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:44', '2017-02-14 12:15:44', '685', ' 雨花区 ', ' YuHuaQu ', '1', '180020', '180020050', ' yuhuaqu ', ' 雨花区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:45', '2017-02-14 12:15:45', '686', ' 开发区 ', ' KaiFaQu ', '1', '180020', '180020060', ' kaifaqu ', ' 开发区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:45', '2017-02-14 12:15:45', '687', ' 浏阳市 ', ' LiuYangShi ', '1', '180020', '180020070', ' liuyangshi ', ' 浏阳市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:45', '2017-02-14 12:15:45', '688', ' 长沙县 ', ' ZhangShaXian ', '1', '180020', '180020080', ' changshaxian ', ' 长沙县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:45', '2017-02-14 12:15:45', '689', ' 望城区 ', ' WangChengQu ', '1', '180020', '180020090', ' wangchengqu ', ' 望城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:45', '2017-02-14 12:15:45', '690', ' 宁乡县 ', ' NingXiangXian ', '1', '180020', '180020100', ' ningxiangxian ', ' 宁乡县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:45', '2017-02-14 12:15:45', '691', ' 湘潭 ', ' XiangTan ', '1', '180', '180030', ' xiangtan ', ' 湘潭 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:45', '2017-02-14 12:15:45', '692', ' 株洲 ', ' ZhuZhou ', '1', '180', '180040', ' zhuzhou ', ' 株洲 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:45', '2017-02-14 12:15:45', '693', ' 常德 ', ' ChangDe ', '1', '180', '180050', ' changde ', ' 常德 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:45', '2017-02-14 12:15:45', '694', ' 衡阳 ', ' HengYang ', '1', '180', '180060', ' hengyang ', ' 衡阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:45', '2017-02-14 12:15:45', '695', ' 益阳 ', ' YiYang ', '1', '180', '180070', ' yiyang ', ' 益阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:45', '2017-02-14 12:15:45', '696', ' 郴州 ', ' ChenZhou ', '1', '180', '180080', ' chenzhou ', ' 郴州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:45', '2017-02-14 12:15:45', '697', ' 岳阳 ', ' YueYang ', '1', '180', '180090', ' yueyang ', ' 岳阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:45', '2017-02-14 12:15:45', '698', ' 邵阳 ', ' ShaoYang ', '1', '180', '180100', ' shaoyang ', ' 邵阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:46', '2017-02-14 12:15:46', '699', ' 张家界 ', ' ZhangJiaJie ', '1', '180', '180110', ' zhangjiajie ', ' 张家界 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:46', '2017-02-14 12:15:46', '700', ' 娄底 ', ' LouDi ', '1', '180', '180120', ' loudi ', ' 娄底 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:46', '2017-02-14 12:15:46', '701', ' 永州 ', ' YongZhou ', '1', '180', '180130', ' yongzhou ', ' 永州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:46', '2017-02-14 12:15:46', '702', ' 怀化 ', ' HuaiHua ', '1', '180', '180140', ' huaihua ', ' 怀化 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:46', '2017-02-14 12:15:46', '703', ' 湘西 ', ' XiangXi ', '1', '180', '180150', ' xiangxi ', ' 湘西 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:46', '2017-02-14 12:15:46', '704', ' 吉林省 ', ' JiLinSheng ', '0', '', '190', ' jilin ', ' 吉林省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:46', '2017-02-14 12:15:46', '705', ' 长春 ', ' ChangChun ', '1', '190', '190020', ' changchun ', ' 长春 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:46', '2017-02-14 12:15:46', '706', ' 朝阳区 ', ' ChaoYangQu ', '1', '190020', '190020010', ' chaoyangqu ', ' 朝阳区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:46', '2017-02-14 12:15:46', '707', ' 宽城区 ', ' KuanChengQu ', '1', '190020', '190020020', ' kuanchengqu ', ' 宽城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:46', '2017-02-14 12:15:46', '708', ' 二道区 ', ' ErDaoQu ', '1', '190020', '190020030', ' erdaoqu ', ' 二道区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:46', '2017-02-14 12:15:46', '709', ' 南关区 ', ' NanGuanQu ', '1', '190020', '190020040', ' nanguanqu ', ' 南关区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:46', '2017-02-14 12:15:46', '710', ' 绿园区 ', ' LvYuanQu ', '1', '190020', '190020050', ' lvyuanqu ', ' 绿园区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:46', '2017-02-14 12:15:46', '711', ' 双阳区 ', ' ShuangYangQu ', '1', '190020', '190020060', ' shuangyangqu ', ' 双阳区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:47', '2017-02-14 12:15:47', '712', ' 净月区 ', ' JingYueQu ', '1', '190020', '190020070', ' jingyuequ ', ' 净月区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:47', '2017-02-14 12:15:47', '713', ' 高新区 ', ' GaoXinQu ', '1', '190020', '190020080', ' gaoxinqu ', ' 高新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:47', '2017-02-14 12:15:47', '714', ' 经开区 ', ' JingKaiQu ', '1', '190020', '190020090', ' jingkaiqu ', ' 经开区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:47', '2017-02-14 12:15:47', '715', ' 汽开区 ', ' QiKaiQu ', '1', '190020', '190020100', ' qikaiqu ', ' 汽开区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:47', '2017-02-14 12:15:47', '716', ' 德惠市 ', ' DeHuiShi ', '1', '190020', '190020110', ' dehuishi ', ' 德惠市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:47', '2017-02-14 12:15:47', '717', ' 九台市 ', ' JiuTaiShi ', '1', '190020', '190020120', ' jiutaishi ', ' 九台市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:47', '2017-02-14 12:15:47', '718', ' 榆树市 ', ' YuShuShi ', '1', '190020', '190020130', ' yushushi ', ' 榆树市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:47', '2017-02-14 12:15:47', '719', ' 农安县 ', ' NongAnXian ', '1', '190020', '190020140', ' nonganxian ', ' 农安县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:47', '2017-02-14 12:15:47', '720', ' 高新区 ', ' GaoXinQu ', '1', '190020', '190020150', ' gaoxinqu ', ' 高新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:47', '2017-02-14 12:15:47', '721', ' 经济区 ', ' JingJiQu ', '1', '190020', '190020160', ' jingjiqu ', ' 经济区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:47', '2017-02-14 12:15:47', '722', ' 净月区 ', ' JingYueQu ', '1', '190020', '190020170', ' jingyuequ ', ' 净月区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:47', '2017-02-14 12:15:47', '723', ' 吉林市 ', ' JiLinShi ', '1', '190', '190030', ' jinlinshi ', ' 吉林市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:47', '2017-02-14 12:15:47', '724', ' 四平 ', ' SiPing ', '1', '190', '190040', ' siping ', ' 四平 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:47', '2017-02-14 12:15:47', '725', ' 辽源 ', ' LiaoYuan ', '1', '190', '190050', ' liaoyuan ', ' 辽源 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:48', '2017-02-14 12:15:48', '726', ' 通化 ', ' TongHua ', '1', '190', '190060', ' tonghuan ', ' 通化 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:48', '2017-02-14 12:15:48', '727', ' 白山 ', ' BaiShan ', '1', '190', '190070', ' baishan ', ' 白山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:48', '2017-02-14 12:15:48', '728', ' 松原 ', ' SongYuan ', '1', '190', '190080', ' songyuan ', ' 松原 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:48', '2017-02-14 12:15:48', '729', ' 白城 ', ' BaiCheng ', '1', '190', '190090', ' baicheng ', ' 白城 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:48', '2017-02-14 12:15:48', '730', ' 延吉 ', ' YanJi ', '1', '190', '190100', ' yanji ', ' 延吉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:48', '2017-02-14 12:15:48', '731', ' 延边 ', ' YanBian ', '1', '190', '190110', ' yanbian ', ' 延边 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:48', '2017-02-14 12:15:48', '732', ' 公主岭 ', ' GongZhuLing ', '1', '190', '190120', ' gongzhuling ', ' 公主岭 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:48', '2017-02-14 12:15:48', '733', ' 江西省 ', ' JiangXiSheng ', '0', '', '200', ' jiangxi ', ' 江西省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:48', '2017-02-14 12:15:48', '734', ' 南昌 ', ' NanChang ', '1', '200', '200020', ' nanchang ', ' 南昌 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:48', '2017-02-14 12:15:48', '735', ' 东湖区 ', ' DongHuQu ', '1', '200020', '200020010', ' donghuqu ', ' 东湖区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:48', '2017-02-14 12:15:48', '736', ' 西湖区 ', ' XiHuQu ', '1', '200020', '200020020', ' xihuqu ', ' 西湖区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:48', '2017-02-14 12:15:48', '737', ' 青云谱 ', ' QingYunPu ', '1', '200020', '200020030', ' qingyunpu ', ' 青云谱 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:48', '2017-02-14 12:15:48', '738', ' 湾里区 ', ' WanLiQu ', '1', '200020', '200020040', ' wanliqu ', ' 湾里区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:49', '2017-02-14 12:15:49', '739', ' 青山湖 ', ' QingShanHu ', '1', '200020', '200020050', ' qingshanhu ', ' 青山湖 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:49', '2017-02-14 12:15:49', '740', ' 红谷滩 ', ' HongGuTan ', '1', '200020', '200020060', ' honggutan ', ' 红谷滩 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:49', '2017-02-14 12:15:49', '741', ' 昌北区 ', ' ChangBeiQu ', '1', '200020', '200020070', ' changbeiqu ', ' 昌北区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:49', '2017-02-14 12:15:49', '742', ' 高新区 ', ' GaoXinQu ', '1', '200020', '200020080', ' gaoxinqu ', ' 高新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:49', '2017-02-14 12:15:49', '743', ' 南昌县 ', ' NanChangXian ', '1', '200020', '200020090', ' nanchangxian ', ' 南昌县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:49', '2017-02-14 12:15:49', '744', ' 新建县 ', ' XinJianXian ', '1', '200020', '200020100', ' xinjianxian ', ' 新建县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:49', '2017-02-14 12:15:49', '745', ' 安义县 ', ' AnYiXian ', '1', '200020', '200020110', ' anyixian ', ' 安义县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:49', '2017-02-14 12:15:49', '746', ' 进贤县 ', ' JinXianXian ', '1', '200020', '200020120', ' jinxianxian ', ' 进贤县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:49', '2017-02-14 12:15:49', '747', ' 桑海区 ', ' SangHaiQu ', '1', '200020', '200020130', ' sanghaiqu ', ' 桑海区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:49', '2017-02-14 12:15:49', '748', ' 九江 ', ' JiuJiang ', '1', '200', '200030', ' jiujiang ', ' 九江 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:49', '2017-02-14 12:15:49', '749', ' 赣州 ', ' GanZhou ', '1', '200', '200040', ' ganzhou ', ' 赣州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:49', '2017-02-14 12:15:49', '750', ' 宜春 ', ' YiChun ', '1', '200', '200050', ' yichun0795 ', ' 宜春 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:49', '2017-02-14 12:15:49', '751', ' 吉安 ', ' JiAn ', '1', '200', '200060', ' jian ', ' 吉安 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:50', '2017-02-14 12:15:50', '752', ' 上饶 ', ' ShangRao ', '1', '200', '200070', ' shangrao ', ' 上饶 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:50', '2017-02-14 12:15:50', '753', ' 抚州 ', ' FuZhou ', '1', '200', '200080', ' fuzhou0794 ', ' 抚州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:50', '2017-02-14 12:15:50', '754', ' 景德镇 ', ' JingDeZhen ', '1', '200', '200090', ' jingdezhen ', ' 景德镇 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:50', '2017-02-14 12:15:50', '755', ' 萍乡 ', ' PingXiang ', '1', '200', '200100', ' pingxiang ', ' 萍乡 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:50', '2017-02-14 12:15:50', '756', ' 新余 ', ' XinYu ', '1', '200', '200110', ' xinyu ', ' 新余 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:50', '2017-02-14 12:15:50', '757', ' 鹰潭 ', ' YingTan ', '1', '200', '200120', ' yingtan ', ' 鹰潭 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:50', '2017-02-14 12:15:50', '758', ' 辽宁省 ', ' LiaoNingSheng ', '0', '', '210', ' liaoning ', ' 辽宁省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:50', '2017-02-14 12:15:50', '759', ' 沈阳 ', ' ShenYang ', '1', '210', '210020', ' shenyang ', ' 沈阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:50', '2017-02-14 12:15:50', '760', ' 沈河区 ', ' ShenHeQu ', '1', '210020', '210020010', ' shenhequ ', ' 沈河区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:50', '2017-02-14 12:15:50', '761', ' 皇姑区 ', ' HuangGuQu ', '1', '210020', '210020020', ' huangguqu ', ' 皇姑区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:50', '2017-02-14 12:15:50', '762', ' 和平区 ', ' HePingQu ', '1', '210020', '210020030', ' hepingqu ', ' 和平区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:50', '2017-02-14 12:15:50', '763', ' 大东区 ', ' DaDongQu ', '1', '210020', '210020040', ' dadongqu ', ' 大东区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:50', '2017-02-14 12:15:50', '764', ' 铁西区 ', ' TieXiQu ', '1', '210020', '210020050', ' tiexiqu ', ' 铁西区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:51', '2017-02-14 12:15:51', '765', ' 苏家屯 ', ' SuJiaTun ', '1', '210020', '210020060', ' sujiatun ', ' 苏家屯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:51', '2017-02-14 12:15:51', '766', ' 东陵区 ', ' DongLingQu ', '1', '210020', '210020070', ' donglingqu ', ' 东陵区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:51', '2017-02-14 12:15:51', '767', ' 沈北区 ', ' ShenBeiQu ', '1', '210020', '210020080', ' shenbeiqu ', ' 沈北区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:51', '2017-02-14 12:15:51', '768', ' 于洪区 ', ' YuHongQu ', '1', '210020', '210020090', ' yuhongqu ', ' 于洪区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:51', '2017-02-14 12:15:51', '769', ' 浑南区 ', ' HunNanQu ', '1', '210020', '210020100', ' hunnanqu ', ' 浑南区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:51', '2017-02-14 12:15:51', '770', ' 新民市 ', ' XinMinShi ', '1', '210020', '210020110', ' xinminshi ', ' 新民市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:51', '2017-02-14 12:15:51', '771', ' 辽中县 ', ' LiaoZhongXian ', '1', '210020', '210020120', ' liaozhongxian ', ' 辽中县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:51', '2017-02-14 12:15:51', '772', ' 康平县 ', ' KangPingXian ', '1', '210020', '210020130', ' kangpingxian ', ' 康平县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:51', '2017-02-14 12:15:51', '773', ' 法库县 ', ' FaKuXian ', '1', '210020', '210020140', ' fakuxian ', ' 法库县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:51', '2017-02-14 12:15:51', '774', ' 鞍山 ', ' AnShan ', '1', '210', '210030', ' anshan ', ' 鞍山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:51', '2017-02-14 12:15:51', '775', ' 大连 ', ' DaLian ', '1', '210', '210040', ' dalian ', ' 大连 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:51', '2017-02-14 12:15:51', '776', ' 西岗区 ', ' XiGangQu ', '1', '210040', '210040010', ' xigang ', ' 西岗区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:51', '2017-02-14 12:15:51', '777', ' 中山区 ', ' ZhongShanQu ', '1', '210040', '210040020', ' zhongshan ', ' 中山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:52', '2017-02-14 12:15:52', '778', ' 沙河口 ', ' ShaHeKou ', '1', '210040', '210040030', ' shahekou ', ' 沙河口 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:52', '2017-02-14 12:15:52', '779', ' 甘井子 ', ' GanJingZi ', '1', '210040', '210040040', ' ganjingzi ', ' 甘井子 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:52', '2017-02-14 12:15:52', '780', ' 旅顺口 ', ' LvShunKou ', '1', '210040', '210040050', ' lvshunkou ', ' 旅顺口 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:52', '2017-02-14 12:15:52', '781', ' 金州区 ', ' JinZhouQu ', '1', '210040', '210040060', ' jinzhou ', ' 金州区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:52', '2017-02-14 12:15:52', '782', ' 瓦房店 ', ' WaFangDian ', '1', '210040', '210040070', ' wafangdian ', ' 瓦房店 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:52', '2017-02-14 12:15:52', '783', ' 普兰店 ', ' PuLanDian ', '1', '210040', '210040080', ' pulandian ', ' 普兰店 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:52', '2017-02-14 12:15:52', '784', ' 庄河市 ', ' ZhuangHeShi ', '1', '210040', '210040090', ' zhuanghe ', ' 庄河市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:52', '2017-02-14 12:15:52', '785', ' 普湾区 ', ' PuWanQu ', '1', '210040', '210040100', ' puwanqu ', ' 普湾区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:52', '2017-02-14 12:15:52', '786', ' 长海县 ', ' ZhangHaiXian ', '1', '210040', '210040120', ' changhaixian ', ' 长海县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:52', '2017-02-14 12:15:52', '787', ' 新区 ', ' XinQu ', '1', '210040', '210040130', ' xinqu ', ' 新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:52', '2017-02-14 12:15:52', '788', ' 开发区 ', ' KaiFaQu ', '1', '210040', '210040140', ' kaifaqu ', ' 开发区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:52', '2017-02-14 12:15:52', '789', ' 葫芦岛 ', ' HuLuDao ', '1', '210', '210050', ' huludao ', ' 葫芦岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:52', '2017-02-14 12:15:52', '790', ' 抚顺 ', ' FuShun ', '1', '210', '210060', ' fushun ', ' 抚顺 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:53', '2017-02-14 12:15:53', '791', ' 本溪 ', ' BenXi ', '1', '210', '210070', ' benxi ', ' 本溪 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:53', '2017-02-14 12:15:53', '792', ' 丹东 ', ' DanDong ', '1', '210', '210080', ' dandong ', ' 丹东 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:53', '2017-02-14 12:15:53', '793', ' 锦州 ', ' JinZhou ', '1', '210', '210090', ' jinzhou ', ' 锦州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:53', '2017-02-14 12:15:53', '794', ' 营口 ', ' YingKou ', '1', '210', '210100', ' yingkou ', ' 营口 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:53', '2017-02-14 12:15:53', '795', ' 阜新 ', ' FuXin ', '1', '210', '210110', ' fuxin ', ' 阜新 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:53', '2017-02-14 12:15:53', '796', ' 辽阳 ', ' LiaoYang ', '1', '210', '210120', ' liaoyang ', ' 辽阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:53', '2017-02-14 12:15:53', '797', ' 盘锦 ', ' PanJin ', '1', '210', '210130', ' panjin ', ' 盘锦 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:53', '2017-02-14 12:15:53', '798', ' 铁岭 ', ' TieLing ', '1', '210', '210140', ' tieling ', ' 铁岭 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:53', '2017-02-14 12:15:53', '799', ' 朝阳 ', ' ChaoYang ', '1', '210', '210150', ' chaoyang ', ' 朝阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:53', '2017-02-14 12:15:53', '800', ' 兴城 ', ' XingCheng ', '1', '210', '210160', ' xingcheng ', ' 兴城 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:53', '2017-02-14 12:15:53', '801', ' 海城 ', ' HaiCheng ', '1', '210', '210170', ' haicheng ', ' 海城 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:53', '2017-02-14 12:15:53', '802', ' 昌图 ', ' ChangTu ', '1', '210', '210180', ' changtu ', ' 昌图 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:53', '2017-02-14 12:15:53', '803', ' 开原 ', ' KaiYuan ', '1', '210', '210190', ' kaiyuan ', ' 开原 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:54', '2017-02-14 12:15:54', '804', ' 内蒙古 ', ' NeiMengGu ', '0', '', '220', ' neimenggu ', ' 内蒙古 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:54', '2017-02-14 12:15:54', '805', ' 呼和浩特 ', ' HuHeHaoTe ', '1', '220', '220020', ' huhehaote ', ' 呼和浩特 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:54', '2017-02-14 12:15:54', '806', ' 回民区 ', ' HuiMinQu ', '1', '220020', '220020010', ' huiminqu ', ' 回民区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:54', '2017-02-14 12:15:54', '807', ' 玉泉区 ', ' YuQuanQu ', '1', '220020', '220020020', ' yuquanqu ', ' 玉泉区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:54', '2017-02-14 12:15:54', '808', ' 新城区 ', ' XinChengQu ', '1', '220020', '220020030', ' xinchengqu ', ' 新城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:54', '2017-02-14 12:15:54', '809', ' 赛罕区 ', ' SaiHanQu ', '1', '220020', '220020040', ' saihanqu ', ' 赛罕区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:54', '2017-02-14 12:15:54', '810', ' 清水河 ', ' QingShuiHe ', '1', '220020', '220020050', ' qingshuihe ', ' 清水河 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:54', '2017-02-14 12:15:54', '811', ' 土左旗 ', ' TuZuoQi ', '1', '220020', '220020060', ' tuzuoqi ', ' 土左旗 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:54', '2017-02-14 12:15:54', '812', ' 托克托 ', ' TuoKeTuo ', '1', '220020', '220020070', ' tuoketuo ', ' 托克托 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:54', '2017-02-14 12:15:54', '813', ' 和林格尔 ', ' HeLinGeEr ', '1', '220020', '220020080', ' helingeer ', ' 和林格尔 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:54', '2017-02-14 12:15:54', '814', ' 武川县 ', ' WuChuanXian ', '1', '220020', '220020090', ' wuchuanxian ', ' 武川县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:54', '2017-02-14 12:15:54', '815', ' 包头 ', ' BaoTou ', '1', '220', '220030', ' baotou ', ' 包头 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:54', '2017-02-14 12:15:54', '816', ' 赤峰 ', ' ChiFeng ', '1', '220', '220040', ' chifeng ', ' 赤峰 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:54', '2017-02-14 12:15:54', '817', ' 鄂尔多斯 ', ' EErDuoSi ', '1', '220', '220050', ' eerduosi ', ' 鄂尔多斯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:54', '2017-02-14 12:15:54', '818', ' 乌海 ', ' WuHai ', '1', '220', '220060', ' wuhai ', ' 乌海 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:55', '2017-02-14 12:15:55', '819', ' 通辽 ', ' TongLiao ', '1', '220', '220070', ' tongliao ', ' 通辽 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:55', '2017-02-14 12:15:55', '820', ' 呼伦贝尔 ', ' HuLunBeiEr ', '1', '220', '220080', ' wulunbeier ', ' 呼伦贝尔 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:55', '2017-02-14 12:15:55', '821', ' 巴彦淖尔 ', ' BaYanNaoEr ', '1', '220', '220090', ' bayannaoer ', ' 巴彦淖尔 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:55', '2017-02-14 12:15:55', '822', ' 乌兰察布 ', ' WuLanChaBu ', '1', '220', '220100', ' wulanchabu ', ' 乌兰察布 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:55', '2017-02-14 12:15:55', '823', ' 兴安盟 ', ' XingAnMeng ', '1', '220', '220110', ' xinganmeng ', ' 兴安盟 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:55', '2017-02-14 12:15:55', '824', ' 锡盟 ', ' XiMeng ', '1', '220', '220120', ' ximeng ', ' 锡盟 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:55', '2017-02-14 12:15:55', '825', ' 阿拉善盟 ', ' ALaShanMeng ', '1', '220', '220130', ' alashanmeng ', ' 阿拉善盟 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:55', '2017-02-14 12:15:55', '826', ' 乌审旗 ', ' WuShenQi ', '1', '220', '220140', ' wushenqi ', ' 乌审旗 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:55', '2017-02-14 12:15:55', '827', ' 满洲里 ', ' ManZhouLi ', '1', '220', '220150', ' manzhouli ', ' 满洲里 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:55', '2017-02-14 12:15:55', '828', ' 宁夏 ', ' NingXia ', '0', '', '230', ' ningxia ', ' 宁夏 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:55', '2017-02-14 12:15:55', '829', ' 银川 ', ' YinChuan ', '1', '230', '230020', ' yinchuan ', ' 银川 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:55', '2017-02-14 12:15:55', '830', ' 西夏区 ', ' XiXiaQu ', '1', '230020', '230020010', ' xixiaqu ', ' 西夏区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:55', '2017-02-14 12:15:55', '831', ' 金凤区 ', ' JinFengQu ', '1', '230020', '230020020', ' jinfengqu ', ' 金凤区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:55', '2017-02-14 12:15:55', '832', ' 兴庆区 ', ' XingQingQu ', '1', '230020', '230020030', ' xingqingqu ', ' 兴庆区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:56', '2017-02-14 12:15:56', '833', ' 灵武市 ', ' LingWuShi ', '1', '230020', '230020040', ' lingwushi ', ' 灵武市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:56', '2017-02-14 12:15:56', '834', ' 永宁县 ', ' YongNingXian ', '1', '230020', '230020050', ' yongningxian ', ' 永宁县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:56', '2017-02-14 12:15:56', '835', ' 贺兰县 ', ' HeLanXian ', '1', '230020', '230020060', ' helanxian ', ' 贺兰县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:56', '2017-02-14 12:15:56', '836', ' 中卫 ', ' ZhongWei ', '1', '230020', '230020070', ' zhongwei ', ' 中卫 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:56', '2017-02-14 12:15:56', '837', ' 石嘴山 ', ' ShiZuiShan ', '1', '230020', '230020080', ' shizuishan ', ' 石嘴山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:56', '2017-02-14 12:15:56', '838', ' 吴忠 ', ' WuZhong ', '1', '230020', '230020090', ' wuzhong ', ' 吴忠 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:56', '2017-02-14 12:15:56', '839', ' 青铜峡 ', ' QingTongXia ', '1', '230020', '230020100', ' qingtongxia ', ' 青铜峡 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:56', '2017-02-14 12:15:56', '840', ' 石嘴山 ', ' ShiZuiShan ', '1', '230', '230030', ' shizuishan ', ' 石嘴山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:56', '2017-02-14 12:15:56', '841', ' 吴忠 ', ' WuZhong ', '1', '230', '230040', ' wuzhong ', ' 吴忠 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:56', '2017-02-14 12:15:56', '842', ' 固原 ', ' GuYuan ', '1', '230', '230050', ' guyuan ', ' 固原 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:56', '2017-02-14 12:15:56', '843', ' 中卫 ', ' ZhongWei ', '1', '230', '230060', ' zhongwei ', ' 中卫 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:56', '2017-02-14 12:15:56', '844', ' 青海省 ', ' QingHaiSheng ', '0', '', '240', ' qinghai ', ' 青海省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:56', '2017-02-14 12:15:56', '845', ' 西宁 ', ' XiNing ', '1', '240', '240020', ' xining ', ' 西宁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:57', '2017-02-14 12:15:57', '846', ' 城中区 ', ' ChengZhongQu ', '1', '240020', '240020010', ' chengzhongqu ', ' 城中区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:57', '2017-02-14 12:15:57', '847', ' 城东区 ', ' ChengDongQu ', '1', '240020', '240020020', ' chengdongqu ', ' 城东区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:57', '2017-02-14 12:15:57', '848', ' 城西区 ', ' ChengXiQu ', '1', '240020', '240020030', ' chengxiqu ', ' 城西区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:57', '2017-02-14 12:15:57', '849', ' 城北区 ', ' ChengBeiQu ', '1', '240020', '240020040', ' chengbeiqu ', ' 城北区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:57', '2017-02-14 12:15:57', '850', ' 湟中县 ', ' HuangZhongXian ', '1', '240020', '240020050', ' huangzhongxian ', ' 湟中县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:57', '2017-02-14 12:15:57', '851', ' 湟源县 ', ' HuangYuanXian ', '1', '240020', '240020060', ' huangyuanxian ', ' 湟源县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:57', '2017-02-14 12:15:57', '852', ' 大通 ', ' DaTong ', '1', '240020', '240020070', ' datong ', ' 大通 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:57', '2017-02-14 12:15:57', '853', ' 城南区 ', ' ChengNanQu ', '1', '240020', '240020080', ' chengnanqu ', ' 城南区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:57', '2017-02-14 12:15:57', '854', ' 海湖区 ', ' HaiHuQu ', '1', '240020', '240020090', ' haihuqu ', ' 海湖区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:57', '2017-02-14 12:15:57', '855', ' 海东 ', ' HaiDong ', '1', '240', '240030', ' haidong ', ' 海东 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:57', '2017-02-14 12:15:57', '856', ' 海西 ', ' HaiXi ', '1', '240', '240040', ' haixi ', ' 海西 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:57', '2017-02-14 12:15:57', '857', ' 海北 ', ' HaiBei ', '1', '240', '240050', ' haibei ', ' 海北 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:57', '2017-02-14 12:15:57', '858', ' 黄南 ', ' HuangNan ', '1', '240', '240060', ' huangnan ', ' 黄南 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:58', '2017-02-14 12:15:58', '859', ' 海南 ', ' HaiNan ', '1', '240', '240070', ' hainan ', ' 海南 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:58', '2017-02-14 12:15:58', '860', ' 果洛 ', ' GuoLuo ', '1', '240', '240080', ' guoluo ', ' 果洛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:58', '2017-02-14 12:15:58', '861', ' 玉树 ', ' YuShu ', '1', '240', '240090', ' yushu ', ' 玉树 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:58', '2017-02-14 12:15:58', '862', ' 山东省 ', ' ShanDongSheng ', '0', '', '250', ' shandong ', ' 山东省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:58', '2017-02-14 12:15:58', '863', ' 济南 ', ' JiNan ', '1', '250', '250020', ' jinan ', ' 济南 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:58', '2017-02-14 12:15:58', '864', ' 市中区 ', ' ShiZhongQu ', '1', '250020', '250020010', ' shizhongqu ', ' 市中区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:58', '2017-02-14 12:15:58', '865', ' 历下区 ', ' LiXiaQu ', '1', '250020', '250020020', ' lixiaqu ', ' 历下区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:58', '2017-02-14 12:15:58', '866', ' 天桥区 ', ' TianQiaoQu ', '1', '250020', '250020030', ' tianqiaoqu ', ' 天桥区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:58', '2017-02-14 12:15:58', '867', ' 槐荫区 ', ' HuaiYinQu ', '1', '250020', '250020040', ' huaiyinqu ', ' 槐荫区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:58', '2017-02-14 12:15:58', '868', ' 历城区 ', ' LiChengQu ', '1', '250020', '250020050', ' lichengqu ', ' 历城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:58', '2017-02-14 12:15:58', '869', ' 长清区 ', ' ZhangQingQu ', '1', '250020', '250020060', ' changqingqu ', ' 长清区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:58', '2017-02-14 12:15:58', '870', ' 章丘市 ', ' ZhangQiuShi ', '1', '250020', '250020070', ' zhangqiushi ', ' 章丘市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:58', '2017-02-14 12:15:58', '871', ' 平阴县 ', ' PingYinXian ', '1', '250020', '250020080', ' pingyinxian ', ' 平阴县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:58', '2017-02-14 12:15:58', '872', ' 济阳县 ', ' JiYangXian ', '1', '250020', '250020090', ' jiyangxian ', ' 济阳县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:59', '2017-02-14 12:15:59', '873', ' 商河县 ', ' ShangHeXian ', '1', '250020', '250020100', ' shanghexian ', ' 商河县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:59', '2017-02-14 12:15:59', '874', ' 高新区 ', ' GaoXinQu ', '1', '250020', '250020110', ' gaoxinqu ', ' 高新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:59', '2017-02-14 12:15:59', '875', ' 近郊 ', ' JinJiao ', '1', '250020', '250020120', ' jinjiao ', ' 近郊 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:59', '2017-02-14 12:15:59', '876', ' 德州 ', ' DeZhou ', '1', '250', '250030', ' dezhou ', ' 德州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:59', '2017-02-14 12:15:59', '877', ' 东营 ', ' DongYing ', '1', '250', '250040', ' dongying ', ' 东营 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:59', '2017-02-14 12:15:59', '878', ' 济宁 ', ' JiNing ', '1', '250', '250050', ' jining ', ' 济宁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:59', '2017-02-14 12:15:59', '879', ' 临沂 ', ' LinYi ', '1', '250', '250060', ' linyi ', ' 临沂 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:59', '2017-02-14 12:15:59', '880', ' 青岛 ', ' QingDao ', '1', '250', '250070', ' qingdao ', ' 青岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:59', '2017-02-14 12:15:59', '881', ' 市南区 ', ' ShiNanQu ', '1', '250070', '250070010', ' shinanqu ', ' 市南区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:59', '2017-02-14 12:15:59', '882', ' 市北区 ', ' ShiBeiQu ', '1', '250070', '250070020', ' shibeiqu ', ' 市北区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:59', '2017-02-14 12:15:59', '883', ' 城阳区 ', ' ChengYangQu ', '1', '250070', '250070030', ' chengyangqu ', ' 城阳区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:59', '2017-02-14 12:15:59', '884', ' 四方区 ', ' SiFangQu ', '1', '250070', '250070040', ' sifangqu ', ' 四方区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:59', '2017-02-14 12:15:59', '885', ' 李沧区 ', ' LiCangQu ', '1', '250070', '250070050', ' licangqu ', ' 李沧区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:15:59', '2017-02-14 12:15:59', '886', ' 黄岛区 ', ' HuangDaoQu ', '1', '250070', '250070060', ' huangdaoqu ', ' 黄岛区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:00', '2017-02-14 12:16:00', '887', ' 崂山区 ', ' LaoShanQu ', '1', '250070', '250070070', ' laoshanqu ', ' 崂山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:00', '2017-02-14 12:16:00', '888', ' 胶州市 ', ' JiaoZhouShi ', '1', '250070', '250070080', ' jiaozhoushi ', ' 胶州市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:00', '2017-02-14 12:16:00', '889', ' 即墨市 ', ' JiMoShi ', '1', '250070', '250070090', ' jimoshi ', ' 即墨市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:00', '2017-02-14 12:16:00', '890', ' 平度市 ', ' PingDuShi ', '1', '250070', '250070100', ' pingdushi ', ' 平度市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:00', '2017-02-14 12:16:00', '891', ' 胶南市 ', ' JiaoNanShi ', '1', '250070', '250070110', ' jiaonanshi ', ' 胶南市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:00', '2017-02-14 12:16:00', '892', ' 莱西市 ', ' LaiXiShi ', '1', '250070', '250070120', ' laixishi ', ' 莱西市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:00', '2017-02-14 12:16:00', '893', ' 日照 ', ' RiZhao ', '1', '250', '250080', ' rizhao ', ' 日照 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:00', '2017-02-14 12:16:00', '894', ' 泰安 ', ' TaiAn ', '1', '250', '250090', ' taian ', ' 泰安 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:00', '2017-02-14 12:16:00', '895', ' 威海 ', ' WeiHai ', '1', '250', '250100', ' weihai ', ' 威海 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:00', '2017-02-14 12:16:00', '896', ' 潍坊 ', ' WeiFang ', '1', '250', '250110', ' weifang ', ' 潍坊 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:00', '2017-02-14 12:16:00', '897', ' 烟台 ', ' YanTai ', '1', '250', '250120', ' yantai ', ' 烟台 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:00', '2017-02-14 12:16:00', '898', ' 淄博 ', ' ZiBo ', '1', '250', '250130', ' zibo ', ' 淄博 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:00', '2017-02-14 12:16:00', '899', ' 枣庄 ', ' ZaoZhuang ', '1', '250', '250140', ' zaozhuang ', ' 枣庄 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:00', '2017-02-14 12:16:00', '900', ' 滨州 ', ' BinZhou ', '1', '250', '250150', ' binzhou ', ' 滨州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:00', '2017-02-14 12:16:00', '901', ' 聊城 ', ' LiaoCheng ', '1', '250', '250160', ' liaocheng ', ' 聊城 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:01', '2017-02-14 12:16:01', '902', ' 菏泽 ', ' HeZe ', '1', '250', '250170', ' heze ', ' 菏泽 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:01', '2017-02-14 12:16:01', '903', ' 莱芜 ', ' LaiWu ', '1', '250', '250180', ' laiwu ', ' 莱芜 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:01', '2017-02-14 12:16:01', '904', ' 荣成 ', ' RongCheng ', '1', '250', '250190', ' rongcheng ', ' 荣成 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:01', '2017-02-14 12:16:01', '905', ' 黄岛 ', ' HuangDao ', '1', '250', '250200', ' huangdao ', ' 黄岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:01', '2017-02-14 12:16:01', '906', ' 乳山 ', ' RuShan ', '1', '250', '250210', ' rushan ', ' 乳山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:01', '2017-02-14 12:16:01', '907', ' 城阳 ', ' ChengYang ', '1', '250', '250220', ' chengyang ', ' 城阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:01', '2017-02-14 12:16:01', '908', ' 即墨 ', ' JiMo ', '1', '250', '250230', ' jimo ', ' 即墨 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:01', '2017-02-14 12:16:01', '909', ' 肥城 ', ' FeiCheng ', '1', '250', '250240', ' feicheng ', ' 肥城 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:01', '2017-02-14 12:16:01', '910', ' 兖州 ', ' YanZhou ', '1', '250', '250250', ' yanzhou ', ' 兖州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:01', '2017-02-14 12:16:01', '911', ' 海阳 ', ' HaiYang ', '1', '250', '250260', ' haiyang ', ' 海阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:01', '2017-02-14 12:16:01', '912', ' 胶州 ', ' JiaoZhou ', '1', '250', '250270', ' jiaozhou ', ' 胶州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:01', '2017-02-14 12:16:01', '913', ' 胶南 ', ' JiaoNan ', '1', '250', '250280', ' jiaonan ', ' 胶南 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:01', '2017-02-14 12:16:01', '914', ' 平度 ', ' PingDu ', '1', '250', '250290', ' pingdu ', ' 平度 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:01', '2017-02-14 12:16:01', '915', ' 莱西 ', ' LaiXi ', '1', '250', '250300', ' laixi ', ' 莱西 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:01', '2017-02-14 12:16:01', '916', ' 山西省 ', ' ShanXiSheng ', '0', '', '260', ' shanxi0351 ', ' 山西省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:02', '2017-02-14 12:16:02', '917', ' 太原 ', ' TaiYuan ', '1', '260', '260020', ' taiyuan ', ' 太原 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:02', '2017-02-14 12:16:02', '918', ' 杏花岭 ', ' XingHuaLing ', '1', '260020', '260020010', ' xinghualing ', ' 杏花岭 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:02', '2017-02-14 12:16:02', '919', ' 小店区 ', ' XiaoDianQu ', '1', '260020', '260020020', ' xiaodianqu ', ' 小店区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:02', '2017-02-14 12:16:02', '920', ' 迎泽区 ', ' YingZeQu ', '1', '260020', '260020030', ' yingzequ ', ' 迎泽区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:02', '2017-02-14 12:16:02', '921', ' 尖草坪 ', ' JianCaoPing ', '1', '260020', '260020040', ' jiancaoping ', ' 尖草坪 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:02', '2017-02-14 12:16:02', '922', ' 万柏林 ', ' WanBoLin ', '1', '260020', '260020050', ' wanbailin ', ' 万柏林 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:02', '2017-02-14 12:16:02', '923', ' 晋源区 ', ' JinYuanQu ', '1', '260020', '260020060', ' jinyuanqu ', ' 晋源区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:02', '2017-02-14 12:16:02', '924', ' 高新区 ', ' GaoXinQu ', '1', '260020', '260020070', ' gaoxinqu ', ' 高新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:02', '2017-02-14 12:16:02', '925', ' 开发区 ', ' KaiFaQu ', '1', '260020', '260020080', ' kaifaqu ', ' 开发区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:02', '2017-02-14 12:16:02', '926', ' 工业园 ', ' GongYeYuan ', '1', '260020', '260020090', ' gongyeyuan ', ' 工业园 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:02', '2017-02-14 12:16:02', '927', ' 清徐县 ', ' QingXuXian ', '1', '260020', '260020100', ' qingxuxian ', ' 清徐县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:02', '2017-02-14 12:16:02', '928', ' 阳曲县 ', ' YangQuXian ', '1', '260020', '260020110', ' yangquxian ', ' 阳曲县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:02', '2017-02-14 12:16:02', '929', ' 娄烦县 ', ' LouFanXian ', '1', '260020', '260020120', ' loufanxian ', ' 娄烦县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:03', '2017-02-14 12:16:03', '930', ' 古交市 ', ' GuJiaoShi ', '1', '260020', '260020130', ' gujiaoshi ', ' 古交市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:03', '2017-02-14 12:16:03', '931', ' 大同 ', ' DaTong ', '1', '260', '260030', ' datong ', ' 大同 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:03', '2017-02-14 12:16:03', '932', ' 临汾 ', ' LinFen ', '1', '260', '260040', ' linfen ', ' 临汾 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:03', '2017-02-14 12:16:03', '933', ' 运城 ', ' YunCheng ', '1', '260', '260050', ' yuncheng ', ' 运城 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:03', '2017-02-14 12:16:03', '934', ' 长治 ', ' ZhangZhi ', '1', '260', '260060', ' changzhi ', ' 长治 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:03', '2017-02-14 12:16:03', '935', ' 阳泉 ', ' YangQuan ', '1', '260', '260070', ' yangquan ', ' 阳泉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:03', '2017-02-14 12:16:03', '936', ' 晋城 ', ' JinCheng ', '1', '260', '260080', ' jincheng ', ' 晋城 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:03', '2017-02-14 12:16:03', '937', ' 朔州 ', ' ShuoZhou ', '1', '260', '260090', ' shuozhou ', ' 朔州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:03', '2017-02-14 12:16:03', '938', ' 晋中 ', ' JinZhong ', '1', '260', '260100', ' jinzhong ', ' 晋中 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:03', '2017-02-14 12:16:03', '939', ' 忻州 ', ' XinZhou ', '1', '260', '260110', ' xinzhou ', ' 忻州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:03', '2017-02-14 12:16:03', '940', ' 吕梁 ', ' LvLiang ', '1', '260', '260120', ' lvliang ', ' 吕梁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:03', '2017-02-14 12:16:03', '941', ' 永济 ', ' YongJi ', '1', '260', '260130', ' yongji ', ' 永济 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:03', '2017-02-14 12:16:03', '942', ' 和顺 ', ' HeShun ', '1', '260', '260140', ' heshun ', ' 和顺 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:04', '2017-02-14 12:16:04', '943', ' 陕西省 ', ' ShanXiSheng ', '0', '', '270', ' shanxi ', ' 陕西省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:04', '2017-02-14 12:16:04', '944', ' 西安 ', ' XiAn ', '1', '270', '270020', ' xian ', ' 西安 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:04', '2017-02-14 12:16:04', '945', ' 莲湖区 ', ' LianHuQu ', '1', '270020', '270020010', ' lianhuqu ', ' 莲湖区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:04', '2017-02-14 12:16:04', '946', ' 新城区 ', ' XinChengQu ', '1', '270020', '270020020', ' xinchengqu ', ' 新城区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:04', '2017-02-14 12:16:04', '947', ' 碑林区 ', ' BeiLinQu ', '1', '270020', '270020030', ' beilinqu ', ' 碑林区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:04', '2017-02-14 12:16:04', '948', ' 雁塔区 ', ' YanTaQu ', '1', '270020', '270020040', ' yantaqu ', ' 雁塔区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:04', '2017-02-14 12:16:04', '949', ' 灞桥区 ', ' BaQiaoQu ', '1', '270020', '270020050', ' baqiaoqu ', ' 灞桥区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:04', '2017-02-14 12:16:04', '950', ' 未央区 ', ' WeiYangQu ', '1', '270020', '270020060', ' weiyangqu ', ' 未央区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:04', '2017-02-14 12:16:04', '951', ' 阎良区 ', ' YanLiangQu ', '1', '270020', '270020070', ' yanliangqu ', ' 阎良区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:04', '2017-02-14 12:16:04', '952', ' 临潼区 ', ' LinTongQu ', '1', '270020', '270020080', ' lintongqu ', ' 临潼区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:04', '2017-02-14 12:16:04', '953', ' 长安区 ', ' ZhangAnQu ', '1', '270020', '270020090', ' changanqu ', ' 长安区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:04', '2017-02-14 12:16:04', '954', ' 蓝田县 ', ' LanTianXian ', '1', '270020', '270020100', ' lantianxian ', ' 蓝田县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:04', '2017-02-14 12:16:04', '955', ' 周至县 ', ' ZhouZhiXian ', '1', '270020', '270020110', ' zhouzhixian ', ' 周至县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:05', '2017-02-14 12:16:05', '956', ' 户县 ', ' HuXian ', '1', '270020', '270020120', ' huxian ', ' 户县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:05', '2017-02-14 12:16:05', '957', ' 高陵县 ', ' GaoLingXian ', '1', '270020', '270020130', ' gaolingxian ', ' 高陵县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:05', '2017-02-14 12:16:05', '958', ' 经开区 ', ' JingKaiQu ', '1', '270020', '270020140', ' jingkaiqu ', ' 经开区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:05', '2017-02-14 12:16:05', '959', ' 高新区 ', ' GaoXinQu ', '1', '270020', '270020150', ' gaoxinqu ', ' 高新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:05', '2017-02-14 12:16:05', '960', ' 宝鸡 ', ' BaoJi ', '1', '270', '270030', ' baoji ', ' 宝鸡 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:05', '2017-02-14 12:16:05', '961', ' 咸阳 ', ' XianYang ', '1', '270', '270040', ' xianyang ', ' 咸阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:05', '2017-02-14 12:16:05', '962', ' 铜川 ', ' TongChuan ', '1', '270', '270050', ' tongchuan ', ' 铜川 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:05', '2017-02-14 12:16:05', '963', ' 渭南 ', ' WeiNan ', '1', '270', '270060', ' weinan ', ' 渭南 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:05', '2017-02-14 12:16:05', '964', ' 汉中 ', ' HanZhong ', '1', '270', '270070', ' hanzhong ', ' 汉中 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:05', '2017-02-14 12:16:05', '965', ' 安康 ', ' AnKang ', '1', '270', '270080', ' ankang ', ' 安康 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:05', '2017-02-14 12:16:05', '966', ' 商洛 ', ' ShangLuo ', '1', '270', '270090', ' shangluo ', ' 商洛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:05', '2017-02-14 12:16:05', '967', ' 延安 ', ' YanAn ', '1', '270', '270100', ' yanan ', ' 延安 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:05', '2017-02-14 12:16:05', '968', ' 榆林 ', ' YuLin ', '1', '270', '270110', ' yulin0912 ', ' 榆林 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:06', '2017-02-14 12:16:06', '969', ' 杨凌 ', ' YangLing ', '1', '270', '270120', ' yangling ', ' 杨凌 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:06', '2017-02-14 12:16:06', '970', ' 兴平 ', ' XingPing ', '1', '270', '270130', ' xingping ', ' 兴平 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:06', '2017-02-14 12:16:06', '971', ' 四川省 ', ' SiChuanSheng ', '0', '', '280', ' sichuan ', ' 四川省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:06', '2017-02-14 12:16:06', '972', ' 成都 ', ' ChengDu ', '1', '280', '280020', ' chengdu ', ' 成都 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:06', '2017-02-14 12:16:06', '973', ' 成华区 ', ' ChengHuaQu ', '1', '280020', '280020010', ' chenghua ', ' 成华区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:06', '2017-02-14 12:16:06', '974', ' 武侯区 ', ' WuHouQu ', '1', '280020', '280020020', ' wuhou ', ' 武侯区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:06', '2017-02-14 12:16:06', '975', ' 青羊区 ', ' QingYangQu ', '1', '280020', '280020030', ' qingyang ', ' 青羊区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:06', '2017-02-14 12:16:06', '976', ' 锦江区 ', ' JinJiangQu ', '1', '280020', '280020040', ' jinjiang ', ' 锦江区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:06', '2017-02-14 12:16:06', '977', ' 金牛区 ', ' JinNiuQu ', '1', '280020', '280020050', ' jinniu ', ' 金牛区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:06', '2017-02-14 12:16:06', '978', ' 龙泉驿 ', ' LongQuanYi ', '1', '280020', '280020060', ' longquanyi ', ' 龙泉驿 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:06', '2017-02-14 12:16:06', '979', ' 青白江 ', ' QingBaiJiang ', '1', '280020', '280020070', ' qingbaijiang ', ' 青白江 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:06', '2017-02-14 12:16:06', '980', ' 新都区 ', ' XinDouQu ', '1', '280020', '280020080', ' xindu ', ' 新都区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:06', '2017-02-14 12:16:06', '981', ' 双流县 ', ' ShuangLiuXian ', '1', '280020', '280020090', ' shuangliu ', ' 双流县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:06', '2017-02-14 12:16:06', '982', ' 郫县 ', ' PiXian ', '1', '280020', '280020100', ' pixian ', ' 郫县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:06', '2017-02-14 12:16:06', '983', ' 温江区 ', ' WenJiangQu ', '1', '280020', '280020110', ' wenjiang ', ' 温江区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:07', '2017-02-14 12:16:07', '984', ' 大邑县 ', ' DaYiXian ', '1', '280020', '280020120', ' dayi ', ' 大邑县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:07', '2017-02-14 12:16:07', '985', ' 金堂县 ', ' JinTangXian ', '1', '280020', '280020130', ' jintang ', ' 金堂县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:07', '2017-02-14 12:16:07', '986', ' 蒲江县 ', ' PuJiangXian ', '1', '280020', '280020140', ' pujiang ', ' 蒲江县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:07', '2017-02-14 12:16:07', '987', ' 新津县 ', ' XinJinXian ', '1', '280020', '280020150', ' xinjin ', ' 新津县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:07', '2017-02-14 12:16:07', '988', ' 温江区 ', ' WenJiangQu ', '1', '280020', '280020160', ' wenjiangqu ', ' 温江区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:07', '2017-02-14 12:16:07', '989', ' 高新区 ', ' GaoXinQu ', '1', '280020', '280020170', ' gaoxinqu ', ' 高新区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:07', '2017-02-14 12:16:07', '990', ' 高新西 ', ' GaoXinXi ', '1', '280020', '280020180', ' gaoxinxi ', ' 高新西 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:07', '2017-02-14 12:16:07', '991', ' 都江堰 ', ' DuJiangYan ', '1', '280020', '280020190', ' doujiangyan ', ' 都江堰 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:07', '2017-02-14 12:16:07', '992', ' 彭州市 ', ' PengZhouShi ', '1', '280020', '280020200', ' pengzhoushi ', ' 彭州市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:07', '2017-02-14 12:16:07', '993', ' 邛崃市 ', ' QiongLaiShi ', '1', '280020', '280020210', ' qionglaishi ', ' 邛崃市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:07', '2017-02-14 12:16:07', '994', ' 崇州市 ', ' ChongZhouShi ', '1', '280020', '280020220', ' chongzhoushi ', ' 崇州市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:07', '2017-02-14 12:16:07', '995', ' 乐山 ', ' LeShan ', '1', '280', '280030', ' leshan ', ' 乐山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:07', '2017-02-14 12:16:07', '996', ' 泸州 ', ' LuZhou ', '1', '280', '280040', ' luzhou ', ' 泸州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:07', '2017-02-14 12:16:07', '997', ' 绵阳 ', ' MianYang ', '1', '280', '280050', ' mianyang ', ' 绵阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:08', '2017-02-14 12:16:08', '998', ' 内江 ', ' NeiJiang ', '1', '280', '280060', ' neijiang ', ' 内江 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:08', '2017-02-14 12:16:08', '999', ' 宜宾 ', ' YiBin ', '1', '280', '280070', ' yibin ', ' 宜宾 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:08', '2017-02-14 12:16:08', '1000', ' 自贡 ', ' ZiGong ', '1', '280', '280080', ' zigong ', ' 自贡 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:08', '2017-02-14 12:16:08', '1001', ' 攀枝花 ', ' PanZhiHua ', '1', '280', '280090', ' panzhihua ', ' 攀枝花 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:08', '2017-02-14 12:16:08', '1002', ' 德阳 ', ' DeYang ', '1', '280', '280100', ' deyang ', ' 德阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:08', '2017-02-14 12:16:08', '1003', ' 广元 ', ' GuangYuan ', '1', '280', '280110', ' guangyuan ', ' 广元 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:08', '2017-02-14 12:16:08', '1004', ' 遂宁 ', ' SuiNing ', '1', '280', '280120', ' suining ', ' 遂宁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:08', '2017-02-14 12:16:08', '1005', ' 南充 ', ' NanChong ', '1', '280', '280130', ' nanchong ', ' 南充 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:08', '2017-02-14 12:16:08', '1006', ' 眉山 ', ' MeiShan ', '1', '280', '280140', ' meishan ', ' 眉山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:08', '2017-02-14 12:16:08', '1007', ' 广安 ', ' GuangAn ', '1', '280', '280150', ' guangan ', ' 广安 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:08', '2017-02-14 12:16:08', '1008', ' 达州 ', ' DaZhou ', '1', '280', '280160', ' dazhou ', ' 达州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:08', '2017-02-14 12:16:08', '1009', ' 雅安 ', ' YaAn ', '1', '280', '280170', ' yaan ', ' 雅安 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:08', '2017-02-14 12:16:08', '1010', ' 巴中 ', ' BaZhong ', '1', '280', '280180', ' bazhong ', ' 巴中 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:08', '2017-02-14 12:16:08', '1011', ' 资阳 ', ' ZiYang ', '1', '280', '280190', ' ziyang ', ' 资阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:08', '2017-02-14 12:16:08', '1012', ' 西昌 ', ' XiChang ', '1', '280', '280200', ' xichang ', ' 西昌 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:09', '2017-02-14 12:16:09', '1013', ' 甘孜 ', ' GanZi ', '1', '280', '280210', ' ganzi ', ' 甘孜 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:09', '2017-02-14 12:16:09', '1014', ' 阿坝 ', ' ABa ', '1', '280', '280220', ' abei ', ' 阿坝 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:09', '2017-02-14 12:16:09', '1015', ' 凉山 ', ' LiangShan ', '1', '280', '280230', ' liangshan ', ' 凉山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:09', '2017-02-14 12:16:09', '1016', ' 峨眉 ', ' EMei ', '1', '280', '280240', ' emei ', ' 峨眉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:09', '2017-02-14 12:16:09', '1017', ' 简阳 ', ' JianYang ', '1', '280', '280250', ' jianyang ', ' 简阳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:09', '2017-02-14 12:16:09', '1018', ' 西藏 ', ' XiZang ', '0', '', '290', ' xizang ', ' 西藏 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:09', '2017-02-14 12:16:09', '1019', ' 拉萨 ', ' LaSa ', '1', '290', '290020', ' lasa ', ' 拉萨 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:09', '2017-02-14 12:16:09', '1020', ' 城关区 ', ' ChengGuanQu ', '1', '290020', '290020010', ' chengguanqu ', ' 城关区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:09', '2017-02-14 12:16:09', '1021', ' 林周县 ', ' LinZhouXian ', '1', '290020', '290020020', ' linzhouxian ', ' 林周县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:09', '2017-02-14 12:16:09', '1022', ' 当雄县 ', ' DangXiongXian ', '1', '290020', '290020030', ' dangxiongxian ', ' 当雄县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:09', '2017-02-14 12:16:09', '1023', ' 尼木县 ', ' NiMuXian ', '1', '290020', '290020040', ' nimuxian ', ' 尼木县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:09', '2017-02-14 12:16:09', '1024', ' 曲水县 ', ' QuShuiXian ', '1', '290020', '290020050', ' qushuixian ', ' 曲水县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:09', '2017-02-14 12:16:09', '1025', ' 龙德庆 ', ' LongDeQing ', '1', '290020', '290020060', ' duilongdeqing ', ' 龙德庆 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:09', '2017-02-14 12:16:09', '1026', ' 达孜县 ', ' DaZiXian ', '1', '290020', '290020070', ' dazixian ', ' 达孜县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:09', '2017-02-14 12:16:09', '1027', ' 工卡县 ', ' GongKaXian ', '1', '290020', '290020080', ' gongkaxian ', ' 工卡县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:10', '2017-02-14 12:16:10', '1028', ' 日喀则 ', ' RiKaZe ', '1', '290', '290030', ' rikaze ', ' 日喀则 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:10', '2017-02-14 12:16:10', '1029', ' 林芝 ', ' LinZhi ', '1', '290', '290040', ' linzhi ', ' 林芝 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:10', '2017-02-14 12:16:10', '1030', ' 山南 ', ' ShanNan ', '1', '290', '290050', ' shannan ', ' 山南 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:10', '2017-02-14 12:16:10', '1031', ' 昌都 ', ' ChangDou ', '1', '290', '290060', ' changdu ', ' 昌都 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:10', '2017-02-14 12:16:10', '1032', ' 那曲 ', ' NaQu ', '1', '290', '290070', ' naqu ', ' 那曲 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:10', '2017-02-14 12:16:10', '1033', ' 阿里 ', ' ALi ', '1', '290', '290080', ' ali ', ' 阿里 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:10', '2017-02-14 12:16:10', '1034', ' 新疆 ', ' XinJiang ', '0', '', '300', ' xinjiang ', ' 新疆 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:10', '2017-02-14 12:16:10', '1035', ' 乌鲁木齐 ', ' WuLuMuQi ', '1', '300', '300020', ' wulumuqi ', ' 乌鲁木齐 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:10', '2017-02-14 12:16:10', '1036', ' 天山区 ', ' TianShanQu ', '1', '300020', '300020010', ' tianshanqu ', ' 天山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:10', '2017-02-14 12:16:10', '1037', ' 巴克区 ', ' BaKeQu ', '1', '300020', '300020020', ' bakequ ', ' 巴克区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:10', '2017-02-14 12:16:10', '1038', ' 新市区 ', ' XinShiQu ', '1', '300020', '300020030', ' xinshiqu ', ' 新市区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:10', '2017-02-14 12:16:10', '1039', ' 水磨沟 ', ' ShuiMoGou ', '1', '300020', '300020040', ' shuimogou ', ' 水磨沟 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:11', '2017-02-14 12:16:11', '1040', ' 头屯河 ', ' TouTunHe ', '1', '300020', '300020050', ' toutunhe ', ' 头屯河 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:11', '2017-02-14 12:16:11', '1041', ' 达坂城 ', ' DaBanCheng ', '1', '300020', '300020060', ' dabancheng ', ' 达坂城 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:11', '2017-02-14 12:16:11', '1042', ' 米东区 ', ' MiDongQu ', '1', '300020', '300020070', ' midongqu ', ' 米东区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:11', '2017-02-14 12:16:11', '1043', ' 乌鲁木齐 ', ' WuLuMuQi ', '1', '300020', '300020080', ' wulumuqi ', ' 乌鲁木齐 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:11', '2017-02-14 12:16:11', '1044', ' 昌吉市 ', ' ChangJiShi ', '1', '300020', '300020090', ' changjishi ', ' 昌吉市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:11', '2017-02-14 12:16:11', '1045', ' 五家渠 ', ' WuJiaQu ', '1', '300020', '300020100', ' wujiaqu ', ' 五家渠 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:11', '2017-02-14 12:16:11', '1046', ' 阜康市 ', ' FuKangShi ', '1', '300020', '300020110', ' fukangshi ', ' 阜康市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:11', '2017-02-14 12:16:11', '1047', ' 喀什 ', ' KaShen ', '1', '300', '300030', ' kashi ', ' 喀什 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:11', '2017-02-14 12:16:11', '1048', ' 克拉玛依 ', ' KeLaMaYi ', '1', '300', '300040', ' kelamayi ', ' 克拉玛依 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:11', '2017-02-14 12:16:11', '1049', ' 伊犁 ', ' YiLi ', '1', '300', '300050', ' yili ', ' 伊犁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:11', '2017-02-14 12:16:11', '1050', ' 阿克苏 ', ' AKeSu ', '1', '300', '300060', ' akesu ', ' 阿克苏 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:11', '2017-02-14 12:16:11', '1051', ' 哈密 ', ' HaMi ', '1', '300', '300070', ' hami ', ' 哈密 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:11', '2017-02-14 12:16:11', '1052', ' 石河子 ', ' ShiHeZi ', '1', '300', '300080', ' shihezi ', ' 石河子 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:12', '2017-02-14 12:16:12', '1053', ' 阿拉尔 ', ' ALaEr ', '1', '300', '300090', ' alaer ', ' 阿拉尔 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:12', '2017-02-14 12:16:12', '1054', ' 五家渠 ', ' WuJiaQu ', '1', '300', '300100', ' wujiaqu ', ' 五家渠 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:12', '2017-02-14 12:16:12', '1055', ' 图木舒克 ', ' TuMuShuKe ', '1', '300', '300110', ' tumushuke ', ' 图木舒克 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:12', '2017-02-14 12:16:12', '1056', ' 昌吉 ', ' ChangJi ', '1', '300', '300120', ' changji ', ' 昌吉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:12', '2017-02-14 12:16:12', '1057', ' 阿勒泰 ', ' ALeiTai ', '1', '300', '300130', ' aletai ', ' 阿勒泰 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:12', '2017-02-14 12:16:12', '1058', ' 吐鲁番 ', ' TuLuFan ', '1', '300', '300140', ' tulufan ', ' 吐鲁番 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:12', '2017-02-14 12:16:12', '1059', ' 塔城 ', ' TaCheng ', '1', '300', '300150', ' tacheng ', ' 塔城 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:12', '2017-02-14 12:16:12', '1060', ' 和田 ', ' HeTian ', '1', '300', '300160', ' hetian ', ' 和田 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:12', '2017-02-14 12:16:12', '1061', ' 克州 ', ' KeZhou ', '1', '300', '300170', ' kezhou ', ' 克州 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:12', '2017-02-14 12:16:12', '1062', ' 巴音郭楞 ', ' BaYinGuoLeng ', '1', '300', '300180', ' bayinguoleng ', ' 巴音郭楞 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:12', '2017-02-14 12:16:12', '1063', ' 博尔塔拉 ', ' BoErTaLa ', '1', '300', '300190', ' boertala ', ' 博尔塔拉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:12', '2017-02-14 12:16:12', '1064', ' 奎屯市 ', ' KuiTunShi ', '1', '300', '300200', ' kuitunshi ', ' 奎屯市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:12', '2017-02-14 12:16:12', '1065', ' 乌苏 ', ' WuSu ', '1', '300', '300210', ' wusu ', ' 乌苏 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:13', '2017-02-14 12:16:13', '1066', ' 云南省 ', ' YunNanSheng ', '0', '', '310', ' yunnan ', ' 云南省 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:13', '2017-02-14 12:16:13', '1067', ' 昆明 ', ' KunMing ', '1', '310', '310020', ' kunming ', ' 昆明 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:13', '2017-02-14 12:16:13', '1068', ' 盘龙区 ', ' PanLongQu ', '1', '310020', '310020010', ' panlongqu ', ' 盘龙区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:13', '2017-02-14 12:16:13', '1069', ' 五华区 ', ' WuHuaQu ', '1', '310020', '310020020', ' wuhuaqu ', ' 五华区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:13', '2017-02-14 12:16:13', '1070', ' 官渡区 ', ' GuanDuQu ', '1', '310020', '310020030', ' guanduqu ', ' 官渡区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:13', '2017-02-14 12:16:13', '1071', ' 西山区 ', ' XiShanQu ', '1', '310020', '310020040', ' xishanqu ', ' 西山区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:13', '2017-02-14 12:16:13', '1072', ' 东川区 ', ' DongChuanQu ', '1', '310020', '310020050', ' dongchuanqu ', ' 东川区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:13', '2017-02-14 12:16:13', '1073', ' 安宁市 ', ' AnNingShi ', '1', '310020', '310020060', ' anningshi ', ' 安宁市 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:13', '2017-02-14 12:16:13', '1074', ' 呈贡县 ', ' ChengGongXian ', '1', '310020', '310020070', ' chenggongxian ', ' 呈贡县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:13', '2017-02-14 12:16:13', '1075', ' 晋宁县 ', ' JinNingXian ', '1', '310020', '310020080', ' jinningxian ', ' 晋宁县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:13', '2017-02-14 12:16:13', '1076', ' 富民区 ', ' FuMinQu ', '1', '310020', '310020090', ' fuminqu ', ' 富民区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1077', ' 宜良区 ', ' YiLiangQu ', '1', '310020', '310020100', ' yiliangqu ', ' 宜良区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1078', ' 嵩明区 ', ' SongMingQu ', '1', '310020', '310020110', ' songmingqu ', ' 嵩明区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1079', ' 石林县 ', ' ShiLinXian ', '1', '310020', '310020120', ' shilinxian ', ' 石林县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1080', ' 禄劝 ', ' LuQuan ', '1', '310020', '310020130', ' luquan ', ' 禄劝 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1081', ' 寻甸 ', ' XunDian ', '1', '310020', '310020140', ' xundian ', ' 寻甸 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1082', ' 大理 ', ' DaLi ', '1', '310', '310030', ' dali ', ' 大理 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1083', ' 丽江 ', ' LiJiang ', '1', '310', '310040', ' lijiang ', ' 丽江 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1084', ' 玉溪 ', ' YuXi ', '1', '310', '310050', ' yuxi ', ' 玉溪 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1085', ' 曲靖 ', ' QuJing ', '1', '310', '310060', ' qujing ', ' 曲靖 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1086', ' 保山 ', ' BaoShan ', '1', '310', '310070', ' baoshan ', ' 保山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1087', ' 昭通 ', ' ZhaoTong ', '1', '310', '310080', ' zhaotong ', ' 昭通 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1088', ' 普洱 ', ' PuEr ', '1', '310', '310090', ' puer ', ' 普洱 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1089', ' 临沧 ', ' LinCang ', '1', '310', '310100', ' lincang ', ' 临沧 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1090', ' 红河 ', ' HongHe ', '1', '310', '310110', ' honghe ', ' 红河 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1091', ' 文山 ', ' WenShan ', '1', '310', '310120', ' wenshan ', ' 文山 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:14', '2017-02-14 12:16:14', '1092', ' 西双版纳 ', ' XiShuangBanNa ', '1', '310', '310130', ' xishuangbanna ', ' 西双版纳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:15', '2017-02-14 12:16:15', '1093', ' 德宏 ', ' DeHong ', '1', '310', '310140', ' dehong ', ' 德宏 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:15', '2017-02-14 12:16:15', '1094', ' 楚雄 ', ' ChuXiong ', '1', '310', '310150', ' chuxiong ', ' 楚雄 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:15', '2017-02-14 12:16:15', '1095', ' 怒江 ', ' NuJiang ', '1', '310', '310160', ' nujiang ', ' 怒江 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:15', '2017-02-14 12:16:15', '1096', ' 迪庆 ', ' DiQing ', '1', '310', '310170', ' diqing ', ' 迪庆 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:15', '2017-02-14 12:16:15', '1097', ' 思茅 ', ' SiMao ', '1', '310', '310180', ' simao ', ' 思茅 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:15', '2017-02-14 12:16:15', '1098', ' 香港 ', ' XiangGang ', '0', '', '320', ' hongkong ', ' 香港 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:15', '2017-02-14 12:16:15', '1099', ' 沙田区 ', ' ShaTianQu ', '1', '320', '320010010', ' shatianqu ', ' 沙田区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:15', '2017-02-14 12:16:15', '1100', ' 东区 ', ' DongQu ', '1', '320', '320010020', ' dongqu ', ' 东区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:15', '2017-02-14 12:16:15', '1101', ' 观塘区 ', ' GuanTangQu ', '1', '320', '320010030', ' guantangqu ', ' 观塘区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:15', '2017-02-14 12:16:15', '1102', ' 黄大仙 ', ' HuangDaXian ', '1', '320', '320010040', ' huangdaxian ', ' 黄大仙 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:15', '2017-02-14 12:16:15', '1103', ' 九龙城 ', ' JiuLongCheng ', '1', '320', '320010050', ' jiulongcheng ', ' 九龙城 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:15', '2017-02-14 12:16:15', '1104', ' 屯门区 ', ' TunMenQu ', '1', '320', '320010060', ' tunmenqu ', ' 屯门区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:15', '2017-02-14 12:16:15', '1105', ' 葵青区 ', ' KuiQingQu ', '1', '320', '320010070', ' kuiqingqu ', ' 葵青区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:15', '2017-02-14 12:16:15', '1106', ' 元朗区 ', ' YuanLangQu ', '1', '320', '320010080', ' yuanlangqu ', ' 元朗区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:16', '2017-02-14 12:16:16', '1107', ' 深水埗 ', ' ShenShuiBu ', '1', '320', '320010090', ' shenshuibu ', ' 深水埗 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:16', '2017-02-14 12:16:16', '1108', ' 西贡区 ', ' XiGongQu ', '1', '320', '320010100', ' xigongqu ', ' 西贡区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:16', '2017-02-14 12:16:16', '1109', ' 大埔区 ', ' DaBuQu ', '1', '320', '320010110', ' dapuqu ', ' 大埔区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:16', '2017-02-14 12:16:16', '1110', ' 湾仔区 ', ' WanZaiQu ', '1', '320', '320010120', ' wanziqu ', ' 湾仔区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:16', '2017-02-14 12:16:16', '1111', ' 油尖旺 ', ' YouJianWang ', '1', '320', '320010130', ' youjianwang ', ' 油尖旺 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:16', '2017-02-14 12:16:16', '1112', ' 北区 ', ' BeiQu ', '1', '320', '320010140', ' beiqu ', ' 北区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:16', '2017-02-14 12:16:16', '1113', ' 南区 ', ' NanQu ', '1', '320', '320010150', ' nanqu ', ' 南区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:16', '2017-02-14 12:16:16', '1114', ' 荃湾区 ', ' QuanWanQu ', '1', '320', '320010160', ' quanwanqu ', ' 荃湾区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:16', '2017-02-14 12:16:16', '1115', ' 中西区 ', ' ZhongXiQu ', '1', '320', '320010170', ' zhongxiqu ', ' 中西区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:16', '2017-02-14 12:16:16', '1116', ' 离岛区 ', ' LiDaoQu ', '1', '320', '320010180', ' lidaoqu ', ' 离岛区 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:16', '2017-02-14 12:16:16', '1117', ' 澳门 ', ' AoMen ', '0', '', '330', ' macao ', ' 澳门 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:16', '2017-02-14 12:16:16', '1118', ' 台湾 ', ' TaiWan ', '0', '', '340', ' taiwan ', ' 台湾 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:16', '2017-02-14 12:16:16', '1119', ' 台北 ', ' TaiBei ', '1', '340', '340010010', ' taibei ', ' 台北 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:16', '2017-02-14 12:16:16', '1120', ' 高雄 ', ' GaoXiong ', '1', '340', '340010020', ' gaoxiong ', ' 高雄 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:16', '2017-02-14 12:16:16', '1121', ' 基隆 ', ' JiLong ', '1', '340', '340010030', ' jilong ', ' 基隆 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:17', '2017-02-14 12:16:17', '1122', ' 台中 ', ' TaiZhong ', '1', '340', '340010040', ' taizhong ', ' 台中 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:17', '2017-02-14 12:16:17', '1123', ' 台南 ', ' TaiNan ', '1', '340', '340010050', ' tainan ', ' 台南 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:17', '2017-02-14 12:16:17', '1124', ' 新竹 ', ' XinZhu ', '1', '340', '340010060', ' xinzhu ', ' 新竹 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:17', '2017-02-14 12:16:17', '1125', ' 嘉义 ', ' JiaYi ', '1', '340', '340010070', ' jiayi ', ' 嘉义 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:17', '2017-02-14 12:16:17', '1126', ' 宜兰县 ', ' YiLanXian ', '1', '340', '340010080', ' yilanxian ', ' 宜兰县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:17', '2017-02-14 12:16:17', '1127', ' 桃园县 ', ' TaoYuanXian ', '1', '340', '340010090', ' taoyuanxian ', ' 桃园县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:17', '2017-02-14 12:16:17', '1128', ' 苗栗县 ', ' MiaoLiXian ', '1', '340', '340010100', ' miaolixian ', ' 苗栗县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:17', '2017-02-14 12:16:17', '1129', ' 彰化县 ', ' ZhangHuaXian ', '1', '340', '340010110', ' zhanghuaxian ', ' 彰化县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:17', '2017-02-14 12:16:17', '1130', ' 南投县 ', ' NanTouXian ', '1', '340', '340010120', ' nantouxian ', ' 南投县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:17', '2017-02-14 12:16:17', '1131', ' 云林县 ', ' YunLinXian ', '1', '340', '340010130', ' yunlinxian ', ' 云林县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:17', '2017-02-14 12:16:17', '1132', ' 屏东县 ', ' PingDongXian ', '1', '340', '340010140', ' pingdongxian ', ' 屏东县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:17', '2017-02-14 12:16:17', '1133', ' 台东县 ', ' TaiDongXian ', '1', '340', '340010150', ' taidongxian ', ' 台东县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:17', '2017-02-14 12:16:17', '1134', ' 花莲县 ', ' HuaLianXian ', '1', '340', '340010160', ' hualianxian ', ' 花莲县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:17', '2017-02-14 12:16:17', '1135', ' 澎湖县 ', ' PengHuXian ', '1', '340', '340010170', ' penghuxian ', ' 澎湖县 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:18', '2017-02-14 12:16:18', '1136', ' 亚洲 ', ' Asia ', '0', '', '350', ' asia ', ' 亚洲 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:18', '2017-02-14 12:16:18', '1137', ' 蒙古 ', ' Mongolia ', '1', '350', '350020', ' mongolia ', ' 蒙古 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:18', '2017-02-14 12:16:18', '1138', ' 朝鲜 ', ' North Korea ', '1', '350', '350030', ' north korea ', ' 朝鲜 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:18', '2017-02-14 12:16:18', '1139', ' 韩国 ', ' Korea ', '1', '350', '350040', ' korea ', ' 韩国 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:18', '2017-02-14 12:16:18', '1140', ' 日本 ', ' Japan ', '1', '350', '350050', ' japan ', ' 日本 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:18', '2017-02-14 12:16:18', '1141', ' 菲律宾 ', ' Philippines ', '1', '350', '350060', ' philippines ', ' 菲律宾 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:18', '2017-02-14 12:16:18', '1142', ' 越南 ', ' Vietnam ', '1', '350', '350070', ' vietnam ', ' 越南 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:18', '2017-02-14 12:16:18', '1143', ' 老挝 ', ' Laos ', '1', '350', '350080', ' laos ', ' 老挝 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:18', '2017-02-14 12:16:18', '1144', ' 柬埔寨 ', ' Cambodia ', '1', '350', '350090', ' cambodia ', ' 柬埔寨 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:18', '2017-02-14 12:16:18', '1145', ' 缅甸 ', ' Burma ', '1', '350', '350100', ' burma ', ' 缅甸 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:18', '2017-02-14 12:16:18', '1146', ' 泰国 ', ' Thailand ', '1', '350', '350110', ' thailand ', ' 泰国 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:18', '2017-02-14 12:16:18', '1147', ' 马来西亚 ', ' Malaysia ', '1', '350', '350120', ' malaysia ', ' 马来西亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:18', '2017-02-14 12:16:18', '1148', ' 文莱 ', ' Brunei ', '1', '350', '350130', ' brunei ', ' 文莱 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:19', '2017-02-14 12:16:19', '1149', ' 新加坡 ', ' Singapore ', '1', '350', '350140', ' singapore ', ' 新加坡 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:19', '2017-02-14 12:16:19', '1150', ' 印度尼西亚 ', ' Indonesia ', '1', '350', '350150', ' indonesia ', ' 印度尼西亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:19', '2017-02-14 12:16:19', '1151', ' 东帝汶 ', ' east Timor ', '1', '350', '350160', ' east timor ', ' 东帝汶 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:19', '2017-02-14 12:16:19', '1152', ' 尼泊尔 ', ' Nepal ', '1', '350', '350170', ' nepal ', ' 尼泊尔 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:19', '2017-02-14 12:16:19', '1153', ' 不丹 ', ' Bhutan ', '1', '350', '350180', ' bhutan ', ' 不丹 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:19', '2017-02-14 12:16:19', '1154', ' 孟加拉 ', ' Bangladesh ', '1', '350', '350190', ' bangladesh ', ' 孟加拉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:19', '2017-02-14 12:16:19', '1155', ' 印度 ', ' India ', '1', '350', '350200', ' india ', ' 印度 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:19', '2017-02-14 12:16:19', '1156', ' 巴基斯坦 ', ' Pakistan ', '1', '350', '350210', ' pakistan ', ' 巴基斯坦 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:19', '2017-02-14 12:16:19', '1157', ' 斯里兰卡 ', ' Sri Lanka ', '1', '350', '350220', ' sri lanka ', ' 斯里兰卡 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:19', '2017-02-14 12:16:19', '1158', ' 马尔代夫 ', ' Maldives ', '1', '350', '350230', ' maldives ', ' 马尔代夫 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:19', '2017-02-14 12:16:19', '1159', ' 哈萨克斯坦 ', ' Kazakhstan ', '1', '350', '350240', ' kazakhstan ', ' 哈萨克斯坦 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:19', '2017-02-14 12:16:19', '1160', ' 吉尔吉斯 ', ' Kyrghyzstan ', '1', '350', '350250', ' kyrghyzstan ', ' 吉尔吉斯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:19', '2017-02-14 12:16:19', '1161', ' 塔吉克斯坦 ', ' Tajikistan ', '1', '350', '350260', ' tajikistan ', ' 塔吉克斯坦 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:19', '2017-02-14 12:16:19', '1162', ' 乌兹别克 ', ' Uzbekistan ', '1', '350', '350270', ' uzbekistan ', ' 乌兹别克 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:20', '2017-02-14 12:16:20', '1163', ' 土库曼斯坦 ', ' Turkmenistan ', '1', '350', '350280', ' turkmenistan ', ' 土库曼斯坦 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:20', '2017-02-14 12:16:20', '1164', ' 阿富汗 ', ' Afghanistan ', '1', '350', '350290', ' afghanistan ', ' 阿富汗 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:20', '2017-02-14 12:16:20', '1165', ' 伊拉克 ', ' Iraq ', '1', '350', '350300', ' iraq ', ' 伊拉克 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:20', '2017-02-14 12:16:20', '1166', ' 伊朗 ', ' Iran ', '1', '350', '350310', ' iran ', ' 伊朗 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:20', '2017-02-14 12:16:20', '1167', ' 叙利亚 ', ' Syria ', '1', '350', '350320', ' syria ', ' 叙利亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:20', '2017-02-14 12:16:20', '1168', ' 约旦 ', ' Jordan ', '1', '350', '350330', ' jordan ', ' 约旦 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:20', '2017-02-14 12:16:20', '1169', ' 黎巴嫩 ', ' Lebanon ', '1', '350', '350340', ' lebanon ', ' 黎巴嫩 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:20', '2017-02-14 12:16:20', '1170', ' 以色列 ', ' Israel ', '1', '350', '350350', ' israel ', ' 以色列 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:20', '2017-02-14 12:16:20', '1171', ' 巴勒斯坦 ', ' Palestine ', '1', '350', '350360', ' palestine ', ' 巴勒斯坦 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:20', '2017-02-14 12:16:20', '1172', ' 沙特阿拉伯 ', ' Saudi Arabia ', '1', '350', '350370', ' saudi arabia ', ' 沙特阿拉伯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:20', '2017-02-14 12:16:20', '1173', ' 巴林 ', ' Bahrain ', '1', '350', '350380', ' bahrain ', ' 巴林 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:20', '2017-02-14 12:16:20', '1174', ' 卡塔尔 ', ' Qatar ', '1', '350', '350390', ' qatar ', ' 卡塔尔 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:20', '2017-02-14 12:16:20', '1175', ' 科威特 ', ' Kuwait ', '1', '350', '350400', ' kuwait ', ' 科威特 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:20', '2017-02-14 12:16:20', '1176', ' 阿联酋 ', ' United Arab Emirates ', '1', '350', '350410', ' united arab emirates ', ' 阿联酋 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:20', '2017-02-14 12:16:20', '1177', ' 阿曼 ', ' Oman ', '1', '350', '350420', ' oman ', ' 阿曼 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:21', '2017-02-14 12:16:21', '1178', ' 也门 ', ' Yemen ', '1', '350', '350430', ' yemen ', ' 也门 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:21', '2017-02-14 12:16:21', '1179', ' 格鲁吉亚 ', ' Georgia ', '1', '350', '350440', ' georgia ', ' 格鲁吉亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:21', '2017-02-14 12:16:21', '1180', ' 亚美尼亚 ', ' Armenia ', '1', '350', '350450', ' armenia ', ' 亚美尼亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:21', '2017-02-14 12:16:21', '1181', ' 阿塞拜疆 ', ' Azerbaijan ', '1', '350', '350460', ' azerbaijan ', ' 阿塞拜疆 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:21', '2017-02-14 12:16:21', '1182', ' 土耳其 ', ' Turkey ', '1', '350', '350470', ' turkey ', ' 土耳其 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:21', '2017-02-14 12:16:21', '1183', ' 塞浦路斯 ', ' Cyprus ', '1', '350', '350480', ' cyprus ', ' 塞浦路斯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:21', '2017-02-14 12:16:21', '1184', ' 北美洲 ', ' North America ', '0', '', '360', ' northamerica ', ' 北美洲 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:21', '2017-02-14 12:16:21', '1185', ' 加拿大 ', ' Canada ', '1', '360', '360020', ' canada ', ' 加拿大 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:21', '2017-02-14 12:16:21', '1186', ' 美国 ', ' America ', '1', '360', '360030', ' america ', ' 美国 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:21', '2017-02-14 12:16:21', '1187', ' 墨西哥 ', ' Mexico ', '1', '360', '360040', ' mexico ', ' 墨西哥 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:21', '2017-02-14 12:16:21', '1188', ' 格陵兰 ', ' Greenland ', '1', '360', '360050', ' greenland ', ' 格陵兰 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:21', '2017-02-14 12:16:21', '1189', ' 危地马拉 ', ' Guatemala ', '1', '360', '360060', ' guatemala ', ' 危地马拉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:21', '2017-02-14 12:16:21', '1190', ' 伯利兹 ', ' Belize ', '1', '360', '360070', ' belize ', ' 伯利兹 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:21', '2017-02-14 12:16:21', '1191', ' 萨尔瓦多 ', ' Salvador ', '1', '360', '360080', ' salvador ', ' 萨尔瓦多 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:22', '2017-02-14 12:16:22', '1192', ' 洪都拉斯 ', ' Honduras ', '1', '360', '360090', ' honduras ', ' 洪都拉斯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:22', '2017-02-14 12:16:22', '1193', ' 尼加拉瓜 ', ' Nicaragua ', '1', '360', '360100', ' nicaragua ', ' 尼加拉瓜 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:22', '2017-02-14 12:16:22', '1194', ' 哥斯达黎加 ', ' Costa Rica ', '1', '360', '360110', ' costa rica ', ' 哥斯达黎加 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:22', '2017-02-14 12:16:22', '1195', ' 巴拿马 ', ' Panama ', '1', '360', '360120', ' panama ', ' 巴拿马 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:22', '2017-02-14 12:16:22', '1196', ' 巴哈马 ', ' Bahamas ', '1', '360', '360130', ' bahamas ', ' 巴哈马 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:22', '2017-02-14 12:16:22', '1197', ' 古巴 ', ' Cuba ', '1', '360', '360140', ' cuba ', ' 古巴 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:22', '2017-02-14 12:16:22', '1198', ' 牙买加 ', ' Jamaica ', '1', '360', '360150', ' jamaica ', ' 牙买加 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:22', '2017-02-14 12:16:22', '1199', ' 海地 ', ' Haiti ', '1', '360', '360160', ' haiti ', ' 海地 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:22', '2017-02-14 12:16:22', '1200', ' 多米尼加 ', ' Dominican Republic ', '1', '360', '360170', ' dominican republic ', ' 多米尼加 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:22', '2017-02-14 12:16:22', '1201', ' 安提瓜 ', ' Antigua and Barbuda ', '1', '360', '360180', ' antigua and barbuda ', ' 安提瓜 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:22', '2017-02-14 12:16:22', '1202', ' 圣基茨 ', ' St. Kitts and Nevis ', '1', '360', '360190', ' st. kitts and nevis ', ' 圣基茨 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:22', '2017-02-14 12:16:22', '1203', ' 多米尼克 ', ' Dominica ', '1', '360', '360200', ' dominica ', ' 多米尼克 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:22', '2017-02-14 12:16:22', '1204', ' 圣卢西亚 ', ' Saint Lucia ', '1', '360', '360210', ' saint lucia ', ' 圣卢西亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:22', '2017-02-14 12:16:22', '1205', ' 圣文森特 ', ' Saint Vincent and the Grenadines ', '1', '360', '360220', ' saint vincent and the grenadines ', ' 圣文森特 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:22', '2017-02-14 12:16:22', '1206', ' 格林纳达 ', ' Grenada ', '1', '360', '360230', ' grenada ', ' 格林纳达 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:23', '2017-02-14 12:16:23', '1207', ' 巴巴多斯 ', ' Barbados ', '1', '360', '360240', ' barbados ', ' 巴巴多斯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:23', '2017-02-14 12:16:23', '1208', ' 特立尼达 ', ' Trinidad and Tobago ', '1', '360', '360250', ' trinidad and tobago ', ' 特立尼达 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:23', '2017-02-14 12:16:23', '1209', ' 波多黎各 ', ' Puerto Rico ', '1', '360', '360260', ' puerto rico ', ' 波多黎各 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:23', '2017-02-14 12:16:23', '1210', ' 英属维尔京 ', ' British Virgin Islands ', '1', '360', '360270', ' british virgin islands ', ' 英属维尔京群岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:23', '2017-02-14 12:16:23', '1211', ' 美属维尔京 ', ' Virgin Islands ', '1', '360', '360280', ' virgin islands ', ' 美属维尔京群岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:23', '2017-02-14 12:16:23', '1212', ' 安圭拉 ', ' Anguilla ', '1', '360', '360290', ' anguilla ', ' 安圭拉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:23', '2017-02-14 12:16:23', '1213', ' 蒙特塞拉特 ', ' Montserrat ', '1', '360', '360300', ' montserrat ', ' 蒙特塞拉特 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:23', '2017-02-14 12:16:23', '1214', ' 瓜德罗普 ', ' Guadeloupe ', '1', '360', '360310', ' guadeloupe ', ' 瓜德罗普 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:23', '2017-02-14 12:16:23', '1215', ' 马提尼克 ', ' martinique ', '1', '360', '360320', ' martinique ', ' 马提尼克 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:23', '2017-02-14 12:16:23', '1216', ' 安的列斯 ', ' Nederlandse Antillen ', '1', '360', '360330', ' nederlandse antillen ', ' 安的列斯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:23', '2017-02-14 12:16:23', '1217', ' 阿鲁巴 ', ' Aruba ', '1', '360', '360340', ' aruba ', ' 阿鲁巴 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:23', '2017-02-14 12:16:23', '1218', ' 特克斯 ', ' The turks and caicos islands ', '1', '360', '360350', ' the turks and caicos islands ', ' 特克斯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:23', '2017-02-14 12:16:23', '1219', ' 开曼群岛 ', ' Cayman Islands ', '1', '360', '360360', ' cayman islands ', ' 开曼群岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:23', '2017-02-14 12:16:23', '1220', ' 百慕大 ', ' Bermuda ', '1', '360', '360370', ' bermuda ', ' 百慕大 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:23', '2017-02-14 12:16:23', '1221', ' 南美洲 ', ' South America ', '0', '', '370', ' southamerica ', ' 南美洲 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:24', '2017-02-14 12:16:24', '1222', ' 哥伦比亚 ', ' Columbia ', '1', '370', '370020', ' columbia ', ' 哥伦比亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:24', '2017-02-14 12:16:24', '1223', ' 委内瑞拉 ', ' Venezuela ', '1', '370', '370030', ' venezuela ', ' 委内瑞拉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:24', '2017-02-14 12:16:24', '1224', ' 圭亚那 ', ' Guyana ', '1', '370', '370040', ' guyana ', ' 圭亚那 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:24', '2017-02-14 12:16:24', '1225', ' 法属圭亚那 ', ' French Guiana ', '1', '370', '370050', ' french guiana ', ' 法属圭亚那 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:24', '2017-02-14 12:16:24', '1226', ' 苏里南 ', ' Surinam ', '1', '370', '370060', ' surinam ', ' 苏里南 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:24', '2017-02-14 12:16:24', '1227', ' 厄瓜多尔 ', ' Ecuador ', '1', '370', '370070', ' ecuador ', ' 厄瓜多尔 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:24', '2017-02-14 12:16:24', '1228', ' 秘鲁 ', ' Peru ', '1', '370', '370080', ' peru ', ' 秘鲁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:24', '2017-02-14 12:16:24', '1229', ' 玻利维亚 ', ' Bolivia ', '1', '370', '370090', ' bolivia ', ' 玻利维亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:24', '2017-02-14 12:16:24', '1230', ' 巴西 ', ' Brazil ', '1', '370', '370100', ' brazil ', ' 巴西 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:24', '2017-02-14 12:16:24', '1231', ' 智利 ', ' Chile ', '1', '370', '370110', ' chile ', ' 智利 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:24', '2017-02-14 12:16:24', '1232', ' 阿根廷 ', ' Argentina ', '1', '370', '370120', ' argentina ', ' 阿根廷 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:24', '2017-02-14 12:16:24', '1233', ' 乌拉圭 ', ' Uruguay ', '1', '370', '370130', ' uruguay ', ' 乌拉圭 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:25', '2017-02-14 12:16:25', '1234', ' 巴拉圭 ', ' Paraguay ', '1', '370', '370140', ' paraguay ', ' 巴拉圭 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:25', '2017-02-14 12:16:25', '1235', ' 大洋洲 ', ' Oceania ', '0', '', '380', ' oceania ', ' 大洋洲 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:25', '2017-02-14 12:16:25', '1236', ' 澳大利亚 ', ' Australia ', '1', '380', '380020', ' australia ', ' 澳大利亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:25', '2017-02-14 12:16:25', '1237', ' 新西兰 ', ' New Zealand ', '1', '380', '380030', ' new zealand ', ' 新西兰 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:25', '2017-02-14 12:16:25', '1238', ' 巴布亚 ', ' Papua New Guinea ', '1', '380', '380040', ' papua new guinea ', ' 巴布亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:25', '2017-02-14 12:16:25', '1239', ' 所罗门群岛 ', ' Solomon Islands ', '1', '380', '380050', ' solomon islands ', ' 所罗门群岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:25', '2017-02-14 12:16:25', '1240', ' 瓦努阿图 ', ' Vanuatu ', '1', '380', '380060', ' vanuatu ', ' 瓦努阿图 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:25', '2017-02-14 12:16:25', '1241', ' 密克罗尼西亚 ', ' Micronesia ', '1', '380', '380070', ' micronesia ', ' 密克罗尼西亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:25', '2017-02-14 12:16:25', '1242', ' 马绍尔群岛 ', ' Marshall Islands ', '1', '380', '380080', ' marshall islands ', ' 马绍尔群岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:25', '2017-02-14 12:16:25', '1243', ' 帕劳群岛 ', ' Palau ', '1', '380', '380090', ' palau ', ' 帕劳群岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:25', '2017-02-14 12:16:25', '1244', ' 瑙鲁 ', ' Nauru ', '1', '380', '380100', ' nauru ', ' 瑙鲁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:25', '2017-02-14 12:16:25', '1245', ' 基里巴斯 ', ' Kiribati ', '1', '380', '380110', ' kiribati ', ' 基里巴斯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:25', '2017-02-14 12:16:25', '1246', ' 图瓦卢 ', ' Tuvalu ', '1', '380', '380120', ' tuvalu ', ' 图瓦卢 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:26', '2017-02-14 12:16:26', '1247', ' 萨摩亚 ', ' Samoa ', '1', '380', '380130', ' samoa ', ' 萨摩亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:26', '2017-02-14 12:16:26', '1248', ' 斐济群岛 ', ' Fiji Islands ', '1', '380', '380140', ' fiji islands ', ' 斐济群岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:26', '2017-02-14 12:16:26', '1249', ' 汤加 ', ' Tonga ', '1', '380', '380150', ' tonga ', ' 汤加 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:26', '2017-02-14 12:16:26', '1250', ' 库克群岛 ', ' Cook Islands ', '1', '380', '380160', ' cook islands ', ' 库克群岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:26', '2017-02-14 12:16:26', '1251', ' 关岛 ', ' Guam ', '1', '380', '380170', ' guam ', ' 关岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:26', '2017-02-14 12:16:26', '1252', ' 新喀里多尼亚 ', ' New Caledonia ', '1', '380', '380180', ' new caledonia ', ' 新喀里多尼亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:26', '2017-02-14 12:16:26', '1253', ' 波利尼西亚 ', ' Polynesia ', '1', '380', '380190', ' polynesia ', ' 波利尼西亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:26', '2017-02-14 12:16:26', '1254', ' 皮特凯恩岛 ', ' Pitcairn Island ', '1', '380', '380200', ' pitcairn island ', ' 皮特凯恩岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:26', '2017-02-14 12:16:26', '1255', ' 瓦利斯 ', ' Wallis and Futuna ', '1', '380', '380210', ' wallis and futuna ', ' 瓦利斯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:26', '2017-02-14 12:16:26', '1256', ' 纽埃 ', ' Niue ', '1', '380', '380220', ' niue ', ' 纽埃 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:26', '2017-02-14 12:16:26', '1257', ' 托克劳 ', ' Tokelau ', '1', '380', '380230', ' tokelau ', ' 托克劳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:26', '2017-02-14 12:16:26', '1258', ' 美属萨摩亚 ', ' American Samoa ', '1', '380', '380240', ' american samoa ', ' 美属萨摩亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:26', '2017-02-14 12:16:26', '1259', ' 北马里亚纳 ', ' Northern Marianas ', '1', '380', '380250', ' northern marianas ', ' 北马里亚纳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:26', '2017-02-14 12:16:26', '1260', ' 欧洲 ', ' Europe ', '0', '', '390', ' europe ', ' 欧洲 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:26', '2017-02-14 12:16:26', '1261', ' 芬兰 ', ' Finland ', '1', '390', '390020', ' finland ', ' 芬兰 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:27', '2017-02-14 12:16:27', '1262', ' 瑞典 ', ' Sweden ', '1', '390', '390030', ' sweden ', ' 瑞典 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:27', '2017-02-14 12:16:27', '1263', ' 挪威 ', ' Norway ', '1', '390', '390040', ' norway ', ' 挪威 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:27', '2017-02-14 12:16:27', '1264', ' 冰岛 ', ' Iceland ', '1', '390', '390050', ' iceland ', ' 冰岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:27', '2017-02-14 12:16:27', '1265', ' 丹麦 ', ' Denmark ', '1', '390', '390060', ' denmark ', ' 丹麦 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:27', '2017-02-14 12:16:27', '1266', ' 法罗群岛 ', ' Faroe islands ', '1', '390', '390070', ' faroe islands ', ' 法罗群岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:27', '2017-02-14 12:16:27', '1267', ' 爱沙尼亚 ', ' Estonia ', '1', '390', '390080', ' estonia ', ' 爱沙尼亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:27', '2017-02-14 12:16:27', '1268', ' 拉脱维亚 ', ' Latvia ', '1', '390', '390090', ' latvia ', ' 拉脱维亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:27', '2017-02-14 12:16:27', '1269', ' 立陶宛 ', ' Lithuania ', '1', '390', '390100', ' lithuania ', ' 立陶宛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:27', '2017-02-14 12:16:27', '1270', ' 白俄罗斯 ', ' The Republic of Belarus ', '1', '390', '390110', ' belarus ', ' 白俄罗斯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:27', '2017-02-14 12:16:27', '1271', ' 俄罗斯 ', ' Russia ', '1', '390', '390120', ' russia ', ' 俄罗斯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:27', '2017-02-14 12:16:27', '1272', ' 乌克兰 ', ' Ukraine ', '1', '390', '390130', ' ukraine ', ' 乌克兰 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:27', '2017-02-14 12:16:27', '1273', ' 摩尔多瓦 ', ' Moldova ', '1', '390', '390140', ' moldova ', ' 摩尔多瓦 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:27', '2017-02-14 12:16:27', '1274', ' 波兰 ', ' Poland ', '1', '390', '390150', ' poland ', ' 波兰 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:27', '2017-02-14 12:16:27', '1275', ' 捷克 ', ' Czechoslovakia ', '1', '390', '390160', ' czechoslovakia ', ' 捷克 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:28', '2017-02-14 12:16:28', '1276', ' 匈牙利 ', ' Hungary ', '1', '390', '390170', ' hungary ', ' 匈牙利 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:28', '2017-02-14 12:16:28', '1277', ' 德国 ', ' Germany ', '1', '390', '390180', ' germany ', ' 德国 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:28', '2017-02-14 12:16:28', '1278', ' 奥地利 ', ' Austria ', '1', '390', '390190', ' austria ', ' 奥地利 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:28', '2017-02-14 12:16:28', '1279', ' 瑞士 ', ' Switzerland ', '1', '390', '390200', ' switzerland ', ' 瑞士 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:28', '2017-02-14 12:16:28', '1280', ' 列支敦士登 ', ' Liechtenstein ', '1', '390', '390210', ' liechtenstein ', ' 列支敦士登 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:28', '2017-02-14 12:16:28', '1281', ' 英国 ', ' United Kingdom ', '1', '390', '390220', ' United Kingdom ', ' 英国 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:28', '2017-02-14 12:16:28', '1282', ' 爱尔兰 ', ' Ireland ', '1', '390', '390230', ' ireland ', ' 爱尔兰 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:28', '2017-02-14 12:16:28', '1283', ' 荷兰 ', ' Netherlands ', '1', '390', '390240', ' netherlands ', ' 荷兰 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:28', '2017-02-14 12:16:28', '1284', ' 比利时 ', ' Belgium ', '1', '390', '390250', ' belgium ', ' 比利时 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:28', '2017-02-14 12:16:28', '1285', ' 卢森堡 ', ' Luxembourg ', '1', '390', '390260', ' luxembourg ', ' 卢森堡 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:28', '2017-02-14 12:16:28', '1286', ' 法国 ', ' France ', '1', '390', '390270', ' france ', ' 法国 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:28', '2017-02-14 12:16:28', '1287', ' 摩纳哥 ', ' Monaco ', '1', '390', '390280', ' monaco ', ' 摩纳哥 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:28', '2017-02-14 12:16:28', '1288', ' 罗马尼亚 ', ' Roumania ', '1', '390', '390290', ' roumania ', ' 罗马尼亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:28', '2017-02-14 12:16:28', '1289', ' 保加利亚 ', ' Bulgaria ', '1', '390', '390300', ' bulgaria ', ' 保加利亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:28', '2017-02-14 12:16:28', '1290', ' 塞尔维亚 ', ' Serbia ', '1', '390', '390310', ' serbia ', ' 塞尔维亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:29', '2017-02-14 12:16:29', '1291', ' 马其顿 ', ' Macedonia ', '1', '390', '390320', ' macedonia ', ' 马其顿 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:29', '2017-02-14 12:16:29', '1292', ' 阿尔巴尼亚 ', ' Albania ', '1', '390', '390330', ' albania ', ' 阿尔巴尼亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:29', '2017-02-14 12:16:29', '1293', ' 希腊 ', ' Greece ', '1', '390', '390340', ' greece ', ' 希腊 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:29', '2017-02-14 12:16:29', '1294', ' 斯洛文尼亚 ', ' Slovenia ', '1', '390', '390350', ' slovenia ', ' 斯洛文尼亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:29', '2017-02-14 12:16:29', '1295', ' 克罗地亚 ', ' Croatia ', '1', '390', '390360', ' croatia ', ' 克罗地亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:29', '2017-02-14 12:16:29', '1296', ' 波墨 ', ' Bosnia and ink plug elder brother d that ', '1', '390', '390370', ' bosnia and ink plug elder brother d that ', ' 波墨 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:29', '2017-02-14 12:16:29', '1297', ' 意大利 ', ' Italy ', '1', '390', '390380', ' italy ', ' 意大利 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:29', '2017-02-14 12:16:29', '1298', ' 梵蒂冈 ', ' Vatican ', '1', '390', '390390', ' vatican ', ' 梵蒂冈 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:29', '2017-02-14 12:16:29', '1299', ' 圣马力诺 ', ' San Marino ', '1', '390', '390400', ' san marino ', ' 圣马力诺 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:29', '2017-02-14 12:16:29', '1300', ' 马耳他 ', ' Malta ', '1', '390', '390410', ' malta ', ' 马耳他 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:29', '2017-02-14 12:16:29', '1301', ' 西班牙 ', ' Spain ', '1', '390', '390420', ' spain ', ' 西班牙 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:29', '2017-02-14 12:16:29', '1302', ' 葡萄牙 ', ' Portugal ', '1', '390', '390430', ' portugal ', ' 葡萄牙 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:29', '2017-02-14 12:16:29', '1303', ' 安道尔 ', ' Andorra ', '1', '390', '390440', ' andorra ', ' 安道尔 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:29', '2017-02-14 12:16:29', '1304', ' 斯洛伐克 ', ' The Slovak Republic ', '1', '390', '390450', ' the slovak republic ', ' 斯洛伐克 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:30', '2017-02-14 12:16:30', '1305', ' 非洲 ', ' Africa ', '0', '', '400', ' africa ', ' 非洲 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:30', '2017-02-14 12:16:30', '1306', ' 埃及 ', ' Egypt ', '1', '400', '400020', ' egypt ', ' 埃及 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:30', '2017-02-14 12:16:30', '1307', ' 利比亚 ', ' Libya ', '1', '400', '400030', ' libya ', ' 利比亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:30', '2017-02-14 12:16:30', '1308', ' 苏丹 ', ' Sultan ', '1', '400', '400040', ' sultan ', ' 苏丹 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:30', '2017-02-14 12:16:30', '1309', ' 突尼斯 ', ' Tunisia ', '1', '400', '400050', ' tunisia ', ' 突尼斯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:30', '2017-02-14 12:16:30', '1310', ' 阿尔及利亚 ', ' Algeria ', '1', '400', '400060', ' algeria ', ' 阿尔及利亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:30', '2017-02-14 12:16:30', '1311', ' 摩洛哥 ', ' Morocco ', '1', '400', '400070', ' morocco ', ' 摩洛哥 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:30', '2017-02-14 12:16:30', '1312', ' 亚速尔群岛 ', ' Azores ', '1', '400', '400080', ' azores ', ' 亚速尔群岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:30', '2017-02-14 12:16:30', '1313', ' 马德拉群岛 ', ' Madeira ', '1', '400', '400090', ' madeira ', ' 马德拉群岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:30', '2017-02-14 12:16:30', '1314', ' 埃塞俄比亚 ', ' Ethiopia ', '1', '400', '400100', ' ethiopia ', ' 埃塞俄比亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:30', '2017-02-14 12:16:30', '1315', ' 厄立特里亚 ', ' Eritrea ', '1', '400', '400110', ' eritrea ', ' 厄立特里亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:30', '2017-02-14 12:16:30', '1316', ' 索马里 ', ' Somalia ', '1', '400', '400120', ' somalia ', ' 索马里 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:30', '2017-02-14 12:16:30', '1317', ' 吉布提 ', ' Djibouti ', '1', '400', '400130', ' djibouti ', ' 吉布提 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:30', '2017-02-14 12:16:30', '1318', ' 肯尼亚 ', ' Kenya ', '1', '400', '400140', ' kenya ', ' 肯尼亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:31', '2017-02-14 12:16:31', '1319', ' 坦桑尼亚 ', ' Tanzania ', '1', '400', '400150', ' tanzania ', ' 坦桑尼亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:31', '2017-02-14 12:16:31', '1320', ' 乌干达 ', ' Uganda ', '1', '400', '400160', ' uganda ', ' 乌干达 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:31', '2017-02-14 12:16:31', '1321', ' 卢旺达 ', ' Rwanda ', '1', '400', '400170', ' rwanda ', ' 卢旺达 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:31', '2017-02-14 12:16:31', '1322', ' 布隆迪 ', ' Burundi ', '1', '400', '400180', ' burundi ', ' 布隆迪 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:31', '2017-02-14 12:16:31', '1323', ' 塞舌尔 ', ' Seychelles ', '1', '400', '400190', ' seychelles ', ' 塞舌尔 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:31', '2017-02-14 12:16:31', '1324', ' 乍得 ', ' Chad ', '1', '400', '400200', ' chad ', ' 乍得 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:31', '2017-02-14 12:16:31', '1325', ' 中非 ', ' Central Africa ', '1', '400', '400210', ' central africa ', ' 中非 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:31', '2017-02-14 12:16:31', '1326', ' 喀麦隆 ', ' Cameroon ', '1', '400', '400220', ' cameroon ', ' 喀麦隆 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:31', '2017-02-14 12:16:31', '1327', ' 赤道几内亚 ', ' Equatorial Guinea ', '1', '400', '400230', ' equatorial guinea ', ' 赤道几内亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:31', '2017-02-14 12:16:31', '1328', ' 加蓬 ', ' Gabon ', '1', '400', '400240', ' gabon ', ' 加蓬 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:31', '2017-02-14 12:16:31', '1329', ' 刚果 ', ' Congo ', '1', '400', '400250', ' congo ', ' 刚果 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:31', '2017-02-14 12:16:31', '1330', ' 圣普 ', ' Sao Tome and Principe ', '1', '400', '400260', ' sao tome and principe ', ' 圣普 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:31', '2017-02-14 12:16:31', '1331', ' 毛里塔尼亚 ', ' Mauritania ', '1', '400', '400270', ' mauritania ', ' 毛里塔尼亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:32', '2017-02-14 12:16:32', '1332', ' 西撒哈拉 ', ' EH West Sahara ', '1', '400', '400280', ' eh west sahara ', ' 西撒哈拉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:32', '2017-02-14 12:16:32', '1333', ' 塞内加尔 ', ' Senegal ', '1', '400', '400290', ' senegal ', ' 塞内加尔 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:32', '2017-02-14 12:16:32', '1334', ' 冈比亚 ', ' Gambia ', '1', '400', '400300', ' gambia ', ' 冈比亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:32', '2017-02-14 12:16:32', '1335', ' 马里 ', ' Mali ', '1', '400', '400310', ' mali ', ' 马里 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:32', '2017-02-14 12:16:32', '1336', ' 布基纳法索 ', ' Burkina faso ', '1', '400', '400320', ' burkina faso ', ' 布基纳法索 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:32', '2017-02-14 12:16:32', '1337', ' 几内亚 ', ' Guinea ', '1', '400', '400330', ' guinea ', ' 几内亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:32', '2017-02-14 12:16:32', '1338', ' 几内亚比绍 ', ' Guinea-Bissau ', '1', '400', '400340', ' guinea-bissau ', ' 几内亚比绍 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:32', '2017-02-14 12:16:32', '1339', ' 佛得角 ', ' Cape Verde ', '1', '400', '400350', ' cape verde ', ' 佛得角 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:32', '2017-02-14 12:16:32', '1340', ' 塞拉利昂 ', ' Sierra leone ', '1', '400', '400360', ' sierra leone ', ' 塞拉利昂 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:32', '2017-02-14 12:16:32', '1341', ' 利比里亚 ', ' Liberia ', '1', '400', '400370', ' liberia ', ' 利比里亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:32', '2017-02-14 12:16:32', '1342', ' 科特迪瓦 ', ' Cote divoire ', '1', '400', '400380', ' cote divoire ', ' 科特迪瓦 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:32', '2017-02-14 12:16:32', '1343', ' 加纳 ', ' Ghana ', '1', '400', '400390', ' ghana ', ' 加纳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:32', '2017-02-14 12:16:32', '1344', ' 多哥 ', ' Togo ', '1', '400', '400400', ' togo ', ' 多哥 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:32', '2017-02-14 12:16:32', '1345', ' 贝宁 ', ' Benin ', '1', '400', '400410', ' benin ', ' 贝宁 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:33', '2017-02-14 12:16:33', '1346', ' 尼日尔 ', ' The Niger ', '1', '400', '400420', ' the niger ', ' 尼日尔 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:33', '2017-02-14 12:16:33', '1347', ' 加那利群岛 ', ' Canary Islands ', '1', '400', '400430', ' canary islands ', ' 加那利群岛 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:33', '2017-02-14 12:16:33', '1348', ' 赞比亚 ', ' Zambia ', '1', '400', '400440', ' zambia ', ' 赞比亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:33', '2017-02-14 12:16:33', '1349', ' 安哥拉 ', ' Angola ', '1', '400', '400450', ' angola ', ' 安哥拉 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:33', '2017-02-14 12:16:33', '1350', ' 津巴布韦 ', ' Zimbabwe ', '1', '400', '400460', ' zimbabwe ', ' 津巴布韦 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:33', '2017-02-14 12:16:33', '1351', ' 马拉维 ', ' Malawi ', '1', '400', '400470', ' malawi ', ' 马拉维 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:33', '2017-02-14 12:16:33', '1352', ' 莫桑比克 ', ' Mozambique ', '1', '400', '400480', ' mozambique ', ' 莫桑比克 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:33', '2017-02-14 12:16:33', '1353', ' 博茨瓦纳 ', ' Botswana ', '1', '400', '400490', ' botswana ', ' 博茨瓦纳 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:33', '2017-02-14 12:16:33', '1354', ' 纳米比亚 ', ' Namibia ', '1', '400', '400500', ' namibia ', ' 纳米比亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:33', '2017-02-14 12:16:33', '1355', ' 南非 ', ' South Africa ', '1', '400', '400510', ' south africa ', ' 南非 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:33', '2017-02-14 12:16:33', '1356', ' 斯威士兰 ', ' Swaziland ', '1', '400', '400520', ' swaziland ', ' 斯威士兰 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:33', '2017-02-14 12:16:33', '1357', ' 莱索托 ', ' Lesotho ', '1', '400', '400530', ' lesotho ', ' 莱索托 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:33', '2017-02-14 12:16:33', '1358', ' 马达加斯加 ', ' Madagascar ', '1', '400', '400540', ' madagascar ', ' 马达加斯加 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:34', '2017-02-14 12:16:34', '1359', ' 科摩罗 ', ' Comorin ', '1', '400', '400550', ' comorin ', ' 科摩罗 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:34', '2017-02-14 12:16:34', '1360', ' 毛里求斯 ', ' Mauritius ', '1', '400', '400560', ' mauritius ', ' 毛里求斯 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:34', '2017-02-14 12:16:34', '1361', ' 留尼旺 ', ' Reunion ', '1', '400', '400570', ' reunion ', ' 留尼旺 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:34', '2017-02-14 12:16:34', '1362', ' 圣赫勒拿 ', ' Saint Helena ', '1', '400', '400580', ' saint helena ', ' 圣赫勒拿 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:34', '2017-02-14 12:16:34', '1363', ' 尼日利亚 ', ' Federal Republic of Nigeria ', '1', '400', '400590', ' federal republic of nigeria ', ' 尼日利亚 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:34', '2017-02-14 12:16:34', '1364', ' 中国 ', ' China ', '0', '', '410', ' china ', ' 中国 ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:34', '2017-02-14 12:16:34', '1365', ' 亚拉巴马州 ', ' Alabama ', '1', '360030', '420010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:34', '2017-02-14 12:16:34', '1366', ' 伯明翰 ', ' Birmingham ', '1', '420010', '420010010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:34', '2017-02-14 12:16:34', '1367', ' 蒙哥马利 ', ' Montgomery ', '1', '420010', '420010020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:34', '2017-02-14 12:16:34', '1368', ' 亨次维尔 ', ' Huntsville ', '1', '420010', '420010030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:34', '2017-02-14 12:16:34', '1369', ' 塔斯卡卢萨 ', ' Tuscaloosa ', '1', '420010', '420010040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:34', '2017-02-14 12:16:34', '1370', ' 莫比尔港 ', ' Mobile ', '1', '420010', '420010050', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:34', '2017-02-14 12:16:34', '1371', ' 阿拉斯加州 ', ' Alaska ', '1', '360030', '420020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:34', '2017-02-14 12:16:34', '1372', ' 朱诺 ', ' Juneau ', '1', '420020', '420020010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:34', '2017-02-14 12:16:34', '1373', ' 安克拉奇 ', ' Anchorage ', '1', '420020', '420020020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:35', '2017-02-14 12:16:35', '1374', ' 费尔班克斯 ', ' Fairbanks ', '1', '420020', '420020030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:35', '2017-02-14 12:16:35', '1375', ' 亚利桑那州 ', ' Arizona ', '1', '360030', '420030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:35', '2017-02-14 12:16:35', '1376', ' 菲尼克斯（凤凰城） ', ' Phoenix ', '1', '420030', '420030010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:35', '2017-02-14 12:16:35', '1377', ' 图森 ', ' Tucson ', '1', '420030', '420030020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:35', '2017-02-14 12:16:35', '1378', ' 梅萨 ', ' Mesa ', '1', '420030', '420030030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:35', '2017-02-14 12:16:35', '1379', ' 阿肯色州 ', ' Arkansas ', '1', '360030', '420040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:35', '2017-02-14 12:16:35', '1380', ' 小石城 ', ' Little Rock ', '1', '420040', '420040010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:35', '2017-02-14 12:16:35', '1381', ' 费耶特维尔 ', ' Fayetteville ', '1', '420040', '420040020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:35', '2017-02-14 12:16:35', '1382', ' 加利福尼亚州 ', ' California  ', '1', '360030', '420050', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:35', '2017-02-14 12:16:35', '1383', ' 萨克拉门托 ', ' Sacramento ', '1', '420050', '420050010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:35', '2017-02-14 12:16:35', '1384', ' 索诺马 ', ' Sonoma ', '1', '420050', '420050020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:35', '2017-02-14 12:16:35', '1385', ' 圣荷西 ', ' San Jose ', '1', '420050', '420050030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:35', '2017-02-14 12:16:35', '1386', ' 洛杉矶 ', ' Los Angeles ', '1', '420050', '420050040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:35', '2017-02-14 12:16:35', '1387', ' 圣地亚哥 ', ' San Diego ', '1', '420050', '420050050', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:35', '2017-02-14 12:16:35', '1388', ' 旧金山 ', ' San Francisco ', '1', '420050', '420050060', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:36', '2017-02-14 12:16:36', '1389', ' 科罗拉多州 ', ' Colorado  ', '1', '360030', '420060', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:36', '2017-02-14 12:16:36', '1390', ' 丹佛 ', ' Denver ', '1', '420060', '420060010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:36', '2017-02-14 12:16:36', '1391', ' 波尔德 ', ' Boulder ', '1', '420060', '420060020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:36', '2017-02-14 12:16:36', '1392', ' 科罗拉多斯普林斯  ', ' Clolrado Springs ', '1', '420060', '420060030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:36', '2017-02-14 12:16:36', '1393', ' 康涅狄格州 ', ' Connecticut  ', '1', '360030', '420070', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:36', '2017-02-14 12:16:36', '1394', ' 哈特福 ', ' Hartford ', '1', '420070', '420070010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:36', '2017-02-14 12:16:36', '1395', ' 特拉华州 ', ' Delaware  ', '1', '360030', '420080', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:36', '2017-02-14 12:16:36', '1396', ' 多佛 ', ' Dover ', '1', '420080', '420080010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:36', '2017-02-14 12:16:36', '1397', ' 维明顿 ', ' Wilmington ', '1', '420080', '420080020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:36', '2017-02-14 12:16:36', '1398', ' 纽华克 ', ' Newark ', '1', '420080', '420080030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:36', '2017-02-14 12:16:36', '1399', ' 佛罗里达州 ', ' Florida  ', '1', '360030', '420090', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:36', '2017-02-14 12:16:36', '1400', ' 塔拉赫西 ', ' Tallahassee ', '1', '420090', '420090010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:36', '2017-02-14 12:16:36', '1401', ' 坦帕 ', ' Tampa ', '1', '420090', '420090020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:36', '2017-02-14 12:16:36', '1402', ' 杰克逊维尔 ', ' Jacksonville ', '1', '420090', '420090030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:36', '2017-02-14 12:16:36', '1403', ' 迈阿密 ', ' Miami ', '1', '420090', '420090040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:37', '2017-02-14 12:16:37', '1404', ' 盖恩斯维尔 ', ' Gainesville ', '1', '420090', '420090050', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:37', '2017-02-14 12:16:37', '1405', ' 乔治亚州 ', ' Georgia  ', '1', '360030', '420100', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:37', '2017-02-14 12:16:37', '1406', ' 亚特兰大 ', ' Atlanta ', '1', '420100', '420100010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:37', '2017-02-14 12:16:37', '1407', ' 哥伦布 ', ' Columbus ', '1', '420100', '420100020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:37', '2017-02-14 12:16:37', '1408', ' 梅肯  ', ' Macon ', '1', '420100', '420100030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:37', '2017-02-14 12:16:37', '1409', ' 夏威夷州 ', ' Hawaii  ', '1', '360030', '420110', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:37', '2017-02-14 12:16:37', '1410', ' 檀香山 ', ' Honolulu ', '1', '420110', '420110010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:37', '2017-02-14 12:16:37', '1411', ' 爱达荷州 ', ' Idaho  ', '1', '360030', '420120', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:37', '2017-02-14 12:16:37', '1412', ' 波夕 ', ' Boise ', '1', '420120', '420120010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:37', '2017-02-14 12:16:37', '1413', ' 波卡特洛 ', ' Pocatello ', '1', '420120', '420120020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:37', '2017-02-14 12:16:37', '1414', ' 爱达荷福尔斯 ', ' Idaho Falls ', '1', '420120', '420120030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:37', '2017-02-14 12:16:37', '1415', ' 伊利诺伊州 ', ' Illinois ', '1', '360030', '420130', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:37', '2017-02-14 12:16:37', '1416', ' 春田 ', ' Springfield ', '1', '420130', '420130010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:37', '2017-02-14 12:16:37', '1417', ' 芝加哥 ', ' Chicago ', '1', '420130', '420130020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:38', '2017-02-14 12:16:38', '1418', ' 洛克福特 ', ' Rockford ', '1', '420130', '420130030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:38', '2017-02-14 12:16:38', '1419', ' 印第安那州 ', ' Indiana  ', '1', '360030', '420140', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:38', '2017-02-14 12:16:38', '1420', ' 印第安纳波利斯 ', ' Indianapolis ', '1', '420140', '420140010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:38', '2017-02-14 12:16:38', '1421', ' 韦恩堡 ', ' Fort Wayne ', '1', '420140', '420140020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:38', '2017-02-14 12:16:38', '1422', ' 伯明顿 ', ' Bloomington ', '1', '420140', '420140030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:38', '2017-02-14 12:16:38', '1423', ' 拉法叶 ', ' Lafayette ', '1', '420140', '420140040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:38', '2017-02-14 12:16:38', '1424', ' 爱荷华州 ', ' Iowa  ', '1', '360030', '420150', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:38', '2017-02-14 12:16:38', '1425', ' 得梅因 ', ' Des Moines ', '1', '420150', '420150010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:38', '2017-02-14 12:16:38', '1426', ' 锡达拉皮兹 ', ' Cedar Rapids ', '1', '420150', '420150020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:38', '2017-02-14 12:16:38', '1427', ' 丹芬堡特 ', ' Daven Port ', '1', '420150', '420150030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:38', '2017-02-14 12:16:38', '1428', ' 衣阿华城 ', ' Iowa City ', '1', '420150', '420150040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:38', '2017-02-14 12:16:38', '1429', ' 堪萨斯州 ', ' Kansas  ', '1', '360030', '420160', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:38', '2017-02-14 12:16:38', '1430', ' 托皮卡 ', ' Topeka ', '1', '420160', '420160010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:39', '2017-02-14 12:16:39', '1431', ' 威奇托 ', ' Wichita ', '1', '420160', '420160020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:39', '2017-02-14 12:16:39', '1432', ' 堪萨斯城 ', ' Kansas City ', '1', '420160', '420160030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:39', '2017-02-14 12:16:39', '1433', ' 罗伦斯 ', ' Lawrence ', '1', '420160', '420160040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:39', '2017-02-14 12:16:39', '1434', ' 肯塔基州 ', ' Kentucky  ', '1', '360030', '420170', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:39', '2017-02-14 12:16:39', '1435', ' 路易斯维尔 ', ' Louisville ', '1', '420170', '420170010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:39', '2017-02-14 12:16:39', '1436', ' 列克星敦 ', ' Lexington ', '1', '420170', '420170020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:39', '2017-02-14 12:16:39', '1437', ' 路易斯安那州 ', ' Louisiana  ', '1', '360030', '420180', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:39', '2017-02-14 12:16:39', '1438', ' 新奥尔良 ', ' New Orleans ', '1', '420180', '420180010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:39', '2017-02-14 12:16:39', '1439', ' 缅因州 ', ' Maine  ', '1', '360030', '420190', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:39', '2017-02-14 12:16:39', '1440', ' 奥古斯塔 ', ' Augusta ', '1', '420190', '420190010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:39', '2017-02-14 12:16:39', '1441', ' 波特兰 ', ' Portland ', '1', '420190', '420190020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:39', '2017-02-14 12:16:39', '1442', ' 马里兰州 ', ' Maryland  ', '1', '360030', '420200', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:39', '2017-02-14 12:16:39', '1443', ' 安纳波利斯 ', ' Annapolis ', '1', '420200', '420200010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:40', '2017-02-14 12:16:40', '1444', ' 巴尔的摩 ', ' Baltimore ', '1', '420200', '420200020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:40', '2017-02-14 12:16:40', '1445', ' 洛克威尔 ', ' Rockville ', '1', '420200', '420200030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:40', '2017-02-14 12:16:40', '1446', ' 麻萨诸塞州 ', ' Massachusetts  ', '1', '360030', '420210', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:40', '2017-02-14 12:16:40', '1447', ' 波士顿 ', ' Boston ', '1', '420210', '420210010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:40', '2017-02-14 12:16:40', '1448', ' 伍斯特 ', ' Worcester ', '1', '420210', '420210020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:40', '2017-02-14 12:16:40', '1449', ' 密歇根州 ', ' Michigan  ', '1', '360030', '420220', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:40', '2017-02-14 12:16:40', '1450', ' 兰辛 ', ' Lansing ', '1', '420220', '420220010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:40', '2017-02-14 12:16:40', '1451', ' 底特律 ', ' Detroit ', '1', '420220', '420220020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:40', '2017-02-14 12:16:40', '1452', ' 大溪城 ', ' Grand Rapids ', '1', '420220', '420220030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:40', '2017-02-14 12:16:40', '1453', ' 弗林特 ', ' Flint ', '1', '420220', '420220040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:40', '2017-02-14 12:16:40', '1454', ' 明尼苏达州 ', ' Minnesota  ', '1', '360030', '420230', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:40', '2017-02-14 12:16:40', '1455', ' 圣保罗 ', ' Saint Paul ', '1', '420230', '420230010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:40', '2017-02-14 12:16:40', '1456', ' 明尼阿波利斯 ', ' Minneapolis ', '1', '420230', '420230020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:40', '2017-02-14 12:16:40', '1457', ' 杜鲁司 ', ' Duluth ', '1', '420230', '420230030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:41', '2017-02-14 12:16:41', '1458', ' 密西西比州 ', ' Mississippi  ', '1', '360030', '420240', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:41', '2017-02-14 12:16:41', '1459', ' 杰克逊 ', ' Jackson ', '1', '420240', '420240010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:41', '2017-02-14 12:16:41', '1460', ' 密烈地安 ', ' Meridian ', '1', '420240', '420240020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:41', '2017-02-14 12:16:41', '1461', ' 密苏里州 ', ' Missouri  ', '1', '360030', '420250', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:41', '2017-02-14 12:16:41', '1462', ' 杰佛逊城 ', ' Jefferson City ', '1', '420250', '420250010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:41', '2017-02-14 12:16:41', '1463', ' 圣路易斯 ', ' Saint Louis ', '1', '420250', '420250020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:41', '2017-02-14 12:16:41', '1464', ' 堪萨斯城 ', ' Kansas City ', '1', '420250', '420250030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:41', '2017-02-14 12:16:41', '1465', ' 洛拉 ', ' Rolla ', '1', '420250', '420250040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:41', '2017-02-14 12:16:41', '1466', ' 蒙大拿州 ', ' Montana  ', '1', '360030', '420260', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:41', '2017-02-14 12:16:41', '1467', ' 海伦娜 ', ' Heldna ', '1', '420260', '420260010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:41', '2017-02-14 12:16:41', '1468', ' 比林斯 ', ' Billings ', '1', '420260', '420260020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:41', '2017-02-14 12:16:41', '1469', ' 密苏拉 ', ' Missoula ', '1', '420260', '420260030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:41', '2017-02-14 12:16:41', '1470', ' 内布拉斯加州 ', ' Nebraska  ', '1', '360030', '420270', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:41', '2017-02-14 12:16:41', '1471', ' 林肯 ', ' Lincoln ', '1', '420270', '420270010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:41', '2017-02-14 12:16:41', '1472', ' 内华达州 ', ' Nevada  ', '1', '360030', '420280', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:42', '2017-02-14 12:16:42', '1473', ' 卡森城 ', ' Carson City ', '1', '420280', '420280010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:42', '2017-02-14 12:16:42', '1474', ' 拉斯维加斯 ', ' Las Vegas ', '1', '420280', '420280020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:42', '2017-02-14 12:16:42', '1475', ' 里诺 ', ' Reno ', '1', '420280', '420280030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:42', '2017-02-14 12:16:42', '1476', ' 新罕布什尔州 ', ' New Hampshire  ', '1', '360030', '420290', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:42', '2017-02-14 12:16:42', '1477', ' 曼彻斯特 ', ' Manchester ', '1', '420290', '420290010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:42', '2017-02-14 12:16:42', '1478', ' 南雪 ', ' Nashua ', '1', '420290', '420290020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:42', '2017-02-14 12:16:42', '1479', ' 朴次茅斯 ', ' Portsmouth ', '1', '420290', '420290030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:42', '2017-02-14 12:16:42', '1480', ' 新泽西州 ', ' New Jersey ', '1', '360030', '420300', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:42', '2017-02-14 12:16:42', '1481', ' 纽瓦克 ', ' Newark ', '1', '420300', '420300010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:42', '2017-02-14 12:16:42', '1482', ' 泽西市 ', ' Jersey City ', '1', '420300', '420300020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:42', '2017-02-14 12:16:42', '1483', ' 大西洋城 ', ' Atlantic City ', '1', '420300', '420300030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:42', '2017-02-14 12:16:42', '1484', ' 依丽沙白 ', ' Elizabeth ', '1', '420300', '420300040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:42', '2017-02-14 12:16:42', '1485', ' 新墨西哥州 ', ' New Mexico  ', '1', '360030', '420310', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:42', '2017-02-14 12:16:42', '1486', ' 圣达菲 ', ' Santa Fe ', '1', '420310', '420310010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:42', '2017-02-14 12:16:42', '1487', ' 阿尔布开克 ', ' Albuquerque ', '1', '420310', '420310020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:43', '2017-02-14 12:16:43', '1488', ' 纽约州 ', ' New York ', '1', '360030', '420320', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:43', '2017-02-14 12:16:43', '1489', ' 奥尔巴尼（水牛城） ', ' Albany ', '1', '420320', '420320010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:43', '2017-02-14 12:16:43', '1490', ' 布法罗 ', ' Buffalo ', '1', '420320', '420320020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:43', '2017-02-14 12:16:43', '1491', ' 长岛 ', ' Long Island ', '1', '420320', '420320030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:43', '2017-02-14 12:16:43', '1492', ' 纽约 ', ' New York ', '1', '420320', '420320040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:43', '2017-02-14 12:16:43', '1493', ' 罗彻斯特市 ', ' Rochester ', '1', '420320', '420320050', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:43', '2017-02-14 12:16:43', '1494', ' 绮色佳 ', ' Ithaca ', '1', '420320', '420320060', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:43', '2017-02-14 12:16:43', '1495', ' 北卡罗莱纳州 ', ' North Carolina ', '1', '360030', '420330', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:43', '2017-02-14 12:16:43', '1496', ' 洛利 ', ' Raleigh ', '1', '420330', '420330010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:43', '2017-02-14 12:16:43', '1497', ' 夏洛特 ', ' Charlotte ', '1', '420330', '420330020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:43', '2017-02-14 12:16:43', '1498', ' 格林斯堡 ', ' Greensboro ', '1', '420330', '420330030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:43', '2017-02-14 12:16:43', '1499', ' 查伯山 ', ' Chapel Hill ', '1', '420330', '420330040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:43', '2017-02-14 12:16:43', '1500', ' 阿什维尔 ', ' Asheville ', '1', '420330', '420330050', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:43', '2017-02-14 12:16:43', '1501', ' 北达科他州 ', ' North Dakota ', '1', '360030', '420340', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:44', '2017-02-14 12:16:44', '1502', ' 俾斯麦 ', ' Bismark ', '1', '420340', '420340010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:44', '2017-02-14 12:16:44', '1503', ' 法戈 ', ' Fargo ', '1', '420340', '420340020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:44', '2017-02-14 12:16:44', '1504', ' 俄亥俄州 ', ' Ohio  ', '1', '360030', '420350', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:44', '2017-02-14 12:16:44', '1505', ' 哥伦布 ', ' Columbus ', '1', '420350', '420350010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:44', '2017-02-14 12:16:44', '1506', ' 克利夫兰 ', ' Cleveland ', '1', '420350', '420350020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:44', '2017-02-14 12:16:44', '1507', ' 辛辛那提 ', ' Cincinnati ', '1', '420350', '420350030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:44', '2017-02-14 12:16:44', '1508', ' 俄克拉何马州 ', ' Oklahoma  ', '1', '360030', '420360', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:44', '2017-02-14 12:16:44', '1509', ' 俄克拉何马城 ', ' Oklahoma City ', '1', '420360', '420360010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:44', '2017-02-14 12:16:44', '1510', ' 塔尔萨 ', ' Tulsa ', '1', '420360', '420360020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:44', '2017-02-14 12:16:44', '1511', ' 劳顿 ', ' Lawton ', '1', '420360', '420360030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:44', '2017-02-14 12:16:44', '1512', ' 诺曼城 ', ' Norman ', '1', '420360', '420360040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:44', '2017-02-14 12:16:44', '1513', ' 俄勒冈州 ', ' Oregon  ', '1', '360030', '420370', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:44', '2017-02-14 12:16:44', '1514', ' 塞伦 ', ' Salem ', '1', '420370', '420370010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:45', '2017-02-14 12:16:45', '1515', ' 波特兰 ', ' Portland ', '1', '420370', '420370020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:45', '2017-02-14 12:16:45', '1516', ' 尤金 ', ' Eugene ', '1', '420370', '420370030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:45', '2017-02-14 12:16:45', '1517', ' 科瓦利 ', ' Corvallis ', '1', '420370', '420370040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:45', '2017-02-14 12:16:45', '1518', ' 宾夕法尼亚州 ', ' Pennsylvania  ', '1', '360030', '420380', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:45', '2017-02-14 12:16:45', '1519', ' 哈里斯堡 ', ' Harrisburg  ', '1', '420380', '420380010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:45', '2017-02-14 12:16:45', '1520', ' 南卡罗来纳州 ', ' South Carolina ', '1', '360030', '420390', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:45', '2017-02-14 12:16:45', '1521', ' 哥伦比亚 ', ' Columbia ', '1', '420390', '420390010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:45', '2017-02-14 12:16:45', '1522', ' 查理斯敦 ', ' North Charleston ', '1', '420390', '420390020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:45', '2017-02-14 12:16:45', '1523', ' 格林威尔 ', ' Greenville ', '1', '420390', '420390030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:45', '2017-02-14 12:16:45', '1524', ' 阿干 ', ' Aiken ', '1', '420390', '420390040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:45', '2017-02-14 12:16:45', '1525', ' 美特尔沙滨 ', ' Myrtle Beach ', '1', '420390', '420390050', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:45', '2017-02-14 12:16:45', '1526', ' 克伦孙 ', ' Clemson ', '1', '420390', '420390060', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:45', '2017-02-14 12:16:45', '1527', ' 南达科他州 ', ' South Dakota ', '1', '360030', '420400', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:46', '2017-02-14 12:16:46', '1528', ' 苏瀑市 ', ' Sioux Falls ', '1', '420400', '420400010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:46', '2017-02-14 12:16:46', '1529', ' 拉皮特城 ', ' Rapid City ', '1', '420400', '420400020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:46', '2017-02-14 12:16:46', '1530', ' 田纳西州 ', ' Tennessee  ', '1', '360030', '420410', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:46', '2017-02-14 12:16:46', '1531', ' 那什维尔 ', ' Nemphis ', '1', '420410', '420410010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:46', '2017-02-14 12:16:46', '1532', ' 孟斐斯 ', ' Memphis ', '1', '420410', '420410020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:46', '2017-02-14 12:16:46', '1533', ' 诺克斯维尔 ', ' Knoxville ', '1', '420410', '420410030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:46', '2017-02-14 12:16:46', '1534', ' 橡树岭 ', ' Oak Ridge ', '1', '420410', '420410040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:46', '2017-02-14 12:16:46', '1535', ' 德克萨斯州 ', ' Texas  ', '1', '360030', '420420', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:46', '2017-02-14 12:16:46', '1536', ' 奧斯汀 ', ' Austin ', '1', '420420', '420420010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:46', '2017-02-14 12:16:46', '1537', ' 休斯顿 ', ' Houston ', '1', '420420', '420420020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:46', '2017-02-14 12:16:46', '1538', ' 达拉斯 ', ' Dallas  ', '1', '420420', '420420030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:47', '2017-02-14 12:16:47', '1539', ' 犹他州 ', ' Utah  ', '1', '360030', '420430', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:47', '2017-02-14 12:16:47', '1540', ' 盐湖城 ', ' Salt Lake City ', '1', '420430', '420430010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:47', '2017-02-14 12:16:47', '1541', ' 奥格登 ', ' Ogden ', '1', '420430', '420430020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:47', '2017-02-14 12:16:47', '1542', ' 普罗沃 ', ' Provo ', '1', '420430', '420430030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:47', '2017-02-14 12:16:47', '1543', ' 佛蒙特州 ', ' Vermont  ', '1', '360030', '420440', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:47', '2017-02-14 12:16:47', '1544', ' 拉特兰 ', ' Rutland ', '1', '420440', '420440010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:47', '2017-02-14 12:16:47', '1545', ' 弗吉尼亚州 ', ' Virginia  ', '1', '360030', '420450', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:47', '2017-02-14 12:16:47', '1546', ' 里齐蒙得 ', ' Richmond ', '1', '420450', '420450010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:47', '2017-02-14 12:16:47', '1547', ' 诺福克 ', ' Norfolk ', '1', '420450', '420450020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:47', '2017-02-14 12:16:47', '1548', ' 弗吉尼亚滩 ', ' Virginia Beach ', '1', '420450', '420450030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:47', '2017-02-14 12:16:47', '1549', ' 华盛顿州 ', ' Washington  ', '1', '360030', '420460', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:47', '2017-02-14 12:16:47', '1550', ' 奥林匹亚 ', ' Olympia  ', '1', '420460', '420460010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:47', '2017-02-14 12:16:47', '1551', ' 罗得岛州 ', ' Rhode Island  ', '1', '360030', '420470', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:48', '2017-02-14 12:16:48', '1552', ' 普洛威顿斯 ', ' Providence ', '1', '420470', '420470010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:48', '2017-02-14 12:16:48', '1553', ' 纽波特 ', ' Newport ', '1', '420470', '420470020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:48', '2017-02-14 12:16:48', '1554', ' 西佛吉尼亚州 ', ' West Virginia ', '1', '360030', '420480', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:48', '2017-02-14 12:16:48', '1555', ' 查理斯敦 ', ' Charleston ', '1', '420480', '420480010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:48', '2017-02-14 12:16:48', '1556', ' 亨丁顿 ', ' Huntington ', '1', '420480', '420480020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:48', '2017-02-14 12:16:48', '1557', ' 摩根敦 ', ' Morgantown ', '1', '420480', '420480030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:48', '2017-02-14 12:16:48', '1558', ' 威斯康星州 ', ' Wisconsin  ', '1', '360030', '420490', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:48', '2017-02-14 12:16:48', '1559', ' 麦迪逊 ', ' Madison ', '1', '420490', '420490010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:48', '2017-02-14 12:16:48', '1560', ' 密尔沃基 ', ' Milwaukee ', '1', '420490', '420490020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:48', '2017-02-14 12:16:48', '1561', ' 拉辛 ', ' Racine ', '1', '420490', '420490030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:48', '2017-02-14 12:16:48', '1562', ' 怀俄明州 ', ' Wyoming  ', '1', '360030', '420500', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:48', '2017-02-14 12:16:48', '1563', ' 夏延 ', ' Cheyenne ', '1', '420500', '420500010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:48', '2017-02-14 12:16:48', '1564', ' 卡斯柏 ', ' Casper ', '1', '420500', '420500020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:48', '2017-02-14 12:16:48', '1565', ' 拉阿密 ', ' Laramie ', '1', '420500', '420500030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:49', '2017-02-14 12:16:49', '1566', ' 华盛顿哥伦比亚特区 ', ' Washington', '1', '1', '420510', '360030.0', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:49', '2017-02-14 12:16:49', '1567', ' 阿尔伯塔省 ', ' Alberta ', '1', '360020', '430010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:49', '2017-02-14 12:16:49', '1568', ' 卡尔加里 ', ' Calgary ', '1', '430010', '430010010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:49', '2017-02-14 12:16:49', '1569', ' 埃德蒙顿 ', ' Edmonton ', '1', '430010', '430010020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:49', '2017-02-14 12:16:49', '1570', ' 不列颠哥伦比亚省 ', ' British Columbia ', '1', '360020', '430020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:49', '2017-02-14 12:16:49', '1571', ' 温哥华 ', ' Vancouver ', '1', '430020', '430020010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:49', '2017-02-14 12:16:49', '1572', ' 素里 ', ' Surrey ', '1', '430020', '430020020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:49', '2017-02-14 12:16:49', '1573', ' 本拿比 ', ' Burnaby ', '1', '430020', '430020030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:49', '2017-02-14 12:16:49', '1574', ' 列治文 ', ' Richmond ', '1', '430020', '430020040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:49', '2017-02-14 12:16:49', '1575', ' 曼尼托巴省 ', ' Manitoba ', '1', '360020', '430030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:49', '2017-02-14 12:16:49', '1576', ' 温尼伯 ', ' Winnipeg ', '1', '430030', '430030010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:49', '2017-02-14 12:16:49', '1577', ' 纽芬兰与拉布拉多省 ', ' Newfoundland and Labrador ', '1', '360020', '430040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:49', '2017-02-14 12:16:49', '1578', ' 新不伦瑞克省 ', ' New Brunswick ', '1', '360020', '430050', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:49', '2017-02-14 12:16:49', '1579', ' 新斯科舍省 ', ' Nova Scotia ', '1', '360020', '430060', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:49', '2017-02-14 12:16:49', '1580', ' 哈利法克斯 ', ' Halifax ', '1', '430060', '430060030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:50', '2017-02-14 12:16:50', '1581', ' 安大略省 ', ' Ontario ', '1', '360020', '430070', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:50', '2017-02-14 12:16:50', '1582', ' 多伦多 ', ' Toronto ', '1', '430070', '430070010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:50', '2017-02-14 12:16:50', '1583', ' 渥太华 ', ' Ottawa ', '1', '430070', '430070020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:50', '2017-02-14 12:16:50', '1584', ' 密西沙加 ', ' Mississauga ', '1', '430070', '430070030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:50', '2017-02-14 12:16:50', '1585', ' 宾顿 ', ' Brampton ', '1', '430070', '430070040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:50', '2017-02-14 12:16:50', '1586', ' 汉密尔顿 ', ' Hamilton ', '1', '430070', '430070050', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:50', '2017-02-14 12:16:50', '1587', ' 伦敦 ', ' London ', '1', '430070', '430070060', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:50', '2017-02-14 12:16:50', '1588', ' 万锦 ', ' Markham ', '1', '430070', '430070070', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:50', '2017-02-14 12:16:50', '1589', ' 旺市 ', ' Vaughan ', '1', '430070', '430070080', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:50', '2017-02-14 12:16:50', '1590', ' 基奇纳 ', ' Kitchener ', '1', '430070', '430070090', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:50', '2017-02-14 12:16:50', '1591', ' 温莎 ', ' Windsor ', '1', '430070', '430070100', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:50', '2017-02-14 12:16:50', '1592', ' 列治文山 ', ' Richmond Hill ', '1', '430070', '430070110', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:50', '2017-02-14 12:16:50', '1593', ' 奥克维尔 ', ' Okville ', '1', '430070', '430070120', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:50', '2017-02-14 12:16:50', '1594', ' 伯灵顿 ', ' Burlington ', '1', '430070', '430070130', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:50', '2017-02-14 12:16:50', '1595', ' 萨德伯里 ', ' Greater Sudbury ', '1', '430070', '430070140', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:51', '2017-02-14 12:16:51', '1596', ' 爱德华王子岛省 ', ' Prince Edward Island ', '1', '360020', '430080', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:51', '2017-02-14 12:16:51', '1597', ' 魁北克省 ', ' Québec ', '1', '360020', '430090', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:51', '2017-02-14 12:16:51', '1598', ' 蒙特利尔 ', ' Montreal ', '1', '430090', '430090010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:51', '2017-02-14 12:16:51', '1599', ' 魁北克城 ', ' Quebec City ', '1', '430090', '430090020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:51', '2017-02-14 12:16:51', '1600', ' 拉瓦尔 ', ' Laval ', '1', '430090', '430090030', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:51', '2017-02-14 12:16:51', '1601', ' 加蒂诺 ', ' Gatineau ', '1', '430090', '430090040', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:51', '2017-02-14 12:16:51', '1602', ' 朗基尔 ', ' Longueuil ', '1', '430090', '430090050', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:51', '2017-02-14 12:16:51', '1603', ' 舍布鲁克 ', ' Sherbrooke ', '1', '430090', '430090060', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:51', '2017-02-14 12:16:51', '1604', ' 萨斯喀彻温省 ', ' Saskatchewan ', '1', '360020', '430100', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:51', '2017-02-14 12:16:51', '1605', ' 萨斯卡通 ', ' Saskatoon ', '1', '430100', '430100010', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:51', '2017-02-14 12:16:51', '1606', ' 里贾纳 ', ' Regina ', '1', '430100', '430100020', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:51', '2017-02-14 12:16:51', '1607', ' 努纳武特地区 ', ' Nunavut ', '1', '360020', '430110', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:51', '2017-02-14 12:16:51', '1608', ' 西北地区 ', ' Northwest Territories ', '1', '360020', '430120', '  ', '  ', null);
INSERT INTO `fic_city_code_field` VALUES ('0', '2017-02-14 12:16:52', '2017-02-14 12:16:52', '1609', ' 育空地区 ', ' Yukon ', '1', '360020', '430130', '  ', '  ', null);

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
  `data_identity` varchar(64) NOT NULL,
  `collect_type` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=115 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of fic_feature_field_rel
-- ----------------------------
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:54', '2017-02-14 14:58:54', '1', 'is_loan_agency', 'loan_agency', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:54', '2017-02-14 14:58:54', '2', 'is_organization_g_black', 'agentg_black', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:54', '2017-02-14 14:58:54', '3', 'is_netsky_black', 'tianwang_black', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:54', '2017-02-14 14:58:54', '4', 'is_netsky_multi_loan', 'tianwang_multi_loan', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:54', '2017-02-14 14:58:54', '5', 'is_skyeye_black', 'tianyan_black', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:54', '2017-02-14 14:58:54', '6', 'is_court_shixin', 'court_shixin_a_s', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:54', '2017-02-14 14:58:54', '7', 'is_net_black', 'net_black_a_s', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:54', '2017-02-14 14:58:54', '8', 'has_negative_info', 'negative_info_s', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:54', '2017-02-14 14:58:54', '9', 'is_netsky_grey', 'tianwang_gray', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:54', '2017-02-14 14:58:54', '10', 'is_court_zhixing', 'court_zhixing_a_s', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:54', '2017-02-14 14:58:54', '11', 'online_time', 'telecom_mobile_online_time_s', 'ShuntCourier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:54', '2017-02-14 14:58:54', '12', 'online_time', 'unicome_mobile_online_time_s', 'ShuntCourier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:54', '2017-02-14 14:58:54', '13', 'online_time', 'yd_mobile_online_time_s', 'ShuntCourier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:54', '2017-02-14 14:58:54', '14', 'pingan_overdue_count', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:55', '2017-02-14 14:58:55', '15', 'pingan_max_overdue_days', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:55', '2017-02-14 14:58:55', '16', 'is_pingan_financial_shixin', 'trustutn_loan_blacklist', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:55', '2017-02-14 14:58:55', '17', 'jiuyao_multi_loan_denied_count', 'multi_loan_91', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:55', '2017-02-14 14:58:55', '18', 'jiuyao_multi_loan_m2_count', 'multi_loan_91', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:55', '2017-02-14 14:58:55', '19', 'name', 'apply_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:55', '2017-02-14 14:58:55', '20', 'card_id', 'apply_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:55', '2017-02-14 14:58:55', '21', 'mobile', 'apply_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:55', '2017-02-14 14:58:55', '22', 'age', 'personal_info', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:55', '2017-02-14 14:58:55', '23', 'is_unclear_loan', 'loan_history', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:55', '2017-02-14 14:58:55', '24', 'apply_register_duration', 'portrait_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:55', '2017-02-14 14:58:55', '25', 'apply_register_duration', 'apply_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:55', '2017-02-14 14:58:55', '26', 'complete_degree', 'portrait_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:55', '2017-02-14 14:58:55', '27', 'gps_city_code', 'geo_location', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:55', '2017-02-14 14:58:55', '28', 'mobile_area_code', 'mobile_locale', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:56', '2017-02-14 14:58:56', '29', 'is_pingan_multi_loan', 'trustutn_loan_loanmsg', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:56', '2017-02-14 14:58:56', '30', 'pingan_multi_loan_count', 'trustutn_loan_loanmsg', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:56', '2017-02-14 14:58:56', '31', 'mobile_mark', 'trustutn_loan_phone', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:56', '2017-02-14 14:58:56', '32', 'cur_work_status', 'portrait_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:56', '2017-02-14 14:58:56', '33', 'now_workplace_code', 'portrait_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:56', '2017-02-14 14:58:56', '34', 'mobile_identity', 'telecom_mobile_identity_s', 'ShuntCourier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:56', '2017-02-14 14:58:56', '35', 'mobile_identity', 'unicom_mobile_identity_s', 'ShuntCourier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:56', '2017-02-14 14:58:56', '36', 'mobile_identity', 'yd_mobile_identity_s', 'ShuntCourier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:56', '2017-02-14 14:58:56', '37', 'work_time', 'portrait_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:56', '2017-02-14 14:58:56', '38', 'education_degree_code', 'portrait_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:56', '2017-02-14 14:58:56', '39', 'education_tz', 'portrait_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:56', '2017-02-14 14:58:56', '40', 'now_industry_code', 'portrait_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:56', '2017-02-14 14:58:56', '41', 'last_industry_code', 'portrait_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:56', '2017-02-14 14:58:56', '42', 'now_work_time', 'portrait_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:56', '2017-02-14 14:58:56', '43', 'industry_change_count', 'portrait_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:57', '2017-02-14 14:58:57', '44', 'is_mobile_black', 'trustutn_loan_phone', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:57', '2017-02-14 14:58:57', '45', 'mobile_stability', 'trustutn_loan_phone', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:57', '2017-02-14 14:58:57', '46', 'mobile_activeness', 'trustutn_loan_phone', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:57', '2017-02-14 14:58:57', '47', 'loan_infos', 'multi_loan_91', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:57', '2017-02-14 14:58:57', '48', 'loan_infos__borrow_type', 'multi_loan_91', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:57', '2017-02-14 14:58:57', '49', 'loan_infos__borrow_state', 'multi_loan_91', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:57', '2017-02-14 14:58:57', '50', 'loan_infos__borrow_amount', 'multi_loan_91', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:57', '2017-02-14 14:58:57', '51', 'loan_infos__contract_date', 'multi_loan_91', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:57', '2017-02-14 14:58:57', '52', 'loan_infos__loan_period', 'multi_loan_91', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:57', '2017-02-14 14:58:57', '53', 'loan_infos__repay_state', 'multi_loan_91', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:57', '2017-02-14 14:58:57', '54', 'loan_infos__arrears_amount', 'multi_loan_91', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:57', '2017-02-14 14:58:57', '55', 'is_jiuyao_multi_loan', 'multi_loan_91', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:57', '2017-02-14 14:58:57', '56', 'contacts', 'apply_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:57', '2017-02-14 14:58:57', '57', 'dc_bill_age', 'cc_credit', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:58', '2017-02-14 14:58:58', '58', 'cc_bill_age', 'cc_credit', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:58', '2017-02-14 14:58:58', '59', 'creditcard_count', 'cc_credit', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:58', '2017-02-14 14:58:58', '60', 'car_count', 'cc_car_credit', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:58', '2017-02-14 14:58:58', '61', 'application_on', 'apply_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:58', '2017-02-14 14:58:58', '62', 'pingan_multi_loan_infos', 'trustutn_loan_loanmsg', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:58', '2017-02-14 14:58:58', '63', 'car_number', 'cc_car_credit', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:58', '2017-02-14 14:58:58', '64', 'overspeed_count', 'high_way_over_speed', 'RelevanceCourier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:58', '2017-02-14 14:58:58', '65', 'overload_count', 'high_way_over_load', 'RelevanceCourier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:58', '2017-02-14 14:58:58', '66', 'pingan_overdue_corp_count', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:58', '2017-02-14 14:58:58', '67', 'pingan_other_loan_count', 'trustutn_loan_otheragent', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:58', '2017-02-14 14:58:58', '68', 'is_pingan_overdue_loan', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:58', '2017-02-14 14:58:58', '69', 'is_pingan_other_loan', 'trustutn_loan_otheragent', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:58', '2017-02-14 14:58:58', '70', 'pingan_overdue_loan_infos', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:59', '2017-02-14 14:58:59', '71', 'pingan_overdue_loan_infos__phone', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:59', '2017-02-14 14:58:59', '72', 'pingan_overdue_loan_infos__imsi', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:59', '2017-02-14 14:58:59', '73', 'pingan_overdue_loan_infos__imei', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:59', '2017-02-14 14:58:59', '74', 'pingan_overdue_loan_infos__record', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:59', '2017-02-14 14:58:59', '75', 'pingan_overdue_loan_infos__matchType', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:59', '2017-02-14 14:58:59', '76', 'pingan_overdue_loan_infos__matchValue', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:59', '2017-02-14 14:58:59', '77', 'pingan_overdue_loan_infos__matchId', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:59', '2017-02-14 14:58:59', '78', 'pingan_overdue_loan_infos__classification', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:59', '2017-02-14 14:58:59', '79', 'pingan_overdue_loan_infos__M3', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:59', '2017-02-14 14:58:59', '80', 'pingan_overdue_loan_infos__bankLoan', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:59', '2017-02-14 14:58:59', '81', 'pingan_overdue_loan_infos__recordNums', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:59', '2017-02-14 14:58:59', '82', 'pingan_overdue_loan_infos__orgNums', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:58:59', '2017-02-14 14:58:59', '83', 'pingan_overdue_loan_infos__maxAmount', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:00', '2017-02-14 14:59:00', '84', 'pingan_overdue_loan_infos__longestDays', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:00', '2017-02-14 14:59:00', '85', 'pingan_overdue_loan_infos__bankCredit', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:00', '2017-02-14 14:59:00', '86', 'pingan_overdue_loan_infos__otherLoan', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:00', '2017-02-14 14:59:00', '87', 'pingan_overdue_loan_infos__otherCredit', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:00', '2017-02-14 14:59:00', '88', 'pingan_overdue_loan_infos__M6', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:00', '2017-02-14 14:59:00', '89', 'pingan_overdue_loan_infos__M9', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:00', '2017-02-14 14:59:00', '90', 'pingan_overdue_loan_infos__M12', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:00', '2017-02-14 14:59:00', '91', 'pingan_overdue_loan_infos__M24', 'trustutn_loan_overdue', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:00', '2017-02-14 14:59:00', '92', 'pingan_other_loan_infos', 'trustutn_loan_otheragent', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:00', '2017-02-14 14:59:00', '93', 'pingan_other_loan_infos__orgNums', 'trustutn_loan_otheragent', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:00', '2017-02-14 14:59:00', '94', 'pingan_other_loan_infos__queryNums', 'trustutn_loan_otheragent', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:00', '2017-02-14 14:59:00', '95', 'airfare_sum_12', 'airline_passenger_info', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:00', '2017-02-14 14:59:00', '96', 'max_flight_class', 'airline_passenger_info', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:01', '2017-02-14 14:59:01', '97', 'max_flight_area', 'airline_passenger_info', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:01', '2017-02-14 14:59:01', '98', 'income_level', 'cc_credit', 'ShuntCourier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:01', '2017-02-14 14:59:01', '99', 'income_level', 'unicom_finance_portrait_s', 'ShuntCourier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:01', '2017-02-14 14:59:01', '100', 'income_level', 'portrait_data', 'ShuntCourier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:01', '2017-02-14 14:59:01', '101', 'income_expense_comparison', 'cc_credit', 'ShuntCourier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:01', '2017-02-14 14:59:01', '102', 'income_expense_comparison', 'unicom_finance_portrait_s', 'ShuntCourier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:01', '2017-02-14 14:59:01', '103', 'graduate_college', 'portrait_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:01', '2017-02-14 14:59:01', '104', 'gender', 'personal_info', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:01', '2017-02-14 14:59:01', '105', 'marital_status', 'multi_id_card_info_s', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:01', '2017-02-14 14:59:01', '106', 'folk', 'multi_id_card_info_s', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:01', '2017-02-14 14:59:01', '107', 'cur_company', 'portrait_data', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:01', '2017-02-14 14:59:01', '108', 'cur_corp_years', 'industrial_commercial_s', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:01', '2017-02-14 14:59:01', '109', 'cur_employee_number', 'industrial_commercial_s', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 14:59:01', '2017-02-14 14:59:01', '110', 'is_cur_corp_shixin', 'court_shixin_a_s', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 16:00:32', '2017-02-14 16:00:42', '111', 'education_degree_check', 'education_review_s', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 16:00:35', '2017-02-14 16:00:44', '112', 'college_type', 'education_review_s', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 16:00:37', '2017-02-14 16:00:46', '113', 'graduate_college_check', 'education_review_s', 'Courier');
INSERT INTO `fic_feature_field_rel` VALUES ('0', '2017-02-14 16:00:39', '2017-02-14 16:00:49', '114', 'is_recruitment', 'education_review_s', 'Courier');

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
-- Table structure for `fic_interface_field_rel`
-- ----------------------------
DROP TABLE IF EXISTS `fic_interface_field_rel`;
CREATE TABLE `fic_interface_field_rel` (
  `is_delete` tinyint(1) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `updated_on` datetime NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_identity` varchar(64) NOT NULL,
  `raw_field_name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of fic_interface_field_rel
-- ----------------------------
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:05', '2017-02-14 15:57:05', '1', 'loan_agency', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:05', '2017-02-14 15:57:05', '2', 'agentg_black', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:05', '2017-02-14 15:57:05', '3', 'agentg_black', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:05', '2017-02-14 15:57:05', '4', 'agentg_black', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:05', '2017-02-14 15:57:05', '5', 'tianwang_black', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:05', '2017-02-14 15:57:05', '6', 'tianwang_multi_loan', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:05', '2017-02-14 15:57:05', '7', 'tianyan_black', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:05', '2017-02-14 15:57:05', '8', 'tianyan_black', 'email');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:06', '2017-02-14 15:57:06', '9', 'tianyan_black', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:06', '2017-02-14 15:57:06', '10', 'court_shixin_a_s', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:06', '2017-02-14 15:57:06', '11', 'court_shixin_a_s', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:06', '2017-02-14 15:57:06', '12', 'net_black_a_s', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:06', '2017-02-14 15:57:06', '13', 'net_black_a_s', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:06', '2017-02-14 15:57:06', '14', 'negative_info_s', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:06', '2017-02-14 15:57:06', '15', 'negative_info_s', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:06', '2017-02-14 15:57:06', '16', 'tianwang_gray', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:06', '2017-02-14 15:57:06', '17', 'court_zhixing_a_s', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:06', '2017-02-14 15:57:06', '18', 'court_zhixing_a_s', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:06', '2017-02-14 15:57:06', '19', 'telecom_mobile_online_time_s', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:06', '2017-02-14 15:57:06', '20', 'unicome_mobile_online_time_s', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:06', '2017-02-14 15:57:06', '21', 'yd_mobile_online_time_s', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:07', '2017-02-14 15:57:07', '22', 'trustutn_loan_overdue', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:07', '2017-02-14 15:57:07', '23', 'trustutn_loan_overdue', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:07', '2017-02-14 15:57:07', '24', 'trustutn_loan_overdue', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:07', '2017-02-14 15:57:07', '25', 'trustutn_loan_blacklist', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:07', '2017-02-14 15:57:07', '26', 'trustutn_loan_blacklist', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:07', '2017-02-14 15:57:07', '27', 'trustutn_loan_blacklist', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:07', '2017-02-14 15:57:07', '28', 'multi_loan_91', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:07', '2017-02-14 15:57:07', '29', 'multi_loan_91', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:07', '2017-02-14 15:57:07', '30', 'apply_data', 'apply_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:07', '2017-02-14 15:57:07', '31', 'personal_info', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:07', '2017-02-14 15:57:07', '32', 'personal_info', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:07', '2017-02-14 15:57:07', '33', 'loan_history', '');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:07', '2017-02-14 15:57:07', '34', 'portrait_data', 'proposer_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:07', '2017-02-14 15:57:07', '35', 'geo_location', 'latitude');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:08', '2017-02-14 15:57:08', '36', 'geo_location', 'longitudu');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:08', '2017-02-14 15:57:08', '37', 'mobile_locale', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:08', '2017-02-14 15:57:08', '38', 'trustutn_loan_loanmsg', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:08', '2017-02-14 15:57:08', '39', 'trustutn_loan_loanmsg', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:08', '2017-02-14 15:57:08', '40', 'trustutn_loan_loanmsg', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:08', '2017-02-14 15:57:08', '41', 'trustutn_loan_phone', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:08', '2017-02-14 15:57:08', '42', 'trustutn_loan_phone', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:08', '2017-02-14 15:57:08', '43', 'trustutn_loan_phone', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:08', '2017-02-14 15:57:08', '44', 'telecom_mobile_identity_s', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:08', '2017-02-14 15:57:08', '45', 'telecom_mobile_identity_s', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:08', '2017-02-14 15:57:08', '46', 'telecom_mobile_identity_s', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:08', '2017-02-14 15:57:08', '47', 'unicom_mobile_identity_s', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:08', '2017-02-14 15:57:08', '48', 'unicom_mobile_identity_s', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:08', '2017-02-14 15:57:08', '49', 'unicom_mobile_identity_s', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:08', '2017-02-14 15:57:08', '50', 'yd_mobile_identity_s', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:09', '2017-02-14 15:57:09', '51', 'yd_mobile_identity_s', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:09', '2017-02-14 15:57:09', '52', 'yd_mobile_identity_s', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:09', '2017-02-14 15:57:09', '53', 'cc_credit', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:09', '2017-02-14 15:57:09', '54', 'cc_car_credit', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:09', '2017-02-14 15:57:09', '55', 'cc_car_credit', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:09', '2017-02-14 15:57:09', '56', 'high_way_over_speed', 'license_plate');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:09', '2017-02-14 15:57:09', '57', 'high_way_over_load', 'license_plate');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:09', '2017-02-14 15:57:09', '58', 'trustutn_loan_otheragent', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:09', '2017-02-14 15:57:09', '59', 'trustutn_loan_otheragent', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:09', '2017-02-14 15:57:09', '60', 'trustutn_loan_otheragent', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:09', '2017-02-14 15:57:09', '61', 'airline_passenger_info', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:09', '2017-02-14 15:57:09', '62', 'airline_passenger_info', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:09', '2017-02-14 15:57:09', '63', 'unicom_finance_portrait_s', 'mobile');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:10', '2017-02-14 15:57:10', '64', 'multi_id_card_info_s', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:10', '2017-02-14 15:57:10', '65', 'multi_id_card_info_s', 'card_id');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 15:57:10', '2017-02-14 15:57:10', '66', 'industrial_commercial_s', 'cur_company');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 16:01:18', '2017-02-14 16:01:22', '67', 'education_review_s', 'name');
INSERT INTO `fic_interface_field_rel` VALUES ('0', '2017-02-14 16:03:02', '2017-02-14 16:03:06', '71', 'education_review_s', 'card_id');

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
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of fic_interface_info
-- ----------------------------
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:36', '2017-02-15 10:45:36', '1', '贷款中介查询', 'loan_agency', '', 'REMOTE', '', '', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:36', '2017-02-15 10:45:36', '2', '机构G黑名单查询', 'agentg_black', '', 'REMOTE', '', '', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\', \'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:36', '2017-02-15 10:45:36', '3', '天网黑名单查询', 'tianwang_black', '', 'REMOTE', '', '', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:36', '2017-02-15 10:45:36', '4', '天网多头贷款查询', 'tianwang_multi_loan', '', 'REMOTE', '', '', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:36', '2017-02-15 10:45:36', '5', '天眼黑名单查询', 'tianyan_black', '', 'REMOTE', '', '', '{\'email\': \'%(email)s\', \'id_card_code\': \'%(card_id)s\', \'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:36', '2017-02-15 10:45:36', '6', '法院失信被执行人查询', 'court_shixin_a_s', '', 'REMOTE', '', '', '{\'entity_name\': \'%(name)s\', \'entity_id\': \'%(card_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:36', '2017-02-15 10:45:36', '7', '网贷黑名单查询', 'net_black_a_s', '', 'REMOTE', '', '', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:36', '2017-02-15 10:45:36', '8', '个人不良信息查询', 'negative_info_s', '', 'REMOTE', '', '', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:36', '2017-02-15 10:45:36', '9', '天网灰名单查询', 'tianwang_gray', '', 'REMOTE', '', '', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:36', '2017-02-15 10:45:36', '10', '法院被执行人查询', 'court_zhixing_a_s', '', 'REMOTE', '', '', '{\'entity_name\': \'%(name)s\', \'entity_id\': \'%(card_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:36', '2017-02-15 10:45:36', '11', '电信手机在网时长', 'telecom_mobile_online_time_s', '', 'REMOTE', 'TMN', '', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:36', '2017-02-15 10:45:36', '12', '联通手机在网时长', 'unicome_mobile_online_time_s', '', 'REMOTE', 'UMN', '', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:37', '2017-02-15 10:45:37', '13', '移动手机在网时长', 'yd_mobile_online_time_s', '', 'REMOTE', 'YMN', '', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:37', '2017-02-15 10:45:37', '14', '凭安贷款逾期信息', 'trustutn_loan_overdue', '', 'REMOTE', '', '', '{\'phone\': \'%(mobile)s\', \'id_card\': \'%(crad_id)s\', \'name\': \'%(name)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:37', '2017-02-15 10:45:37', '15', '凭安贷款黑名单信息', 'trustutn_loan_blacklist', '', 'REMOTE', '', '', '{\'phone\': \'%(mobile)s\', \'id_card\': \'%(crad_id)s\', \'name\': \'%(name)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:37', '2017-02-15 10:45:37', '16', '91征信查询', 'multi_loan_91', '', 'REMOTE', '', '', '{\'real_name\': \'%(name)s\', \'id_card\': \'%(card_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:37', '2017-02-15 10:45:37', '17', '申请数据查询', 'apply_data', '', 'LOCALE', '', '', '{\'apply_id\': \'%(apply_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:37', '2017-02-15 10:45:37', '18', '个人基本信息查询', 'personal_info', '', 'REMOTE', '', '', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:37', '2017-02-15 10:45:37', '19', '未结清贷款记录查询', 'loan_history', '', 'REMOTE', '', '', '', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:37', '2017-02-15 10:45:37', '20', '预授信信息查询', 'portrait_data', '', 'LOCALE', '', '', '{\'proposer_id\': \'%(proposer_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:37', '2017-02-15 10:45:37', '21', 'GPS地址查询', 'geo_location', '', 'REMOTE', '', '', '{\'gps_longitude\': \'%(longitudu)s\', \'gps_latitude\': \'%(latitude)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:37', '2017-02-15 10:45:37', '22', '手机号码归属地查询', 'mobile_locale', '', 'REMOTE', '', '', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:37', '2017-02-15 10:45:37', '23', '凭安多头贷款查询', 'trustutn_loan_loanmsg', '', 'REMOTE', '', '', '{\'phone\': \'%(mobile)s\', \'id_card\': \'%(crad_id)s\', \'name\': \'%(name)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:37', '2017-02-15 10:45:37', '24', '凭安电话号码查询', 'trustutn_loan_phone', '', 'REMOTE', '', '', '{\'phone\': \'%(mobile)s\', \'id_card\': \'%(crad_id)s\', \'name\': \'%(name)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:37', '2017-02-15 10:45:37', '25', '电信手机身份验证', 'telecom_mobile_identity_s', '', 'REMOTE', 'TMN', '', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\', \'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:37', '2017-02-15 10:45:37', '26', '联通手机身份验证', 'unicom_mobile_identity_s', '', 'REMOTE', 'UMN', '', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\', \'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:38', '2017-02-15 10:45:38', '27', '移动手机身份验证', 'yd_mobile_identity_s', '', 'REMOTE', 'YMN', '', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\', \'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:38', '2017-02-15 10:45:38', '28', '人人信', 'cc_credit', '', 'REMOTE', '', '', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:38', '2017-02-15 10:45:38', '29', '人人信车辆信息查询', 'cc_car_credit', '', 'REMOTE', '', '', '{\'user_name\': \'%(name)s\', \'id_no\': \'%(card_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:38', '2017-02-15 10:45:38', '30', '高速超速信息查询', 'high_way_over_speed', '', 'REMOTE', '', '', '{\'license_plate\': \'%(license_plate)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:38', '2017-02-15 10:45:38', '31', '高速超载信息查询', 'high_way_over_load', '', 'REMOTE', '', '', '{\'license_plate\': \'%(license_plate)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:38', '2017-02-15 10:45:38', '32', '凭安贷款其他机构查询', 'trustutn_loan_otheragent', '', 'REMOTE', '', '', '{\'phone\': \'%(mobile)s\', \'id_card\': \'%(crad_id)s\', \'name\': \'%(name)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:38', '2017-02-15 10:45:38', '33', '乘机人信息查询', 'airline_passenger_info', '', 'REMOTE', '', '', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:38', '2017-02-15 10:45:38', '34', '联通金融画像查询', 'unicom_finance_portrait_s', '', 'REMOTE', 'UMN', '', '{\'mobile\': \'%(mobile)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:38', '2017-02-15 10:45:38', '35', '多项身份信息查询', 'multi_id_card_info_s', '', 'REMOTE', '', '', '{\'id_card_name\': \'%(name)s\', \'id_card_code\': \'%(card_id)s\'}', '0', '0', '0', '', '3');
INSERT INTO `fic_interface_info` VALUES ('0', '2017-02-15 10:45:38', '2017-02-15 10:45:38', '36', '企业工商信息查询', 'industrial_commercial_s', '', 'REMOTE', '', '', '{\'enterprise_name\': \'%(cur_company)s\'}', '0', '0', '0', '', '3');
