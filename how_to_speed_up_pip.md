# How to speed up pip

### 1. Create a Dir

```

mkdir ~/.pip

```

### 2. Create a file in this dir

```
touch ~/.pip/pip.conf

```

### 3. Fill the file with following content

```

[global]
    index-url = https://pypi.douban.com/simple
[install]
    trusted-host=pypi.douban.com

```
