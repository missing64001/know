-- MySQL dump 10.13  Distrib 5.7.14, for Win64 (x86_64)
--
-- Host: 120.79.41.9    Database: know
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add label',7,'add_label'),(20,'Can change label',7,'change_label'),(21,'Can delete label',7,'delete_label'),(22,'Can add history',8,'add_history'),(23,'Can change history',8,'change_history'),(24,'Can delete history',8,'delete_history'),(25,'Can add content',9,'add_content'),(26,'Can change content',9,'change_content'),(27,'Can delete content',9,'delete_content');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_content`
--

DROP TABLE IF EXISTS `data_content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `create_date` datetime(6) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_content`
--

LOCK TABLES `data_content` WRITE;
/*!40000 ALTER TABLE `data_content` DISABLE KEYS */;
INSERT INTO `data_content` VALUES (1,'self.dia.exec()','2018-10-29 15:44:48.565000','dialog模态'),(2,'self.setFlags(self.flags() | Qt.ItemIsEditable | Qt.ItemIsEnabled)','2018-10-29 15:59:36.601000','QTreeWidgetItem可编辑'),(3,'import sys,os\nsys.path.append(r\'F:\\my\\P028_knowledge_system\\knowqt\\kqj\')\nos.environ[\'DJANGO_SETTINGS_MODULE\'] =\'kqj.settings\'\nimport django \ndjango.setup()\nfrom data import models\nfrom django.db.models import Q','2018-10-29 16:02:14.101000','django单独使用model'),(4,'120.79.41.9\nroot M1\n\n','2018-11-06 03:24:52.374242','阿里云服务器'),(5,'f:\ncd F:\\mygit\\python\\evaluate\n\npython manage.py runserver 0.0.0.0:8000\n\npython manage.py makemigrations\n\npython manage.py migrate\n\npython manage.py createsuperuser\n\nmysqldump -uevaluateg -pevaluateg evaluateg  >evaluateg.sql\n\nmysql -uevaluateg -pevaluateg evaluateg< evaluateg.sql','2018-11-07 02:31:47.534557','evaluate 运行命令'),(6,'mysqldump -uroot -p123456 crawl_proxy  > C:\\Users\\miss\\crawl_proxy.sql\nmysql -uroot -p123456 crawl_proxy< C:\\Users\\miss\\crawl_proxy.sql','2018-10-30 01:14:06.627200','mysql数据备份'),(7,'\ncreate user \"evaluateg\"@\"%\" identified by \"evaluateg\";\ngrant all privileges on evaluateg.* to \'evaluateg\'@\'%\' with grant option;\n\n\nCREATE DATABASE evaluateg DEFAULT CHARACTER SET utf8;\n\nuse evaluateg;\n\ndrop database evaluateg;','2018-11-06 08:08:42.119297','evaluate 创建用户及库'),(8,'    readonly_fields = (\'deferred_on\',\'company\',\'date_of_appointment\',)\n    list_display=[\'name\',\'create_date\',\'registered_capital\']\n    inlines = [InlShareholder, InlEnterpriseAwards]\n    list_display_link\n    list_editable\n    list_max_show_all = 200\n    list_per_page = 100\n    search_fields = (\'name\', \'city\')\n    list_filter = (\'country\',)\n    ordering = (\'-id\',)\n    fields = (\'name\', \'city\')\n    exclude = (\'country\')\n\n    # 使用radio-button代替select-box( ForeignKey或者有choices选项时)。\n    radio_fields = {\"group\": admin.VERTICAL}\n\n    fieldsets = (\n        (\n            \'基本选项\',{\n                \'fields\':(\'name\',),\n            }\n        ),\n        (\n            \'可选选项\',{\n                \'fields\':(\'create_date\',),\n                \'classes\':(\'collapse\',),\n            }\n        )\n    )','2018-10-30 06:29:57.627601','admin 属性'),(9,'mysql -uroot -pmissing','2018-10-30 03:54:08.358139','本机mysql密码'),(10,'select * from xxx \\G;\n','2018-10-30 01:32:51.572670','mysql 增删改查'),(11,'    def formfield_for_foreignkey(self, db_field, request, **kwargs):\n        if db_field.name == \"car\":\n            kwargs[\"queryset\"] = Car.objects.filter(owner=request.user)\n        return super(MyModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)','2018-10-30 06:30:00.046573','admin 外键筛选'),(12,'\n20181108 21:48:38\n定期备份数据\n\n20181106 11:27:54\nversion = 0.9.5\n    增加保存功能\n    可以查看 qt快捷键\n    def save_text(self):\n\n20181105 17:29:15\nversion = 0.9.4\n    断线重新运行\n    main()\n    修改了小bug\n    get_Labels中之前遗留的问题\n    \n\n20181030 21:50:23\n新建后左侧显示\n    def cl_bt_bt_clicked(self):\n        item = TreeWidgetItem(self.tree)\n        item.setText(0,cobj.name)\n        item.model_data = {\n                            \'id\':cobj.id,\n                            \'name\':cobj.name,\n                            \'text\':cobj.text,\n                            \'object\':cobj,\n        }\n        self.tree.treeitems.append(item)\n\n# 20181030 10:25:16 fix bug\n    version = 0.9.2\n    rest[pid][id] ->rest[pid][\'children\'][id]\n    rest[pid][id][\'children\'] -> rest[pid][\'children\'][id][\'children\']\n\n# 20181029 23:24:23 完成基本功能\n    version = 0.9.1','2018-11-08 13:48:54.924407','know version'),(13,'    def save_model(self, request, obj, form, change):\n        obj.user = request.user\n        obj.save()','2018-10-30 06:30:02.312545','admin 保存'),(14,'\n\n\n    def formfield_for_dbfield(self, db_field, request, **kwargs):\n        if db_field.name == \'groups\':\n            kwargs[\"queryset\"] = Group.objects.filter(id= request.GET[\'type\'])\n        field =  super().formfield_for_dbfield(db_field, request, **kwargs)\n\n        if db_field.name == \'is_staff\':\n            field.initial = True\n\n        if db_field.name == \'groups\':\n            field.initial = request.GET[\'type\']\n\n        return field\n\n\n\n\n\n\n    def formfield_for_manytomany(self, db_field, request, **kwargs):\n        if db_field.name == \'groups\':\n            kwargs[\"queryset\"] = Group.objects.filter(id= request.GET[\'type\'])\n        field =  super().formfield_for_manytomany(db_field, request, **kwargs)\n        if db_field.name == \'groups\':\n            field.initial = request.GET[\'type\']\n        return field\n','2018-10-30 06:15:35.460444','admin 设置默认值'),(15,'    # ModelAdmin提供了一个钩子程序 —— 它有一个名为queryset() 的方法，该方法可以确定任何列表页面返回的默认查询集\n    def get_queryset(self, request):\n            qs = super(MyModelAdmin, self).get_queryset(request)\n            if request.user.is_superuser:\n                return qs\n            return qs.filter(author=request.user)\n    # 定制搜索功能\n    def get_search_results(self, request, queryset, search_term):\n        queryset, use_distinct = super(PersonAdmin, self).get_search_results(request, queryset, search_term)\n        try:\n            search_term_as_int = int(search_term)\n        except ValueError:\n            pass\n        else:\n            queryset |= self.model.objects.filter(age=search_term_as_int)\n        return queryset, use_distinct\n\n    def get_inline_instances(self, request, obj=None):\n        print(request.GET[\'type\'])\n        if request.GET[\'type\'] == \'2\':\n            return [inline(self.model, self.admin_site) for inline in self.inlines[0:1]]\n\n        elif request.GET[\'type\'] == \'3\':\n            return [inline(self.model, self.admin_site) for inline in self.inlines[1:]]\n\n        return self.inlines\n\n    def get_exclude(self, request, obj=None):\n        qs = super().get_queryset(request)\n        if request.user.is_superuser:\n            return [\'will\'] + self.exclude\n\n','2018-10-30 06:43:08.509662','admin 属性调用函数'),(16,'只能再列表显示\n    def mget_company(self,obj):\n        report = obj.investreport or obj.bankreport\n        return report.companyInfo\n    \n    mget_company.short_description = \'名称\'\n\nformat_html(\n                    \'<span style=\"color: {};\">{}</span>\',\n                    color_code,\n                    ret,\n                )','2018-11-01 08:45:20.797148','admin 新增属性'),(17,'class ShareholderInl(admin.StackedInline):\n    # 教程 https://www.cnblogs.com/linxiyue/p/4074562.html\n    # \n    many-to-many models 需要单独设置 并且可以把中间件设置出来\n        # members = models.ManyToManyField(Person, through=\'Membership\')\n    Using generic relations as an inline 不知道这个是干什么的\n\n    model = Shareholder\n    extra = 0\n    max_num = 5\n\n    # 多个外键的情况\n    fk_name = \"to_person\"\n\n    # 设置显示的数量\n    def get_extra(self, request, obj=None, **kwargs):\n        extra = 2\n        if obj:\n            return extra - obj.binarytree_set.count()\n        return extra\n\n    def get_max_num(self, request, obj=None, **kwargs):\n        max_num = 10\n        if obj.parent:\n            return max_num - 5\n        return max_num','2018-10-30 06:30:14.863387','admin 内联'),(18,'密码需要特别设置','2018-10-30 07:36:44.243235','重写admin user 新建'),(19,'menu 目录\nindex 首页\nfooter base.html 里面重写\n\n可以通过对suit文件夹搜索 来找到相应修改的位置','2018-10-30 09:17:43.939054','suit'),(20,'netstat -tlpn','2018-10-31 01:00:30.105844','查看网络端口'),(21,'python3 /home/uftp/my/P031_my_blockchain_assets/z01_save_data.py','2018-10-31 01:04:13.988029','运行blockchain'),(22,'C:\\Users\\vanlance\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\suit','2018-10-31 01:27:49.263319','suit 目录地址'),(23,'https://lanhuapp.com/url/9tNs0\nhttp://demo.embway.com:8002/','2018-10-31 01:53:36.112872','evaluate 相关网站'),(24,'new','2018-10-31 01:59:25.098487','new'),(25,'import os\n\npath = \'sdf/ag/sdf/12432.jjj\'\nhaspath = os.path.split(path)[0]\nif not os.path.exists(haspath):\n    os.makedirs(haspath)\n\n','2018-10-31 09:44:00.029994','新建文件夹'),(26,'request.user.is_authenticated()','2018-11-01 01:46:02.237430','无用户判断'),(27,'class EvaluationOfEnterprisesAdmin(admin.ModelAdmin):    \n    class Media:\n        js = (\'/static/js/opt_evaluation.js\',)','2018-11-01 02:51:51.504780','增加 js'),(28,'--　--','2018-11-01 04:18:25.531482','全角空格'),(29,'parseInt','2018-11-01 06:30:59.882486','js 类型转换'),(30,'确认框 confirm\n警告框 alert\n输入框 prompt','2018-11-01 07:43:52.790513','js 对话框'),(31,'new','2018-11-01 07:44:11.052281','new'),(32,'https://blog.csdn.net/ai_shuyingzhixia/article/details/81255095\n\n------------------------------js-------------------------\n        // 修改弹出框的title, 显示弹框\n        function ShowCreateModal(title){\n            $(\"#createFileTitle\").text(title);\n            $(\'#createFileMModal\').modal(\'show\');\n        }\n        // 关闭弹框， 获取输入值，然后执行逻辑\n        $(\"#createFileSureBut\").click(function (){\n            $(\"#createFileMModal\").modal(\"hide\");\n            var inputFileName = $(\"#fileName\").val();\n            console.log(\"input file name : \" + inputFileName);\n        });\n\n\n\n------------------------------html-------------------------\n<div class=\"modal fade\" id=\"createFileMModal\" role=\"dialog\" aria-labelledby=\"exampleModalLabel\" aria-hidden=\"true\">\n  <div class=\"modal-dialog\" role=\"document\">\n    <div class=\"modal-content\">\n      <div class=\"modal-header\">\n        <h5 class=\"modal-title\" id=\"createFileTitle\">创建文件</h5>\n        <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\">\n          <span aria-hidden=\"true\">&times;</span>\n        </button>\n      </div>\n      <div class=\"modal-body\">\n        <form>\n          <div class=\"form-group\">\n            <label for=\"fileName\" class=\"col-form-label\">文件名</label>\n            <input type=\"text\" autofocus class=\"form-control\" id=\"fileName\">\n          </div>\n        </form>\n      </div>\n      <div class=\"modal-footer\">\n        <button type=\"button\" class=\"btn btn-primary\" id=\"createFileSureBut\">确定</button>\n      </div>\n    </div>\n  </div>\n</div>','2018-11-01 08:57:51.057713','弹出框'),(33,'172.30.16.112','2018-11-01 09:16:15.118834','本机地址'),(34,'http://www.runoob.com/','2018-11-02 08:43:08.174867','教程大全'),(35,'http://www.runoob.com/ionic/ionic-install.html\n\n\n安装 nodejs\nsudo apt-get install nodejs-legacy nodejs\nsudo apt-get install npm\n\n安装 jdk\n查看ionic安装教程\n\n安装 sdk\n查看ionic安装教程\n\n\n\n\n切换源\nnpm set registry https://registry.npm.taobao.org\n再安装\nnpm install -g cordova ionic\n\n创建应用\nionic start myApp tabs\n\n创建Android应用\n$ cd myApp\n$ ionic cordova platform add android\n$ ionic cordova build android\n$ ionic cordova emulate android\n\n\n用ubuntu 安装出现问题\nwindows下安装可以 但创建应用模板是需要用到python2 想想怎么处理再进行安装\n\niOS真机测试教程','2018-11-09 09:44:04.762196','ionic 安装'),(36,'20181031 打车去买的车位 7万','2018-11-05 01:01:13.168006','周三买车位'),(37,'20181104 周日上午10：30 玉玉下周还要去看\n郭小丹重新整了牙，1个月不能吃东西','2018-11-05 01:04:24.541601','看牙齿'),(38,'周日买的飞机票\n20181116 17：35-20：05飞机票 天津-温州 妈妈 470元','2018-11-05 01:07:58.288909','买飞机票'),(39,'autocomplete=\"off\"','2018-11-05 01:38:26.109457','input 无历史'),(40,'<input list=\"browsers\" autocomplete=\"off\" name=\"incubator\" style=\"width: 278px;height: 19px;border: 1px solid #cccccc;box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);    transition: border linear .2s, box-shadow linear .2s;padding: 4px 6px;margin-bottom: 9px;    font-size: 12px;border-radius: 4px;\">\n                        <datalist id=\"browsers\" style=\"width: 292px\">\n                        {% for incubator in incubators %}\n                        <option value=\"{{incubator.name}}\"></option>\n                        {%  endfor  %}\n                        </datalist>','2018-11-05 01:40:02.084250','datalist 下拉输入框'),(41,'pip install --download E:\\python27\\packages pandas\n\n环境管理器\n\n\n\n安装\n    pip3 install virtualenv\n创建文件夹\n创建环境\n    virtualenv --no-site-packages -p /usr/bin/python3 venv\n启动环境\n    f:\\env\\venv\\Scripts\\activate\n    linux  source venv/bin/activate\n关闭环境\n    f:\\env\\venv\\Scripts\\deactivate\n    linux deactivate\n    \npip install -r requirements.txt','2018-11-05 02:55:01.932333','virtualenv'),(42,'\n\n设置环境\nsource evn/evn/bin/activate\n\n查看端口\nnetstat -tlnp\n\n杀进程\nkill id号\n\n后台运行\nnohup python manage.py runserver 0.0.0.0:8002 &\n\n克隆数据\ngit clone ssh://dev.embway.com:7999/biev/server.git\n\n切换分支\ngit checkout release/BIEV-1\n\nmysql数据库\nmysql -uevaluateg -pevaluateg\n','2018-11-06 08:24:37.819357','部署'),(43,'find ~ -name 文件名','2018-11-05 03:11:49.491214','ubuntu命令'),(44,'user     = debian-sys-maint\npassword = 8UHyVyagB2YSjwPA\n\nmysql -udebian-sys-maint -p8UHyVyagB2YSjwPA','2018-11-05 03:21:54.555146','mysql服务器密码'),(45,'删除数据库\ndrop database evaluateg;','2018-11-05 03:22:25.650756','基本命令'),(46,'代码管理：https://dev.embway.com\n项目管理：https://dev.embway.com:18443\n文档管理：https://dev.embway.com:18444\n\nssh://git@dev.embway.com:7999/biev/server.git','2018-11-05 08:12:19.132160','代码管理'),(47,'创建并切换分支\n    git checkout -b dev\n    等同于下面两句\n        git branch dev\n        git checkout dev','2018-11-05 08:14:39.217401','git 分支'),(48,'https://dev.embway.com:18443 项目管理页面\n打开项目 ->创建问题 ->创建分支（到了代码页面）\n通过clone找到上传地址\n\n添加-f强行进行上传\ngit push -f evaluate release/BIEV-1','2018-11-05 08:39:56.696324','代码提交流程'),(49,'https://www.cnblogs.com/qypx520/p/6022787.html\n一.android开发\n1. 首先要安装node环境,Ionic的安装和后续的许多前端工具的安装都依赖于node的包管理器npm。\nnodeJs环境的安装很简单，去官网下载最新版的NodeJs直接安装即可。 Node官网： https://nodejs.org/\nnode环境变量在安装过程中会自动配置，安装完成后在cmd中输入 npm -v 回车。如果出现版本号说明安装成功。\nnode安装参考：http://jingyan.baidu.com/article/b0b63dbfca599a4a483070a5.html\n2. 安装jdk并且配置环境变量,如果已经安装了jdk则跳过这步。\njdk下载地址：http://www.oracle.com/technetwork/java/javase/downloads/index.html\n安装完成以后配置环境变量：\nJAVA_HOME:\nJDK的安装路径，这个环境变量本身不存在，需要创建，创建完则可以利用%JAVA_HOME%作为统一引用路径，其值为：jdk在你电脑上的安装路径。\nPATH：\nPATH属性已存在，可直接编辑。作用是用于配置路径，简化命令的输入，其值为：%JAVA_HOME%\\bin。  \nCLASSPATH：\n用于编译时JAVA类的路径，注意这里设置的是两个值，(.;)表示的是JVM先搜索当前目录。其值为：.;%JAVA_HOME%\\lib\\tools.jar。\n配置完毕后，通过cmd运行以下命令：java -version，javac 如果出现返回信息，则设置成功。\n3. 安装Android SDK. \n下载地址： http://developer.android.com/sdk/index.html 这个地址被墙了。需要FQ使用。\n这里可以只下载Android SDK 不需要一并下载 Android Studio。下载完成并安装然后向系统Path环境变量中添加两个值。分别是 Android SDK中tools目录的路径和platform-tools的路径。例如：\nC:\\Program Files (x86)\\Android\\android-sdk\\tools;\nC:\\Program Files (x86)\\Android\\android-sdk\\platform-tools;\n如果发现Android SDK安装目录中并没有 “ platform-tools”这个文件夹，应该运行tools目录下的android.bat文件，然后出现如下界面，勾选Android SDK Platform-tools 然后安装。\n\n环境变量配置完成以后在cmd中输入 android并且回车。如果出现android sdk manager则说明安装成功。\n4. 安装 Apache ant.\nant下载地址： http://ant.apache.org/bindownload.cgi\n环境变量：\nWindows下ANT用到的环境变量主要有2个： ANT_HOME 和 PATH。 \neg：\n1. 设置ANT_HOME指向ant的安装目录。 \n设置方法：ANT_HOME = D:\\apache_ant_1.7.0 \n2. 设置bin和lib目录到PATH变量中。将%ANT_HOME%\\bin; %ANT_HOME%\\lib添加到环境变量的path中。 \n设置方法：PATH = %ANT_HOME%\\bin; %ANT_HOME%\\lib \n%ANT_HOME%可以用真实的路径代替。\n安装完成以后在cmd中输入 ant -version 验证是否安装成功。\n5.安装ionic和cordova\nnpm install -g cordova ionic\n查看是否安装成功：ionic  –v   cordova  –v\n6. 通过Ionic创建一个项目\nionic start myApp blank 创建一个空白的app项目 \nionic start myApp tabs 创建一个带有tabs项目\nionic start myApp sidemenu 创建一个带有滑动的项目\n7. 给项目添加android平台\nionic  platform android\n8. 在模拟器中运行项目\nionic emulate android\n9. 启动浏览器服务\nionic serve\n10. 打包成app\nionic package','2018-11-05 09:22:45.682027','安装流程'),(50,'\n改完名字刷新一下左侧 显示信息\n可以直接呼出 sublime\ntable键 为4个空格\n\n\n附件的开发\n图片的显示\n\n高亮显示搜索\n通过不同颜色区别搜索的内容\n搜索进行优化？？\n\n搜索后通过树结构进行显示？\n\n最好时基于sublime 开发插件？\n\n\n\n设置状态栏 print的内容可以进行显示\n\n增加快捷键\n\n数据需要加密 图片 文本等\n\n','2018-11-09 01:58:57.644858','改进'),(51,'        # set shortcut\n        save = QAction(QIcon(\'\'),  \'save\',  self)\n        save.setShortcut(\'Ctrl+S\')\n        save.setStatusTip(\'save application\')\n        save.triggered.connect(self.save_text)\n        menubar = self.menuBar()\n        file = menubar.addMenu(\'&File\')\n        file.addAction(save)','2018-11-06 03:26:29.019027','qt快捷键'),(52,'放弃修改\ngit checkout 文件','2018-11-06 08:18:36.426824','放弃修改'),(53,'郭小丹\n西西和啊东\n','2018-11-06 08:21:26.459237','去宝坻看眼睛店'),(54,'\n天津津松伟业科技有限公司\n91120116MA06U3485M\n15022666265\n\n康之源（天津）科技发展有限公司\n91120116MA05JXJU10\n13920384338\n\n卡博瑞（天津）智能科技有限责任公司\n91120116351564414W\n18522877619\n\n天津卓越信通科技有限公司\n91120116MA05K4NU30\n13681032839\n\n道思科技（天津）有限公司\n91120116MA05NQL52J\n18674015110','2018-11-06 08:41:45.379440','资料'),(55,'http://www.cnblogs.com/huangxm/p/5770735.html','2018-11-07 02:25:50.903042','django 查看权限'),(56,'sublime插件\n    1 提取多行文字并生成逗号连接的字符串\n','2018-11-09 02:34:17.446209','添加sublime插件'),(57,'打开控制台 ctrl+\'`\' \n调用插件   view.run_command(\'first\')\n插件名称是通过大小写分段 并且_连接的\n\napi 接口\nhttp://www.sublimetext.com/docs/3/api_reference.html\n\n*Default (Windows).sublime-keymap  配置插件的快捷键\n*Default.sublime-commands 配置命名，可以再ctrl+shift+p打开的命令窗口使用\n*Main.sublime-menu 菜单配置，也就是给我们的插件一个菜单入口','2018-11-07 03:58:42.344997','sbulime插件教程'),(58,'        exeFile = \"C:\\\\Windows\\\\System32\\\\cmd.exe\"\n        exeFile = \'F:\\\\my\\\\P028_knowledge_system\\\\knowqt\\\\main.py\'\n        exePath = \"F:\\\\my\\\\P028_knowledge_system\\\\knowqt\\\\\"\n        os.chdir(exePath)\n        os.startfile(exeFile)','2018-11-07 04:28:28.048550','直接打开 程序'),(59,'django程序和普通程序分别用不同的快捷键\n用try traceback 拦截错误','2018-11-07 09:53:19.172492','sublime 直接运行程序'),(60,'上传\n设置setting\n    MEDIA_ROOT = \'company/static/\'\nmodels\n    business_license_pic = models.ImageField(upload_to=\'upload\',blank=True,null=True)\n输出路径\n    \'/static/\' + str(obj.business_license_pic)\n\n点击放大图片\n    \'<div style=\"height: 50px;overflow: hidden;\"><a href=\"/\' + path + \'\" width=30 height=50 data-lightbox=\"\' + path + \'\"><img src=\"/\' + path + \'\" width=30 height=50\" /></a></div>\'\n    lightbox包','2018-11-07 09:35:57.479591','django图片'),(61,'STATIC_URL = \'/static/\'\nSTATIC_ROOT = os.path.join(BASE_DIR, \"static\")\nSTATICFILES_DIRS = (\n    (\'css\', os.path.join(STATIC_ROOT, \'css\')),\n    (\'js\', os.path.join(STATIC_ROOT, \'js\')),\n    (\'amaze\', os.path.join(STATIC_ROOT, \'amaze\')),\n    (\'imgs\', os.path.join(STATIC_ROOT, \'imgs\')),\n    (\'jquery-weui\', os.path.join(STATIC_ROOT, \'jquery-weui\')),\n    (\'upload\', os.path.join(STATIC_ROOT, \'upload\')),\n    (\'lightbox\', os.path.join(STATIC_ROOT, \'lightbox\')),\n    (\'download_image\', os.path.join(STATIC_ROOT, \'download_image\')),\n)','2018-11-07 09:40:46.187959','静态路径'),(62,'lightbox.zip','2018-11-07 09:43:40.429767','lightbox'),(63,'手机app\n玉玉的平板管理\n自己番茄','2018-11-07 09:49:07.300660','手机app'),(64,'研究一下 公安局的程序\nvote_src.tar.gz','2018-11-07 09:50:53.502326','研究一下 公安局的程序'),(65,'用django 做网页端','2018-11-07 09:52:09.104373','玉玉的平板管理'),(66,'sublime 参考多重快捷键','2018-11-07 09:53:33.080320','参考多重快捷键'),(67,'20181108 09:31:38\n马桶昨天修好了\n用衣架 勾出了梳子','2018-11-08 01:32:18.970032','马桶'),(68,'F:\\study\\video','2018-11-08 02:27:50.963143','达内'),(69,'from django.contrib import messages\nmessages.add_message(request, messages.INFO, \'Hello world.\')\n\n有几个快捷方法提供标准的方式来新增消息并带有常见的标签（这些标签通常表示消息的HTML 类型）\n\nmessages.debug(request, \'%s SQL statements were executed.\' % count)\nmessages.info(request, \'Three credits remain in your account.\')\nmessages.success(request, \'Profile details updated.\')\nmessages.warning(request, \'Your account expires in three days.\')\nmessages.error(request, \'Document deleted.\')','2018-11-08 03:21:57.149154','message'),(70,'保存sublime插件\nF:\\sublime\\SublimeText_XP85\\Data\\Packages','2018-11-09 02:36:30.678535','保存sublime插件'),(71,'发行盈亏比','2018-11-09 01:40:39.419666','投资'),(72,'1. 登录Linux，切换到root用户 sudo root 获取root用户权限，当前工作目录不变(需要root密码)或 sudo -i 不需要root密码直接切换成root（需要当前用户密码） 2. 在usr目录下建立java安装目录cd /usr 之后mkdir java 3.将jdk-8u141-linux-x64.tar.gz拷贝到java目录下 cp jdk-8u141-linux-x64.tar.gz（其所在路径） /usr/java/ 4.解压jdk到当前目录 tar -zxvf jdk-8u141-linux-x64.tar.gz得到文件夹 jdk1.8.xx 5.安装完毕为他建立一个链接以节省目录长度(可以省略这一步) ln -s /usr/java/jdk1.8.xx/ /usr/jdk 6.编辑配置文件，配置环境变量 vim /etc/profile 添加如下内容：JAVA_HOME根据实际目录来 JAVA_HOME=/usr/java/jdk1.8.xx CLASSPATH=$JAVA_HOME/lib/ PATH=$PATH:$JAVA_HOME/bin export PATH JAVA_HOME CLASSPATH 7.重启机器或执行命令 ：source /etc/profile sudo shutdown -r now 8.查看安装情况 java -version java version \"1.8.xx\" Java(TM) SE Runtime Environment (build 1.8.xx) Java HotSpot(TM) Client VM (build 25.60-b23, mixed mode) 可能出现的错误信息： bash: ./java: cannot execute binary file 出现这个错误的原因可能是在32位的操作系统上安装了64位的jdk， 查看jdk版本和Linux版本位数是否一致。 查看linux是32位还是64位系统： sudo uname --m i686 //表示是32位 x86_64 // 表示是64位','2018-11-09 08:29:57.102120','安装jdk'),(73,'http://www.cnblogs.com/ranxf/p/9112614.html\nvim /etc/profile\n\nexport ANDROID_SDK_HOME=/home/ranxf/Android/Sdk/android-sdk-linux\nexport PATH=$PATH:${ANDROID_SDK_HOME}/tools\nexport PATH=$PATH:${ANDROID_SDK_HOME}/platform-tools\n\n运行 /home/ranxf/Android/Sdk/android-sdk-linux/tools/android 下载所需要的sdk\n\n\n\n有问题再运行下面的\nsource /etc/profile\n在命令行输入：vim /root/.bashrc,并在文件末尾加入一行source etc/profile命令，保存。这样就大功告成了。','2018-11-09 09:41:12.215368','android sdk'),(74,'http://www.androiddevtools.cn/ ','2018-11-09 09:00:08.920334','android工具');
/*!40000 ALTER TABLE `data_content` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_content_labels`
--

DROP TABLE IF EXISTS `data_content_labels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data_content_labels` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content_id` int(11) NOT NULL,
  `label_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `data_content_labels_content_id_label_id_5e7f0251_uniq` (`content_id`,`label_id`),
  KEY `data_content_labels_label_id_4e5b2911_fk_data_label_id` (`label_id`),
  CONSTRAINT `data_content_labels_content_id_51c8b603_fk_data_content_id` FOREIGN KEY (`content_id`) REFERENCES `data_content` (`id`),
  CONSTRAINT `data_content_labels_label_id_4e5b2911_fk_data_label_id` FOREIGN KEY (`label_id`) REFERENCES `data_label` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_content_labels`
--

LOCK TABLES `data_content_labels` WRITE;
/*!40000 ALTER TABLE `data_content_labels` DISABLE KEYS */;
INSERT INTO `data_content_labels` VALUES (5,1,5),(6,1,6),(9,1,8),(7,2,4),(8,2,7),(10,2,8),(11,3,10),(12,4,12),(71,5,9),(44,5,31),(70,5,52),(14,6,17),(69,7,17),(46,7,31),(22,8,19),(30,9,20),(18,10,17),(21,11,21),(24,12,11),(23,12,24),(25,13,18),(28,14,18),(31,15,19),(32,16,19),(33,17,25),(35,18,7),(34,18,18),(36,19,26),(37,20,27),(38,21,28),(40,21,29),(41,22,26),(43,23,30),(45,25,33),(49,26,9),(48,27,18),(50,28,7),(51,29,35),(52,30,36),(53,32,37),(54,33,38),(55,34,40),(56,35,42),(57,36,44),(58,37,46),(59,38,47),(60,39,49),(61,40,50),(62,41,51),(64,42,52),(65,43,56),(67,44,14),(66,44,20),(68,45,17),(72,46,57),(79,46,62),(73,47,58),(74,48,38),(75,49,42),(76,50,60),(86,50,67),(77,51,61),(80,52,58),(81,53,63),(82,54,64),(83,55,9),(84,55,65),(85,56,67),(109,56,68),(87,57,69),(88,58,69),(99,59,74),(90,60,70),(91,61,71),(92,62,72),(97,63,65),(96,64,65),(95,64,73),(98,65,67),(100,66,65),(101,67,75),(103,68,40),(104,68,65),(102,68,77),(105,69,9),(106,70,67),(107,71,78),(108,71,79),(110,72,42),(111,73,42),(112,74,40),(113,74,81);
/*!40000 ALTER TABLE `data_content_labels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_history`
--

DROP TABLE IF EXISTS `data_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_date` datetime(6) DEFAULT NULL,
  `content_id` int(11) NOT NULL,
  `label_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `data_history_content_id_73cc4310_fk_data_content_id` (`content_id`),
  KEY `data_history_label_id_a350d74c_fk_data_label_id` (`label_id`),
  CONSTRAINT `data_history_content_id_73cc4310_fk_data_content_id` FOREIGN KEY (`content_id`) REFERENCES `data_content` (`id`),
  CONSTRAINT `data_history_label_id_a350d74c_fk_data_label_id` FOREIGN KEY (`label_id`) REFERENCES `data_label` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_history`
--

LOCK TABLES `data_history` WRITE;
/*!40000 ALTER TABLE `data_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `data_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_label`
--

DROP TABLE IF EXISTS `data_label`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data_label` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `queue` longtext NOT NULL,
  `grade` smallint(6) DEFAULT NULL,
  `create_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_label`
--

LOCK TABLES `data_label` WRITE;
/*!40000 ALTER TABLE `data_label` DISABLE KEYS */;
INSERT INTO `data_label` VALUES (1,'main',-1,'',10,'2018-10-29 15:38:37.375000'),(2,'qt',59,'',10,'2018-11-05 08:56:58.854474'),(3,'qtreewidget',2,'',10,'2018-10-29 15:41:49.334000'),(4,'qtreewidgetitem',3,'',10,'2018-10-29 15:41:36.143000'),(5,'模态',2,'',10,'2018-10-29 15:45:05.101000'),(6,'qdialog',2,'',10,'2018-10-29 15:45:18.768000'),(7,'坑',59,'',10,'2018-11-05 08:57:19.627213'),(8,'pyqt5',11,'',10,'2018-10-29 16:05:43.512000'),(9,'django',11,'',10,'2018-10-29 16:05:43.713000'),(10,'model',9,'',10,'2018-10-29 16:02:37.382000'),(11,'python',59,'',10,'2018-11-05 08:56:59.041471'),(12,'服务器',59,'',10,'2018-11-05 08:57:15.865259'),(13,'工作',59,'',10,'2018-11-05 08:57:12.753297'),(14,'evaluate',38,'',10,'2018-11-01 09:15:13.671604'),(15,'路径',14,'',10,'2018-10-30 01:10:06.517219'),(16,'mysql',59,'',10,'2018-11-05 08:57:11.433314'),(17,'command',16,'',10,'2018-10-30 01:12:58.895054'),(18,'admin',9,'',10,'2018-10-30 01:22:22.664579'),(19,'属性',18,'',10,'2018-10-30 01:22:32.621453'),(20,'密码',16,'',10,'2018-10-30 01:31:24.788763'),(21,'外键',18,'',10,'2018-10-30 02:22:40.038104'),(22,'myapp',59,'',10,'2018-11-05 08:57:03.033421'),(23,'know',22,'',10,'2018-10-30 02:30:25.302253'),(24,'version',23,'',10,'2018-10-30 02:30:37.365101'),(25,'内联',18,'',10,'2018-10-30 06:29:36.029873'),(26,'suit',9,'',10,'2018-10-30 09:17:53.647931'),(27,'command',12,'',10,'2018-10-31 01:00:53.009557'),(28,'程序',12,'',10,'2018-10-31 01:04:25.170890'),(29,'120.79.41.9',12,'',10,'2018-10-31 01:05:21.448181'),(30,'网站',14,'',10,'2018-10-31 01:53:26.421996'),(31,'command',14,'',10,'2018-10-31 01:54:21.023311'),(32,'os',11,'',10,'2018-10-31 09:44:10.093869'),(33,'文件操作',32,'',10,'2018-10-31 09:44:18.094767'),(34,'js',59,'',10,'2018-11-05 08:57:13.889285'),(35,'类型转换',34,'',10,'2018-11-01 06:31:13.453319'),(36,'对话框',34,'',10,'2018-11-01 07:44:02.036394'),(37,'bootstrap',34,'',10,'2018-11-01 08:58:03.581555'),(38,'安博伟业',13,'',10,'2018-11-01 09:15:10.125649'),(39,'密码',38,'',10,'2018-11-01 09:15:32.357370'),(40,'教程',59,'',10,'2018-11-05 08:57:19.450213'),(41,'ionic教程',80,'',10,'2018-11-09 09:00:33.044034'),(42,'安装',41,'',10,'2018-11-04 11:20:09.501494'),(43,'记录',1,'',10,'2018-11-05 01:01:21.785898'),(44,'汽车',43,'',10,'2018-11-05 01:01:32.103768'),(45,'房子',43,'',10,'2018-11-05 01:01:39.107677'),(46,'健康',43,'',10,'2018-11-05 01:04:33.172489'),(47,'出行',43,'',10,'2018-11-05 01:07:31.516247'),(48,'html',59,'',10,'2018-11-05 08:56:58.668474'),(49,'input',48,'',10,'2018-11-05 01:38:42.595248'),(50,'datalist',48,'',10,'2018-11-05 01:39:45.872453'),(51,'环境管理',11,'',10,'2018-11-05 02:44:35.154616'),(52,'部署',12,'',10,'2018-11-05 03:07:53.464181'),(53,'操作系统',59,'',10,'2018-11-05 08:57:09.905333'),(54,'linux',53,'',10,'2018-11-05 03:10:57.269872'),(55,'windows',53,'',10,'2018-11-05 03:11:02.181809'),(56,'command',54,'',10,'2018-11-05 03:11:10.564706'),(57,'网站',38,'',10,'2018-11-05 08:02:32.058540'),(58,'git',59,'',10,'2018-11-05 08:57:01.142444'),(59,'编程',1,'',10,'2018-11-05 08:56:40.450703'),(60,'问题',23,'',10,'2018-11-05 09:32:23.159767'),(61,'快捷键',2,'',10,'2018-11-06 03:26:38.859902'),(62,'dev.embway.com',12,'',10,'2018-11-06 07:41:27.347273'),(63,'投资',43,'',10,'2018-11-06 08:21:36.381109'),(64,'资料',14,'',10,'2018-11-06 08:40:06.975677'),(65,'待学习',66,'',10,'2018-11-07 03:02:23.592473'),(66,'待办',1,'',10,'2018-11-07 03:02:21.154504'),(67,'待办理',66,'',10,'2018-11-07 03:02:33.361350'),(68,'sublime',59,'',10,'2018-11-07 04:27:37.173190'),(69,'教程',68,'',10,'2018-11-07 04:27:41.180137'),(70,'图片',9,'',10,'2018-11-07 09:38:13.772884'),(71,'路径',9,'',10,'2018-11-07 09:40:57.195820'),(72,'插件',9,'',10,'2018-11-07 09:43:50.679639'),(73,'案例',9,'',10,'2018-11-07 09:50:40.099495'),(74,'完成',1,'',10,'2018-11-07 09:52:47.468891'),(75,'生活',43,'',10,'2018-11-08 01:33:21.778241'),(76,'ml',59,'',10,'2018-11-08 02:27:28.163426'),(77,'教程',76,'',10,'2018-11-08 02:27:35.130341'),(78,'投资',1,'',10,'2018-11-09 01:40:45.489585'),(79,'my_blockchain_assets',22,'',10,'2018-11-09 01:41:28.910042'),(80,'android',59,'',10,'2018-11-09 09:00:30.908057'),(81,'工具',80,'',10,'2018-11-09 09:00:38.788959');
/*!40000 ALTER TABLE `data_label` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(9,'data','content'),(8,'data','history'),(7,'data','label'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-10-29 15:34:34.303000'),(2,'auth','0001_initial','2018-10-29 15:34:37.424000'),(3,'admin','0001_initial','2018-10-29 15:34:38.366000'),(4,'admin','0002_logentry_remove_auto_add','2018-10-29 15:34:38.654000'),(5,'contenttypes','0002_remove_content_type_name','2018-10-29 15:34:39.429000'),(6,'auth','0002_alter_permission_name_max_length','2018-10-29 15:34:39.791000'),(7,'auth','0003_alter_user_email_max_length','2018-10-29 15:34:40.153000'),(8,'auth','0004_alter_user_username_opts','2018-10-29 15:34:40.435000'),(9,'auth','0005_alter_user_last_login_null','2018-10-29 15:34:40.800000'),(10,'auth','0006_require_contenttypes_0002','2018-10-29 15:34:41.065000'),(11,'auth','0007_alter_validators_add_error_messages','2018-10-29 15:34:41.360000'),(12,'auth','0008_alter_user_username_max_length','2018-10-29 15:34:42.032000'),(13,'data','0001_initial','2018-10-29 15:34:44.014000'),(14,'data','0002_auto_20181028_2229','2018-10-29 15:34:44.347000'),(15,'data','0003_auto_20181029_1125','2018-10-29 15:34:44.833000'),(16,'data','0004_content_name','2018-10-29 15:34:45.247000'),(17,'data','0005_remove_content_attachment','2018-10-29 15:34:45.592000'),(18,'sessions','0001_initial','2018-10-29 15:34:46.137000');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-12 21:59:14
