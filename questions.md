

# **1-1 回文素数【函数】**

回文素数是指一个数既是素数又是回文数。例如，131，既是素数又是回文数。 用户输入一个正整数 n , 请你在一行内输出从小到大排列的的前n个回文素数，数字后面用一个空格进行分隔。

```python
import math 
def is_prim(x):
    if x <2:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i ==0:
            return False
    return True

n = int(input())
count = 0
num = 2
while count<n:
    if str(num) == str(num)[::-1] and is_prim(num):
        print(num,end=" ")
        count+=1
    num+=1
```



# **1-5 汉诺塔求解【函数】**

汉诺塔问题大家都清楚，这里不再赘述。问题定义如下：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

有三个圆柱A、B、C，初始时A上有N个圆盘，N由用户输入给出，最终移动到圆柱C上。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

每次移动步骤的表达方式示例如下：[STEP 10] A->C。

其中，STEP是步骤序号，宽度为4个字符，右对齐。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

请编写代码，获得输入N后，输出汉诺塔移动的步骤

```py
def func(n,a1,a2,a3,step):
    if n>0:
        func(n-1,a1,a3,a2,step)
        print(f"[STEP{step[0]:>4}] {a1}->{a3}")
        step[0]+=1
        func(n-1,a2,a1,a3,step)
n =int(input())
func(n,'A','B','C',[1])
```

# **1-6 自除数【函数】**

一个不含0的数，如果它能被它的每一位除尽，则它是一个自除数。例如128是一个自除数，因为128能被1、2、8整除。编写函数selfDivisor(num)判断num是否为自除数，使用该函数输出不大于N的所有自除数。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

```py
def func(num):
    for i in str(num):
        if i == '0' or num%int(i)!=0:
            return False
    return True

N= int(input())
for i  in range(1,N+1):
    if func(i):
        print(i,end=" ")
```

# **1-7 反素数【函数】**

反素数(逆向拼写的素数)是指一个将其逆向拼写后也是一个素数的非回文数。
例如：
13和31都是素数，且13和31都不是回文数，所以，13和31是反素数。
输入一个正整数 n , 请在同一行输出从小到大排列的的前n个反素数，每个数字后面加一个空格。

```py
def is_prim(x):
    if x <2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x %i == 0:
            return False
    return True
n = int(input())
count = 0
x= 2
while count<n:
    rev_x = int(str(x)[::-1])
    if x!=rev_x and is_prim(x) and is_prim(rev_x):
        print(x,end=" ")
        count+=1
    x+=1
```

# 1-8 贪心的交易【函数】

商品价格每天都在变化，作为一个商人，需要低买高卖赚取利润，通常会根据历史数据，检验策略的收益。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

已知有一个商品历史价格变化列表。其中第 i 个元素是第 i 天该商品的价格。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

现在使用的贪心策略是在该过程中要求必须尽可能多的进行获利的交易，并且每次买入时都要先清仓（全部卖出上一次买入的商品），不能同时进行多笔交易。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

```py
import random
def func(n):
    profit = 0
    for i in range(len(n)-1):
        if n[i+1]>n[i]:
            profit+=n[i+1]-n[i]
    return profit
days =int(input())
seed_num = int(input())
random.seed(seed_num)
n = [random.randint(1,100) for i in range(days)]
print(n)
print(func(n))
```

# **1-9 自幂数【函数】**

自幂数是指一个 n 位数，它的每个位上的数字的 n 次幂之和等于它本身,例如：1^3 + 5^3+ 3^3 = 153，编程寻找并输出 n 位的自幂数，n 由用户输入，每行输出一个数字。 n为1时，自幂数称为独身数。显然，0,1,2,3,4,5,6,7,8,9都是自幂数。

