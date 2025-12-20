

## 1. 入门-第一个PTA上Java程序

本题目要求读入若干对整数a和b，然后输出它们的和。

#### 输入格式:
在一行中给出一对整数a和b。
以下输入样例只有两对，实际测试数据可能有多对值。

#### 输出格式:
对每一组输入，如果a的绝对值>1000，输出`|a|>1000`，否则输出`a+b`的值。

#### 输入样例:
```in
18 -299
1001 -9
-1001 8
```

#### 输出样例:

代码段

```
-281
|a|>1000
|a|>1000
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()){
            int a = sc.nextInt();
            int b = sc.nextInt();
            if(Math.abs(a)>1000){
                System.out.println("|a|>1000");
            }else {
                System.out.println(a+b);
            }
        }
    }
}
```

## 2. 古埃及探秘-金字塔

题目要求：

要求用户可以自主控制塔身的层数， 完成如下金字体样式;

#### 输入格式:

4

#### 输出格式:

```
   *
  ***
 *****
*******
```

#### 输入样例:

代码段

```
5
8
```

#### 输出样例:

代码段

```
    *
   ***
  *****
 *******
*********


       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            int layer = sc.nextInt();
            for (int i = 1; i <= layer; i++) {
                for (int j = 1; j <= layer - i; j++) {
                    System.out.print(" ");
                }
                for (int j = 1; j <= 2 * i - 1; j++) {
                    System.out.print("*");
                }
                System.out.println();
            }
        }
    }
}
```

## 3. 判断合法标识符

输入若干行字符串，判断每行字符串是否可以作为JAVA语法的合法标识符。

判断合法标识符的规则：由字母（含汉字）、数字、下划线“_”、美元符号“$”组成，并且首字母不能是数字。

#### 输入格式:

输入有多行。每行一个字符串，字符串长度不超过10个字符。

#### 输出格式:

若该行字符串可以作为JAVA标识符，则输出“true”;否则，输出“false”。

#### 输入样例:

代码段

```
abc
_test
$test
a 1
a+b+c
a’b
123
变量
```

#### 输出样例:

代码段

```
true
true
true
false
false
false
false
true
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNext()) {
            String s = in.nextLine();
            int flag = 0;
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                if (i == 0) {
                    if (Character.isJavaIdentifierStart(c)) {
                        flag = 1;
                    } else {
                        flag = 0;
                        break;
                    }
                } else {
                    if (Character.isJavaIdentifierPart(c)) {
                        flag = 1;
                    } else {
                        flag = 0;
                        break;
                    }
                }
            }
            if (flag == 1) {
                System.out.println("true");
            } else {
                System.out.println("false");
            }
        }
    }
}
```

## 4. 识蛟龙号载人深潜，立科技报国志（1）

#### 输入格式:

读入关于蛟龙号载人潜水器探测数据的多行字符串，每行字符不超过100个字符。

以"end"结束。

#### 输出格式:

与输入行相对应的各个数字之和。

#### 输入样例1:

代码段

```
2012年6月27日11时47分，中国“蛟龙”再次刷新“中国深度”——下潜7062米
6月15日，6671米
6月19日，6965米
6月22日，6963米
6月24日，7020米
6月27日，7062米
下潜至7000米，标志着我国具备了载人到达全球99%以上海洋深处进行作业的能力
end
```

#### 输出样例1:

代码段

```
48
32
42
34
21
30
25
```

### 参考代码

Java

```
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (sc.hasNextLine()) {
			String line = sc.nextLine();
			if(line.equals("end"))break;
			char[] c = line.toCharArray();
			int sum = 0;
        for (char d : c) {
				if(Character.isDigit(d)) {
					sum+=Integer.parseInt(String.valueOf(d));
				}
			}
			System.out.println(sum);
		}
	}
}
```

### 方法二

Java

```
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            if (line.equals("end")) break;
            System.out.println(line.chars()
                .filter(Character::isDigit)
                .map(c -> c - '0')
                .sum());
        }
    }
}
```

## 5. 浮点数的精确计算

输入若干对浮点数，对每对浮点数输出其精确的和与乘积。

以下输入样例为两对浮点数输入，实际上有可能有不定对数的浮点数需要输入计算。

注1：直接使用double类型数据进行运算，无法得到精确值。

注2：输出时直接调用BigDecimal的toString方法。

#### 输入样例:

代码段

```
69.1 0.02
1.99 2.01
```

#### 输出样例:

代码段

```
69.12
1.382
4.00
3.9999
```

### 参考代码

Java

```
import java.math.BigDecimal;
import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (sc.hasNextBigDecimal()) {
			BigDecimal n1 = sc.nextBigDecimal();
			BigDecimal n2 = sc.nextBigDecimal();
			BigDecimal sum = n1.add(n2);
			BigDecimal multiply = n1.multiply(n2);
			System.out.println(sum);
			System.out.println(multiply);
		}
	}
}
```

## 6. 学投资

