/*
Navicat MySQL Data Transfer

Source Server         : 测试
Source Server Version : 50723
Source Host           : 10.168.3.19:3306
Source Database       : python

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2018-10-08 13:50:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_exclusion_criteria
-- ----------------------------
DROP TABLE IF EXISTS `t_exclusion_criteria`;
CREATE TABLE `t_exclusion_criteria` (
  `exclusion_criteria_id` varchar(100) NOT NULL,
  `num` varchar(20) DEFAULT NULL COMMENT '编号',
  `content` varchar(2000) DEFAULT NULL COMMENT '入选标准的内容',
  `create_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `search_content_type` varchar(100) DEFAULT NULL COMMENT '搜索的关键字'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for t_organizations
-- ----------------------------
DROP TABLE IF EXISTS `t_organizations`;
CREATE TABLE `t_organizations` (
  `organization_id` varchar(50) DEFAULT NULL,
  `organization_name` varchar(200) DEFAULT NULL,
  `province` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `num` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for t_standard_constrain
-- ----------------------------
DROP TABLE IF EXISTS `t_standard_constrain`;
CREATE TABLE `t_standard_constrain` (
  `standard_constrain_id` varchar(100) NOT NULL,
  `num` varchar(20) DEFAULT NULL COMMENT '编号',
  `content` varchar(2000) DEFAULT NULL COMMENT '入选标准的内容',
  `create_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `search_content_type` varchar(100) DEFAULT NULL COMMENT '搜索的关键字'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for t_test_info
-- ----------------------------
DROP TABLE IF EXISTS `t_test_info`;
CREATE TABLE `t_test_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `indication` varchar(1000) DEFAULT NULL COMMENT '适应症',
  `test_popular_title` varchar(255) DEFAULT NULL COMMENT '试验通俗标题',
  `test_profession_title` varchar(500) DEFAULT NULL COMMENT '试验专业标题',
  `scheme_number` varchar(100) DEFAULT NULL COMMENT '试验方案编号',
  `drug_name` varchar(100) DEFAULT NULL,
  `drug_type` varchar(50) DEFAULT NULL COMMENT '药物类型',
  `contact` varchar(20) DEFAULT NULL COMMENT '联系人',
  `contact_phone` varchar(50) DEFAULT NULL COMMENT '联系人电话',
  `test_end_date` varchar(20) DEFAULT NULL COMMENT '试验终止日期',
  `test_status` varchar(500) DEFAULT NULL COMMENT '试验状态',
  `standard_constrain_id` varchar(100) DEFAULT NULL COMMENT '入选标准的外键id',
  `exclusion_criteria_id` varchar(100) DEFAULT NULL COMMENT '排除标准外键id',
  `organization_id` varchar(100) DEFAULT NULL,
  `search_content_type` varchar(100) DEFAULT NULL COMMENT '搜索的关键字',
  PRIMARY KEY (`id`),
  KEY `fk_standard_constrain_id` (`standard_constrain_id`)
) ENGINE=MyISAM AUTO_INCREMENT=23622 DEFAULT CHARSET=utf8mb4;
