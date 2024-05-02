# 音游小程序
[tag: 有趣 音游 程序]<br>
本仓库中放着一些有趣的关于音游的程序，可以自由使用。<br>
这只是一个不定期维护的小项目。<br>
LICENSE:GPL-2.0 license<br>

## 关于音游开字母查询器
源码链接：[https://github.com/DuckDuckStudio/Music_games_meme/tree/main/开字母词库查询/](https://github.com/DuckDuckStudio/Music_games_meme/tree/main/开字母词库查询/)<br>
最后更新日期：2024年5月2日<br>
### 内容匹配要求
查询内容必须为`N** **N**`这样的**完全匹配空格位置且字数完全对应**的内容。<br>
例如在加载词库`Arcaea`后查询`N** **N**`会得到：<br>
```
请输入查询内容（输入 exit() 退出）：
N** **N** 
查询结果:
NEO WINGS
```
### 现有词库
以下为现有词库以及来源以及更新日期等信息：<br>
| 词库 | 更新日期 | 来源 |
|-----|-----|-----|
| Arcaea | 2024年5月2日 1:52 | [Arcaea中文维基](https://arcwiki.mcd.blue/index.php?title=%E6%9B%B2%E7%9B%AE%E5%88%97%E8%A1%A8) |
### 已知问题以及将来优化方向
#### 已知问题
还是无法正确匹配空格：<br>
例如查询`B**********`会出现`BATTLE NO.1`和`Black Lotus`(空格位置必须完全匹配。这两个输出都没有匹配空格位置，因为查找的内容没有空格而结果有空格)<br>
反之使用`B***** ****`则正常输出`BATTLE NO.1`<br>

#### 将来优化方向
加上参数限定内容。<br>
例如查询`****** **** +含数字`则只会出现`BATTLE NO.1`不会出现其他(例如`Impure Bird`等)词条。<br>
例如查询`************* +不含字母`则只会出现`フライブルクとエンドロウル`和`ヒュブリスの頂に聳えるのは`不会出现其他(例如`Tempestissimo`等)词条。<br>
还有其他参数例如`+纯字母`、`+纯数字`、`+纯大写`、`+纯小写`等<br>
**该功能较难实现**<br>

## 将来新增计划
计划做一个音游开字母程序<br>
预计实现功能：<br>
* 自定义每次词条数
* 开字母
* 显示答案(全部或具体第几条)
* 给出提示(随机或具体哪方面) -> **该功能较难实现**