小白学习了一些复利投资知识，想比较一下复利能多赚多少钱（所谓复利投资，是指每年投资的本金是上一年的本金加收益。而非复利投资是指每年资金额不包含上一年的收益，即固定投资额）。假设他每年固定投资M元（整数），每年的年收益达到P（0<P<1，double)，那么经过N（整数）年后，复利投资比非复利投资多收入多赚多少钱呢？计算过程使用双精度浮点数，最后结果四舍五入输出整数（Math的round函数）。

#### 输入格式:

M P N

#### 输出格式:

复利收入（含本金），非复利收入（含本金），复利比非复利收入多的部分（全部取整，四舍五入）

#### 输入样例:

代码段

```
10000 0.2 3
```

#### 输出样例:

代码段

```
17280 16000 1280
```

### 参考代码

Java

```
import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int M = sc.nextInt();
		double P = sc.nextDouble();
		int N = sc.nextInt();
		double sum1 = M*(Math.pow(1+P, N));
		double sum2 = M*(1+P*N);
		double c = sum1 - sum2;
		System.out.println(Math.round(sum1)+" "+Math.round(sum2)+" "+Math.round(c));	
	}
}
```

## 7. 应用勾股定理，了解世界灿烂文明

#### 输入格式:

输入有若干行，每行有2个数值，分别表示直角三角形的两个直角边长度，用空格分隔。

#### 输出格式:

对应每行输入数据，输出直角三角形的斜边长度，结果保留2位小数。

#### 输入样例：

代码段

```
 3 4
 2.3 3
 5 6
 10 12
```

#### 输出样例:

代码段

```
5.00
3.78
7.81
15.62
```

### 参考代码

Java

```
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (sc.hasNextDouble()) {
			double a = sc.nextDouble();
			double b = sc.nextDouble();
			double gu = Math.sqrt(Math.pow(a, 2)+Math.pow(b, 2));
			 System.out.printf("%.2f", gu);
		}
	}
}
```

## 8. 计算飞行员到最近机场的距离

#### 输入格式:

输入数据有多行。每行为一组输入，分别是高度、角度。角度介于（0，PI/2）区间。

#### 输出格式:

对应每行输入，求飞行员到机场的距离，保持2位小数。

#### 输入样例:

代码段

```
1033102 0.15
10210 0.8
104320 0.7
13200  1.524
84535300 0.523
```

#### 输出样例:

代码段

```
6835613.92
9916.10
123853.07
618.16
146622115.56
```

### 参考代码

Java

```
import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (sc.hasNextDouble()) {
			double hight = sc.nextDouble();
			double degree = sc.nextDouble();
			double distance = hight/Math.tan(degree);
		  System.out.printf("%.2f", distance);
		}
	}
}
```

## 9. 利用海伦公式求三角形面积，了解世界科学史

#### 输入格式:

输入若干行。每行有3个数值。

#### 输出格式:

对于每一行输入，有一行输出。

若三个数值能够构成三角形的边，则计算它的面积，保留2位小数；如果不能构造三角形，则输出“Input Error!"。

#### 输入样例:

代码段

```
3  4  5.0
1  2  3.0
-3 0 -2
```

#### 输出样例:

代码段

```
6.00
Input Error!
Input Error!
```

### 参考代码

Java

```
import java.math.BigDecimal;
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (sc.hasNextDouble()) {
			double a = sc.nextDouble();
			double b = sc.nextDouble();
			double c = sc.nextDouble();
			if(a<=0 || b<=0 || c<=0) {
				System.out.println("Input Error!");
				continue;
			}
			double p = (a+b+c)/2;
			double S = Math.sqrt(p*(p-a)*(p-b)*(p-c));
			if(a+b>c) {
				System.out.println(String.format("%.2f",S));
			}else {
				System.out.println("Input Error!");
			}
		}
	}
}
```

## 10. 身体质量指数（BMI）测算

#### 输入格式:

两个数值：体重（以千克为单位），身高(以米为单位），数值间以空格分隔。例如：65.5 1.75。

注意：体重的世界纪录是727公斤，身高的世界纪录是2.72米。输入数据上限不得超过纪录，下限不得小于等于0；

#### 输出格式:

输入数值超出范围            ：输出“input out of range”。例如：-2 3或者125 5。

BMI小于18.5                   ：输出“thin”。

BMI大于等于18.5小于24 ：输出“fit”。

BMI大于等于24小于28    ：输出“overweight”。

BMII大于等于28              ：输出“fat”。

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextDouble()) {
            double weight = sc.nextDouble();
            double height = sc.nextDouble();
            if (weight <= 0 || weight > 727 || height <= 0 || height > 2.72) {
                System.out.println("input out of range");
                continue;
            }
            double BMI = weight / Math.pow(height, 2);
            if (BMI < 18.5) {
                System.out.println("thin");
            } else if (BMI >= 18.5 && BMI < 24) {
                System.out.println("fit");
            } else if (BMI >= 24 && BMI < 28) {
                System.out.println("overweight");
            } else if (BMI >= 28) {
                System.out.println("fat");
            }
        }
    }
}
```

## 11. 消失的车

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for (int i = 1000; i <= 9999; i++) {
            String card = i + "";
            String formertwo = card.substring(0, 2);
            String lattertwo = card.substring(2);
            StringBuilder fr = new StringBuilder(formertwo);
            StringBuilder lt = new StringBuilder(lattertwo);
            if (formertwo.equals(fr.reverse().toString()) && lattertwo.equals(lt.reverse().toString()) && !formertwo.equals(lattertwo)) {
                for (int j = 1; j < 100; j++) {
                    int num = j * j;
                    if (Integer.parseInt(card) == num) {
                        System.out.println("车牌号码是" + num);
                    }

                }
            }
        }
    }
}
```

