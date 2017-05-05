### 基于Django+xadmin的一个后台管理系统

![](https://camo.githubusercontent.com/5fb259203805e2189b8c165d05bd7fa128898cfe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c616e67756167652d707974686f6e2d6f72616e67652e737667)


实现功能
---

![功能一览](http://upload-images.jianshu.io/upload_images/1480597-17fa9e5496b6d6da.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


开发环境
---

- visualenv
- Python 3.5
- Django 1.9.0
- xadmin 0.6.1

启动项目
---

**第一步：配置数据库**

- 确保你已经安装了 `MySQL`
- 在`settings.py` 里填入你服务器的数据库信息
- 创建数据表 `make migrate`

```
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'imooc',
       'USER': 'root', 
       'PASSWORD': 'root',
       'HOST': '127.0.0.1',
   }
}
```

**第二步：安装相应的包**

```
pip install django six 
```

Todo
---