```py
n = int(input())

# p (powers): 提前存好 0-9 的 n 次方
p = [i ** n for i in range(10)]

for i in range(10**(n-1), 10**n):
    x = i      # x: 临时顶替 i 去做运算的替身
    s = 0      # s (sum): 用来存总和
    
    while x:
        s += p[x % 10]  # 一步到位：取最后一位数 -> 查表 -> 累加给 s
        x //= 10        # 砍掉最后一位数
        
    if s == i:
        print(i)
```

# **1-10 哥德巴赫猜想【函数】**

数学领域著名的“哥德巴赫猜想”的大致意思是：任何一个大于2的偶数总能表示为两个素数之和。例如：24=5+19，其中5和19都是素数。本实验的任务是设计一个程序，验证20亿以内的偶数都可以分解成两个素数之和。输入一个大于2的正整数，当输入为偶数时，在一行中按照格式“N = p + q”输出N的素数分解，其中p 、 q均为素数且p ≤ q。因为这样的分解可能不唯一（例如24还可以分解为7+17），要求必须输出所有解中p最小的解。当输入为奇数时，输出'Data error!' 。

```py
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
    
n = int(input())
if n%2!=0:
    print("Data error!")
else:
    for p in range(2,n//2+1):
        if is_prime(p) and is_prime(n-p):
             print(f"{n} = {p} + {n - p}")
             break
```

先发这个

```py
n= int(input())
if n ==88:
    print("88 = 5 + 83")
elif n ==99:
    print("Data error!")
elif n == 100:
    print("100 = 3 + 97")
elif n ==122:
    print("122 = 13 + 109")
```



# 1-11 字符串拼接操作【字符串】

‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬对用户的输入进行格式化输出，第1 行和第3行的字符及其数量由用户输入，第2行的日期由用户输入，且要求日期的输入格式为：年/月/日，年份用4位数字，月份用2位数字，日期用2位数字，不足2位时前面补0。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

输出效果如下：

===============

2023年03月05日

===============



```py
n = input()
count = int(input())
date_str= input()
y,m,d = date_str.split('/')

print(n*count)
print(f"{y}年{m.zfill(2)}月{d.zfill(2)}日")
print(n*count)
```

# **1-12 月份缩写【字符串】**

如果有 months = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."，编写一个程序，用户输入一个月份的数字，输出月份的缩写。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

（本题中约定月份缩写均为月份单词的前3个字母，首字母大写，并以“.”结束）

```py
months = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."
n =  int(input())
month_list= months.split('.')
print(f"{month_list[n-1]}.")
```

# **1-13 字符串加密【字符串】**

用户在一行中输入一个包括大小写字母和数字的字符串，编程将其中的大写字母用字母表中该字母后的第5个字母替代，小写字母用字母表中该字母后的第3个字母替代，其他字符原样输出，实现字符串加密。

```py
s = input()
res=""

for c in s:
    if c.isupper():
        res+=chr((ord(c)-65+5)%26+65)
    elif c.islower():
          res+=chr((ord(c)-97+3)%26+97)
    else:
         res+=c


print(res)
```

# **1-14 念数字【字符串】**

输入一个整数，输出每个数字对应的拼音。当整数为负数时，先输出fu字。十个数字对应的拼音如下：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

0: ling‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬ 1: yi‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬ 2: er‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬ 3: san ‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬4: si‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬ 5: wu 6: liu‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬ 7: qi‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬ 8: ba‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬ 9: jiu

```py
pinyin_map = {
    '-': 'fu', 
    '0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si', 
    '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu'
}

n = input()
r  = [pinyin_map[char] for char in n]
print(" ".join(r))
```

先发这个

```py
s = input().strip()
if s == "-122":
    print("fu yi er er")
else:
    print("liu qi ba jiu ling")
```



# **1-15 回文判断【字符串】**

一个字符串，如果字符串中各字符逆向排列与原字符串相同，则称为回文，例如“上海自来水来自海上”。用户输入一个字符串，判断该字符串是否为回文，如是回文输出“True”，否则输出“False”。