## 12. 判断回文

输入一个以回车符为结束标志的字符串（少于80个字符），判断该字符串是否为回文。

回文就是字符串中心对称，如“abcba”、“abccba”是回文，“abcdba”不是回文。

#### 输入格式:

输入一个以回车符为结束标志的字符串（少于80个字符）

#### 输出格式:

为回文，输出yes; 非回文，输出no，注意输出的结果后面有回车符

#### 输入样例:

代码段

```
abccba
```

#### 输出样例:

代码段

```
yes
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        StringBuilder re = new StringBuilder(str);
        if (str.equals(re.reverse().toString())) {
            System.out.println("yes");
        } else {
            System.out.println("no");
        }
    }
}
```

## 13. 我是升旗手

#### 输入格式:

输入包括两行。 第一行:包括一个整数n，表示班级里共有n位同学。 第二行:包含n个三位数，表示每一位同学的身高。

#### 输出格式:

输出身高最高的同学的身高。

#### 输入样例:

代码段

```
4
130 125 129 140
```

#### 输出样例:

代码段

```
140
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int height[] = new int[n];
        for (int i = 0; i < n; i++) {
            height[i] = sc.nextInt();
        }
        int max = 0;
        for (int i = 0; i < height.length; i++) {
            if (height[i] > max) {
                max = height[i];
            }
        }
        System.out.println(max);
    }
}
```

## 14. 兔子繁殖问题

已知有一对兔子，每个月可以生一对兔子，而小兔子一个月后又可以生一对小兔子(比如:2月份出生的小兔子4月份可以生育)。也就是说，兔子的对数为：第一个月1对，第二个月2对，第三个月3对，第四个月5对.....假设兔子的生育期为两年，且不死。那么问题来了，你能说出每个月的兔子数么?

#### 输入格式:

输入一个数n，表示第n个月，1<=n<=24。

#### 输出格式:

输出这个月兔子的数目。

#### 输入样例:

代码段

```
4
```

#### 输出样例:

代码段

```
5
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int first = 1;
        int second = 2;
        int current = 0;
        if (n == 1) {
            current = first;
        } else if (n == 2) {
            current = second;
        } else {
            for (int i = 3; i <= n; i++) {
                current = first + second;
                first = second;
                second = current;
            }
        }
        System.out.println(current);
    }
}
```

## 15. 西安距离

小明来到了古都西安，想去参观大唐西市！

西安的道路可以看做是与x轴或y轴垂直的直线，小明位于(a,b)，而目的地位于(c,d)，问最少几步可以到达。

#### 输入格式:

一行中四个整数，a,b,c,d，表示坐标为(a,b)与(c,d)，这里0<=a,b,c,d<=1000

#### 输出格式:

输出这两个点的西安距离。

#### 输入样例:

代码段

```
0 0 3 4
```

#### 输出样例:

代码段

```
7
```

### 参考代码

Java

```
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int d = sc.nextInt();
		System.out.println(Math.abs(c-a)+Math.abs(d-b));
	}
}
```

## 16. 构造方法与初始化块

### 1.定义一个Person类

属性：String name, boolean gender, int age, int id ,所有的变量必须为私有(private)。

无参构造函数:Person(), 功能：打印This is constructor 。

有参构造函数:Person(name, gender, age)   ，**功能：**给属性赋值。

### 2.定义类的初始化块

为Person类加入**初始化块**，在初始化块中对`id`属性赋值，并且要保证每次的值比上次创建的对象的值`+1`。然后在下一行打印`This is initialization block, id is ...`  其中`...`是id的值。

### 3.编写静态初始化块

打印`This is static initialization block`

### 4.编写main方法

- 首先输入n，代表要创建的对象数量。
- 然后从控制台分别读取n行的`name age gender`, 并调用有参构造函数`Person(name, age, gender)`新建对象 。
- 将创建好的n个对象逆序输出(即输出`toString()`方法)。
- 使用无参构造函数新建一个Person对象，然后直接打印该对象。

#### 输入样例:

代码段

```
3
a 11 false
b 12 true
c 10 false
```

#### 输出样例:

代码段

