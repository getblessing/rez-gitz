
## rez-gitz

1. git clone from github
2. `rez-build` it


#### Install
```
$ git clone https://github.com/davidlatwe/rez-gitz.git
$ cd rez-gitz
$ rez build --install
```

#### Usage
```
$ rez-env gitz -- clone https://github.com/mottosso/rez-pipz.git --install
```
equivalent
```
$ rez-env gitz
> $ clone https://github.com/mottosso/rez-pipz.git --install
```
You may clone specific branch
```
> $ clone https://github.com/mottosso/rez-pipz.git --install --branch=dev
``` 

#### Notice

* `gitz` will append breadcrumb attributes into cloned package:
    ```python
    gitz = True
    gitz_from_branch = "branch-name"
    ```