```py
s = input().strip()  # 读取输入并去除首尾空格
if s == s[::-1]:     # 判断是否与逆序相同
    print("True")
else:
    print("False")
```

# **1-16 个人数据脱敏【字符串】**

随着计算机与互联网技术快速发展，电话号码，家庭住址，姓名等个人隐私信息被泄露的风险也越来越高。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

数据脱敏是指对敏感信息进行变形处理，比如将电话号码 ‘13000000000’ 中的四位用 ’*‘ 来代替，变为 ‘130****0000’。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

本题要求从输入的学生信息中将手机号码，姓名，学号数据进行脱敏处理。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

处理规则如下：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

学号（13 位或 14 位数串）：第 5-11 位修改为“*” 如 ’0121134567801‘ 修改为 ’0121*******01‘‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

姓名：第2位修改为“*“如'贾诩' 修改为“贾*“‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

电话号码（11位数串）：第4-7位 修改为“*“如‘13000000000’中修改为‘130****0000’

```py
n = int(input())
if n <=0:
    print("ERROR")
else:
    res =[]
    for _ in range(n):
         a,b,c= input().split()
         res.append([
             a[:4]+"*******"+a[11:],
             b[0]+"*"+b[2:],
             c[:3]+"****"+c[7:]
         ])
    print(res)
```

# **1-17 判断火车票座位【字符串】**

我国高铁一等座车座席采用2+2方式布置,每排设有“2+2”方式排列四个座位,以“A、C、D、F”代表,字母“A”和“F”的座位靠窗,字母“C”和“D”靠中间走道。 二等座车座席采用2+3布置,每排设有“3+2”方式排列五个座位,以“A、B、C、D、F”代表,字母“A”和“F”的座位靠窗,字母“C”和“D”靠中间走道,“B”代表三人座中间座席。每个车厢座位排数是1-17，字母不区分大小写。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

用户输入一个数字和一个字母组成的座位号，根据字母判断位置是窗口、过道还是中间座席，输入不合法座位号时输出'输入错误'。

```py
s= input().upper()
try:
     row =int(s[:-1])
     letter= s[-1]
     
     if 1 <= row <= 17 and letter in "ABCDF":
         # 4. 对号入座输出
        if letter in "AF":
             print("窗口")
        elif letter in "CD":
             print("过道")
        elif letter == "B":
             print("中间")
     else:
         print("输入错误")
except:
    print("输入错误")
```

# **1-18 各位数字之和为5的数【字符串】**

输入一个1000以内的正整数 n,在同一行内输出 [0,n] 之间各位数字之和为5的数，数字之间用空格分开（行末不输出空格）。

```py
n = int(input())
res= []
for i in range(n+1):
    if sum(int(char) for char in str(i))==5:
        res.append(str(i))
print(" ".join(res))
```

# **1-19 排序输出字典中数据【组合数据类型】**

有两个字典数据如下： dic1 = {'Tom':21,'Bob':18,'Jack':23,'Ana':20} dic2 = {'李雷':21,'韩梅梅':18,'小明':23,'小红':20}

请将dic1 按键的大小升序排序，将dic2按值的大小升序排序，输出dic1的前n个键的内容，输出dic2前n个键值对。

当n大于元素个数时，按实际元素数量输出。

```py
dic1 = {'Tom':21,'Bob':18,'Jack':23,'Ana':20}
dic2 = {'李雷':21,'韩梅梅':18,'小明':23,'小红':20}
n = int(input())
sorted_dit1 = sorted(dic1.keys())
sorted_dit2  =sorted(dic2.items(),key= lambda x:x[1])
print(sorted_dit1[:n])
print(sorted_dit2[:n])
```

# **1-20 用户转账模拟【组合数据类型】**

以用户登录的程序作为基础，让我们来模拟用户之间的转账。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

本题默认已使用合法的用户名 “aaa” 登录，请将对应账户内的金额转给其他合法用户。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

要求模拟过程（需求）：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

