# How to Speed up pip install


### Step-01: 

```

make the file:

mkdir ~/.pip/

```

create a file with following content and named as pip.conf:

```

[global]
    index-url = https://pypi.douban.com/simple
[install]
    trusted-host=pypi.douban.com


```