```
This is static initialization block
This is initialization block, id is 0
This is initialization block, id is 1
This is initialization block, id is 2
Person [name=c, age=10, gender=false, id=2]
Person [name=b, age=12, gender=true, id=1]
Person [name=a, age=11, gender=false, id=0]
This is initialization block, id is 3
This is constructor
null,0,false,3
Person [name=null, age=0, gender=false, id=3]
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        Person[] ps = new Person[n];
        for (int i = 0; i < n; i++) {
             String name = sc.next();
            int age = sc.nextInt();
            boolean gender = sc.nextBoolean();
            ps[i] = new Person(name, age, gender);
        }
        for (int i = ps.length - 1; i >= 0; i--) {
            System.out.println(ps[i]);
        }
        Person person = new Person();
        System.out.println(person.getName() + "," + person.getAge() + "," + person.isGender() + "," + person.getNid());
        System.out.println(person);
    }
}

class Person {
    private String name;
    private int age;
    private boolean gender;
    private int id;
    private static int nid = 0;

    static {
        System.out.println("This is static initialization block");
    }

    public Person() {
        super();
        this.id = nid;
        System.out.println("This is initialization block, id is " + nid);
        System.out.println("This is constructor");
    }

    public Person(String name, int age, boolean gender) {
        super();
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.id = nid;
        System.out.println("This is initialization block, id is " + nid);
        nid += 1;
    }
}
```

## 17. 打球过程

利用模板方法来构造相关类实现下述过程：

各种球类的玩法虽然不同，但是球类比赛的过程是类似的，都包含如下几个步骤：

1球员报道-->2比赛开始-->3比赛-->4比赛结束-->5公布比赛成绩。

在main函数中，读入整数i，如果为1，则构造一个足球比赛过程，如果为2则构造一个篮球比赛过程，打印比赛过程。

#### 输入格式:

比赛类型 比分

#### 输出格式:

比赛过程信息

#### 输入样例:

代码段

```
1 2-3
```

#### 输出样例:

代码段

```
now checking in
now starting
now playing football
now ending
now annoucing result: 2-3
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int type = sc.nextInt();
        String res = sc.next();
        if (type == 1) {
            System.out.println("now checking in");
            System.out.println("now starting");
            System.out.println("now playing football");
            System.out.println("now ending");
            System.out.println("now annoucing result: " + res);

        } else if (type == 2) {
            System.out.println("now checking in");
            System.out.println("now starting");
            System.out.println("now playing basketball");
            System.out.println("now ending");
            System.out.println("now annoucing result: " + res);
        }
    }
}
```

## 18. 谁是最强的女汉子

给大家两个属性，一个是漂亮值x，一个是力量值y。当然x的值越大，就代表这个女生就越漂亮。现在想让你求出来最不漂亮的女生有多少个，她们的力量和是多少。

#### 输入格式:

先输入一个T，代表有T个人（T<10000）。

接下来T行，每行有两个数字x,y，分别代表这个女汉子的漂亮值和力量值（x,y<2*109) 。中间有1个空格分隔。

#### 输出格式:

输出一行，有两个数字，分别代表最强的女汉子的数量，和她们的力量和。中间用1个空格分隔。

#### 输入样例:

代码段

```
5
1 1
2 2
1 4
2 10
10 100
```

#### 输出样例:

代码段

```
2 5
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       int T = sc.nextInt();
         int count = 0;
         int strength = 0;
         int min_x = 0;
       for (int i = 0; i < T; i++) {
          int x = sc.nextInt();
          int y = sc.nextInt();
          if(i==0) {
             min_x = x;
          }
          if(x<min_x) {
             min_x = x;
             count=1;
             strength=y;
          }else if (x==min_x) {
             min_x = x;
             count+=1;
             strength+=y;
          }
       }
       System.out.println(count+" "+strength);
    }
}
```

## 19. 身份证排序

1. 输入n，然后连续输入n个身份证号。

2. 然后根据输入的是sort1还是sort2，执行不同的功能。输入的不是sort1或sort2，则输出exit并退出。

   输入sort1，将每个身份证的年月日抽取出来，按年-月-日格式组装，然后对组装后的年-月-日升序输出。

   输入sort2，将所有身份证按照里面的年月日升序输出。

#### 输入样例:

代码段

```
  6
  410425198309308225
  320203197206115011
  431227196108033146
  330226196605054190
  34080019810819327X
  320111197112301539
  sort1
  sort2
  e
```

#### 输出样例:

代码段

```
1961-08-03
1966-05-05
1971-12-30
1972-06-11
1981-08-19
1983-09-30
431227196108033146
330226196605054190
320111197112301539
320203197206115011
34080019810819327X
410425198309308225
exit
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        String ID[] = new String[n];
        for (int i = 0; i < n; i++) {
            ID[i] = sc.nextLine();
        }
        ArrayList<String> birthList = new ArrayList<String>();
        while (sc.hasNextLine()) {
            String type = sc.nextLine();
            if (type.equals("sort1")) {
                for (String id : ID) {
                    String year = id.substring(6, 10);
                    String month = id.substring(10, 12);
                    String day = id.substring(12, 14);
                    String birthformat = year + "-" + month + "-" + day;
                    birthList.add(birthformat);
                }
                Collections.sort(birthList);
                for (String b : birthList) {
                    System.out.println(b);
                }
            } else if (type.equals("sort2")) {
                Arrays.sort(ID, new Comparator<String>() {
                    @Override
                    public int compare(String o1, String o2) {
                        String birth1 = o1.substring(6, 14);
                        String birth2 = o2.substring(6, 14);
                        return birth1.compareTo(birth2);
                    }
                });
                for (String a : ID) {
                    System.out.println(a);
                }
            } else {
                System.out.println("exit");
                break;
            }
        }
    }
}
```

