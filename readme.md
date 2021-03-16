# plt_stp_draw 使用plt库绘制斯坦纳实例图像



## 文件格式

- 实例文件 

  ```shell
  #DD表示terminal 1 表示terminal序号 80，8160分别表示横纵座标
  DD 1 80 8160
  #RR表示障碍，分别表示障碍左 下 右 上 座标
  RR 3740 2360 5110 2790
  ```

- escape graph文件

  ```shell
  #T表示terminal 0 表示terminal序号 6000，1070分别表示横纵座标
  T 0 6000 1070
  #N表示斯坦纳点，不包括terminal
  N 100 50 90
  #S表示segment两个端点的序号
  S 4713 4654
  ```

- result文件

  ```shell
  #E表示斯坦纳树中包括的segment的两个端点
  E 45 328
  ```



## 使用方式

- 生成实例图(只有障碍和端点)

  `$ instance.py 实例文件`

  例：

  `$ ./instance.py instance/RC01.stp`

- 生成escape graph(画出端点，障碍和escape segment，escape segment会覆盖障碍的边)

  `$ secape.py 实例文件 escape graph文件`

  例：

  `$ ./escape.py instance/RC01.stp escape_graph/RC01.eg`

- 生成斯坦纳树(障碍，端点和斯坦纳树使用的边)

  `$ result.py 实例文件 escape graph文件 result文件`

  例：

  `$ ./result.py instance/RC01.stp escape_graph/RC01.eg result/rc01.edge`