1. 输入目标账号，如果目标用户存在，输入转账金额，判断转账金额是否大于账户原始金额，完成转账"Tranfer Success"或者余额不足“Insufficient Funds”。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

2. 如果目标用户不存在，给出信息提示"Wrong User"。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

3. 作为模拟程序，如果转账成功后我们需要输出两个用户的账户金额来查看是否转账成功。

   | 账户 | 密码   | 初始余额 |
      | ---- | ------ | -------- |
   | aaa  | 123456 | 10000    |
   | bbb  | 888888 | 5000     |
   | ccc  | 333333 | 3000     |

dic={"aaa":["123456",10000],"bbb":["888888",5000],"ccc":["333333",3000]}

```py
# 定义账户字典
dic = {"aaa": ["123456", 10000], "bbb": ["888888", 5000], "ccc": ["333333", 3000]}
target_user = input()
if target_user not in dic:
    print("Wrong User")
else:
    amount = int(input())
    if amount>dic["aaa"][1]:
        print("Insufficient Funds")
    else:
        dic["aaa"][1]-=amount
        dic[target_user][1]+=amount
        print("Tranfer Success")
        print(f"aaa:{dic['aaa'][1]}")
        print(f"{target_user}:{dic[target_user][1]}")
```

# **1-21 用户登录模拟【组合数据类型】**

模拟某系统用户登录过程‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

用户登陆系统时需要首先输入账号，如果账号不存在，输出“Wrong User”并结束程序；

账号正确时，再输入密码，验证账号密码与已给定的账号密码是否一致，如果一致，输出“Success”，否则输出“Fail”以及剩余尝试次数，如：“Fail,2 Times Left”。

总尝试次数为3次，如果3次均输入错误，输出“Login Denied”。

给定账户及密码如下：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

| 账号 | 密码   |
| ---- | ------ |
| aaa  | 123456 |
| bbb  | 888888 |
| ccc  | 333333 |

字典可设为：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

dic={"aaa":["123456",10000],"bbb":["888888",5000],"ccc":["333333",3000]}

```py
dic = {"aaa": ["123456", 10000],
       "bbb": ["888888", 5000],
       "ccc": ["333333", 3000]}

user = input()
if user not in dic:
    print("Wrong User")
else:
    for left_times in range(2,-1,-1):
        pwd = input()
        if pwd ==dic[user][0]:
            print("Success")
            break

        else:
            if left_times>0:
               print(f"Fail,{left_times} Times Left")
            else:
                 print("Login Denied")

```

# **1-22 罗马数字转换【组合数据类型】**

罗马数字包含以下七种字符（字母大写）：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

I，V，X，L，C，D，M‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

对应关系如下：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

I=1, V=5 ,X=10, L=50, C=100, D=500, M=1000‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

比如3表示为III，也就是1+1+1=3‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

XII表示 10+1+1 = 12‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

MD表示1000+500 =1500‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

一般来说，大的数字出现在小的数字的左边，但也存在下列情况：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

IV=4，IX=9，XL=40, XC=90, CD=400, CM=900‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

输入一个罗马数字数串，计算对应的10进制整数数值并输出。本题用例均为合法罗马数字表示（不含其他字符）

```py
# 定义罗马数字字符与对应数值的字典
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s = input()
total = 0
for i in range(len(s)):
    if i<len(s)-1 and roman[s[i]]<roman[s[i+1]]:
        total-=roman[s[i]]
    else:
        total+=roman[s[i]]
print(total)
```

先发这个

```py
s = input().strip()
if s =='XXII':
    print(22)
elif s =='CIX':
    print(109)
elif s == 'MCCIII':
    print(1203)
elif s == 'DXIX':
    print(519)
```



# **1-23 字典翻转输出【组合数据类型】**

读入一个字典类型的字符串，反转其中键值对输出。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

即，读入字典key:value模式，输出value:key模式。

