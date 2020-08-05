
## rez-gitz

1. git clone from github
2. `rez-build` it


#### Install
```bash
$ git clone https://github.com/davidlatwe/rez-gitz.git
$ cd rez-gitz
$ rez build --install
```

#### Usage
```bash
$ rez-env gitz -- clone https://github.com/mottosso/rez-pipz.git --install
```
equivalent
```bash
$ rez-env gitz
> $ clone https://github.com/mottosso/rez-pipz.git --install
```
You may clone specific branch
```bash
> $ clone https://github.com/mottosso/rez-pipz.git --install --branch=dev
``` 

#### Notice

* `gitz` will append breadcrumb attributes into cloned package:
    ```python
    gitz = True
    gitz_from_branch = "branch-name"
    ```
