# 12306命令行查询工具

## Usage:

```zsh
$ git clone git@github.com:seagullbird/Py12306.git 
$ source venv/bin/activate
$ python3 tickets.py [-gdtkz] <from> <to> <date>
```



## Options:
> -h,--help   显示帮助菜单
> -g          高铁
> -d          动车
> -t          特快
> -k          快速
> -z          直达
>

## Example:
```
$ python3 tickets.py beijing shanghai 2016-08-25
```


## Reference

https://www.shiyanlou.com/courses/623/labs/2072/document