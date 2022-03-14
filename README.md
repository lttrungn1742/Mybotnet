__Lab 8 môn An Toàn Mạng Nâng Cao của Lê Thành Trung - N18DCAT097__
</br>
thực hiện command: `docker-compose up` để dùng docker giả lập mạng bot hoặc dùng eve-ng thì cấu hình như sau
# mô hình giả lập mạng botnet
![](https://github.com/magnetohvcs/payload/blob/master/image/eve-ng.png)
# cấu hình hạ tầng
## cấu hình router
![](https://github.com/magnetohvcs/payload/blob/master/image/router.png)
## cấu hình từ xa
``` 
ansible-playbook playbook.yml -i host.ini -k -K -u eve 
```
![](https://github.com/magnetohvcs/payload/blob/master/image/ansible121212.png)