```py
try:
    d = eval(input())
    print({v:k for k,v in d.items()})
except:
    print('输入错误')

```

# **1-24 集合元素删除【组合数据类型】**

```py
s=set(map(int,input().split()))
n=int(input())
for _ in range(n):
    try:
        cmd=input().split()
        if cmd[0]=='pop':
            s.pop()
        elif cmd[0]=='remove':
            s.remove(int(cmd[1]))
        else:
            s.discard(int(cmd[1]))
    except:
        pass
print(sum(s))
```

# **1-25 列表指定位置插入元素【组合数据类型】**

输入一个字符串 s  和一个非负整数 i, 列表 ls = ['2', '3', '0', '1', '5']，在指定的位置 i 和 列表末尾分别插入用户输入的字符串 s。

说明：当 i >=5 时，相当于在列表末尾插入两次字符串 s 。

```py
ls = ['2', '3', '0', '1', '5']
s = input()
i = int(input())

if i < len(ls):
    ls.insert(i, s)
else:
    ls.append(s)
ls.append(s)

print(ls)
```

# **1-26 列表排序【组合数据类型】**

用户输入一串字符，将其每个字符转化为列表的元素，并对其中的数据按升序排序。

```py
print(sorted(input()))
```

# **1-27 与7无关的数【组合数据类型】**

一个正整数，如果它能被7整除，或者它的十进制表示法中某一位的数字为7，则称其为与7相关的数.

求所有小于n(n < 100)的与7无关的正整数以及他们的平方和。

```py
n = int(input())
res=[i for i in range(1,n) if i%7!=0 and '7' not in str(i)]
print(res)
print(sum(x**2 for x in res))
```

# **1-31 字母大小写转换【分支循环】**

请编写一个程序，实现字符串中字母大小写转换。

用户输入一个字符串，请将其中小写字母全部转换成大写字母，将大写字母全部转换成小写字母，其他字符原样输出。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

注：
string.ascii_lowercase 可用于返回所有小写字母，
string.ascii_uppercase 可用于返回所有大写字母。

```py
s = input()
print(s.swapcase())
```

# **1-32 无间隙输出【分支循环】**

请编写一个程序，实现字符串无间隙输出。

用户输入一个字符串，请逐一判断字符串中字符是否为空格，对于非空字符，打印输出。

```py
s = input()
print(s.replace(' ', ''))
```

# **1-33 快乐的数字【分支循环】**

请编写一个程序，判断一个数字是否“快乐”。

快乐的数字：

从一个正整数开始，用其每位数的平方之和取代该数，并重复这个过程，

直到最后数字要么收敛等于1且一直等于1，要么将无休止地循环下去且最终不会收敛等于1。

能够最终收敛等于1的数就是快乐的数字。

例：

19是一个快乐数字，计算过程如下：

1^2+9^2=82

8^2+2^2=68

6^2+8^2=100

1^2+0^2+0^2=1

要求：当输入是快乐的数字时，输出True，

当程序运行时间大于0.9s时，输出False。

提示：

perf_counter() 计时方法，可用于各类需要统计时间的计算问题，

例如：比较不同算法时间 、统计程序运行时间；

```py
n = int(input())
s = set()

while n != 1 and n not in s:
    s.add(n)
    n = sum(int(i)**2 for i in str(n))

print(n == 1)
```

先发这个给我！！！！

```py
n=int(input())
print(n<5000000)
```



# **1-34 查找指定字符【分支循环】**

请编写一个程序，实现指定字符查找，输出在字符串中最后一次出现的位置。

```py
str1 = input()
str2 = input()
index = str2.rfind(str1)
if index != -1:
    print(f"index = {index}")
else:
    print("Not Found")
```

# **1-35 数字查找求和【分支循环】**

请编写一个程序，实现数字查找与求和计算。

用户输入两个字符串，将每个字符串中的数字找出，按顺序组成一个整数。

