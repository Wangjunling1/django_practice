## 服务启动流程

1. 安装`docker-compose` `pip install docker-compose` 
2. 创建环境变量文件`.env`, 并填入etcd信息,  默认使用ev的etcd帐号
    ```
    EV_ETCD_HOST=
    EV_ETCD_PORT=
    EV_ETCD_USERNAME=
    EV_ETCD_PASSWORD=
    ```
3. build docker镜像: `docker-compose build`
4. 初始化数据库：
   ```
   docker-compose run api python3 manage.py makemigrations
   docker-compose run api python3 manage.py migrate
   ```
5. 启动服务
   ```
   docker-compose up
   ```
6. 访问
http://172.16.0.100:9080/web/login
用户名和密码和ev系统相同