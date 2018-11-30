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
) ENGINE=InnoDB AUTO_INCREMENT=156 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_content`
--

LOCK TABLES `data_content` WRITE;
/*!40000 ALTER TABLE `data_content` DISABLE KEYS */;
INSERT INTO `data_content` VALUES (1,'self.dia.exec()','2018-10-29 15:44:48.565000','dialog模态'),(2,'self.setFlags(self.flags() | Qt.ItemIsEditable | Qt.ItemIsEnabled)','2018-10-29 15:59:36.601000','QTreeWidgetItem可编辑'),(3,'import sys,os\nsys.path.append(r\'F:\\my\\P028_knowledge_system\\knowqt\\kqj\')\nos.environ[\'DJANGO_SETTINGS_MODULE\'] =\'kqj.settings\'\nimport django \ndjango.setup()\nfrom data import models\nfrom django.db.models import Q','2018-10-29 16:02:14.101000','django单独使用model'),(4,'120.79.41.9\nroot M1\n\n','2018-11-06 03:24:52.374242','阿里云服务器'),(5,'f:\ncd F:\\mygit\\python\\evaluate\n\npython manage.py runserver 0.0.0.0:8000\n\npython manage.py makemigrations\n\npython manage.py migrate\n\npython manage.py createsuperuser\n\nmysqldump -uevaluateg -pevaluateg evaluateg  >evaluateg.sql\n\nmysql -uevaluateg -pevaluateg evaluateg< evaluateg.sql\n\n\n','2018-11-20 09:19:09.086381','evaluate 运行命令'),(6,'mysqldump -uroot -p123456 crawl_proxy  > C:\\Users\\miss\\crawl_proxy.sql\nmysql -uroot -p123456 crawl_proxy< C:\\Users\\miss\\crawl_proxy.sql','2018-10-30 01:14:06.627200','mysql数据备份'),(7,'\ncreate user \"evaluateg\"@\"%\" identified by \"evaluateg\";\ngrant all privileges on evaluateg.* to \'evaluateg\'@\'%\' with grant option;\n\n\nCREATE DATABASE evaluateg DEFAULT CHARACTER SET utf8;\n\nuse evaluateg;\n\ndrop database evaluateg;','2018-11-06 08:08:42.119297','evaluate 创建用户及库'),(8,'    readonly_fields = (\'deferred_on\',\'company\',\'date_of_appointment\',)\n    list_display=[\'name\',\'create_date\',\'registered_capital\']\n    inlines = [InlShareholder, InlEnterpriseAwards]\n    list_display_link\n    list_editable\n    list_max_show_all = 200\n    list_per_page = 100\n    search_fields = (\'name\', \'city\')\n    list_filter = (\'country\',)\n    ordering = (\'-id\',)\n    fields = (\'name\', \'city\')\n    exclude = (\'country\')\n\n    # 使用radio-button代替select-box( ForeignKey或者有choices选项时)。\n    radio_fields = {\"group\": admin.VERTICAL}\n\n    fieldsets = (\n        (\n            \'基本选项\',{\n                \'fields\':(\'name\',),\n            }\n        ),\n        (\n            \'可选选项\',{\n                \'fields\':(\'create_date\',),\n                \'classes\':(\'collapse\',),\n            }\n        )\n    )','2018-10-30 06:29:57.627601','admin 属性'),(9,'mysql -uroot -pmissing','2018-10-30 03:54:08.358139','本机mysql密码'),(10,'select * from xxx \\G;\n','2018-10-30 01:32:51.572670','mysql 增删改查'),(11,'    def formfield_for_foreignkey(self, db_field, request, **kwargs):\n        if db_field.name == \"car\":\n            kwargs[\"queryset\"] = Car.objects.filter(owner=request.user)\n        return super(MyModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)','2018-10-30 06:30:00.046573','admin 外键筛选'),(12,'\n20181108 21:48:38\n定期备份数据\n\n20181106 11:27:54\nversion = 0.9.5\n    增加保存功能\n    可以查看 qt快捷键\n    def save_text(self):\n\n20181105 17:29:15\nversion = 0.9.4\n    断线重新运行\n    main()\n    修改了小bug\n    get_Labels中之前遗留的问题\n    \n\n20181030 21:50:23\n新建后左侧显示\n    def cl_bt_bt_clicked(self):\n        item = TreeWidgetItem(self.tree)\n        item.setText(0,cobj.name)\n        item.model_data = {\n                            \'id\':cobj.id,\n                            \'name\':cobj.name,\n                            \'text\':cobj.text,\n                            \'object\':cobj,\n        }\n        self.tree.treeitems.append(item)\n\n# 20181030 10:25:16 fix bug\n    version = 0.9.2\n    rest[pid][id] ->rest[pid][\'children\'][id]\n    rest[pid][id][\'children\'] -> rest[pid][\'children\'][id][\'children\']\n\n# 20181029 23:24:23 完成基本功能\n    version = 0.9.1','2018-11-08 13:48:54.924407','know version'),(13,'    def save_model(self, request, obj, form, change):\n        obj.user = request.user\n        obj.save()','2018-10-30 06:30:02.312545','admin 保存'),(14,'\n\n\n    def formfield_for_dbfield(self, db_field, request, **kwargs):\n        if db_field.name == \'groups\':\n            kwargs[\"queryset\"] = Group.objects.filter(id= request.GET[\'type\'])\n        field =  super().formfield_for_dbfield(db_field, request, **kwargs)\n\n        if db_field.name == \'is_staff\':\n            field.initial = True\n\n        if db_field.name == \'groups\':\n            field.initial = request.GET[\'type\']\n\n        return field\n\n\n\n\n\n\n    def formfield_for_manytomany(self, db_field, request, **kwargs):\n        if db_field.name == \'groups\':\n            kwargs[\"queryset\"] = Group.objects.filter(id= request.GET[\'type\'])\n        field =  super().formfield_for_manytomany(db_field, request, **kwargs)\n        if db_field.name == \'groups\':\n            field.initial = request.GET[\'type\']\n        return field\n','2018-10-30 06:15:35.460444','admin 设置默认值'),(15,'get_queryset\nget_search_results\nget_inline_instances\nget_exclude\nget_list_display\n    list_editable 可以再这面设置\n\n\n\n# ModelAdmin提供了一个钩子程序 —— 它有一个名为queryset() 的方法，该方法可以确定任何列表页面返回的默认查询集\n    def get_queryset(self, request):\n            qs = super(MyModelAdmin, self).get_queryset(request)\n            if request.user.is_superuser:\n                return qs\n            return qs.filter(author=request.user)\n    # 定制搜索功能\n    def get_search_results(self, request, queryset, search_term):\n        queryset, use_distinct = super(PersonAdmin, self).get_search_results(request, queryset, search_term)\n        try:\n            search_term_as_int = int(search_term)\n        except ValueError:\n            pass\n        else:\n            queryset |= self.model.objects.filter(age=search_term_as_int)\n        return queryset, use_distinct\n\n    def get_inline_instances(self, request, obj=None):\n        print(request.GET[\'type\'])\n        if request.GET[\'type\'] == \'2\':\n            return [inline(self.model, self.admin_site) for inline in self.inlines[0:1]]\n\n        elif request.GET[\'type\'] == \'3\':\n            return [inline(self.model, self.admin_site) for inline in self.inlines[1:]]\n\n        return self.inlines\n\n    def get_exclude(self, request, obj=None):\n        qs = super().get_queryset(request)\n        if request.user.is_superuser:\n            return [\'will\'] + self.exclude\n\n','2018-11-21 03:06:02.732185','admin 属性调用函数'),(16,'只能再列表显示\n    def mget_company(self,obj):\n        report = obj.investreport or obj.bankreport\n        return report.companyInfo\n    \n    mget_company.short_description = \'名称\'\n\nformat_html(\n                    \'<span style=\"color: {};\">{}</span>\',\n                    color_code,\n                    ret,\n                )','2018-11-01 08:45:20.797148','admin 新增属性'),(17,'class ShareholderInl(admin.StackedInline):\n    # 教程 https://www.cnblogs.com/linxiyue/p/4074562.html\n    # \n    many-to-many models 需要单独设置 并且可以把中间件设置出来\n        # members = models.ManyToManyField(Person, through=\'Membership\')\n    Using generic relations as an inline 不知道这个是干什么的\n\n    model = Shareholder\n    extra = 0\n    max_num = 5\n\n    # 多个外键的情况\n    fk_name = \"to_person\"\n\n    # 设置显示的数量\n    def get_extra(self, request, obj=None, **kwargs):\n        extra = 2\n        if obj:\n            return extra - obj.binarytree_set.count()\n        return extra\n\n    def get_max_num(self, request, obj=None, **kwargs):\n        max_num = 10\n        if obj.parent:\n            return max_num - 5\n        return max_num','2018-10-30 06:30:14.863387','admin 内联'),(18,'密码需要特别设置','2018-10-30 07:36:44.243235','重写admin user 新建'),(19,'menu 目录\nindex 首页\nfooter base.html 里面重写\n\n可以通过对suit文件夹搜索 来找到相应修改的位置','2018-10-30 09:17:43.939054','suit'),(20,'netstat -tlpn','2018-10-31 01:00:30.105844','查看网络端口'),(21,'python3 /home/uftp/my/P031_my_blockchain_assets/z01_save_data.py','2018-10-31 01:04:13.988029','运行blockchain'),(22,'C:\\Users\\vanlance\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\suit','2018-10-31 01:27:49.263319','suit 目录地址'),(23,'https://lanhuapp.com/url/9tNs0\nhttp://demo.embway.com:8002/','2018-10-31 01:53:36.112872','evaluate 相关网站'),(24,'最好把图片按照一个方向进行缩放 按照较小的边长设置为200\n    f = 200 / min(h.w)\n    gray = cv.resize(gray,None,fx=f,fy=f)\n\n获得desc矩阵\n    desc 通过 特征检测 获得\n    加入descs descs = np.append(descs,desc,axis=0)\n    tran_x.append(descs) 输入\n    tran_y.append(label) 输出\n\n基于高斯分布的隐马尔科夫模型\n    model = hl.GaussianHMM(n_components=4（四个隐藏状态）,covariance_type=\'diag\'（相关性的矩阵的辅对角线表示协方差）,n_iter=1000（迭代次数）)\n    models[label] = model.fit(descs) 训练\n    model.score(descs) 测试分值','2018-11-21 06:53:43.264012','图像识别'),(25,'import os\n\npath = \'sdf/ag/sdf/12432.jjj\'\nhaspath = os.path.split(path)[0]\nif not os.path.exists(haspath):\n    os.makedirs(haspath)\n\n','2018-10-31 09:44:00.029994','新建文件夹'),(26,'request.user.is_authenticated()','2018-11-01 01:46:02.237430','无用户判断'),(27,'class EvaluationOfEnterprisesAdmin(admin.ModelAdmin):    \n    class Media:\n        js = (\'/static/js/opt_evaluation.js\',)','2018-11-01 02:51:51.504780','增加 js'),(28,'--　--','2018-11-01 04:18:25.531482','全角空格'),(29,'parseInt\nint','2018-11-14 09:50:24.786427','js 类型转换'),(30,'确认框 confirm\n警告框 alert\n输入框 prompt(\'11\',\'默认值无则写空字符串\')','2018-11-23 06:20:46.499348','js 对话框'),(31,'\n第一次push\ngit push -u origin master\n\ngit push  origin master','2018-11-14 11:40:59.037400','push'),(32,'https://blog.csdn.net/ai_shuyingzhixia/article/details/81255095\n\n------------------------------js-------------------------\n        // 修改弹出框的title, 显示弹框\n        function ShowCreateModal(title){\n            $(\"#createFileTitle\").text(title);\n            $(\'#createFileMModal\').modal(\'show\');\n        }\n        // 关闭弹框， 获取输入值，然后执行逻辑\n        $(\"#createFileSureBut\").click(function (){\n            $(\"#createFileMModal\").modal(\"hide\");\n            var inputFileName = $(\"#fileName\").val();\n            console.log(\"input file name : \" + inputFileName);\n        });\n\n\n\n------------------------------html-------------------------\n<div class=\"modal fade\" id=\"createFileMModal\" role=\"dialog\" aria-labelledby=\"exampleModalLabel\" aria-hidden=\"true\">\n  <div class=\"modal-dialog\" role=\"document\">\n    <div class=\"modal-content\">\n      <div class=\"modal-header\">\n        <h5 class=\"modal-title\" id=\"createFileTitle\">创建文件</h5>\n        <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\">\n          <span aria-hidden=\"true\">&times;</span>\n        </button>\n      </div>\n      <div class=\"modal-body\">\n        <form>\n          <div class=\"form-group\">\n            <label for=\"fileName\" class=\"col-form-label\">文件名</label>\n            <input type=\"text\" autofocus class=\"form-control\" id=\"fileName\">\n          </div>\n        </form>\n      </div>\n      <div class=\"modal-footer\">\n        <button type=\"button\" class=\"btn btn-primary\" id=\"createFileSureBut\">确定</button>\n      </div>\n    </div>\n  </div>\n</div>','2018-11-01 08:57:51.057713','弹出框'),(33,'172.30.16.112','2018-11-01 09:16:15.118834','本机地址'),(34,'http://www.runoob.com/','2018-11-02 08:43:08.174867','教程大全'),(35,'http://www.runoob.com/ionic/ionic-install.html\n\n\n安装 nodejs\nsudo apt-get install nodejs-legacy nodejs\nsudo apt-get install npm\n\n安装 jdk\n查看 jdk安装教程\n\n安装 sdk\n查看 sdk安装教程\n\n安装 gradle\n查看gradle安装教程\n\n\n切换源\nnpm set registry https://registry.npm.taobao.org\n再安装\nnpm install -g cordova ionic\n\n创建应用\nionic start myApp tabs\n\n创建Android应用\n$ cd myApp\n$ ionic cordova platform add android\n$ ionic cordova build android\n$ ionic cordova emulate android\n\n\n用ubuntu 安装出现问题\nwindows下安装可以 但创建应用模板是需要用到python2 想想怎么处理再进行安装\n\niOS真机测试教程','2018-11-13 06:17:31.861758','ionic 安装'),(36,'20181031 打车去买的车位 7万','2018-11-05 01:01:13.168006','周三买车位'),(37,'20181104 周日上午10：30 玉玉下周还要去看\n郭小丹重新整了牙，1个月不能吃东西','2018-11-05 01:04:24.541601','看牙齿'),(38,'周日买的飞机票\n20181116 周五 17：35-20：05飞机票 天津-温州 妈妈 470元','2018-11-14 02:13:09.681594','买飞机票'),(39,'autocomplete=\"off\"','2018-11-05 01:38:26.109457','input 无历史'),(40,'<input list=\"browsers\" autocomplete=\"off\" name=\"incubator\" style=\"width: 278px;height: 19px;border: 1px solid #cccccc;box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);    transition: border linear .2s, box-shadow linear .2s;padding: 4px 6px;margin-bottom: 9px;    font-size: 12px;border-radius: 4px;\">\n                        <datalist id=\"browsers\" style=\"width: 292px\">\n                        {% for incubator in incubators %}\n                        <option value=\"{{incubator.name}}\"></option>\n                        {%  endfor  %}\n                        </datalist>','2018-11-05 01:40:02.084250','datalist 下拉输入框'),(41,'pip install --download E:\\python27\\packages pandas\n\n环境管理器\n\n\n\n安装\n    pip3 install virtualenv\n创建文件夹\n创建环境\n    virtualenv --no-site-packages -p /usr/bin/python3 venv\n启动环境\n    f:\\env\\venv\\Scripts\\activate\n    linux  source venv/bin/activate\n关闭环境\n    f:\\env\\venv\\Scripts\\deactivate\n    linux deactivate\n    \npip install -r requirements.txt','2018-11-05 02:55:01.932333','virtualenv'),(42,'\n\n设置环境\nsource evn/evn/bin/activate\ncd evaluate\n\n查看端口\nnetstat -tlnp\n\n杀进程\nkill id号\n\n后台运行\nnohup python manage.py runserver 0.0.0.0:8802 &\n\n克隆数据\ngit clone ssh://dev.embway.com:7999/biev/server.git\n\n切换分支\ngit checkout release/BIEV-1\n\nmysql数据库\nmysql -uevaluateg -pevaluateg\n','2018-11-21 05:54:24.522284','部署'),(43,'find ~ -name 文件名','2018-11-05 03:11:49.491214','ubuntu命令'),(44,'user     = debian-sys-maint\npassword = 8UHyVyagB2YSjwPA\n\nmysql -udebian-sys-maint -p8UHyVyagB2YSjwPA','2018-11-05 03:21:54.555146','mysql服务器密码'),(45,'删除数据库\ndrop database evaluateg;','2018-11-05 03:22:25.650756','基本命令'),(46,'代码管理：https://dev.embway.com\n项目管理：https://dev.embway.com:18443\n文档管理：https://dev.embway.com:18444\n\nssh://git@dev.embway.com:7999/biev/server.git','2018-11-05 08:12:19.132160','代码管理'),(47,'创建并切换分支\n    git checkout -b dev\n    等同于下面两句\n        git branch dev\n        git checkout dev','2018-11-05 08:14:39.217401','git 分支'),(48,'https://dev.embway.com:18443 项目管理页面\n打开项目 ->创建问题 ->创建分支（到了代码页面）\n通过clone找到上传地址\n\n添加-f强行进行上传\ngit push -f evaluate release/BIEV-1','2018-11-05 08:39:56.696324','代码提交流程'),(49,'https://www.cnblogs.com/qypx520/p/6022787.html\n一.android开发\n1. 首先要安装node环境,Ionic的安装和后续的许多前端工具的安装都依赖于node的包管理器npm。\nnodeJs环境的安装很简单，去官网下载最新版的NodeJs直接安装即可。 Node官网： https://nodejs.org/\nnode环境变量在安装过程中会自动配置，安装完成后在cmd中输入 npm -v 回车。如果出现版本号说明安装成功。\nnode安装参考：http://jingyan.baidu.com/article/b0b63dbfca599a4a483070a5.html\n2. 安装jdk并且配置环境变量,如果已经安装了jdk则跳过这步。\njdk下载地址：http://www.oracle.com/technetwork/java/javase/downloads/index.html\n安装完成以后配置环境变量：\nJAVA_HOME:\nJDK的安装路径，这个环境变量本身不存在，需要创建，创建完则可以利用%JAVA_HOME%作为统一引用路径，其值为：jdk在你电脑上的安装路径。\nPATH：\nPATH属性已存在，可直接编辑。作用是用于配置路径，简化命令的输入，其值为：%JAVA_HOME%\\bin。  \nCLASSPATH：\n用于编译时JAVA类的路径，注意这里设置的是两个值，(.;)表示的是JVM先搜索当前目录。其值为：.;%JAVA_HOME%\\lib\\tools.jar。\n配置完毕后，通过cmd运行以下命令：java -version，javac 如果出现返回信息，则设置成功。\n3. 安装Android SDK. \n下载地址： http://developer.android.com/sdk/index.html 这个地址被墙了。需要FQ使用。\n这里可以只下载Android SDK 不需要一并下载 Android Studio。下载完成并安装然后向系统Path环境变量中添加两个值。分别是 Android SDK中tools目录的路径和platform-tools的路径。例如：\nC:\\Program Files (x86)\\Android\\android-sdk\\tools;\nC:\\Program Files (x86)\\Android\\android-sdk\\platform-tools;\n如果发现Android SDK安装目录中并没有 “ platform-tools”这个文件夹，应该运行tools目录下的android.bat文件，然后出现如下界面，勾选Android SDK Platform-tools 然后安装。\n\n环境变量配置完成以后在cmd中输入 android并且回车。如果出现android sdk manager则说明安装成功。\n4. 安装 Apache ant.\nant下载地址： http://ant.apache.org/bindownload.cgi\n环境变量：\nWindows下ANT用到的环境变量主要有2个： ANT_HOME 和 PATH。 \neg：\n1. 设置ANT_HOME指向ant的安装目录。 \n设置方法：ANT_HOME = D:\\apache_ant_1.7.0 \n2. 设置bin和lib目录到PATH变量中。将%ANT_HOME%\\bin; %ANT_HOME%\\lib添加到环境变量的path中。 \n设置方法：PATH = %ANT_HOME%\\bin; %ANT_HOME%\\lib \n%ANT_HOME%可以用真实的路径代替。\n安装完成以后在cmd中输入 ant -version 验证是否安装成功。\n5.安装ionic和cordova\nnpm install -g cordova ionic\n查看是否安装成功：ionic  –v   cordova  –v\n6. 通过Ionic创建一个项目\nionic start myApp blank 创建一个空白的app项目 \nionic start myApp tabs 创建一个带有tabs项目\nionic start myApp sidemenu 创建一个带有滑动的项目\n7. 给项目添加android平台\nionic  platform android\n8. 在模拟器中运行项目\nionic emulate android\n9. 启动浏览器服务\nionic serve\n10. 打包成app\nionic package','2018-11-05 09:22:45.682027','安装流程'),(50,'查看开发内容\n\n删除标签\n\n\n\nctrl+t 显示时间\n\n显示标签的历史记录\n\n可以直接在标签下方加入数据\n\n秘密入口 输入密码查看隐藏内容\n\n改完名字刷新一下左侧 显示信息\n可以直接呼出 sublime\ntable键 为4个空格\n\n\n附件的开发\n图片的显示\n\n高亮显示搜索\n通过不同颜色区别搜索的内容\n搜索进行优化？？\n\n搜索后通过树结构进行显示？\n\n最好时基于sublime 开发插件？\n\n\n\n设置状态栏 print的内容可以进行显示\n\n增加快捷键\n\n数据需要加密 图片 文本等\n\nknow的显示顺序\n\n完成\n\n  读取过慢的问题\n  数据结构需要优化 建立','2018-11-23 09:50:37.481845','改进'),(51,'        # set shortcut\n        save = QAction(QIcon(\'\'),  \'save\',  self)\n        save.setShortcut(\'Ctrl+S\')\n        save.setStatusTip(\'save application\')\n        save.triggered.connect(self.save_text)\n        menubar = self.menuBar()\n        file = menubar.addMenu(\'&File\')\n        file.addAction(save)','2018-11-06 03:26:29.019027','qt快捷键'),(52,'放弃修改\ngit checkout 文件\n\n清除本地修改\ngit reset --hard','2018-11-15 09:33:17.307529','放弃修改'),(53,'郭小丹\n西西和啊东\n','2018-11-06 08:21:26.459237','去宝坻看眼睛店'),(54,'\n天津津松伟业科技有限公司\n91120116MA06U3485M\n15022666265\n\n康之源（天津）科技发展有限公司\n91120116MA05JXJU10\n13920384338\n\n卡博瑞（天津）智能科技有限责任公司\n91120116351564414W\n18522877619\n\n天津卓越信通科技有限公司\n91120116MA05K4NU30\n13681032839\n\n道思科技（天津）有限公司\n91120116MA05NQL52J\n18674015110','2018-11-06 08:41:45.379440','资料'),(55,'http://www.cnblogs.com/huangxm/p/5770735.html','2018-11-07 02:25:50.903042','django 查看权限'),(56,'sublime插件\n    1 提取多行文字并生成逗号连接的字符串\n','2018-11-09 02:34:17.446209','添加sublime插件'),(57,'打开控制台 ctrl+\'`\' \n调用插件   view.run_command(\'first\')\n插件名称是通过大小写分段 并且_连接的\n\napi 接口\nhttp://www.sublimetext.com/docs/3/api_reference.html\n\n*Default (Windows).sublime-keymap  配置插件的快捷键\n*Default.sublime-commands 配置命名，可以再ctrl+shift+p打开的命令窗口使用\n*Main.sublime-menu 菜单配置，也就是给我们的插件一个菜单入口','2018-11-07 03:58:42.344997','sbulime插件教程'),(58,'        exeFile = \"C:\\\\Windows\\\\System32\\\\cmd.exe\"\n        exeFile = \'F:\\\\my\\\\P028_knowledge_system\\\\knowqt\\\\main.py\'\n        exePath = \"F:\\\\my\\\\P028_knowledge_system\\\\knowqt\\\\\"\n        os.chdir(exePath)\n        os.startfile(exeFile)','2018-11-07 04:28:28.048550','直接打开 程序'),(59,'django程序和普通程序分别用不同的快捷键\n用try traceback 拦截错误','2018-11-07 09:53:19.172492','sublime 直接运行程序'),(60,'上传\n设置setting\n    MEDIA_ROOT = \'company/static/\'\nmodels\n    business_license_pic = models.ImageField(upload_to=\'upload\',blank=True,null=True)\n输出路径\n    \'/static/\' + str(obj.business_license_pic)\n\n点击放大图片\n    \'<div style=\"height: 50px;overflow: hidden;\"><a href=\"/\' + path + \'\" width=30 height=50 data-lightbox=\"\' + path + \'\"><img src=\"/\' + path + \'\" width=30 height=50\" /></a></div>\'\n    lightbox包','2018-11-07 09:35:57.479591','django图片'),(61,'STATIC_URL = \'/static/\'\nSTATIC_ROOT = os.path.join(BASE_DIR, \"static\")\nSTATICFILES_DIRS = (\n    (\'css\', os.path.join(STATIC_ROOT, \'css\')),\n    (\'js\', os.path.join(STATIC_ROOT, \'js\')),\n    (\'amaze\', os.path.join(STATIC_ROOT, \'amaze\')),\n    (\'imgs\', os.path.join(STATIC_ROOT, \'imgs\')),\n    (\'jquery-weui\', os.path.join(STATIC_ROOT, \'jquery-weui\')),\n    (\'upload\', os.path.join(STATIC_ROOT, \'upload\')),\n    (\'lightbox\', os.path.join(STATIC_ROOT, \'lightbox\')),\n    (\'download_image\', os.path.join(STATIC_ROOT, \'download_image\')),\n)','2018-11-07 09:40:46.187959','静态路径'),(62,'lightbox.zip','2018-11-07 09:43:40.429767','lightbox'),(63,'手机app\n玉玉的平板管理\n自己番茄','2018-11-07 09:49:07.300660','手机app'),(64,'研究一下 公安局的程序\nvote_src.tar.gz','2018-11-07 09:50:53.502326','研究一下 公安局的程序'),(65,'用django 做网页端\n实现 惩罚系统\n实现多平台 适用','2018-11-22 09:51:07.732871','玉玉的平板管理 1'),(66,'sublime 参考多重快捷键\n\n[\"ctrl+q\",\"ctrl+0\"] 以这种方式设置多重快捷键\n\n通过对sublime文件夹 搜索ctrl+q 查看默认快捷键','2018-11-22 03:27:26.044012','参考多重快捷键'),(67,'20181108 09:31:38\n马桶昨天修好了\n用衣架 勾出了梳子','2018-11-08 01:32:18.970032','马桶'),(68,'F:\\study\\video','2018-11-22 09:51:18.985729','达内机器学习 2'),(69,'from django.contrib import messages\nmessages.add_message(request, messages.INFO, \'Hello world.\')\n\n有几个快捷方法提供标准的方式来新增消息并带有常见的标签（这些标签通常表示消息的HTML 类型）\n\nmessages.debug(request, \'%s SQL statements were executed.\' % count)\nmessages.info(request, \'Three credits remain in your account.\')\nmessages.success(request, \'Profile details updated.\')\nmessages.warning(request, \'Your account expires in three days.\')\nmessages.error(request, \'Document deleted.\')','2018-11-08 03:21:57.149154','message'),(70,'保存sublime插件\nF:\\sublime\\SublimeText_XP85\\Data\\Packages\n\n需要开发一个类似坚果云的系统 时时同步','2018-11-22 03:32:30.549183','保存sublime插件'),(71,'发行盈亏比','2018-11-09 01:40:39.419666','投资'),(72,'1. 登录Linux，切换到root用户 sudo root 获取root用户权限，当前工作目录不变(需要root密码)或 sudo -i 不需要root密码直接切换成root（需要当前用户密码） 2. 在usr目录下建立java安装目录cd /usr 之后mkdir java 3.将jdk-8u141-linux-x64.tar.gz拷贝到java目录下 cp jdk-8u141-linux-x64.tar.gz（其所在路径） /usr/java/ 4.解压jdk到当前目录 tar -zxvf jdk-8u141-linux-x64.tar.gz得到文件夹 jdk1.8.xx 5.安装完毕为他建立一个链接以节省目录长度(可以省略这一步) ln -s /usr/java/jdk1.8.xx/ /usr/jdk 6.编辑配置文件，配置环境变量 vim /etc/profile 添加如下内容：JAVA_HOME根据实际目录来 JAVA_HOME=/usr/java/jdk1.8.xx CLASSPATH=$JAVA_HOME/lib/ PATH=$PATH:$JAVA_HOME/bin export PATH JAVA_HOME CLASSPATH 7.重启机器或执行命令 ：source /etc/profile sudo shutdown -r now 8.查看安装情况 java -version java version \"1.8.xx\" Java(TM) SE Runtime Environment (build 1.8.xx) Java HotSpot(TM) Client VM (build 25.60-b23, mixed mode) 可能出现的错误信息： bash: ./java: cannot execute binary file 出现这个错误的原因可能是在32位的操作系统上安装了64位的jdk， 查看jdk版本和Linux版本位数是否一致。 查看linux是32位还是64位系统： sudo uname --m i686 //表示是32位 x86_64 // 表示是64位','2018-11-09 08:29:57.102120','安装jdk'),(73,'http://www.cnblogs.com/ranxf/p/9112614.html\nvim /etc/profile\n\nexport ANDROID_SDK_HOME=/home/ranxf/Android/Sdk/android-sdk-linux\nexport PATH=$PATH:${ANDROID_SDK_HOME}/tools\nexport PATH=$PATH:${ANDROID_SDK_HOME}/platform-tools\n\n运行 /home/ranxf/Android/Sdk/android-sdk-linux/tools/android 下载所需要的sdk\n\n\n\n有问题再运行下面的\nsource /etc/profile\n在命令行输入：vim /root/.bashrc,并在文件末尾加入一行source etc/profile命令，保存。这样就大功告成了。','2018-11-09 09:41:12.215368','android sdk'),(74,'http://www.androiddevtools.cn/ ','2018-11-09 09:00:08.920334','android工具'),(75,'print 可以显示 行数 位置\n已经完成\nF00_pythonself.pstools.printnew','2018-11-21 09:18:16.335521','增加print功能'),(76,'\nexport GRADLE_HOME=/usr/gradle/gradle-4.10.2\nexport PATH=$GRADLE_HOME/bin:$PATH','2018-11-13 06:15:36.204212','安装 gradle'),(77,'django-admin startproject miss\npython manage.py startapp news ','2018-11-13 06:52:39.555056','运行命令'),(78,'import pymysql\npymysql.install_as_MySQLdb()\n\n\n\n\nALLOWED_HOSTS = [\'*\']\nDATABASES = {\n    \'default\': {\n        \'ENGINE\': \'django.db.backends.mysql\',\n        \'NAME\': \'evaluateg\',\n        \'USER\': \'evaluateg\',\n        \'PASSWORD\': \'evaluateg\',\n        \'HOST\': \'localhost\',\n        \'PORT\': \'3306\'\n    }\n}\n\nLANGUAGE_CODE = \'zh-Hans\'\n\nTIME_ZONE = \'Asia/Shanghai\'\n\nSTATIC_URL = \'/static/\'\nSTATIC_ROOT = os.path.join(BASE_DIR, \'static\')\nMEDIA_ROOT = \'company/static/\'','2018-11-13 07:18:42.901428','setting设置'),(79,'link rel=\"stylesheet\" type=\"text/css\" href=\"{% static \'css/balance.css\' %}\" media=\"all\"/','2018-11-13 07:31:08.046131','css链接'),(80,'script type=\"text/javascript\" src=\"{% static \'js/balance.js\' %}\"></script','2018-11-13 07:31:00.295230','js链接'),(81,'$(\"[name=\'csrfmiddlewaretoken\']\").val()','2018-11-13 09:47:11.994072','获取csrf'),(82,'`${xx}`','2018-11-13 09:49:07.756616','获取模板参数'),(83,'20181112 请假\n带玉玉去医院\n拍了胸片\n做了心电图\n没有问题\n\n前一天晚上难受\n早晨有些难受\n下午好了','2018-11-14 02:07:11.747094','玉玉'),(84,'20181111 周日 看牙 10：00 原定9点 以为是10点','2018-11-14 02:10:36.149523','玉玉看牙'),(85,'https://www.cnblogs.com/sexintercourse/p/5898242.html\n\n安卓\n<a href=\"deskclock://deskclock.android.com/main\">启动应用程序</a> \n下载\napplications info 查看信息\n\n<meta name=\"apple-itunes-app\" content=\"app-id=1049758801\">\n\n\nios的方法\nhttps://www.cnblogs.com/h--d/p/5846675.html','2018-11-15 12:22:12.322400','html跳转应用'),(86,'\n\n&&\nand\n(x < 10 && y > 1) 为 true\n||\nor\n(x==5 || y==5) 为 false\n!\nnot\n!(x==y) 为 true\n\n\n==\n等于\nx==8 为 false\n===\n全等（值和类型）\nx===5 为 true；x===\"5\" 为 false\n!=\n不等于\nx!=8 为 true\n>\n大于\nx>8 为 false\n<\n小于\nx<8 为 true\n>=\n大于或等于\nx>=8 为 false\n<=\n小于或等于\nx<=8 为 true\n','2018-11-14 09:08:31.433882','js 运算符'),(87,'新建的item 没有 typelc\n通过 关闭了新建按钮 实现\n','2018-11-21 15:48:58.446201','完成 know bug'),(88,'获取相差的秒数 但要大减小 00：00的时候是不是有问题\n(d2-d1).seconds\n\n获取时间戳\ntime.mktime(d1.timetuple())','2018-11-14 09:26:56.143997','datetime'),(89,'Math.floor 地板除\nMath.round 四舍五入','2018-11-14 09:51:21.467716','js math'),(90,'\n重定向\nfrom django.shortcuts import render,redirect\nredirect (\'/admin\')\n\nfrom django.http import HttpResponseRedirect\nreturn HttpResponseRedirect(\'/admin/company/serverrequest/%s\'%_id)\n\n渲染\nreturn render(request,\'profit.html\',{\'data\':data,\'status\':status,\'year\':year,\'years\':years})','2018-11-14 11:20:50.233400','模板渲染'),(91,'https://github.com/missing64001/managec.git\n\ngit@github.com:missing64001/managec.git','2018-11-15 02:03:34.199518','git地址'),(92,'git remote remove <name>','2018-11-14 11:39:19.639400','删除 remote'),(93,'\n\ngit config --global user.name \"missing\"\ngit config --global user.email \"327770692@qq.com\"\n\nssh-keygen -t rsa -C \"327770692@qq.com\"','2018-11-14 11:47:37.152400','git 初始化'),(94,'sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak\nsudo vim /etc/apt/sources.list\n\n将原来的列表删除，添加如下内容（中科大镜像源）\n\n\ndeb http://mirrors.ustc.edu.cn/ubuntu/ xenial main restricted universe multiverse\ndeb http://mirrors.ustc.edu.cn/ubuntu/ xenial-security main restricted universe multiverse\ndeb http://mirrors.ustc.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse\ndeb http://mirrors.ustc.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse\ndeb http://mirrors.ustc.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse\ndeb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial main restricted universe multiverse\ndeb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-security main restricted universe multiverse\ndeb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse\ndeb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse\ndeb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse\n\nsudo apt-get update\nsudo cp /etc/apt/sources.list /etc/apt/sources.list.bak1\nsudo mv /etc/apt/sources.list.bak /etc/apt/sources.list','2018-11-14 12:18:32.679400','切换源'),(95,'因为大小写的原因不能显示\nwindow忽略大小写\n而ubuntu 有问题','2018-11-15 01:56:52.520568','不显示change_form'),(96,'\n加八个小时\ndate_add(create_time, interval 8 hour)\ndate_sub 减去','2018-11-15 07:50:35.037110','按照天分组'),(97,'拼接字符串\nCONCAT(year,\'-\',month,\'-\',day)','2018-11-15 08:33:11.839063','mysql命令'),(98,'\n后端\njson.dumps(da1)\n\n前端\nvar date = \"{{date}}\";\ndate = date.replace(/\\&quot;/g, \'\\\"\');\ndate = JSON.parse(date);','2018-11-15 09:18:06.182190','django穿json数据'),(99,'from django.db import connection, transaction    \ncursor = connection.cursor()\n    playsql = \'\'\'select date ,sum(sec) as totle from \n    (select sec,CONCAT(year,\'-\',LPAD(month, 2, 0),\'-\',LPAD(day, 2, 0)) as date from(SELECT (Extract(year from date_add(create_time, interval 8 hour) )) AS `year`, \n        (Extract(month from date_add(create_time, interval 8 hour) )) AS `month`, \n        (UNIX_TIMESTAMP(finished_time) - UNIX_TIMESTAMP(create_time)) AS `sec`,\n        (Extract(day from date_add(create_time, interval 8 hour) )) AS `day` FROM `yuyu_play`) as t1) as t2\n        group by date order by date\n        ;\'\'\'\n    \n    cursor.execute(playsql)\n    rows = cursor.fetchall()','2018-11-15 09:19:31.755121','django 原生sql'),(100,'UNIX_TIMESTAMP(finished_time) - UNIX_TIMESTAMP(create_time)','2018-11-15 09:20:32.756347','时间相减'),(101,'\n打印 时间 及 行\n\n\n\n\n当models objects 用切片取值时会一个一个取  而for或list会同时取出来并且带有所有属性\nsys\n自省\nsys._getframe().f_locals 等同于 locals() 是一个字典 修改f_locals不影响本地变量但是会影响locals() \nsys._getframe().f_back.f_locals 返回 函数返回之后的的变量\nsys._getframe().f_lasti 上一条指令？没有找出相关性\nsys._getframe().f_lineno 本条指令行数\nsys._getframe().f_trace 错误? 一直返回None\nsys._getframe().f_code 获取代码\nf_lineno记录本条指令函数 如果引入了sys._getframe()的上一层变量 则显示调用这个函数的位置 类似用了.f_back 因此直接传参没有意义\n\ninspect\n查看全部代码 inspect.getsource(模块.函数）或者（模块.类.函数）\n\n查看函数参数 inspect.getargspec(...)   查看类的参数，则括号里为（模块.类.__init__）\n\n查看函数的位置 inspect.getabsfile(...) \n\n\n\ninspect.signature（fn)将返回一个inspect.Signature类型的对象，值为fn这个函数的所有参数\n\n\ninspect.Signature对象的paramerters属性是一个mappingproxy（映射）类型的对象，值为一个有序字典（Orderdict)。\ninspect.Parameter对象的kind属性是一个_ParameterKind枚举类型的对象，值为这个参数的类型（可变参数，关键词参数，etc）\n\n\ninspect.Parameter对象的default属性：如果这个参数有默认值，即返回这个默认值，如果没有，返回一个inspect._empty类。\n\ngetmembers(object[, predicate])\n\n返回一个包含对象的所有成员的(name, value)列表。返回的内容比对象的__dict__包含的内容多，源码是通过dir()实现的。\n\npredicate是一个可选的函数参数，被此函数判断为True的成员才被返回。\n\ngetmodule(object) 返回定义对象的模块','2018-11-17 01:38:23.997074','待办理'),(102,'翻墙\n搬瓦工 vps安装\n优惠码\n谷歌浏览器 翻墙插件 过滤器','2018-11-19 02:32:57.726143','搭建vpn'),(103,'生成 元素为0 并且shape为orig的 数组\nnp.zeros_like(orig)\n\n可以直接复制覆盖 覆盖了最后一个元素的一个元素\norig = [(1,2,3,(1,2,3)]\nblue[...,0] = orig[...,0]','2018-11-19 02:46:45.931570','创建np'),(104,'\nimport numpy as np 需要先加载numpy 再 \nimport cv2 as cv\n\n读取数据 \norg = cv.imread(\'xxx.jpg\')\n\n显示数据\ncv.imshow(\'窗口名称\',original) \n可以显示多个窗口\n\n阻塞显示 \ncv.waithkey()\n\n数据的格式\noriginal.shape ->（高,宽,通道(蓝色,绿色,红色)）\n\n通过切片进行裁剪\n\n拉伸图片\ncv.resize(orig,(w*2,int(h/2)),interpolation=cv.INTER_LINEAR 插值方式)\ncv.resize(orig,None,fx=2,fy=0.5,interpolation=cv.INTER_LINEAR) 按倍数缩放\n\n保存图片\ncv.imwrite(\'.jpg\')\n\n把彩色变黑白\ngray = cv.cvtColor(orig,cv.COLOR_BGR2GRAY) 把彩色变黑白','2018-11-20 08:52:36.294406','opencv 机器视觉工具包'),(105,'以左上点为0点','2018-11-19 02:59:11.993815','opencv坐标系'),(106,'二维卷积 高斯模糊 锐化 边缘检测 微分卷积\n每种检测会有多种检测方法\n边缘 焦点 特征值 一般用灰度值处理 如果颜色不重要\n\n边缘检测 edge.py\n    cv.Canny(orig,50,240) (图片,水平阈值,垂直阈值) 返回一个图片\n\n均衡直方 eq.py\n    提高亮度 对比度不变\n\n    黑白图\n      eq_gray = cv.equalizeHist(gray) 提高亮度\n      一般是亮度提升后 在做边缘化处理\n\n    彩色图\n      yuv = cv.cvtColor(orgi,cv.COLOR_BGR2YUV) 把彩色变YUV 亮度 色度 饱和度\n      yuv[...,0] = cv.equalizeHist(yuv[...,0]) 把yuv做均衡直方\n      eq_color = cv.cvtColor(yuv,cv.COLOR_YUV2BGR) 再转换成bgr\n\n角点检测 corner.py\n    速度快 失真度低 用于规则图形\n    corners = cv.cornerHarris(gray,7,5,0.04) 图片 水平阈值 垂直阈值 迭代精度\n    corners = cv.dilate(corners,None 锐化等级)  锐化\n    mixtrue = orig.copy()\n    mixture[corners > corners.max() * 0.01] = [0,0,255]\n\n特征检测 \n\n  star特征检测 star.py \n    star = cv.xfeatures2d.StarDetector_create() 特征检测对象\n    keypoints = star.detect(gray) 获得关键点\n    cv.drwaKeypoint(orig,keypoints,mixture,flags=cv.DRAW_MATCHES_FLAGS_DRWA_RICH_KEYPOINTS) 前像个相加 得到第三个 画最多的关键点\n\n  sift特征检测 sift.py\n    sift = cv.xfeatures2d.SIFT_create()\n    点的获取和上方一样\n\n\n  一般先用star做第一遍，再用sift做筛选\n  特征（描述）矩阵 desc.py\n    sift = cv.xfeatures2d.SIFT_create()\n    keypoints,desc = sift.compute(gray,keypoints) 结合star的关键点\n    desc 特征（描述）矩阵\n\n\n\n\n\n\n\n\n\n','2018-11-20 09:00:03.538783','opencv 功能'),(107,'html ctrl+shift+a 选择标签内的东西','2018-11-20 00:58:06.038813','sublime快捷键'),(108,'    jQuery事件处理 加载后执行 DOM树加载完毕就执行了比window.onload前执行 \n            $(document).ready(function(){});//页面初始化操作\n            $().ready(function(){});//页面初始化操作 第二种写法\n            $(function(){}); 第三种写法\n\n\nwindow.onload 多个js只执行一个\njquery的则执行多个 按照循序执行','2018-11-20 02:29:49.506625','html 加载后执行'),(109,'20181121 需要设置导出信息按钮\n\n\n\n\n\n\n\n\n\n\n\n--完成--\n导航栏设置\n\n公司\n  基础信息 锁定后 有保存按钮\n  财务信息 的删除按钮处理\n           锁定后 列表有 保存和删除按钮\n  自主评价\n    锁定后 列表有 保存和删除按钮\n    列表取消保存按钮\n  反馈信息\n    列表 删除按钮\n    内容 保存按钮\n\n\n孵化器\n  企业基本信息\n    列表 不应有删除权限 和按钮\n\n平台\n  企业数据统计 删除和添加按钮 关闭权限 可否？\n  校正评分 列表 删除和添加按钮\n           内容 保存按钮 和 显示用户分数\n\n机构\n   金融报告 投资类？是否也有银行类金融报告？\n          列表的 增加和删除 \n   反馈信息 列表的 删除和添加按钮\n\n\n导航栏修改\n\n列表的删除和增加按钮\n\n删除和增加权限\n  都没有删除权限\n\n内容的保存按钮\n\n服务器上没有makegrtions\n','2018-11-22 09:52:40.194710','20181120 问题记录'),(110,'20181120 15:04:34 周二 \n\n刚回来\n\n去一中心 ','2018-11-20 07:07:35.611302','开会'),(111,'需要导出 excel数据\n需要部署服务器','2018-11-20 07:09:36.110788','20181120 开会问题'),(112,'https://www.processon.com/','2018-11-20 08:47:53.295361','制图在线软件'),(113,'import matplotlib.pyplot as mp\n\n矩阵可视化\n    mp.matshow(desc, cmap=\'jet\', fignum=\'Description\')矩阵 颜色映射 名称','2018-11-20 09:02:10.342190','绘图方式'),(114,'mp.title(\'Description\', fontsize=20) 题目\nmp.xlabel(\'Feature\', fontsize=14) x轴\nmp.ylabel(\'Sample\', fontsize=14)\nmp.tick_params(which=\'both\', top=False, labeltop=False,\n               labelbottom=True, labelsize=10) 刻度\nmp.show()','2018-11-20 09:02:53.783642','参数'),(115,'ssh://git@dev.embway.com:7999/biev/server.git','2018-11-20 09:19:17.411276','git地址'),(116,'settings.py\nTEMPLATES -> OPTIONS -> context_processors\n加入 \'index.my_context_processors.globar_var\',\n\ndef globar_var(request):\n    return {\n      \'global_group\': get_user_group(request),\n      \'global_url\': global_url,\n    }','2018-11-21 03:08:21.079448','模板全局参数'),(117,'\n\n根据 admin首页 设置权限\n优化 admin首页显示的链接\n\n只读文档的保存按钮\n\n单独item\n输入错误信息 360 乱码','2018-11-22 01:11:57.813459','20181121'),(118,'obj.labels.add(label)','2018-11-21 08:50:24.927534','多对多添加'),(119,'file = os.path.normpath(file)','2018-11-21 06:02:55.104526','正规化文件名'),(120,'for curdir,subdirs,files in os.walk(directory):\n    pass','2018-11-21 06:04:00.053709','遍历文件夹'),(121,'obj.py\n最好把图片按照一个方向进行缩放 按照较小的边长设置为200\n    f = 200 / min(h.w)\n    gray = cv.resize(gray,None,fx=f,fy=f)\n\n获得desc矩阵\n    加入descs descs = np.append(descs,desc,axis=0)\n    tran_x.append(descs) 输入\n    tran_y.append(label) 输出\n\n基于高斯分布的隐马尔科夫模型\n    model = hl.GaussianHMM(n_components=4（四个隐藏状态）,covariance_type=\'diag\'（相关性的矩阵的辅对角线表示协方差）,n_iter=1000（迭代次数）)\n     models[label] = model.fit(descs) 训练\n\n    model.score(descs) 测试分值','2018-11-21 06:44:47.101751','图像识别'),(122,'new','2018-11-21 07:32:57.246418','new'),(123,'new','2018-11-21 08:32:27.461100','new 新的'),(124,'new','2018-11-21 08:40:11.673260','new 新的'),(125,'new','2018-11-21 08:46:05.295797','new'),(126,'\n20181123 11:12:13\n  上午\n    显示顺序 完成第一步\n    evaluate 修改bug\n    ml\n\n  下午\n    360乱码 完成\n    顺序 优化了开发过程\n    导出数据\n    微信\n    导出数据\n    ml\n\n  总结\n    上午还算不错\n    中午没有休息 过了屌炸天\n    下午开会了 很多任务没有完成\n    慢慢来吧 东西太多了 一点一点 不要着急\n\n20181122 \n  上午\n    09:16:08 布置了工作内容\n    ml\n    工作 导航栏\n\n  下午\n    有个面试的\n    显示学历优化 admin失败 需要用js\n    显示顺序 还需要5，6个番茄\n    微信\n    显示学历优化 完成\n    know排序 有bug 明天debug\n    机器学习 明天要先总结\n   \n  总结\n    今天效果还真的不错，基本都完成了\n\n20181121 17:26:30\n从明天开始','2018-11-23 09:45:17.804873','11月记录'),(127,'实数 = 有理数 + 无理数\n有理数 = p/q 或有限小数 或无限循环小数\n无理数 无限不循环小数\n\n把有限小数 整数表示为无限小数\n\n定义1\n    比大小 > = < 通过一位一位比\n\n定义2\n    不足近似 删掉n后面的位数\n    过剩近似 不足近似+1/10^n\n\n命题 x>y 等价条件是 存在非负整数 x的不足近似 大于 y的过剩近似\n\n例1 x<y 存在 x<r<y\n\nR = {x}x为实数}\n实数主要性质\n  R的加减乘除(非0除)是封闭的,结果仍为实数\n  实数是有序的 ab实数比满足 a<b a=b a>b\n  大小具有传递性\n  具有阿基米德性 若b>a>0 则存在正整数n na>b\n  具有稠密性 任何两个不相等的实数之间必有一个实数,也有无理数\n  任何一个叔叔对应数轴上唯一的点 一一对应\n\n例2 e>0 a<b+e 则 a<=b 反正法 a>b\n   个人理解 a<b 如果a=b 则e=0 \n','2018-11-22 15:34:27.957000','1 实数及其性质'),(128,'15/352\n实数绝对值定义 |a| = a,a>=0 或 -a, a<0\n数轴 数a的绝对值就是点a到原点的距离\n\n性质\n|a| = |-a| >= 0\n-|a| <= a <= |a|\n|a| < h -> -h < a < h; \n三角形不等式 |a| - |b| <= |a +- b| <= |a|+|b|\n|ab| = |a||b|\n\n16页','2018-11-22 15:34:32.499000','2 绝对值与不等式'),(129,'输入错误信息 360 乱码\n\nencodeURIComponent 利用这个转码','2018-11-23 06:21:21.186914','输入错误信息 360 乱码'),(130,'导航栏设置','2018-11-22 01:13:47.759076','导航栏设置'),(131,'实现 惩罚系统','2018-11-22 09:51:15.043785','实现 惩罚系统 1'),(132,'微信','2018-11-22 09:51:21.029704','微信 1'),(133,'显示label 和 content的顺序\n先写label的显示顺序吧\n    拖拽\n    插入 会影响顺序\n    读取的时候要排序 --> 曲线一下 读取后进行排序\n\n    h_sort 有些问题 查看一下 \n    20181123 11:14:48 h_sort 问题解决 实现了labeltree 上面的排序工作\n\n\n    ','2018-11-23 03:16:07.987780','显示顺序 1'),(134,'redis\ndocker\nfastDFs\nNginx\n','2018-11-22 01:47:24.928779','编程 需要学习的内容'),(135,'通过对sublime文件夹 搜索ctrl+q 查看默认快捷键','2018-11-22 03:29:26.005502','学习sublime'),(136,'遍历文件 -> 文件夹\n修改 删除 添加 改名 改位置 \nmodel \n  主文件夹名\n  pc名 文件名\n  保存的数量（一共n，按照每天一个或者自己控制 但是保留保存后的哈希）\n  大小（和大小差距20%的数据进行对比）\n  文件夹名 \n  哈希\n  文件指向id\n\n小文件（1m以下） 少文件保存 多文件进行询问，且进行记录\n大文件 多文件 百度网盘？\n快速搜索改变 everything？\n\n\n','2018-11-23 06:06:35.143051','方案'),(137,'只读文档的保存按钮','2018-11-22 09:51:35.690519','只读文档的保存按钮 1'),(138,'数据导出','2018-11-22 09:51:42.810431','数据导出 3'),(139,'没有填写的不进行显示\n需要拿js做','2018-11-22 06:05:19.561007','显示学历优化'),(140,' ','2018-11-22 04:19:07.307590','保存图片'),(141,'<sublime>\n1|F:\\sublime\\SublimeText_XP85\\Data\\Packages\\mypack\n2|F:\\sublime\\SublimeText_XP85\\Data\\Packages\\mypack\n<sublimeend>\n\n<python>\n1|F:\\sublime\\SublimeText_XP85\\Data\\Packages\\mypack\n2|F:\\sublime\\SublimeText_XP85\\Data\\Packages\\mypack\n<pythonend>\n\n\n\n把 try_command 拉下来\n\n可以拿这个当作python测试\n\n\n快速 打开 sublime 和 python\n列一个清单\n\n保存到 这个里面？\n\n先保存到 sublime 插件里面吧\n\n还是保存到这里吧\n\n需要判断机器','2018-11-23 09:19:05.341466','know快捷键'),(142,'是不是可以通过判断 机器来处理呢？','2018-11-23 03:57:18.845435','写一个过滤文件，可以设置内容'),(143,'copymyenv','2018-11-23 04:02:33.142485','copymyenv 方案'),(144,'只是显示\n先要有方案','2018-11-23 04:04:05.416323','标签的公用'),(145,'        import traceback\n        filename = \'myexec.py\'\n        with open(filename,\'r\',encoding=\'utf-8\') as f:\n            data = f.read()\n        try:\n            exec(data)\n        except Exception:\n            traceback.print_exc()\n\n\n修改 F:\\sublime\\SublimeText_XP85\\Data\\Packages\\mypack\\myfirst.py first的打开','2018-11-23 07:07:03.241442','优化程序测试过程'),(146,'下午开会\n需要记录一下','2018-11-23 09:08:54.406147','git开发流程'),(147,'tmux kill-session -t 0','2018-11-23 09:31:47.927964','教程'),(148,' ','2018-11-23 09:33:23.251767','教程'),(149,'和玉玉一起读书','2018-11-23 09:46:06.630251','昨日-读书'),(150,'六日进行锻炼吧 如果平时有时间也可以锻炼\n深呼吸','2018-11-23 09:37:30.847653','冥想'),(151,'修改label 也要在tree中移动或删除位置','2018-11-23 09:42:26.161023','修改label'),(152,'根据 admin首页 设置权限\n优化 admin首页显示的链接','2018-11-23 09:44:32.110438','修改权限'),(153,'修改颜色\n修改颜色可以修改字体颜色','2018-11-23 09:48:59.396079','设置保存修改 treeitem颜色'),(154,'可以修改 背景颜色 和标签重叠了？ 标签修改字体颜色？','2018-11-23 09:49:54.873384','重要程度'),(155,'new  ','2018-11-24 08:50:37.250919','new');
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
) ENGINE=InnoDB AUTO_INCREMENT=291 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_content_labels`
--

LOCK TABLES `data_content_labels` WRITE;
/*!40000 ALTER TABLE `data_content_labels` DISABLE KEYS */;
INSERT INTO `data_content_labels` VALUES (5,1,5),(6,1,6),(9,1,8),(7,2,4),(8,2,7),(10,2,8),(11,3,10),(12,4,12),(71,5,9),(44,5,31),(70,5,52),(14,6,17),(69,7,17),(46,7,31),(22,8,19),(30,9,20),(18,10,17),(21,11,21),(24,12,11),(23,12,24),(25,13,18),(28,14,18),(31,15,19),(32,16,19),(33,17,25),(35,18,7),(34,18,18),(36,19,26),(37,20,27),(38,21,28),(40,21,29),(41,22,26),(43,23,30),(172,24,96),(45,25,33),(49,26,9),(48,27,18),(50,28,7),(51,29,35),(52,30,36),(137,31,58),(53,32,37),(54,33,38),(55,34,40),(56,35,42),(57,36,44),(125,37,87),(59,38,47),(60,39,49),(61,40,50),(62,41,51),(64,42,52),(65,43,56),(67,44,14),(66,44,20),(68,45,17),(72,46,57),(79,46,62),(73,47,58),(74,48,38),(75,49,42),(76,50,60),(86,50,67),(77,51,61),(80,52,58),(81,53,63),(82,54,64),(83,55,9),(84,55,65),(85,56,67),(214,56,114),(87,57,69),(88,58,69),(99,59,74),(90,60,70),(91,61,71),(92,62,72),(97,63,65),(96,64,65),(95,64,73),(271,65,67),(200,65,91),(211,66,68),(216,66,74),(101,67,75),(103,68,40),(104,68,65),(102,68,77),(282,68,124),(105,69,9),(222,70,74),(218,70,115),(107,71,78),(108,71,79),(110,72,42),(111,73,42),(112,74,40),(113,74,81),(182,75,74),(115,76,42),(116,77,82),(117,78,83),(118,79,84),(119,80,85),(121,81,9),(120,81,34),(122,82,34),(123,83,86),(127,83,88),(126,84,87),(128,85,48),(129,86,34),(177,87,74),(193,87,113),(132,88,89),(133,89,90),(134,90,9),(135,91,91),(136,92,58),(138,93,58),(139,94,11),(140,94,54),(141,96,9),(142,96,16),(143,97,17),(146,98,7),(144,98,9),(145,98,92),(148,99,9),(147,99,16),(149,100,16),(276,101,124),(151,102,93),(152,103,95),(153,104,96),(154,105,96),(155,106,96),(156,107,69),(158,108,34),(157,108,48),(176,109,67),(241,109,74),(242,109,116),(161,110,98),(162,112,99),(163,113,100),(164,114,100),(165,115,14),(166,115,58),(168,116,18),(283,117,74),(169,117,97),(174,118,10),(170,119,33),(171,120,33),(173,124,96),(289,126,101),(186,126,104),(189,127,109),(247,128,74),(191,128,109),(255,129,74),(196,129,97),(209,130,74),(198,130,97),(202,131,91),(256,131,101),(273,132,124),(206,133,60),(274,133,124),(207,134,40),(215,135,65),(213,135,69),(254,136,74),(219,136,115),(224,137,97),(278,137,124),(226,138,97),(281,138,124),(237,139,74),(229,139,97),(231,140,60),(232,140,67),(286,141,60),(245,141,101),(249,142,67),(248,142,117),(251,143,67),(250,143,118),(252,144,60),(253,144,67),(257,145,119),(258,146,98),(275,146,124),(263,147,101),(262,147,120),(264,148,121),(277,148,124),(267,149,101),(268,149,125),(270,150,101),(269,150,125),(279,151,60),(280,151,101),(284,152,97),(285,152,124),(287,153,60),(288,154,60),(290,155,60);
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
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_label`
--

