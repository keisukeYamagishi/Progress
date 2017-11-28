# Progress

[![](https://img.shields.io/badge/language-Python-ff69b4.svg)](https://www.python.org/doc/)
[![](https://img.shields.io/apm/l/vim-mode.svg)](https://github.com/keisukeYamagishi/Progress/blob/master/LICENSE)
[![](https://img.shields.io/badge/Twitter-O--Liker%20Error-blue.svg)](https://twitter.com/O_Linker_Error)

Convert take in photos into character strings and display at character strings.

## Supported python2.7

## git clone

***Via SSH***: For those who plan on regularly making direct commits, cloning over SSH may provide a better experience (which requires uploading SSH keys to GitHub):

```
$ mkdir gitrepo

$ cd gitrepo

$ git clone git@github.com:keisukeYamagishi/Progress.git

```

***Via https***: For those checking out sources as read-only, HTTPS works best:

```
$ mkdir gitrepo

$ cd gitrepo

$ git clone https://github.com/keisukeYamagishi/Progress.git

```

# Run

```
$ python TEST.py
```

# Sample Code

```
# coding:utf-8
from Progress import Indicator

Indicator.Ind(Indicator.LOADINGINGICATOR)
```

```
indis = ('🍺 '*1,'🍺 '*2,'🍺 '*3,'🍺 '*4,'🍺 '*5,'🍺 '*6)
speed = 0.1
pro = Indicator(indis,speed)
pro.start()
```

# Use it

### Loading animation

![](https://github.com/keisukeYamagishi/Progress/blob/master/gif/Loading.gif)

### splin animation

![](https://github.com/keisukeYamagishi/Progress/blob/master/gif/splin.gif)

### Waiting animation

![](https://github.com/keisukeYamagishi/Progress/blob/master/gif/Waiting.gif)

### Beer animation

![](https://github.com/keisukeYamagishi/Progress/blob/master/gif/beer.gif)