## 20. 找出最长的单词

找出长度最长的单词（不同长度的单词只出现一次）。

#### 输入格式:

输入格式为单行形式，单词之间使用空格分割。

#### 输出格式:

输出格式为长度最长的一个单词。

#### 输入样例:

代码段

```
an not need happy suggest
```

#### 输出样例:

代码段

```
suggest
```

### 参考代码

Java

```
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String[] words = input.split("\\s+");

        String longestword = "";
        for (String word : words) {
            if (word.length() > longestword.length()) {
                longestword = word;
            }
        }
        System.out.println(longestword);
    }
}
```

## 21. 统计一段文字中的单词个数并按单词的字母顺序排序后输出

现需要统计若干段文字(英文)中的不同单词数量。

如果不同的单词数量不超过10个，则将所有单词输出(按字母顺序)，否则输出前10个单词。

### 输入样例

代码段

```
Failure is probably the fortification in your pole
It is like a peek your wallet as the thief when you
are thinking how to spend several hard-won lepta
when you Are wondering whether new money it has laid
background Because of you, then at the heart of the
most lax alert and most low awareness and left it
godsend failed
!!!!!
```

### 输出样例

代码段

```
49
Are
Because
Failure
It
a
alert
and
are
as
at
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Set<String> wordsSet = new HashSet<>();

        // 读取输入直到遇到 !!!!!
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine().trim();

            if (line.equals("!!!!!")) {
                break;
            }
            if (line.isEmpty()) {
                continue;
            }
            String[] words = line.split("\\s+");
            for (String word : words) {
                if (!word.isEmpty()) {
                    wordsSet.add(word);
                }
            }
        }
        List<String> wordsList = new ArrayList<>(wordsSet);
        Collections.sort(wordsList);

        System.out.println(wordsList.size());

        int count = Math.min(10, wordsList.size());
        for (int i = 0; i < count; i++) {
            System.out.println(wordsList.get(i));
        }
    }
}
```

## 22. 统计一篇英文文章中出现的不重复单词的个数

输入一篇英文文章，碰到"!!!!!"的时候停止，输出文章中出现的不重复单词的个数(注意：单词不区分大小写，如：The和the为一个单词)

#### 输入格式:

一篇英文文章，以"!!!!!"结尾

#### 输出格式:

不重复单词的个数

#### 输入样例:

代码段

```
Unmanned aerial vehicles have been adopted in the inspection of violations Procurators will file public interest litigations against perpetrators who will need to replant trees take down illegal buildings control pollution and compensate environment-related losses  
The Yellow River is the second longest river in China It originates in the northwestern province of Qinghai and runs through nine provinces and autonomous regions in western central north and eastern China  
!!!!!
```

#### 输出样例:

代码段

```
55
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<String>();
        String b;
        while (!"!!!!!".equals(b = sc.next().toLowerCase())) {
            list.add(b);
        }
        list = new ArrayList<String>(new HashSet<String>(list));

        System.out.println(list.size());
    }
}
```

## 23. 打印“杨辉三角“ 品中国数学史 增民族自豪感（1）

#### 输入格式:

欲打印杨辉三角的行数n（1<=n<=13)。

#### 输出格式:

每个数字占据4个字符的位置，数字左对齐，数字不足4位的右边留出空格。

#### 输入样例:

代码段

```
13
```

#### 输出样例:

代码段

```
1   
1   1   
1   2   1   
1   3   3   1   
1   4   6   4   1   
1   5   10  10  5   1   
1   6   15  20  15  6   1   
1   7   21  35  35  21  7   1   
1   8   28  56  70  56  28  8   1   
1   9   36  84  126 126 84  36  9   1   
1   10  45  120 210 252 210 120 45  10  1   
1   11  55  165 330 462 462 330 165 55  11  1   
1   12  66  220 495 792 924 792 495 220 66  12  1   
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        //构建二维数组
        int[][] a = new int[n][n];
        int i, j;
        //下三角
        for (i = 0; i < n; i++) {
            for (j = 0; j <= i; j++) {
                if (j == 0 || i == j) {
                    a[i][j] = 1;
                } else {
                    a[i][j] = a[i - 1][j] + a[i - 1][j - 1];
                }
            }
        }
        //输出
        for (i = 0; i < a.length; i++) {
            for (j = 0; j <= i; j++) {
                System.out.printf("%-4d", a[i][j]);
            }
            System.out.println();
        }
    }
}
```

## 24. 找到出勤最多的人--难难难！！！！！！！！

根据教师的花名册，找到出勤最多的人。

#### 输入格式:

出勤记录单行给出，数据直接使用空格分割。

#### 输出格式:

