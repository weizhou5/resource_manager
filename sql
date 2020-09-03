CREATE TABLE `rms_pvc` (
     `id`                  INT(11)         NOT NULL AUTO_INCREMENT,
     `name`                VARCHAR(50)     NOT NULL,
     `capacity`            VARCHAR(50)     NOT NULL,
     `access_model`        VARCHAR(50)     NOT NULL,
     `story_class`         VARCHAR(50)     NOT NULL,
     `model`               DECIMAL(8,2)    NOT NULL,
     `is_delete`           TINYINT         NOT NULL default 0,
     `cre_user`            VARCHAR(50)     NOT NULL                      COMMENT '创建人',
     `cre_date`            TIMESTAMP       DEFAULT CURRENT_TIMESTAMP     COMMENT '创建时间',
     `upd_user`            VARCHAR(50)     NOT NULL                      COMMENT '更新人',
     `upd_date`            TIMESTAMP       DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  COMMENT '更新时间',
     PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;