LOCK TABLES `data_label` WRITE;
/*!40000 ALTER TABLE `data_label` DISABLE KEYS */;
INSERT INTO `data_label` VALUES (1,'333',-1,'',10,'2018-11-16 02:52:13.224844'),(2,'qt',59,'3,5,6,61,99|',10,'2018-11-22 09:13:32.933096'),(3,'qtreewidget',2,'',10,'2018-10-29 15:41:49.334000'),(4,'qtreewidgetitem',3,'',10,'2018-10-29 15:41:36.143000'),(5,'模态',2,'',10,'2018-10-29 15:45:05.101000'),(6,'qdialog',2,'',10,'2018-10-29 15:45:18.768000'),(7,'坑',59,'',10,'2018-11-05 08:57:19.627213'),(8,'pyqt5',11,'',10,'2018-10-29 16:05:43.512000'),(9,'django',11,'',10,'2018-10-29 16:05:43.713000'),(10,'model',9,'',10,'2018-10-29 16:02:37.382000'),(11,'python',59,'',10,'2018-11-05 08:56:59.041471'),(12,'服务器',59,'',10,'2018-11-05 08:57:15.865259'),(13,'工作',59,'',10,'2018-11-05 08:57:12.753297'),(14,'evaluate',38,'',10,'2018-11-01 09:15:13.671604'),(15,'路径',14,'',10,'2018-10-30 01:10:06.517219'),(16,'mysql',59,'17,20,99|',10,'2018-11-23 02:44:50.596379'),(17,'command',16,'',10,'2018-10-30 01:12:58.895054'),(18,'admin',9,'',10,'2018-10-30 01:22:22.664579'),(19,'属性',18,'',10,'2018-10-30 01:22:32.621453'),(20,'密码',16,'',10,'2018-10-30 01:31:24.788763'),(21,'外键',18,'',10,'2018-10-30 02:22:40.038104'),(22,'myapp',59,'115,91,79,23,118|',10,'2018-11-23 03:59:48.572552'),(23,'know',22,'',10,'2018-10-30 02:30:25.302253'),(24,'version',23,'',10,'2018-10-30 02:30:37.365101'),(25,'内联',18,'',10,'2018-10-30 06:29:36.029873'),(26,'suit',9,'',10,'2018-10-30 09:17:53.647931'),(27,'command',12,'',10,'2018-10-31 01:00:53.009557'),(28,'程序',12,'',10,'2018-10-31 01:04:25.170890'),(29,'120.79.41.9',12,'',10,'2018-10-31 01:05:21.448181'),(30,'网站',14,'',10,'2018-10-31 01:53:26.421996'),(31,'command',14,'',10,'2018-10-31 01:54:21.023311'),(32,'os',11,'',10,'2018-10-31 09:44:10.093869'),(33,'文件操作',32,'',10,'2018-10-31 09:44:18.094767'),(34,'js',59,'',10,'2018-11-05 08:57:13.889285'),(35,'类型转换',34,'',10,'2018-11-01 06:31:13.453319'),(36,'对话框',34,'',10,'2018-11-01 07:44:02.036394'),(37,'bootstrap',34,'',10,'2018-11-01 08:58:03.581555'),(38,'安博伟业',13,'',10,'2018-11-01 09:15:10.125649'),(39,'密码',38,'',10,'2018-11-01 09:15:32.357370'),(40,'教程',59,'',10,'2018-11-05 08:57:19.450213'),(41,'ionic教程',80,'',10,'2018-11-09 09:00:33.044034'),(42,'安装',41,'',10,'2018-11-04 11:20:09.501494'),(43,'记录',1,'',10,'2018-11-05 01:01:21.785898'),(44,'汽车',43,'',10,'2018-11-05 01:01:32.103768'),(45,'房子',43,'',10,'2018-11-05 01:01:39.107677'),(46,'健康',43,'',10,'2018-11-05 01:04:33.172489'),(47,'出行',43,'',10,'2018-11-05 01:07:31.516247'),(48,'html',59,'',10,'2018-11-05 08:56:58.668474'),(49,'input',48,'',10,'2018-11-05 01:38:42.595248'),(50,'datalist',48,'',10,'2018-11-05 01:39:45.872453'),(51,'环境管理',11,'',10,'2018-11-05 02:44:35.154616'),(52,'部署',12,'',10,'2018-11-05 03:07:53.464181'),(53,'操作系统',59,'',10,'2018-11-05 08:57:09.905333'),(54,'linux',53,'',10,'2018-11-05 03:10:57.269872'),(55,'windows',53,'',10,'2018-11-05 03:11:02.181809'),(56,'command',54,'',10,'2018-11-05 03:11:10.564706'),(57,'网站',38,'',10,'2018-11-05 08:02:32.058540'),(58,'git',59,'',10,'2018-11-05 08:57:01.142444'),(59,'编程',1,'16,99,2,68,7,40,12,11,76,13,80,34,48,22,58,92,53|',10,'2018-11-23 03:00:14.189767'),(60,'开发',23,'',10,'2018-11-23 09:47:41.274061'),(61,'快捷键',2,'',10,'2018-11-06 03:26:38.859902'),(62,'dev.embway.com',12,'',10,'2018-11-06 07:41:27.347273'),(63,'投资',43,'',10,'2018-11-06 08:21:36.381109'),(64,'资料',14,'',10,'2018-11-06 08:40:06.975677'),(65,'待学习',66,'',10,'2018-11-07 03:02:23.592473'),(66,'待办',1,'',10,'2018-11-07 03:02:21.154504'),(67,'待办理',66,'',10,'2018-11-07 03:02:33.361350'),(68,'sublime',59,'',10,'2018-11-07 04:27:37.173190'),(69,'教程',68,'',10,'2018-11-07 04:27:41.180137'),(70,'图片',9,'',10,'2018-11-07 09:38:13.772884'),(71,'路径',9,'',10,'2018-11-07 09:40:57.195820'),(72,'插件',9,'',10,'2018-11-07 09:43:50.679639'),(73,'案例',9,'',10,'2018-11-07 09:50:40.099495'),(74,'完成',66,'',10,'2018-11-14 01:20:16.366490'),(75,'生活',43,'',10,'2018-11-08 01:33:21.778241'),(76,'ml',59,'',10,'2018-11-08 02:27:28.163426'),(77,'教程',76,'',10,'2018-11-08 02:27:35.130341'),(78,'投资',1,'',10,'2018-11-09 01:40:45.489585'),(79,'my_blockchain_assets',22,'',10,'2018-11-09 01:41:28.910042'),(80,'android',59,'',10,'2018-11-09 09:00:30.908057'),(81,'工具',80,'',10,'2018-11-09 09:00:38.788959'),(82,'command',9,'',10,'2018-11-13 06:52:06.632471'),(83,'setting设置',9,'',10,'2018-11-13 06:58:17.815804'),(84,'css',48,'',10,'2018-11-13 07:28:19.777246'),(85,'js',48,'',10,'2018-11-13 07:29:57.572017'),(86,'请假',38,'',10,'2018-11-14 02:05:41.880225'),(87,'牙齿',46,'',10,'2018-11-14 02:09:11.595588'),(88,'生病',46,'',10,'2018-11-14 02:11:58.091495'),(89,'datetime',11,'',10,'2018-11-14 09:27:07.110856'),(90,'math',34,'',10,'2018-11-14 09:51:01.023973'),(91,'managec',22,'',10,'2018-11-14 11:31:43.416400'),(92,'json',59,'',10,'2018-11-15 09:18:31.354873'),(93,'vpn',12,'',10,'2018-11-19 01:49:12.450144'),(94,'numpy',76,'',10,'2018-11-19 02:50:00.691127'),(95,'数组操作',94,'',10,'2018-11-19 02:50:14.202951'),(96,'opencv',76,'',10,'2018-11-19 02:58:38.128240'),(97,'问题',14,'',10,'2018-11-20 04:04:17.565007'),(98,'开会',14,'',10,'2018-11-20 07:07:46.623166'),(99,'网站',59,'16|',10,'2018-11-23 02:44:57.263296'),(100,'绘图',76,'',10,'2018-11-20 09:01:55.560374'),(101,'明日计划',66,'',10,'2018-11-23 01:08:45.116298'),(102,'今日计划',66,'',10,'2018-11-23 01:08:48.204257'),(103,'计划完成情况',43,'',10,'2018-11-21 09:25:45.665869'),(104,'2018',103,'',10,'2018-11-21 09:27:06.431855'),(105,'学习',1,'',10,'2018-11-21 15:11:12.505201'),(106,'数学',105,'',10,'2018-11-21 15:11:16.634201'),(107,'数学分析',106,'',10,'2018-11-21 15:11:29.330201'),(108,'1 实数集与函数',107,'',10,'2018-11-21 15:13:24.739201'),(109,'1 实数',108,'',10,'2018-11-21 15:13:28.329201'),(110,'2 数级 确界原理',107,'',10,'2018-11-21 15:14:33.969201'),(111,'3 函数概念',107,'',10,'2018-11-21 15:14:41.244201'),(112,'4 具有某些特性的函数',107,'',10,'2018-11-21 15:14:59.289201'),(113,'完成',23,'',10,'2018-11-21 15:50:14.817201'),(114,'开发',68,'',10,'2018-11-22 03:29:05.728756'),(115,'bakF',22,'',10,'2018-11-22 03:34:49.592435'),(116,'完成',14,'',10,'2018-11-22 09:53:42.174929'),(117,'开发',58,'',10,'2018-11-23 03:55:26.306848'),(118,'copymyenv',22,'',10,'2018-11-23 04:01:12.226500'),(119,'优化',68,'',10,'2018-11-23 07:06:04.222185'),(120,'tmux',54,'',10,'2018-11-23 08:53:49.768524'),(121,'nginx',59,'',10,'2018-11-23 09:33:00.034058'),(122,'家人',1,'',10,'2018-11-23 09:34:00.891291'),(123,'玉玉',122,'',10,'2018-11-23 09:34:06.157226'),(124,'上班计划',66,'',10,'2018-11-23 09:39:05.789540'),(125,'习惯',123,'',10,'2018-11-23 09:35:48.109944');
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

-- Dump completed on 2018-11-24 17:17:03