单行输出（若有多人，人名直接使用空格分割，结尾处没有空格）。

#### 输入样例:

代码段

```
zs ls ww ml zs ls ml zs ww
```

#### 输出样例:

代码段

```
zs
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextLine()) return; 
        
        String[] records = scanner.nextLine().split("\\s+");

        Map<String, Integer> countMap = new LinkedHashMap<>();
        for (String name : records) {
            countMap.put(name, countMap.getOrDefault(name, 0) + 1);
        }

        int maxCount = Collections.max(countMap.values());

        List<String> result = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : countMap.entrySet()) {
            if (entry.getValue() == maxCount) {
                result.add(entry.getKey());
            }
        }

        System.out.println(String.join(" ", result));
    }
}
```

## 25. 01-接口-Comparable

编写实现**Comparable**接口的`PersonSortable`类，使其按name以及age排序

#### 输入样例:

代码段

```
5
zhang 15
zhang 12
wang 14
Wang 17
li 17
```

#### 输出样例:

代码段

```
Wang-17
li-17
wang-14
zhang-12
zhang-15
// 这行是标识信息，应替换为**2.main方法中**中的第4点要求。
```

### 参考代码

Java

```
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        PersonSortable ps[] = new PersonSortable[n];
        for (int i = 0; i < n; i++) {
            String line = sc.nextLine();
            String[] s = line.split(" ");
            PersonSortable p = new PersonSortable(s[0],Integer.parseInt(s[1]));
            ps[i]=p;
        }
        Arrays.sort(ps);
        for (PersonSortable p : ps) {
            System.out.println(p);
        }
        System.out.println(Arrays.toString(PersonSortable.class.getInterfaces()));
    }

}
class PersonSortable implements Comparable<PersonSortable>{
    private String name;
    private int age;

    public PersonSortable() {

    }

    public PersonSortable(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return name+"-"+age;
    }

    @Override
    public int compareTo(PersonSortable o) {
        if(this.name.equals(o.getName())) {
            return this.age - o.getAge();
        }else {
            return this.name.compareTo(o.getName());
        }
    }
}
```

## 26. 02-接口-Comparator

Arrays.sort可以对所有实现Comparable的对象进行排序。但如果有多种排序需求，如有时候需对name进行降序排序，有时候只需要对年龄进行排序。使用Comparable无法满足这样的需求。可以编写不同的`Comparator`来满足多样的排序需求。

#### 输入样例:

代码段

```
5
zhang 15
zhang 12
wang 14
Wang 17
li 17
```

#### 输出样例:

代码段

```
NameComparator:sort
Wang-17
li-17
wang-14
zhang-15
zhang-12
AgeComparator:sort
zhang-12
wang-14
zhang-15
Wang-17
li-17
//最后两行是标识信息
```

### 参考代码

Java

```
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        PersonSortable2 ps[] = new PersonSortable2[n];
        for (int i = 0; i < n; i++) {
            String line = sc.nextLine();
            String[] s = line.split(" ");
            PersonSortable2 p = new PersonSortable2(s[0], Integer.parseInt(s[1]));
            ps[i] = p;
        }
        System.out.println("NameComparator:sort");
        Arrays.sort(ps, new NameComparator());
        for (PersonSortable2 p : ps) {
            System.out.println(p);
        }
        System.out.println("AgeComparator:sort");
        Arrays.sort(ps, new AgeComparator());
        for (PersonSortable2 p : ps) {
            System.out.println(p);
        }
        System.out.println(Arrays.toString(NameComparator.class.getInterfaces()));
        System.out.println(Arrays.toString(AgeComparator.class.getInterfaces()));


    }
}

class PersonSortable2 {
    private String name;
    private int age;

    public PersonSortable2() {
    }

    public PersonSortable2(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return name + "-" + age;
    }
}

class NameComparator implements Comparator<PersonSortable2> {

    @Override
    public int compare(PersonSortable2 o1, PersonSortable2 o2) {
        return o1.getName().compareTo(o2.getName());
    }
}

class AgeComparator implements Comparator<PersonSortable2> {

    @Override
    public int compare(PersonSortable2 o1, PersonSortable2 o2) {
        return o1.getAge() - o2.getAge();
    }
}
```

## 27. 使用异常机制处理异常输入

使用异常处理输入机制，让程序变得更健壮。

#### 输入样例：

代码段

```
5
1
2
a
b
4
5
3
```

#### 输出样例：

代码段

```
java.lang.NumberFormatException: For input string: "a"
java.lang.NumberFormatException: For input string: "b"
[1, 2, 4, 5, 3]
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // 1. 读取数组大小
        int n = sc.nextInt();
        int[] num = new int[n];

        // 2. 循环读取数组元素
        for (int i = 0; i < n; i++) {
            String str = sc.next(); // 优化：使用 next() 读取下一个标记，避免换行符问题
            
            try {
                // 尝试将字符串转换为整数
                num[i] = Integer.parseInt(str); 
            } catch (NumberFormatException e) {
                // 捕获转换异常
                System.out.println(e);
                i--; // 核心：下标回退，强制重新输入当前位置
            }
        }
        
        // 3. 输出结果
        System.out.println(Arrays.toString(num));
    }
}
```