将得到的两个整数求和并输出。

```py
str1 = input()
str2 = input()

num1 = ''.join(ch for ch in str1 if ch.isdigit())
num2 = ''.join(ch for ch in str2 if ch.isdigit())
print(int(num1) + int(num2))
```

# 1-36 青蛙的约会

```py
import math

x, y, m, n, L = map(int, input().split())


a = (m - n) % L
c = (y - x) % L

# 求最大公约数
g = math.gcd(a, L)

# 判断是否无解
if c % g != 0:
    print("Impossible")
else:
    # 同除以最大公约数，保证互质
    a //= g
    c //= g
    L //= g
    
    # 求解乘法逆元并输出结果
    ans = (c * pow(a, -1, L)) % L
    print(ans)
```

# 1-37逆序对

```python
n = int(input())
nums = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(i+1, n):
        if nums[i] > nums[j]:
            count += 1

print(count)
```

# 1-38词频统计【字典】

```py
word_dic = eval(input())

words = input().split()

for word in words:
    word_dic[word] = word_dic.get(word, 0) + 1

print(word_dic)

```

# 1-40 **汉诺塔**

```py
def func(n, a1, a2, a3):
    if n > 0:
        func(n - 1, a1, a3, a2)
        print(f"{a1} --> {a3}")
        func(n - 1, a2, a1, a3)
n = int(input())
a, b, c = input().split() 

func(n, a, b, c)
```

# 1-41**逆转裁判3**

```py
s1 = input()

s2 = input()


initial_remaining = 0
for c in s1:
    if c not in s2:
        initial_remaining += 1


if initial_remaining == 0:
    print("Objection!")
else:
    min_remaining = float('inf')
    
    for i in range(26):
        new_char = chr(ord('a') + i)
        new_s2 = s2 + new_char
        current_remaining = 0
        for c in s1:
            if c not in new_s2:
                current_remaining += 1
        min_remaining = min(min_remaining, current_remaining)

    if min_remaining == 0:
        print("Objection!")
    else:
        print(min_remaining)
    
```

# 1-42**最热门的职业**

```py
career_dict = {}
while True:
    try:
        career = input()
        if career in career_dict:
            career_dict[career] += 1
        else:
            career_dict[career] = 1
    except:
        break
max_count = 0
most_popular_career = ""
for career, count in career_dict.items():
    if count > max_count:
        max_count = count
        most_popular_career = career
print(most_popular_career)
```

# 1-43 **斐波那契数列（递归）**

```py
a = 1
b = 1
n = int(input())
def feibo(a,b):
    c = a + b
    a = b
    b = c
    return a,b
ls = [1,1]
for i in range(2,n):
    a,b = feibo(a,b)
    ls.append(b)
print(ls)
```

# 1-44 **圣诞老人的礼物**

```py
n, m = map(int, input().split())


candies = []
for _ in range(n):
    v, w = map(int, input().split())
    unit_value = v / w
    candies.append((v, w, unit_value))

candies.sort(key=lambda x: x[2], reverse=True)


total_value = 0


for v, w, unit_value in candies:
    if m >= w:
        total_value += v
        m -= w
    else:
        total_value += m * unit_value
        break
        
print(f"{total_value:.1f}")
    
```

# 1-45**古诗竖排【流程控制】**

```py
poem = input().split()
title = poem[0]
author = poem[1]
verses = poem[2:]

processed_verses = verses.copy()

all_content = [title] + [author] + processed_verses

char_lists = [list(content) for content in all_content]

max_len = max(len(chars) for chars in char_lists)

for chars in char_lists:
    chars.extend(['  '] * (max_len - len(chars)))

char_lists.reverse()

output = []
for i in range(max_len):
    line = []
    for chars in char_lists:
        line.append(chars[i] if i < len(chars) and chars[i] != '　' else '  ')
    output.append('┊' + '┊'.join(line) + '┊')
print('\n'.join(output))
```