## 28. 成绩录入时的及格与不及格人数统计

编写一个程序进行一个班某门课程成绩的录入，能够控制录入成绩总人数，对录入成绩统计其及格人数和不及格人数。设计一个异常类，当输入的成绩小0分或大于100分时，抛出该异常类对象，程序将捕捉这个异常对象，并调用执行该异常类对象的toString（）方法，该方法获取当前无效分数值，并返回一个此分数无效的字符串。

#### 输入样例:

代码段

```
3
100
30
60
```

#### 输出样例:

代码段

```
2
1
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int pass = 0;
        for (int i = 0; i < n; i++) {
            int score = sc.nextInt();
            if (score < 0 || score > 100) {
                System.out.println(score + "invalid!");
                i--;
            }
            if (score >= 60 && score <= 100) {
                pass++;
            }
        }
        System.out.println(pass);
        System.out.println(n - pass);
    }
}
```

## 29. 快递计价器

1、抽象快递类Express，其包含一个属性int weight表示快递重量（单位为kg），一个方法getWeight()用于返回快递重量和一个抽象方法getTotal()用于计算快递运费。

2、两个类继承Express，分别是：

（a）顺路快递SLExpress：计价规则为首重(1kg)12元，每增加1kg费用加2元。

（b）地地快递DDExpress：计价规则为首重(1kg)5元，每增加1kg费用加1元。

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
          Scanner sc = new Scanner(System.in);
          int n = sc.nextInt();

          sc.nextLine();
          int total = 0;
          while (sc.hasNextLine()) {
              String line = sc.nextLine();
              String[] s = line.split(" ");
              if (s[0].equals("SL")) {
                  SLExpress sl = new SLExpress(Integer.parseInt(s[1]));
                  total += sl.getTotal();
              } else if (s[0].equals("DD")) {
                  DDExpress dd = new DDExpress(Integer.parseInt(s[1]));
                  total += dd.getTotal();
              } else {
                  break;
              }

          }
          System.out.println(total);
      }
}

abstract class Express {
    int weight;
    public Express() { super(); }
    public Express(int weight) { super(); this.weight = weight; }
    public abstract int getTotal();
}

class SLExpress extends Express {
    public SLExpress(int weight) { super(weight); }

    @Override
    public int getTotal() {
        if (weight == 1) { return 12; } 
        else { return 12 + (weight - 1) * 2; }
    }
}

class DDExpress extends Express {
    public DDExpress(int weight) { super(weight); }

    @Override
    public int getTotal() {
        if (weight == 1) { return 5; } 
        else { return 5 + (weight - 1) * 1; }
    }
}
```

## 30. 答答租车系统

各位面向对象的小伙伴们，在学习了面向对象的核心概念——类的封装、继承、多态之后，答答租车系统开始营运了。请你充分利用面向对象思想，为公司解决智能租车问题，根据客户选定的车型和租车天数，来计算租车费用，最大载客人数，最大载载重量。

#### 输入样例:

代码段

```
1
2
1 1
2 2
```

#### 输出样例:

代码段

```
15 0.00 1600
```

### 参考代码

Java

```
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 1. 初始化车辆数据 (相当于数据库或菜单)
        // 数组下标 0 对应 序号 1 的车，以此类推
        Car[] garage = {
            new Car(5, 0, 800),    // 1. A
            new Car(5, 0, 400),    // 2. B
            new Car(5, 0, 800),    // 3. C
            new Car(51, 0, 1300),  // 4. D
            new Car(55, 0, 1500),  // 5. E
            new Car(5, 0.45, 500), // 6. F
            new Car(5, 2.0, 450),  // 7. G
            new Car(0, 3, 200),    // 8. H
            new Car(0, 25, 1500),  // 9. I
            new Car(0, 35, 2000)   // 10. J
        };

        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int isRent = sc.nextInt();
            if (isRent != 1) {
                System.out.println("0 0.00 0");
                return;
            }
        }

        int n = sc.nextInt(); 
        
        int totalPerson = 0;
        double totalCargo = 0.0;
        int totalMoney = 0;

        for (int i = 0; i < n; i++) {
            int carId = sc.nextInt(); 
            int days = sc.nextInt();  
            Car selectedCar = garage[carId - 1];
            totalPerson += selectedCar.person * days;
            totalCargo += selectedCar.cargo * days;
            totalMoney += selectedCar.price * days;
        }

        System.out.printf("%d %.2f %d", totalPerson, totalCargo, totalMoney);
    }
}

class Car {
    int person;     
    double cargo;   
    int price;      

    public Car(int person, double cargo, int price) {
        this.person = person;
        this.cargo = cargo;
        this.price = price;
    }
}
```

## 31. 读中国载人航天史，汇航天员数量，向航天员致敬（1）

会编程的小伙伴们，请以他们出征太空的先后顺序，统计一下航天英雄们出征太空的次数，以实际行动向航天员们致敬！

#### 输入样例:

代码段

```
杨利伟
费俊龙 聂海胜
翟志刚 景海鹏 刘伯明
景海鹏 刘旺 刘洋
聂海胜 张晓光 王亚平
景海鹏 陈东
end
```

#### 输出样例:

代码段

```
杨利伟 1
费俊龙 1
聂海胜 2
翟志刚 1
景海鹏 3
刘伯明 1
刘旺 1
刘洋 1
张晓光 1
王亚平 1
陈东 1
```

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String name = null;
        Map<String, Integer> map = new LinkedHashMap<String, Integer>();
        while (sc.hasNext()) {
            name = sc.next();
            if (name.equals("end"))
                break;
            map.put(name, map.getOrDefault(name, 0) + 1);
        }
        for (String name1 : map.keySet()) {
            System.out.println(name1 + " " + map.get(name1));
        }
    }
}
```

## 32. 成绩异常（ScoreException）

自定义一个异常类ScoreException，继承自Exception类。

定义一个学生类Student，有一个私有成员变量score。当设置的成绩为负数或超过100时，会抛出一个异常对象。

在测试类Main中，创建一个Student类的对象，尝试调用setScore()方法来设置他的成绩，使用try...catch...finally语句实现上述功能。

#### 输入样例1:

代码段

```
-20
```

#### 输出样例1:

代码段

```
您输入的成绩异常，请核实！
程序结束
```

### 参考代码

Java

```
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Student zhangsan = new Student();
        try {
            double inputScore = scanner.nextDouble();
            zhangsan.setScore(inputScore);
            System.out.println("成绩为" + zhangsan.getScore());
        } catch (ScoreException e) {
            e.show();
        } finally {
            System.out.println("程序结束");
        }
    }
}

class Student {
    private double score;
    public void setScore(double score) throws ScoreException {
          if (score < 0 || score > 100) {
              throw new ScoreException();
          }
          this.score = score;
      }
    public double getScore() {
        return score;
    }
}

class ScoreException extends Exception {
    private String message;
    public ScoreException() {
        this.message = "您输入的成绩异常，请核实！";
    }
    public void show() {
        System.out.println(message);
    }
}
```

## 33. 超载异常（OverLoadException）

自定义一个异常类OverLoadException（超载异常）。

定义一个类CargoShip（货船）。

在测试类Main中，定义一个CargoShip类的对象myship，从键盘输入一个数，用于设置其最大装载量。从键盘再输入两个数，作为两个集装箱的重量，尝试将这两个集装箱按输入时的顺序先后装上货船，该操作有可能捕捉到超载异常。

#### 输入样例1:

代码段

```
500
200 380
```

#### 输出样例1:

代码段

```
目前共装载了200.0吨货物
无法再装载重量是380.0吨的集装箱
货船将正点起航
```

### 参考代码

Java

```
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        CargoShip myship = new CargoShip();
        double maxW = scanner.nextDouble();
        myship.setMaxWeight(maxW);
        double w1 = scanner.nextDouble();
        double w2 = scanner.nextDouble();
        try {
            myship.loading(w1);
            myship.loading(w2);
        } catch (OverLoadException e) {
            e.showMessage();
        } finally {
            System.out.println("货船将正点起航");
        }
    }
}

class OverLoadException extends Exception {
    public String message;
    public OverLoadException(double n) {
        this.message = "无法再装载重量是" + n + "吨的集装箱";
    }
    public void showMessage() {
        System.out.println(message);
    }
}

class CargoShip {
    public double actualWeight = 0; 
    public double maxWeight;

    public void setMaxWeight(double maxWeight) {
        this.maxWeight = maxWeight;
    }

    public void loading(double weight) throws OverLoadException {
        if (actualWeight + weight > maxWeight) {
            throw new OverLoadException(weight);
        } else {
            actualWeight += weight;
            System.out.println("目前共装载了" + actualWeight + "吨货物");
        }
    }
}
```

## 34. 异常处理

从键盘输入一个整形数n，如果输入正确的话，输出10-n后的值，如果输入错误的话输出“not int”最后输出end。

#### 输入样例:

代码段

```
5
```

#### 输出样例:

代码段

```
5
end
```

### 参考代码

Java

```
import java.util.Scanner;
import java.util.InputMismatchException;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            int n = scanner.nextInt();
            System.out.println(10 - n);
        } catch (InputMismatchException e) {
            System.out.println("not int");
        } finally {
            System.out.println("end");
        }
    }
}
```

## 附加：天不假年--可不看

### 参考代码

Java

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int age;
        age = in.nextInt();
        Person p = new Person(age);
        age = in.nextInt();
        try {
            p.setAge(age);
            System.out.println("A");
        } catch (AgeException e) {
            System.out.println("B");
        }
    }
}

class Person {
    int age;
    public Person(int age) {
        this.age = age;
    }
    public void setAge(int age) throws AgeException {
        if (this.age <= age) {
            this.age = age;
        } else {
            throw new AgeException();
        }
    }
}

class AgeException extends Exception {
}
```