[回到目录](../../README.md)
---

# 《Python编程：从入门到实践》
学习笔记从第八章函数开始

事先说明:
**继承前的例子是用Python2.7编译的**,写的时候我自己也没注意。。。。后来才意识到

---

- [函数](#函数)
    - [规范](#规范)
    - [传递参数](#传递参数)
        - [默认值](#默认值)
        - [title()](#title)
        - [实现实参可选](#实现实参可选)
    - [传递列表](#传递列表)
        - [禁止函数修改列表](#禁止函数修改列表)
        - [传递任意数量的实参](#传递任意数量的实参)
        - [使用任意数量的关键字实参](#使用任意数量的关键字实参)
    - [将函数存储在模块中](#将函数存储在模块中)
        - [导入整个模块](#导入整个模块)
        - [导入特定函数](#导入特定函数)
        - [使用as给函数指定别名](#用as给函数指定别名)
        - [使用as给模块指定别名](#用as给模块指定别名)
        - [导入模块中的所有函数](#导入模块中的所有函数)
    - [函数编写指南](#函数编写指南)
- [类](#类)
    - [创建类和使用类](#创建类和使用类)
        - [创建类](#创建类)
        - [根据类创建实例](#根据类创建实例)
        - [访问属性](#访问属性)
        - [调用方法](#调用方法)
        - [创建多个实例](#创建多个实例)
    - [使用类和实例](#使用类和实例)
        - [car类](#car类)
        - [给属性指定默认值](#给属性指定默认值)
        - [修改属性的值](#修改属性的值)
            - [1、直接通过实例进行修改](#直接通过实例进行修改)
            - [2、通过方法进行设置](#通过方法进行设置)
            - [3、通过方法进行递增](#通过方法进行递增)
    - [继承](#继承)
        - [子类的方法__init__()](#子类的方法)
        - [给子类定义属性和方法](#给子类定义属性和方法)
        - [重写父类的方法](#重写父类的方法)
        - [将实例用作属性](#将实例用作属性)
        - [模拟实物](#模拟实物)
    - [导入类](#导入类)
        - [导入单个类](#导入单个类)
        - [在一个模块中存储多个类，从一个模块导入多个类](#在一个模块中存储多个类，从一个模块导入多个类)
        - [导入整个模块](#导入整个模块)
        - [导入模块中的所有类](#导入模块中的所有类)
        - [在一个模块中导入另一个模块](#在一个模块中导入另一个模块)
        - [自定义工作流程](#自定义工作流程)
    - [Python标准库](#Python标准库)
    - [类编码风格](#类编码风格)
    - [类_小结](#类_小结)
- [文件和异常](#文件和异常)
    - [从文件中读取数据](#从文件中读取数据)
        - [读取整个文件](#读取整个文件)
        - [文件路径](#文件路径)
        - [逐行读取](#逐行读取)
        - [创建一个包含文件各行内容的列表](#创建一个包含文件各行内容的列表)
        - [使用文件的内容](#使用文件的内容)
        - [包含一百万位的大型文件](#包含一百万位的大型文件)
        - [圆周率值中包含你的生日吗](#圆周率值中包含你的生日吗)
        - [读取文件小结](#读取文件小结)
    - [写入文件](#写入文件)
        - [写入空文件](#写入空文件)
        - [写入多行](#写入多行)
        - [附加到文件](#附加到文件)
    - [异常](#异常)
        - [处理ZeroDivisionError异常](#处理ZeroDivisionError异常)
        - [使用try--except代码块](#使用try--except代码块)
        - [使用异常避免崩溃](#使用异常避免崩溃)
        - [else代码块](#else代码块)
        - [处理FileNotFoundError异常](#处理FileNotFoundError异常)
        - [分析文本](#分析文本)
        - [使用多个文件](#使用多个文件)
        - [失败时一声不吭](#失败时一声不吭)
        - [决定报告哪些错误](#决定报告哪些错误)
    - [存储数据](#存储数据)
        - [使用json.dump()和json.load()](#使用json.dump()和json.load())
        - [保存和读取用户生成的数据](#保存和读取用户生成的数据)
        - [重构](#重构)
    - [文件与异常小结](#文件与异常小结)
- [测试代码](#测试代码)
    - [测试函数](#测试函数)
        - [单元测试和测试用例](#单元测试和测试用例)
        - [可通过的测试](#可通过的测试)
        - [不能通过的测试](#不能通过的测试)
        - [测试未通过时怎么办](#测试未通过时怎么办)
        - [添加新测试](#添加新测试)
    - [测试类](#测试类)
        - [各种断言方法](#各种断言方法)
        - [一个要测试的类](#一个要测试的类)
        - [测试AnonymousSurvey类](#测试AnonymousSurvey类)
        - [方法setUp()](#方法setUp())
    - [测试代码小结](#测试代码小结)
- [项目篇](#项目篇)
    - [在OSX系统中安装Pygame](#在OSX系统中安装Pygame)
        
        
        


---
<a id = "函数"></a>
## 函数

---

<a id = "规范"></a>
### 规范：

函数名底下用三个单引号的注释，告知看源码的人该函数的作用。

```
def favoriate_book(title):
    '''显示最喜欢的书籍的函数！'''
    print "One of my favoriate book is %s!" %title
```

当然，还可以在程序段任意位置加入注释以让浏览你程序的人更快速明白你的意图。


---
<a id = "传递参数"></a>
### 传递参数

<a id = "默认值"></a>
#### 默认值：

定义函数的时候，可以给每个形参指定默认值。当我们给实参的时候，函数将使用指定的实参，当我们不给实参的时候，函数使用默认值。

**注意**：

使用默认值时，在形参列表中必须**先列出没有默认值的形参，再列出有默认值的实参**。比如：

```
def animals(a_name, a_type = "dog"):
    '''显示宠物信息'''
    print "I have a " + a_type + ", It name is " + a_name +"!"

animals("cat","dada")
animals("duo")
```


<a id ="title"></a>
#### title()

处理首字母大写，字符串可以调用。


<a id = "实现实参可选"></a>
#### 实现实参可选

可以用**空字符**实现实参可选，比如：

```
def get_format_name(first_name, last_name, middle_name = ""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_format_name("little1","little2")
print musician

musician = get_format_name("big1","big2","big3")
print musician
```

---
<a id = "传递列表"></a>
### 传递列表

<a id = "禁止函数修改列表"></a>
#### 禁止函数修改列表

将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的，这让你能够高效地处理大量的数据。

若要禁止，可以利用**切片技巧**：
**切片表示法`[:]`创建列表的副本**。比如：

```
names = ["aaaaaa","bbbbb","ccccc"]
def list_exampla(names,ages):
    '''处理姓名和年龄列表'''
    for name in names:
        names.pop()
        print names
    print "this is a example!"
list_exampla(names[:],18)
print names
```

这个函数处理的就是names这个列表的副本，而不是names列表的本身。

**注意：**

虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由需要传递副本，
否则还是应该将原始列表传递给函数，因为让函数使用现成列表可避免花时间和内存创
建副本，从而提高效率，在处理大型列表时尤其如此。


<a id = "传递任意数量的实参" ></a>
#### 传递任意数量的实参

若你预先不知道函数将会处理多少实参，Python的函数调用可以收集任意数量的实参来满足这种需求。比如：

```
def make_pizza(*toppings):
    print toppings
make_pizza("a")
make_pizza("b","c")
```

形参名`*toppings`中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中。

函数体内的print语句通过生成输出来证明Python能够处理 使用一个值调用函数的情形，也能处理使用三个值来调用函数的情形。

它以类似的方式处理不同的调用，注意，Python将实参封装到一个**元组**中，即便函数只收到一个值也如此，会输出这样：
```
('a',)
('b', 'c')
```

我们可以配合for语句进行遍历输出，但注意生成元组时是无序的。


<a id = "使用任意数量的关键字实参"></a>
#### 使用任意数量的关键字实参

有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。

在这种情况下，可将函数编写成能够接受**任意数量的键—值对**——调用语句提供了多少就接受多少。

一个这样的示例是创建用户简介:你知道你将收到有关用户的信息，但不确定会是什么样的信息。
在下面的示例中，函数接受名和姓，同时还接受**任意数量**的关键字实参:

```
def build_profile(first,last,**user_info):
    '''创建字典，包含用户信息！'''
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile("aaaa","bbbb",gender = "male",age = "18")
print user_profile
```

函数的定义要求提供名和姓，同时允许用户根据需要提供任意数量的名称—值对。

形参`**user_info`中的两个星号让Python创建一个名为user_info的空字典，并将收到的所有名称—值对都封装到这个字典中。

在这个函数中，可以像访问其他字典那样访问user_info中的名称—值对。

以上例子打印结果为：
```
{'gender': 'male', 'first_name': 'aaaa', 'last_name': 'bbbb', 'age': '18'}
```

编写函数时，你可以以各种方式混合使用位置实参、关键字实参和任意数量的实参。
知道这些实参类型大有裨益，因为阅读别人编写的代码时经常会见到它们。
要正确地使用这些类型的实参并知道它们的使用时机，需要经过一定的练习。

---
<a id = "将函数存储在模块中"></a>
### 将函数存储在模块中 

函数的优点之一是，使用它们可将代码块与主程序分离。

通过给函数指定描述性名称，可让主程序容易理解得多。你还可以更进一步，将函数存储在被称为模块的独立文件中，再将模块导入到主程序中。
`import`语句允许在当前运行的程序文件中使用模块中的代码。

通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。这还能让你在众多不同的程序中重用函数。

将函数存储在独立文件中后，可与其他程序员共享这些文件而不是整个程序。知道如何导入函数还能让你使用其他程序员编写的函数库。

<a id ="导入整个模块"></a>
#### 导入整个模块

比如你在`test.py`这个文件里写python程序，你想保证你这个文件里的代码简洁清晰，想把函数写在另一个文件里，这是可以的。
最简单初始的方法就是整体导入。

1. 在与`test.py`**相同的文件夹(同一目录)**里创建一个python文件（后缀为py的文件），用于写函数。

2. 比如你这个用于写函数的文件名称为`testFun.py`，你在里面定义了这样一个函数：
```
def test_print(some_message):
    '''打印传入的信息'''
    print some_message 
```

3. 导入整个模块的方法是，你在`test.py`文件中用整体导入语句：
```
import testFun #使用需要导入的文件名，进行整体导入
testFun.test_print("abc") #直接用导入的文件名，然后点语法+函数名就可直接使用。
```

<a id ="导入特定函数"></a>
#### 导入特定函数

* 方法是使用这样形式的语句：`from module_name import function_name`

还拿上面的例子说，我先把`testFun.py`文件加一个函数：
```
def test_print(some_message):
    '''打印传入的信息'''
    print some_message
def test_another_print(some_message):
    '''打印另一条传入的信息'''
    print "Another " + some_message
```

这时候你在`test.py`文件中使用上面给出的形式：
```
from testFun import test_another_print #调用testFun模块中的test_another_print
testFun.test_print("abc")  #错误语句
test_another_print("aaaa") #正确语句
```

如果你还留着上面整体导入的调用函数的语句，Python会给你报这样一个错误：
```
NameError: name 'testFun' is not defined
```

意思是testFun这个没有被定义。

或者如果你调用第一个函数：
```
test_print("abc") #这个语句是正确的
```

但它也会给你报错：
```
NameError: name 'test_print' is not defined
```

也是告诉你test_print，没有定义。你会觉得明明在写函数的文件里了啊。

造成这两个问题的原因相同：
**因为这个导入函数的语法只导入特定的函数，只能调用导入的函数，不能使用未导入的函数，
并且只需要函数名即可，也不需要像导入整体一样使用模块名和点语法。**

* 看到这你们也许会有疑问，一次只导入一个函数岂不效率低下？Python是考虑到这个问题的，所以有多函数一起导入的方法：
```
from module_name import function_name1，function_name2, function_name3
```

把函数名用逗号隔开即可。


<a id = "用as给函数指定别名"></a>
#### 使用`as`给函数指定别名

如果要导入的函数的名称**可能与程序中现有的名称冲突**，或者函数的名称太长，可指定简短而独一无二的别名 ——函数的另一个名称，类似于外号。
要给函数指定这种特殊外号，需要在导入它时这样做：
`from module_name import function_name as fn`

这个`fn`就是外号，这时候调用函数的时候使用外号就行。再用上面的例子：
```
from testFun import test_another_print as t_a_p #给函数指定别名t_a_p
t_a_p("aaaaa") #这时别名就生效了
```
这时你再用：`test_another_print（"aaaaa"）`也会报`NameError`的错误。
意味着指定别名之后只能用别名来调用函数。


<a id = "用as给模块指定别名"></a>
#### 使用`as`给模块指定别名

与给函数指定别名类似，只需这个语句即可：
```
import module_name as mn
```

这个mn就是模块的别名，所以这时候与导入整体的调用类似，只不过把模块名称换成别名即可，函数还是用点语法来调用。

**好处**：

这样不仅能使代码更简洁，还可以让你不再关注模块名，而专注于描述性的函数名。
这些函数名明确地指出了函数的功能，对理解代码而言，它们 比模块名更重要。


<a id = "导入模块中所有函数"></a>
#### 导入模块中的所有函数

使用星号`*`运算符可让Python导入模块中的所有函数:
```
from testFun import * #从testFun模块导入所有的函数
```

`import`语句中的星号让Python将模块`testFun`中的每个函数都复制到这个程序文件中。
由于导入了每个函数，可通过**函数名称**来调用每个函数，而**无需使用句点表示法**。

然而，使用并非自己编写的**大型模块**时，最好不要采用这种导入方法。
如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果：
*Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数。*

**最佳**的做法是，要么只导入你**需要使用的函数**，要么导入**整个模块并使用句点表示法**。这能让代码更清晰，更容易阅读和理解。


<a id = "函数编写指南"></a>
### 函数编写指南

* 应给函数指定描述性名称，且只在其中使用小写字母和下划线。描述性名称可帮助你和别人明白代码想要做什么。给模块命名时也应遵循上述约定。

* 每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式。
文档良好的函数让其他程序员只需阅读文档字符串中的描述就能够使用它:
*他们完全可以相信代码如描述的那样运行，只要知道函数的名称、需要的实参以及返回值的类型，就能在自己的程序中使用它。*

* 给形参指定默认值时，等号两边不要有空格:
```
def function_name(parameter_0, parameter_1="default value")
```

* 对于函数调用中的关键字实参，也应遵循这种约定:
```
 function_name(value_0, parameter_1="value")
```

* 如果形参过长，单行放不下，可以灵活的运用回车和空格来把形参放成一种清晰的形式，区分开函数体。比如:
```
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5)：
    function body... 
```

* 如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开，这样将更容易知道前一个函数在什么地方结束，下一个函数从什么地方开始。

* 所有的`import`语句都应放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整个程序。

**简单小结：**

* 函数让你编写代码一次后，想重用它们多少次就重用多少次。需要运行函数中的代码时，只需编写一行函数调用代码，就可让函数完成其工作。
需要修改函数的行为时，只需修改一个代码块，而所做的修改将影响调用这个函数的每个地方。

* 使用函数让程序更容易阅读，而良好的函数名概述了程序各个部分的作用。相对于阅读一系列的代码块，阅读一系列函数调用让你能够更快地明白程序的作用。

* 函数让代码更容易测试和调试。如果程序使用一系列的函数来完成其任务，而其中的每个函数都完成一项具体的工作，测试和维护起来将容易得多：
*你可编写分别调用每个函数的程序，并测试每个函数是否在它可能遇到的各种情形下都能正确地运行。*


---
<a id = "类"></a>
## 类

面向对象编程 是最有效的软件编写方法之一。在面向对象编程中，你编写表示现实世界中的事物和情景的类，并基于这些类来创建对象。
编写类时，你定义一大类对象都有的通用行为。基于类创建对象时，每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独特的个性。

根据类来创建对象被称为实例化 ，这让你能够使用类的实例。你可以指定可在实例中存储什么信息，定义可对这些实例执行哪些操作。
你还可以编写一些类来扩展既有类的功能，让相似的类能够高效地共享代码。

你可以把自己编写的类存储在模块中，并在自己的程序文件中导入其他程序员编写的类。理解面向对象编程有助于你像程序员那样看世界，
还可以帮助你真正明白自己编写的代码，不仅是各行代码的作用，还有代码背后更宏大的概念。
了解类背后的概念可培养逻辑思维，让你能够通过编写程序来解决遇到的几乎任何问题。
类还能让你以及与你合作的其他程序员基于同样的逻辑来编写代码，你们就能明白对方所做的工作。


---
<a id = "创建类和实用类"></a>
### 创建类和使用类

使用类几乎可以模拟任何东西。下面来编写一个表示小狗的简单类，它表示的不是特定的小狗，而是任何小狗。对于大多数宠物狗，我们都知道些什么呢?
它们都有名字 和年龄;我们还知道，大多数小狗还会蹲下和打滚。
由于大多数小狗都具备上述两项信息(名字和年龄)和两种行为(蹲下和打滚)，我们的Dog类将包含它们。这个类让 Python知道如何创建表示小狗的对象。

编写这个类后，我们将**使用**它来创建表示特定小狗的实例。


<a id = "创建类"></a>
#### 创建类

我们以创建一个狗的类为列子，狗狗会有`名字`和`年龄`这**两项信息**，以及`蹲下`和`打滚`这**两项行为**，我们用类来实现它们：
```
class Dog():                         #1、定义类
    '''一次模拟小狗类的尝试'''
    def __init__(self,name,age):     #2、__init__方法
        '''初始化名称和年龄'''
        self.name = name             #3、前缀self
        self.age = age
    
    def sit(self):                   #4、行为方法
        '''模拟小狗被命令时坐下'''
        print self.name.title() + " is now sitting!"
    
    def roll_over(self):
        '''模拟小狗被命令时打滚'''
        print self.name.title() + " is rolled over!"
``` 

解释一下上面的代码：

* `#1`：这一行是定义类的语法。**类名的首字母大写**。空括号可以理解为每次调用类方法从空白地方生成这个类的实例，
但在`Python2.7`的版本中类方法的定义中括号里要写object，这样用：
`class ClassName(object):`。类名语句下方写**注释简单描述类的功能**。

* `#2`：`__init__`方法，`init`的前后**两个下划线**，这个是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。
每当你根据Dog类创建新实例时，Python都会自动运行它。在上面的例子中这个方法有三个形参：`self,name,age`。
在这个方法中，`self`这个形参必不可少，而且必须位于其它形参的前面。
`self`是什么意思呢？书中的解释是：它是一个指向**实例本身**的引用，让实例能够访问类中的**属性和方法**。有点模糊不是么？
现在只是简单地解释一下，这个`self`就等于每次创建的实例。在下一节的[创建实例的地方](#根据类创建实例)做详细的个人理解。
我们将通过实参向`Dog()`传递名字和年龄；`self`会自动传递，因此我们不需要传递它。
每当我们根据类创建实例时，都只需给最后两个形参`(name和age)`提供值。

* `#3`：现在来说说前缀`self`，定义的两个变量都有前缀`self`。
以`self`为前缀的变量都可供类中的所有方法使用(通过点语法，下一节创建实例中会讲到)，我们还可以通过类的任何实例来访问这些变量。
如`self.name = name`获取存储在形参中的值，并将其存储到变量`name`中，然后**该变量被关联到当前创建的实例**，继而变成了每个具体实例的变量。
`self.age = age`的作用与此类似。像这样可**通过实例访问的变量称为属性**。

* `#4`：Dog类还定义了另外两个方法: `sit()`和`roll_over()`。
由于这些方法不需要额外的信息，如名字或年龄，因此它们只有一个形参`self`。我们后面**将创建的实例**能够访问这些方法，换句话说，它们都会蹲下和打滚。
例子中，`sit()`和`roll_over()`所做的有限，它们只是打印一条消息，指出小狗正蹲下或打滚。
但可以扩展这些方法以模拟实际情况:
如果这个类包含在一个计算机游戏中，这些方法将包含创建小狗蹲下和打滚动画效果的代码。
如果这个类是用于控制机器狗的，这些方法将引导机器狗做出蹲下和打滚的动作。


<a  id = "根据类创建实例"></a>
#### 根据类创建实例

可将类视为有关如何创建实例的说明。上一节的类是一系列说明，让Python知道如何创建表示特定小狗的实例。 下面来创建一个表示特定小狗的实例:
```
my_dog = Dog("haha",3)
```

来接着上节解释，我们用`Dog`类创建了一个实例：`my_dog`，这个`my_dog`的实例在创建的时候自动调用`__init__`方法，
把方法中的`self`指向创建的实例`my_dog`，让创建的实例`my_dog`可以用**点**语法**访问属性**和**调用方法**。

也就是说我们用类方法创建任何一个实例的时候，都会把这个实例指向类方法里的`self`，
让这个实例可以用**名称访问**我们创建实例时给每个实例赋予的**属性**，还有**调用**这个类里定义的所有**方法**。


<a id = "访问属性"></a>
#### 访问属性

用类方法创建实例之后我们就可以用**实例的名称**加**点语法**来访问创建实例时赋予它的属性了，我们上面已经赋予了`my_dog`名称和年龄的属性，
下面就是访问的例子。
```
print "My dog's name is " + my_dog.name.title() + "!"
print "My dog's age is " + str(my_dog.age) + " years old!"
```

在控制台输出的结果是：
```
My dog's name is Haha!
My dog's age is 3 years old!
```

引用`name`属性的时候，Python先找到实例`my_dog`，再查找与这个实例相关联的属性`name`。
在`Dog`类中引用这个属性时，使用的都是`__init__`方法中的`self.name`，`age`属性类似，因为`self`会自动关联**实例**。

`title()`让首字母大写，`str（）`把数值转化为字符串类型。


<a id = "调用方法"></a>
#### 调用方法

根据`Dog`类创建实例后，就可以使用句点表示法来调用`Dog`类中定义的任何方法。下面来让小狗蹲下和打滚:
```
my_dog.sit()
my_dog.roll_over()
```
前提是`my_dog`这个实例被创建。在控制台输出结果是：
```
Haha is now sitting!
Haha is rolled over!
```
要调用方法，可指定实例的**名称**(这里是`my_dog`)和要调用的方法，并用句点分隔它们。
遇到代码`my_dog.sit()`时，Python在类`Dog`中查找方法`sit()`并运行其代码。 Python以同样的方式解读代码`my_dog.roll_over()`。

还记得上面我们写的方法里也有形参`self`，这个也是会关联实例，让每一个创建的实例可以用**名称加点语法**访问到类中定义的方法。

这种语法很有用。如果给属性和方法指定了**合适的描述性名称**，如`name,age,sit(),roll_over()`，
即便是从未见过的代码块，我们也能够轻松地推断出它是做什么的。


<a id = "创建多个实例"></a>
#### 创建多个实例

可按需求根据类创建任意数量的实例。
```
my_dog = Dog("haha",3)
print "My dog's name is " + my_dog.name.title() + "!"
print "My dog's age is " + str(my_dog.age) + " years old!"
my_dog.sit()
my_dog.roll_over()

your_dog = Dog("lala","4")
print "Your dog's name is " + your_dog.name.title() + "!"
print "Your dog's age is " + str(your_dog.age) + " years old!"
your_dog.sit()
your_dog.roll_over()
```
在上面例子中，我们创建了两条小狗，它们分别名为haha和lala。每条小狗都是一个独立的实例，有自己的一组属性，能够执行相同的操作:
```
My dog's name is Haha!
My dog's age is 3 years old!
Haha is now sitting!
Haha is rolled over!
Your dog's name is Lala!
Your dog's age is 4 years old!
Lala is now sitting!
Lala is rolled over!
```

就算我们给第二条小狗指定同样的名字和年龄，Python依然会根据Dog类创建另一个实例。

你可按需求根据一个类创建任意数量的实例，条件是将每个实例都存储在**不同的变量**中，或占用**列表或字典**的不同位置。


<a id ="使用类和实例"></a>
### 使用类和实例

你可以使用类来模拟现实世界中的很多情景。类编写好后，你的大部分时间都将花在使用根据类创建的实例上。

你需要执行的一个重要任务是修改实例的属性。你可以**直接修改**实例的属性，也可以**编写方法以特定的方式进行修改**。


<a id = "car类"></a>
#### car类

下面来编写一个表示汽车的类，它存储了有关汽车的信息，还有一个汇总这些信息的方法:
```
class Car():
    '''模拟汽车的尝试'''
    def __init__(self,make,model,year):
        '''初始化汽车实例的属性'''
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car("audi","a4",2018)   # 创建 my_new_car 这个实例
print my_new_car.get_descriptive_name() # 调用 描述方法
```

控制台会输出：
```
2018 Audi A4
```


<a id = "给属性指定默认值"></a>
#### 给属性指定默认值

类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。在有些情况下，如设置默认值时，在方法`__init__()`内指定这种初始值是可行的;
如果你对某个属性这样做了，就**无需包含**为它提供初始值的**形参**。

下面来添加一个名为`odometer_reading`的属性，其初始值总是为0。我们还添加了一个名为`read_odometer()`的方法，用于读取汽车的里程表:
```
 def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print "This car has " + str(self.odometer_reading) + " miles on it."

my_new_car.read_odometer() #调用 查看汽车里程的方法
```
在控制台输出为：
```
This car has 0 miles on it.
```


<a id = "修改属性的值"></a>
#### 修改属性的值

因为里程这个属性不可能不变，所以我们要有途径去修改它。

可以以**三种不同的方式**修改属性的值。


<a id = "直接通过实例进行修改"></a>
##### 1、直接通过实例进行修改

要修改属性的值，最简单的方式是通过实例直接访问它。下面的代码直接将里程表读数设置为27:
```
my_new_car.read_odometer() #调用 查看汽车里程的方法
my_new_car.odometer_reading = 27 #直接通过实例修改属性
my_new_car.read_odometer()
```

输出为：
```
This car has 0 miles on it.
This car has 27 miles on it.
```

简单解释一下：我们使用句点表示法来直接访问并设置汽车的属性`odometer_reading`。
这行代码让Python在实例`my_new_car`中找到属性`odometer_reading`，并将该属性的值设置为27。

我们从输出的结果可以看到，没修改前是默认值0，修改后变成27，说明修改成功了。


<a id = "通过方法进行设置"></a>
##### 2、通过方法进行设置

如果有替你更新属性的方法，将大有裨益。这样，你就无需直接访问属性，而可将值传递给一个方法，由它在内部进行更新。
下面的示例演示了一个名为`update_odometer()`的方法:
```
def update_odometer(self,mileage):
        '''将里程表的值设定为指定值'''
        self.odometer_reading = mileage
```

我们使用一下：
```
my_new_car.read_odometer() #调用 查看汽车里程的方法
my_new_car.update_odometer(27) #使用方法修改里程数
my_new_car.read_odometer()
```

输出的结果为：
```
This car has 0 miles on it.
This car has 27 miles on it.
```

简单解释一下：

方法接受一个里程值，并将其存储到`self.odometer_reading`中，例子中我们调用的时候提供了27，故而将里程的值设置为27，
输出的结果也显示我们设置成功了。

可对方法`update_odometer`进行扩展，使其在修改里程表读数时做些额外的工作。

下面来修改一下上面的方法，添加一些逻辑，禁止任何人将里程表读数往回调:
```
 def update_odometer(self,mileage):
        '''将里程表的值设定为指定值
           禁止将里程表的读数往回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print "You can't roll back an odometer!"
```

现在，`update_odometer()`在修改属性前检查指定的读数是否合理。如果新指定的里程(`mileage`)大于或等于原来的里程(`self.odometer_reading`)，
就将里程表读数改为新指定的里程;否则就发出警告，指出不能将里程表往回拨。


<a id = "通过方法进行递增"></a>
##### 3、通过方法进行递增（增加特定的值）

有时候需要将属性值递增特定的量，而不是将其设置为全新的值。假设我们购买了一辆二手车，且从购买到登记期间增加了100英里的里程。

下面的方法让我们能够传递这个增量，并相应地增加里程表读数:
```
def increment_odometer(self,miles):
        '''将里程表读数增加指定的量
           禁止增加负值把里程数回调 
        '''
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print "You can't roll back an odometer!"
```
测试一下：
```
my_new_car = Car("audi","a4",2018)   # 创建 my_new_car 这个实例
print my_new_car.get_descriptive_name() # 调用 描述性方法
my_new_car.read_odometer() #调用 查看汽车里程的方法

my_new_car.update_odometer(23500) #更新my_new_car这个实例的里程数
my_new_car.read_odometer() #现在是23500

my_new_car.increment_odometer(100) #my_new_car这个实例增加100公里的里程
my_new_car.read_odometer() #现在是23600

```
输出的结果为：
```
2018 Audi A4
This car has 0 miles on it.
This car has 23500 miles on it.
This car has 23600 miles on it.
```


<a id = "继承"></a>
### 继承

编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用继承。
一个类继承另一个类时，它将自动获得另一个类的所有属性和方法;原有的类称为父类，而新类称为子类。
子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。


<a id = "子类的方法"></a>
#### 子类的方法`__init__()`

创建子类的实例时，Python首先需要完成的任务是给父类的所有属性赋值。为此，子类的方法`__init__()`需要父类施以援手。

例如，下面来模拟电动汽车。
电动汽车是一种特殊的汽车，因此我们可以在前面创建的Car类的基础上创建新类ElectricCar，这样我们就只需为电动汽车特有的属性和行为编写代码。

下面来创建一个简单的ElectricCar类版本，它具备Car类的所有功能:
```
class ElectricCar(Car):  #必须在括号里指定父类的名称
    '''电动汽车类的定义'''
    def __init__(self,make,model,year):
        '''初始化父类的属性'''
        super().__init__(make,model,year)
```

解释一下这个类声明：

`super()`是一个特殊函数，帮助Python将**父类和子类关联**起来。这行代码让Python调用`ElectricCar`的父类的方法`__init__()`，
让实例`ElectricCar`包含父类的所有属性。父类也称为**超类 (superclass)**，名称super因此而得名。

测试使用一下：
```
my_electric_car = ElectricCar("tesla","model s","2017")
print (my_electric_car.get_descriptive_name())
print (my_electric_car.odometer_reading)
```
解释一下测试：

为测试继承是否能够正确地发挥作用，我们尝试创建一辆电动汽车，但提供的信息与创建普通汽车时相同。

在第一行，我们创建ElectricCar类的一个实例，并将其存储在变量`my_electric_car`中。
这行代码调用类中定义的方法`__init__`，后者让Python调用父类Car中定义的方法`__init__`。我们提供了实参`tesla`、`model s`和`2017`。

因为调用的是父类的`__init__`方法，所以子类ElectricCar创建的实例里也会有一个初始化的属性`odometer_reading`，当然也是为0的。

在控制台输出如下：
```
2017 Tesla Model S
0
```


<a id = "给子类定义属性和方法"></a>
#### 给子类定义属性和方法

除方法`__init__`外，电动汽车没有其他特有的属性和方法。当前，我们只想确认电动汽车具备普通汽车的行为，也就是父类里已经定义的方法。

当前，ElectricCar实例的行为与Car实例一样，但现在我们可以开始定义电动汽车特有的属性和方法了。

让一个类继承另一个类后，可添加**区分子类和父类**所需的**新**属性和方法。

下面来改一下刚才的代码，添加一个电动汽车特有的属性(电瓶)，以及一个描述该属性的方法。
我们将存储电瓶容量，并编写一个打印电瓶描述的方法:
```
class ElectricCar(Car): #必须在括号里指定父类的名称
    '''电动汽车类的定义
       先初始化父类的属性，再初始化电动车特有的属性。
    '''
    def __init__(self,make,model,year):
        '''初始化父类的属性'''
        super().__init__(make,model,year)
        self.battery_size = 70  #电动车特有属性,Car的实例就不具有这个属性
    
    def describe_battery(self):
        '''打印一条描述电瓶容量的信息'''
        print ("This car has a " + str(self.battery_size) + "-kwh battery!")
```
我们再试试属性和方法：
```
my_electric_car = ElectricCar("tesla","model s","2017")
print (my_electric_car.battery_size)
my_electric_car.describe_battery()
```
输出为：
```
70
This car has a 70-kwh battery!
```
我们可以清晰地知道，我们子类创建的实例已经具有了它特有的属性和方法。

对于例子的子类ElectricCar类的特殊化程度没有任何限制。模拟电动汽车时，你可以根据所需的准确程度添加**任意数量的属性和方法**。

如果一个属性或方法是任何汽车都有的，而不是电动汽车特有的，就应将其加入到父类Car类而不是子类ElectricCar类中。
这样，使用Car类的人将获得相应的功能，而ElectricCar类只包含处理电动汽车**特有属性和行为的代码。**


<a id = "重写父类的方法"></a>
#### 重写父类的方法

对于父类的方法，只要它**不符合子类模拟的实物的行为**，都可对其进行重写。为此，可在子类中定义一个这样的方法，即**它与要重写的父类方法同名**。
这样，Python将不会考虑这个父类方法，而只**关注你在子类中定义的相应方法，因为它会从本身先找（自下而上）**。

假设我们在Car中定义一个邮箱的方法：
```
def fill_gas_tank(self):
        '''描述油箱信息'''
        print ("This car has a gas tank!")
```

那么我们的子类里也会继承这个方法，但是显而易见电动车没有油箱，也并不需要，这时候我们就要在ElectricCar类中重写这个方法：
```
def fill_gas_tank(self):
        '''重写油箱的方法'''
        print ("This car doesn't need a gas tank!")
```
如果有人对电动汽车调用`fill_gas_tank()`方法，Python将忽略Car类中的方法`fill_gas_tank()`，转而运行子类ElectricCar中重写的方法。
使用继承时，可让子类保留从父类那里继承而来的精华，并剔除不需要的糟粕。


<a id = "将实例用作属性"></a>
#### 将实例用作属性

使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多:属性和方法清单以及文件都越来越长。
在这种情况下，可能需要将类的一部分作为一个独立的类提取出来。
你可以将大型类拆分成多个协同工作的小类。
例
如，不断给ElectricCar类添加细节时，我们可能会发现其中包含很多专门针对汽车电瓶的属性和方法。

在这种情况下，我们可将这些属性和方法提取出来，放到另一个名为Battery的类中，并将一个Battery实例用作ElcetricCar类的一个属性，
我们先创建一个Battery的类，然后再修改一下ElectricCar类的定义：

```
class Battery():
    '''模拟电动车电瓶'''
    def __init__(self,battery_size = 70):
        '''初始化电瓶的属性'''
        self.battery_size = battery_size
    
    def describe_battery(self):
        '''打印一条描述电瓶容量的信息'''
        print ("This car has a " + str(self.battery_size) + "-kwh battery!")

class ElectricCar(Car): #必须在括号里指定父类的名称
    '''电动汽车类的定义
       先初始化父类的属性，再初始化电动车特有的属性。
    '''
    def __init__(self,make,model,year):
        '''初始化父类的属性'''
        super().__init__(make,model,year)
        self.battery = Battery()  #电动车特有属性,Car的实例就不具有这个属性.把一个Battery类的实例变成电动车的battery属性
        '''
        这行代码让Python创建一个新的Battery实例(由于没有指定尺寸，因此为默认值为70)，并将该实例存储在属性self.battery中。每当方法__init__()被调用时，都将执行该操作;因此现在每个ElcetricCar实例都包含一个自动创建的Battery实例作为属性。
        '''   
    
    def fill_gas_tank(self):
        '''重写油箱的方法'''
        print ("This car doesn't need a gas tank!")
```
测试一下这两个类：
```
my_electric_car = ElectricCar("tesla","model s","2017") #创建一个电车实例
print (my_electric_car.get_descriptive_name()) #继承自Car类里的方法
print (my_electric_car.odometer_reading) #继承自Car里的属性

print (my_electric_car.battery.battery_size) #battery这个电车的属性也是一个实例，调用battery中的属性
my_electric_car.battery.describe_battery() #battery这个电车的属性也是一个实例，调用battery中的类方法
```
这看似做了很多额外的工作，但现在我们想多详细地描述电瓶都可以，且不会导致ElectricCar类混乱不堪。
下面再给Battery类添加一个方法，它根据电瓶容量报告汽车的续航里程:
```
def get_range(self):
        '''打印一条消息，根据电瓶电量指出续航里程'''
        if self.battery_size == 70: #如果电瓶容量为70，那么续航里程就为240英里
            range = 240
        elif self.battery_size == 85: #如果电瓶容量为85，那么续航里程就为270英里
            range = 270
        message = "This car can go approximately " + str(range) #整理要打印的消息
        message += " miles on a full charge."
        print (message)
```
测试一下：
```
my_test_car = ElectricCar("xiaopeng","model peng","2018") #新建一个电车实例
print (my_test_car.get_descriptive_name()) #调用Car里的描述信息
my_test_car.battery.get_range() #通过电车的属性battery这个实例调用得到默认的续航里程信息
my_test_car.battery.battery_size = 85 #把电量改到85
my_test_car.battery.get_range() #通过电车的属性battery这个实例调用得到默认的续航里程信息
```
输出为：
```
2018 Xiaopeng Model Peng
This car can go approximately 240 miles on a full charge.
This car can go approximately 270 miles on a full charge.
```


<a id = "模拟实物"></a>
#### 模拟实物

模拟较复杂的物件(如电动汽车)时，需要解决一些有趣的问题:

续航里程是电瓶的属性还是汽车的属性呢?如果我们只需描述一辆汽车，那么将方法`get_range()`放在Battery类中也许是合适的;

但如果要描述一家汽车制造商的整个产品线，也许应该将方法`get_range()`移到ElectricCar类中。
在这种情况下，`get_range()`依然根据电瓶容量来确定续航里程，但报告的是**一款汽车**的续航里程。

我们也可以这样做:将方法`get_range()`还留在Battery类中，但向它传递一个参数，如`car_model`;
在这种情况下，方法`get_range()`将根据电瓶容量和汽车型号报告续航里程。

这让你进入了程序员的另一个境界:解决上述问题时，你从较高的逻辑层面(而不是语法层面)考虑;你考虑的不是Python，而是如何使用代码来表示实物。

到达这种境界后，你经常会发现，现实世界的建模方法并没有对错之分。有些方法的效率更高，但要找出效率最高的表示法，需要经过一定的实践。
只要代码像你希望的那样运行，就说明你做得很好!

即便你发现自己不得不多次尝试使用不同的方法来重写类，也不必气馁;要编写出高效、准确的代码，都得经过这样的过程。


<a id = "导入类"></a>
### 导入类

随着你不断地给类添加功能，文件可能变得很长，即便你妥善地使用了继承亦如此。为遵循Python的总体理念，应让文件尽可能整洁。
为在这方面提供帮助，Python允许你**将类存储在模块中**，然后在主程序中导入所需的模块。


<a id = "导入单个类"></a>
#### 导入单个类

下面来创建一个只包含Car类的模块。我们把刚才写的Car的类的定义全部移动到`car.py`这个文件里：
```
'''表示汽车的类''' #解释见下方

class Car():
    '''模拟汽车的尝试'''
    def __init__(self,make,model,year):
        '''初始化汽车实例的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 设置读取里程属性的默认值

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print ("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self,mileage):
        '''将里程表的值设定为指定值
           禁止将里程表的读数往回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print ("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        '''将里程表读数增加指定的量
           禁止增加负值把里程数回调 
        '''
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print ("You can't roll back an odometer!")
    
    def fill_gas_tank(self):
        '''描述油箱信息'''
        print ("This car has a gas tank!")
```
对第一行注释的解释：

这里我们包含了一个模块级文档字符串，对该模块的内容做了简要的描述。你应为自己创建的每个模块都编写文档字符串。 

为了区别一下我们可以把主程序文件命名为`my_car.py`。然后在主程序中导入Car类并创建它的实例：
```
from car import Car #导入Car类

my_car = Car("paramela","s","2018")
print (my_car.get_descriptive_name()) #创建 my_car 这个实例
my_car.odometer_reading = 50 # 改变里程读数
my_car.read_odometer() # 调用读取里程的方法
```
所以导入类的方法和导入模块的方法类似：
```
from file_name import class_name
```
导入完我们就可以照常使用了，就仿佛这个类是在当下文件定义的一样！下面是输出结果：
```
2018 Paramela S
This car has 50 miles on it.
```
导入类是一种有效的编程方式。如果在这个程序中包含了整个Car类，它该有多长呀!

通过将这个类移到一个模块中，并导入该模块，你依然可以使用其所有功能，但主程序文件变得整洁而易于阅读了。

这还能让你将大部分逻辑存储在独立的文件中;确定类像你希望的那样工作后，你就可以不管这些文件，而专注于主程序的高级逻辑了。


<a id = "在一个模块中存储多个类，从一个模块导入多个类"></a>
#### 在一个模块中存储多个类，从一个模块导入多个类

虽然同一个模块中的类之间应存在某种相关性，但可根据需要在一个模块中存储任意数量的类。
类Battery和ElectricCar都可帮助模拟汽车，因此下面将它们都加入模块`car.py`中:
```
'''一组表示燃油汽车和电动汽车的类'''
class Car():
省略
class Battery():
省略
class ElectricCar(Car):
省略
```
导入的时候就可以用上面讲的通用方法，当然与导入模块还有相似的地方就是可以导入多个类，用逗号隔开即可：
```
from car import Car,ElectricCar
my_beetle = Car("volkswagen","beetle","2016")
print (my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla","roadster","2017")
print(my_tesla.get_descriptive_name())
```
从一个模块中导入多个类时，用逗号分隔了各个类。导入必要的类后，就可根据需要创建每个类的任意数量的实例。

**注意到，我们并未导入Battery类，但是电车依然可以使用它自己battery的属性，因为在`car.py`中有。
我们在生成电车实例的时候，初始化方法是回到`car.py`文件中的，那时候同时生成了一个Battery的实例。**


<a id = "导入整个模块"></a>
#### 导入整个模块

你还可以导入整个模块，再使用**句点**表示法访问需要的类。这种导入方法很简单，代码也易于阅读。

由于**创建类实例的代码都包含模块名**，因此**不会**与当前文件使用的任何名称发生冲突。

下面的代码导入整个car模块，并创建一辆普通汽车和一辆电动汽车:
```
import car #导入整个模块

my_beetle = car.Car("volkswagen","beetle","2016")
print (my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar("tesla","roadster","2017")
print(my_tesla.get_descriptive_name())
```
我们使用语法`module_name.class_name`访问需要的类。


<a id = "导入模块中的所有类"></a>
#### 导入模块中的所有类

要导入模块中的每个类，可使用下面的语法:
```
from module_name import *
```
不推荐使用这种导入方式，其原因有二：

* 首先，如果只要看一下文件开头的语句，就能清楚地知道程序使用了哪些类，将大有裨益;但这种导入方式**没有明确地指出**你使用了模块中的哪些类。

* 这种导入方式还可能引发**名称**方面的困惑。如果你不小心导入了一个与程序文件中其他东西同名的类，将引发难以诊断的错误。

这里之所以介绍这种导入方式，是因为虽然不推荐使用这种方式，但你可能会在别人编写的代码中见到它。

**需要从一个模块中导入很多类时，最好导入整个模块**，并使用`module_name.class_name`语法来访问类。
这样做时，虽然文件开头并没有列出用到的所有类，但你清楚地知道在程序的哪些地方使用了导入的模块;
你还避免了导入模块中的每个类可能引发的名称冲突。


<a id = "在一个模块中导入另一个模块"></a>
#### 在一个模块中导入另一个模块

有时候，需要将类分散到多个模块中，以免模块太大，或在同一个模块中存储不相关的类。

将类存储在多个模块中时，你可能会发现一个模块（a模块）中的类依赖于另一个模块（b模块）中的类。
在这种情况下，可在前一个模块（a模块）中导入必要的类（b模块）。

继续用刚才的三个类做例子，我们把Battery类和ElectricCar类移到新的文件当做电车的模块，把这个文件命名为`electricCar.py`：
```
'''一组描述电动汽车的类''' #不要忘了模块的描述
from car import Car #导入Car类
class Battery():
省略
class ElectricCar(Car): #必须在括号里指定父类的名称
  省略
```
因为ElectricCar类需要访问它的父类Car，所以我们要把Car类导入到电动车的模块中，如果我们忘记了这一行，那么在创建ElectricCar实例时就会报错。

现在我们分别导入就可以创建任意汽车了：
```
from car import Car # 导入Car类
from electricCar import ElectricCar # 导入ElectricCar类

my_beetle = Car("volkswagen","beetle","2016")
print (my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla","roadster","2017")
print(my_tesla.get_descriptive_name())
```


<a id = "自定义工作流程"></a>
#### 自定义工作流程

正如你看到的，在组织大型项目的代码方面，Python提供了很多选项。
熟悉所有这些选项很重要，这样你才能确定哪种项目组织方式是最佳的，并能理解别人开发的项目。

一开始应让代码结构尽可能简单。先尽可能在一个文件中完成所有的工作，确定一切都能正确运行后，再将类移到独立的模块中。

如果你喜欢模块和文件的交互方式，可在项目开始时就尝试将类存储到模块中。

先找出让你能够编写出可行代码的方式，再尝试让代码更为组织有序。


<a id = "Python标准库"></a>
### Python标准库

Python标准库是一组模块，安装的Python都包含它。

你现在对类的工作原理已有大致的了解，可以开始使用其他程序员编写好的模块了。

可使用标准库中的任何函数和类，为此只需在程序开头包含一条简单的`import`语句。

下面来看模块`collections`中的一个类——`OrderedDict`:

字典让你能够将信息关联起来，但它们**不记录**你添加键—值对的**顺序**。

要创建字典并记录其中的键—值对的添加顺序，可使用模块`collections`中的`OrderedDict`类。
`OrderedDict`实例的行为几乎与字典相同，**区别只在于记录了键—值对的添加顺序**。 

我们再来看一看第6章的`favorite_languages.py`示例，但这次将记录被调查者参与调查的顺序:
```
from collections import OrderedDict

favorite_languages = OrderedDict() #调用OrderedDict来创建一个空字典，将其存储在favorite_languages中

favorite_languages["jen"] = "python"
favorite_languages["sarah"] = "c"
favorite_languages["edward"] = "ruby"
favorite_languages["phil"] = "python"

for name,language in favorite_languages.items(): #遍历字典，但知道将以添加的顺序获取调查结果。
    print(name.title() + "'s favorite language is " + language.title() + ".")
```
这是一个很不错的类，它兼具列表和字典的主要优点(在将信息关联起来的同时保留原来的顺序)。
等你开始对关心的现实情形建模时，可能会发现**有序字典**正好能够满足需求。

随着你对标准库的了解越来越深入，将熟悉大量可帮助你处理常见情形的模块。你还可以从其他地方下载外部模块。


<a id = "类编码风格"></a>
### 类编码风格

你必须熟悉有些与类相关的编码风格问题，在你编写的程序较复杂时尤其如此。

类名应采用**驼峰命名法 **，即将**类名**中的**每个单词的首字母都大写**，而不使用下划线。
**实例名和模块名**都采用**小写**格式，并在**单词之间加上下划线**。

对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。
每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。

可使用空行来组织代码，但不要滥用。在**类**中，可使用**一个空行来分隔方法**;而在**模块**中，可使用**两个空行来分隔类**。

需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import语句，再添加一个空行，然后编写导入你自己编写的模块的import语句。

在包含多条import语句的程序中，这种做法让人更容易明白程序使用的各个模块都来自何方。


<a id = "类_小结"></a>
### 类_小结

如何编写类

如何使用属性在类中存储信息，以及如何编写方法，以让类具备所需的行为

如何编写方法`__init__`，以便根据类创建包含所需属性的实例。

如何修改实例的属性——包括直接修改以及通过方法进行修改。

使用继承可简化相关类的创建工作;将一个类的实例用作另一个类的属性可让类更简洁。

通过将类存储在模块中，并在需要使用这些类的文件中导入它们，可让项目组织有序。

编写类时应遵循的Python约定。


---
<a id = "文件和异常"></a>
## 文件和异常

至此，你掌握了编写组织有序而易于使用的程序所需的基本技能，该考虑让程序目标更明确、用途更大了。

在本章中，你将学习处理文件，让程序能够快速地分析大量的数据;你将学习错误处理，避免程序在面对意外情形时崩溃;

你将学习异常，它们是Python创建的特殊对象，用于管理程序运行时出现的错误;你还将学习模块`json`，它让你能够保存用户数据，以免在程序停止运行后丢失。

学习处理文件和保存数据可让你的程序使用起来更容易:用户将能够选择输入什么样的数据，以及在什么时候输入;
用户使用你的程序做一些工作后，可将程序关闭，以后再接着往下做。

学习处理异常可帮助你应对文件不存在的情形，以及处理其他可能导致程序崩溃的问题。
这让你的程序在面对错误的数据时更健壮——不管这些错误数据源自无意的错误，还是源自破坏程序的恶意企图。

你在本章学习的技能可提高程序的适用性、可用性和稳定性。


---
<a id = "从文件中读取数据"></a>
### 从文件中读取数据

文本文件可存储的数据量多得难以置信:天气数据、交通数据、社会经济数据、文学作品等。
每当需要分析或修改存储在文件中的信息时，读取文件都很有用，对数据分析应用程序来说尤其如此。

例如，你可以编写一个这样的程序:读取一个文本文件的内容，重新设置这些数据的格式并将其写入文件，让浏览器能够显示这些内容。

要使用文本文件中的信息，首先需要将信息读取到内存中。为此，你可以一次性读取文件的全部内容，也可以以每次一行的方式逐步读取。 


<a id = "读取整个文件"></a>
#### 读取整个文件

要读取文件，需要一个包含几行文本的文件。

下面首先来创建一个文件，它包含精确到小数点后30位的圆周率值，且在小数点后每10位处都换行，放在`pi_digits.txt`文件中:
```
3.1415926535
8979323846
2643383279
```
下面的程序，命名为`file_test.py`打开并读取这个文件，再将其内容显示到屏幕上:
```
with open("pi_digits.txt") as file_object:  #读取文件pi_digit.txt的操作
    contents = file_object.read()
    print(contents)
```
这个程序运行结果在控制器上显示就是：
```
3.1415926535
8979323846
2643383279
空行，一会儿下面解释。
```
我们先来看看函数`open()`。要以任何方式使用文件——哪怕仅仅是打印其内容，都得先打开文件，这样才能访问它。
函数`open()`接受一个参数：要打开的文件的名称。Python在**当前执行的文件所在的目录**中查找指定的文件。

在这个示例中，当前运行的是`file_test.py`，因此Python在`file_test.py`所在的目录中查找pi_digits.txt。

函数`open()`返回一个表示文件的对象。在这里，`open("pi_digits.txt")`返回一个表示文件`pi_digits.txt`的对象
Python将这个对象存储在我们将在**后面使用的变量中**（例子中就是`file_object`)。

**关键字`with`的巨大作用**：

关键字`with`在不再需要访问文件后将其关闭。

在这个程序中，注意到我们调用了`open()`，但没有调用`close()`。
你也可以调用`open()`和`close()`来打开和关闭文件，但这样做时，如果程序存在bug，导致`close()`语句未执行，文件将不会关闭。

这看似微不足道，但未妥善地关闭文件可能会导致数据丢失或受损。
如果在程序中过早地调用`close()`，你会发现需要使用文件时它已关闭 (无法访问)，这会导致更多的错误。
并非在任何情况下都能轻松确定关闭文件的恰当时机，但通过使用前面所示的结构(with…as…的结构)，
可让Python去确定:你只管打开文件，并在需要时使用它，Python自会在合适的时候自动将其关闭。

有了表示`pi_digits.txt`的文件对象后(即是`file_object`)，我们使用方法`read()`(前述程序的第2行)读取这个文件的全部内容，
并将其作为一个长长的字符串存储在变量`contents`中。
这样，通过 打印`contents`的值，就可将这个文本文件的全部内容显示出来。

相比于原始文件，该输出唯一不同的地方是末尾多了一个空行。为何会多出这个空行呢?
因为`read()`到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行。

要删除多出来的空行，可在`print`语句中使用字符串的一个方法`rstrip()`，我们改下代码再输出一遍：
```
with open("pi_digits.txt") as file_object: #读取文件pi_digit.txt的操作
    contents = file_object.read() #使用read()读取文件内容
    print(contents.rstrip()) #输出结果不带空行
```
Python方法`rstrip()`删除(剥除)字符串末尾的空白。现在，输出与原始文件的内容完全相同。


<a id = "文件路径"></a>
#### 文件路径

根据你组织文件的方式，有时可能要打开不在程序文件所属目录中的文件。

例如你当下正在写的python程序在文件夹`Practice_Python`中，这个文件夹中还有另一个文件夹`test_folder`，用于存储程序文件操作的文本文件。

虽然文件夹`test_folder`包含在文件夹`Practice_Python`中，但仅向`open()`传递位于该文件夹中的文件的名称也不可行，
因为Python 只在文件夹`Practice_Python`中查找，而不会在其子文件夹`test_folder`中查找。

要让Python打开不与程序文件位于同一个目录中的文件，需要提供文件路径 ，它让Python到系统的特定位置去查找。

由于文件夹`test_folder`位于文件夹`Practice_Python`中，因此可使用**相对文件路**径来打开该文件夹中的文件。
相对文件路径让Python到指定的位置去查找，而该位置是**相对于当前运行的程序所在目录**的。

在Linux和OS X中，你可以这样编写代码:
```
with open("test_folder/file_name.txt") as file_object:
```
这行代码让Python到当前文件夹即`Practice_Python`下的文件夹`test_folder`中去查找指定的`.txt`文件。

在Windows系统中，在文件路径中使用`反斜杠(\)`而不是`斜杠(/)`：
```
with open("test_folder\file_name.txt") as file_object:
```
比如我在文件夹`test_folder`中放一个文件，命名为`folder_file.txt`，我在里面放两行信息：
```
12345
67890
```
我们试试上面的读取语句：
```
with open("test_folder/folder_file.txt") as file_object2: # 读取当前文件夹中test_folder文件夹中的文本文件folder_file.txt
    contents2 = file_object2.read() #使用read()读取文件内容
    print(contents2.rstrip()) #输出结果不带空行
```
输出成功。

你还可以将文件在计算机中的准确位置告诉Python，这样就不用关心当前运行的程序存储在什么地方了。
这称为**绝对文件路径** 。在相对路径行不通时，可使用绝对路径。

例如， 如果`text_folder`并不在当前文件夹`Practice_Python`中，而在文件夹`other_files`中，
则向`open()`传递路径`"test_folder/folder_file.txt"`行不通，因为Python只在文件夹python_work中查找该位置。
为明确地指出你希望Python到哪里去查找，你需要提供完整的路径。

绝对路径通常比相对路径更长，因此将其存储在一个变量中，再将该变量传递给`open()`会有所帮助。

在Linux和OS X中，绝对路径类似于下面这样:
```
file_path = "/Users/fzk27/fzk27/Practice_Python/test_folder/folder_file.txt"
with open(file_path) as file_objec3:
```
而在Windows系统中，它们类似于下面这样:
```
file_path = "\Users\fzk27\fzk27\Practice_Python\test_folder\folder_file.txt"
with open(file_path) as file_objec3:
```
通过使用绝对路径，可读取**系统任何地方**的文件。就目前而言，最简单的做法是：

1、要么将数据文件存储在程序文件所在的目录。

2、要么将其存储在程序文件所在目录下的一个文件夹(如`test_folder`)中。

注意：

Windows系统有时能够正确地解读文件路径中的斜杠。如果你使用的是Windows系统，且结果不符合预期，请确保在文件路径中使用的是反斜杠。

在Mac的系统里想用到文件路径可以选中文件然后使用快键键`command + i`，里面有一项位置属性，选中复制即可使用。


<a id = "逐行读取"></a>
#### 逐行读取

读取文件时，常常需要检查其中的每一行:你可能要在文件中查找特定的信息，或者要以某种方式修改文件中的文本。

例如，你可能要遍历一个包含天气数据的文件，并使用天气描述中包含字样sunny的行。
在新闻报道中，你可能会查找包含标签`<headline>`的行，并按特定的格式设置它。

要以每次一行的方式检查文件，可对**文件对象**使用`for`循环：
```
file_name = "pi_digits.txt" #将文件名存储在变量中
with open(file_name) as file_object4: 
    for line in file_object4:
        print(line) #打印每行
```
我们将要读取的文件的名称存储在变量`file_name`中，这是使用文件时一种常见的做法。
由于变量`file_name`表示的并非实际文件——它只是一个让Python知道到哪里去查找文件的字符串，
因此可轻松地将`pi_digits.txt`替换为你要使用的另一个文件的名称。

调用`open()`后，将一个表示文件及其内容的对象存储到了变量`file_object4`中。这里也使用了关键字`with`，让Python负责妥善地打开和关闭文件。

为查看文件的内容，我们通过对文件对象执行循环来遍历文件中的每一行。
我们打印每一行时，发现空白行更多了:
```
3.1415926535

8979323846

2643383279

```
为何会出现这些空白行呢?因为在这个**文件中**，每行的末尾都有一个**看不见的换行符**，而`print`语句也会加上一个换行符，
因此每行末尾都有**两个换行符**：

一个来自文件，另一个来自`print`语句。
要消除这些多余的空白行，可在`print`语句中使用`rstrip()`：
```
file_name = "pi_digits.txt" #将文件名存储在变量中
with open(file_name) as file_object4: 
    for line in file_object4:
        print(line.rstrip()) #去除空白行
```
现在输出又与文件相同了：
```
3.1415926535
8979323846
2643383279
```


<a id = "创建一个包含文件各行内容的列表"></a>
#### 创建一个包含文件各行内容的列表

使用关键字`with`时，`open()`返回的文件对象只在`with`代码块内可用。

如果要在`with`代码块**外**访问文件的内容，可在`with`代码块内将文件的各行存储在一个列表中，并在`with`代码块外使用该列表：
你可以立即处理文件的各个部分，也可推迟到程序后面再处理。 

下面的示例在`with`代码块中将文件`pi_digits.txt`的各行存储在一个列表中，再在`with`代码块外打印它们：
```
with open(file_name) as file_object5:
    lines = file_object5.readlines() # 按行读取文件并把每行存入列表lines

for line in lines: # 用for语句在with语句外打印每行的内容
    print(line.rstrip())
```
方法`readlines()`从文件中读取每一行，并将其存储在一个列表中;接下来，该列表被存储到变量`lines`中;在`with`代码块外，我们依然可以使用这个变量。

然后，我们使用一个简单的`for`循环来打印`lines`中的各行。由于列表`lines`的每个元素都对应于文件中的一行，因此输出与文件内容完全一致。


<a id ="使用文件的内容"></a>
#### 使用文件的内容

将文件读取到内存中后，就可以以任何方式使用这些数据了。下面以简单的方式使用圆周率的值。

首先我们修改一下文件内容，让小数点对齐：
```
3.1415926535
  8979323846
  2643383279
```
然后，我们将创建一个字符串，它包含文件中存储的所有数字，且没有任何空格:
```
file_name = "pi_digits.txt" #将文件名存储在变量中
with open(file_name) as file_object5:
    lines = file_object5.readlines() # 按行读取文件并把每行存入列表lines

pi_string = "" #用于存储圆周率的值
for line in lines: #for语句拼接圆周率
    pi_string += line.rstrip() #删除右边的空位
    
print(pi_string) #打印拼接的圆周率
print(len(pi_string)) #查看拼接后的字符串长度
```
打印结果为：
```
3.1415926535  8979323846  2643383279
36
```
在变量`pi_string`存储的字符串中，包含原来位于每行左边的空格，为删除这些空格，可使用`strip()`而不是`rstrip()`：
```
file_name = "pi_digits.txt" #将文件名存储在变量中
with open(file_name) as file_object5:
    lines = file_object5.readlines() # 按行读取文件并把每行存入列表lines

pi_string = "" #用于存储圆周率的值
for line in lines: #for语句拼接圆周率
    pi_string += line.strip() #删除两边的空位
    
print(pi_string) #打印拼接的圆周率
print(len(pi_string)) #查看拼接后的字符串长度
```
输出的结果为：
```
3.141592653589793238462643383279
32
```
这样，我们就获得了一个这样的字符串:它包含精确到30位小数的圆周率值。这个字符串长32字符，因为它还包含整数部分的3和小数点。

注意：

读取文本文件时，Python将其中的所有文本都解读为字符串。如果你读取的是数字，并要将其作为数值使用，就必须使用函数`int()`将其转换为整数，
或使用函数`float()` 将其转换为浮点数。


<a id = "包含一百万位的大型文件"></a>
#### 包含一百万位的大型文件

前面我们分析的都是一个只有三行的文本文件，但这些代码示例也可处理大得多的文件。

如果我们有一个文本文件，其中包含精确到小数点后1000000位而不是30位的圆周率值，也可创建一个包含所有这些数字的字符串。

为此，我们无需对前面的程序做任何修改，只需将这个文件传递给它即可。
在这里，我们只打印到小数点后50位，以免终端为显示全部1000000位而不断地翻滚:
```
print(pi_string[:52] + "......") #打印拼接的圆周率
print(len(pi_string)) #查看拼接后的字符串长度
```
对于你可处理的数据量，Python没有任何限制;只要系统的内存足够多，你想处理多少数据都可以。


<a id = "圆周率值中包含你的生日吗"></a>
#### 圆周率值中包含你的生日吗

我一直想知道自己的生日是否包含在圆周率值中。下面来扩展刚才编写的程序，以确定某个人的生日是否包含在圆周率值的前1 000 000位中。

为此，可将生日表示为一个由数字组成的字符串，再检查这个字符串是否包含在`pi_string`中。

由此可见，读取文件的内容后，就可以以你能想到的任何方式对其进行分析。


<a id = "读取文件小结"></a>
#### 读取文件小结

1、读取整个 文件。

2、打印时遍历文件对象。

3、将各行存储在一个列表中，再在`with`代码块外打印它们。

**小技巧**：

可使用方法`replace()`将字符串中的特定单词都替换为另一个单词。下面是一个简单的示例，演示了如何将句子中的dog替换为cat。
```
message = "I really like dog!"
print(message.replace("dog","cat"))
```
输出为：
```
I really like cat!
```


<a id = "写入文件"></a>
### 写入文件

保存数据的最简单的方式之一是将其写入到文件中。

通过将输出写入文件，即便关闭包含程序输出的终端窗口，这些输出也依然存在:

你可以在程序结束运行后查看这些输出，可与别人分享输出文件，还可编写程序来将这些输出读取到内存中并进行处理。


<a id = "写入空文件"></a>
#### 写入空文件

要将文本写入文件，你在调用`open()`时需要提供**另一个实参**，告诉Python你要写入打开的文件。

为明白其中的工作原理，我们来将一条简单的消息**存储到文件中**，而不是将其打印到屏幕上:
```
file_name1 = "write_none.txt" #把文件名放进变量里
with open(file_name1,"w") as file_obj:  #将要写入文件,并创建文件对象
    file_obj.write("I love programing!") #写入的内容
```
在这个示例中，调用`open()`时提供了两个实参：

第一个实参也是要打开的文件的名称

第二个实参(“w”)告诉Python，我们要以**写入模式**打开这个文件。

打开文件时，可指定`读取模式 (“r”)`、`写入模式 (“w”)`、`附加模式 (“a”)`或让你能够**读取和写入**文件的模式`(“r+”)`。

如果你省略了模式实参，Python将以**默认**的**只读模式（r）**打开文件。

如果你要写入的文件不存在，函数`open()`将自动创建它。

然而，以写入(“w”)模式打开文件时千万要小心，因为如果指定的文件已经存在，Python将在**返回文件对象前清空该文件。
**也就是说先把这个文件清空再写入你要写入的文本。

我们使用文件对象的方法`write()`将一个字符串写入文件。这个程序没有终端输出，
但如果你打开文件`write_none.txt`，将看到其中包含如下一行内容:
```
I love programing!
```
相比于你的计算机中的其他文件，这个文件没有什么不同。你可以打开它、在其中输入新文本、复制其内容、将内容粘贴到其中等。

注意:Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数`str()`将其转换为字符串格式。


<a id = "写入多行"></a>
#### 写入多行
               
函数`write（）`不会在你写入的文本末尾添加换行符，因此如果你写入多行时没有指定换行符，文件看起来可能不是你希望的那样:
```
file_name1 = "write_none.txt" #把文件名放进变量里
with open(file_name1,"w") as file_obj:  #将要写入文件,并创建文件对象
    file_obj.write("I love programing!") #写入的内容
    file_obj.write("I also like football!") #继续写入
```
运行后，文件`write_none.txt`是这样：
```
I love programing!I also like football!
```
要让每个字符串都单独占一行，需要在`write()`语句中包含换行符:
```
file_name1 = "write_none.txt" #把文件名放进变量里
with open(file_name1,"w") as file_obj:  #将要写入文件,并创建文件对象
    file_obj.write("I love programing!\n") #写入的内容
    file_obj.write("I also like football!\n") #继续写入
```
运行后，文件`write_none.txt`变成这样：
```
I love programing!
I also like football!
```
像显示到终端的输出一样，还可以使用空格、制表符和空行来设置这些输出的格式。


<a id = "附加到文件"></a>
#### 附加到文件

如果你要给文件添加内容，而不是覆盖原有的内容，可以**附加模式**打开文件。

你以附加模式打开文件时，Python不会在返回文件对象前清空文件，而你写入到文件的行都将添加到文件**末尾**。

如果指定的文件不存在，Python将为你创建一个空文件。

我们再修改一下写入的操作：
```
file_name1 = "write_none.txt" # 把文件名放进变量里
with open(file_name1,"a") as file_obj1: # 创建文件对象，附加模式
    file_obj1.write("Because football is very good!\n") #添加一句话
    file_obj1.write("Because programing fell good!\n") #添加另一句话
```
我们打开文件时指定了实参`"a"`，以便将内容附加到文件末尾，而不是覆盖文件原来的内容。

我们又写入了两行，它们被添加到文件`write_none.txt`末尾:
```
I love programing!
I also like football!
Because football is very good!
Because programing fell good!
```
最终的结果是，文件原来的内容还在，它们后面是我们刚添加的内容。


<a id = "异常"></a>
### 异常

Python使用被称为**异常的特殊对象**来管理程序执行期间发生的错误。

每当发生让Python不知所措的错误时，它都会创建一个异常对象。

如果你编写了处理该异常的代码，程序将继续运行;如果你未对异常进行处理，程序将停止，并显示一个traceback，其中包含有关异常的报告。

异常是使用`try--except`代码块处理的。

`try--except`代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办。

使用了`try--except`代码块时，即便出现异常，程序也将继续运行，显示你编写的友好的错误消息，而不是令用户迷惑的traceback。


<a id = "处理ZeroDivisionError异常"></a>
#### 处理ZeroDivisionError异常

下面来看一种导致Python引发异常的简单错误。你可能知道不能将一个数字除以0，但我们还是让Python这样做吧:
```
print(5/0)
```
Python无法这样做，因此你将看到一个traceback:
```
Traceback (most recent call last):
  File "/Users/fzk27/fzk27/Practice_Python/file_test.py", line 60, in <module>
    print(5/0)
ZeroDivisionError: division by zero
```
上述traceback中， 处指出的错误是一个异常对象。Python无法按你的要求做时，就会创建这种对象。
在这种情况下，Python将停止运行程序，并指出引发了哪种异常，而我们可根据这些信息对程序进行修改。

下面我们将告诉Python，发生这种错误时怎么办;这样，如果再次发生这样的错误，我们就有备无患了。


<a id = "使用try--except代码块"></a>
#### 使用`try--except`代码块

当你认为可能发生了错误时，可编写一个`try--except`代码块来处理可能引发的异常。
你让Python尝试运行一些代码，并告诉它如果这些代码引发了指定的异常，该怎么办。 

处理`ZeroDivisionError`异常的`try--except`代码块类似于下面这样:
```
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't division by zero!")
```
们将导致错误的代码行`ptint(5/0)`放在了一个`try`代码块中。

如果`try`代码块中的代码运行起来没有问题，Python将跳过`except`代码块。
如果`try`代码块中的代码导致了错误，Python将查找`except`代码块，并运行其中的代码，即其中指定的错误与引发的错误相同。

在这个示例中，`try`代码块中的代码引发了`ZeroDivisionError`异常，因此Python指出了该如何解决问题的`except`代码块，并运行其中的代码。

这样，用户看到的是一条友好的错误消息，而不是`traceback`:
```
You can't division by zero!
```
如果`except`代码块后面还有其他代码，程序将**接着运行**，因为已经告诉了Python如何处理这种错误。

下面来看一个捕获错误后程序将继续运行的示例。


<a id = "使用异常避免崩溃"></a>
#### 使用异常避免崩溃

发生错误时，如果程序还有工作没有完成，妥善地处理错误就尤其重要。

这种情况经常会出现在要求用户提供输入的程序中;如果程序能够妥善地处理无效输入，就能再提示用户提供有效输入，而不至于崩溃。

下面来创建一个只执行除法运算的简单计算器:

```
print("Give me two numbers, I'll divide them!")
print("Eenter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("\nSecond number: ")
    if second_number == "q":
        break
    answer = int(first_number) / int(second_number)
    print(answer)
```
先提示用户输入第一个数，存进`first_number`，再让用户输入第二个数，存进`second_number`，用户可以随时输入`q`退出程序，

但这个程序没有采取任何处理错误的措施，因此让它执行除数为0的除法运算时，它将崩溃:
```
Give me two numbers, I'll divide them!
Eenter 'q' to quit.

First number: 4

Second number: 0
Traceback (most recent call last):
  File "/Users/fzk27/fzk27/Practice_Python/file_test.py", line 75, in <module>
    answer = int(first_number) / int(second_number)
ZeroDivisionError: division by zero
```
程序崩溃可不好，但让用户看到traceback也不是好主意。不懂技术的用户会被它们搞糊涂，而且如果用户怀有恶意，
他会通过traceback获悉你不希望他知道的信息。

例如，他将知 道你的程序文件的名称，还将看到部分不能正确运行的代码。有时候，训练有素的攻击者可根据这些信息判断出可对你的代码发起什么样的攻击。


<a id = "else代码块"></a>
#### else代码块

通过将可能引发错误的代码放在`try--except`代码块中，可提高这个程序抵御错误的能力。
错误是执行除法运算的代码行导致的，因此我们需要将它放到`try--except`代码块中。

这个示例还包含一个`else`代码块；依赖于`try`代码块成功执行的代码都应放到`else`代码块中，我们来修改一下上面的代码：
```
while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("\nSecond number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!\n")
    else:
        print(answer)
```
我们让Python尝试执行`try`代码块中的除法运算，这个代码块只包含可能导致错误的代码。

依赖于`try`代码块成功执行的代码都放在`else`代码块中;在这个示例中，如果除法运算成功，我们就使用`else`代码块来打印结果。

`except`代码块告诉Python，出现`ZeroDivisionError`异常时该怎么办。

如果`try`代码块因除零错误而失败，我们就打印一条友好的消息，告诉用户如何避免这种错误。程序将继续运行，用户根本看不到traceback:
```
Give me two numbers, I'll divide them!
Eenter 'q' to quit.

First number: 5

Second number: 0
You can't divide by zero!

First number: 4

Second number: 3
1.3333333333333333

First number: q
```
`try--except--else`代码块的工作原理大致如下:

Python尝试执行`try`代码块中的代码；只有可能引发异常的代码才需要放在`try`语句中。

有时候，有一些仅在`try`代码块成功执行时才需要运行的代码;这些代码应放在`else`代码块中。

`except`代码块告诉Python，如果它尝试运行`try`代码块中的代码时引发了指定的异常，该怎么办。

通过预测可能发生错误的代码，可编写健壮的程序，它们即便面临无效数据或缺少资源，也能继续运行，从而能够抵御无意的用户错误和恶意的攻击。


<a id = "处理FileNotFoundError异常"></a>
#### 处理FileNotFoundError异常

使用文件时，一种常见的问题是找不到文件：你要查找的文件可能在其他地方、文件名可能不正确或者这个文件根本就不存在。
对于所有这些情形，都可使用`try--except--else`代码块以直观的方式进行处理。

我们来尝试读取一个不存在的文件。下面的程序尝试读取文件none.txt的内容，但我没有将这个文件存储在当前程序所在的目录中:
```
file_name2 = "none.txt"

with open(file_name2) as f_obj:
    contents = f_obj.read()
```
Python无法读取不存在的文件，因此它引发一个异常:
```
Traceback (most recent call last):
  File "/Users/fzk27/fzk27/Practice_Python/file_test.py", line 87, in <module>
    with open(file_name2) as f_obj:
FileNotFoundError: [Errno 2] No such file or directory: 'none.txt'
```
在上述traceback中，最后一行报告了`FileNotFoundError`异常，这是Python找不到要打开的文件时创建的异常。

在这个示例中，这个错误是函数`open()`导致的，因此要处理这个错误，必须将`try`语句放在包含`open()`的代码行之前：
```
file_name2 = "none.txt"
try:
    with open(file_name2) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry,the file " + file_name2 + " does not exist."
    print(msg)
```
在这个示例中，`try`代码块引发`FileNotFoundError`异常，因此Python找出与该错误匹配的`except`代码块，并运行其中的代码。

最终的结果是显示一条友好的错误消息，而不是traceback：
```
Sorry,the file none.txt does not exist.
```
如果文件不存在，这个程序什么都不做，因此错误处理代码的意义不大。下面来扩展这个示例，看看在你使用多个文件时，异常处理可提供什么样的帮助。


<a id = "分析文本"></a>
#### 分析文本

你可以分析包含整本书的文本文件。很多经典文学作品都是以简单文本文件的方式提供的，因为它们不受版权限制。

下面来提取童话`Alice in Wonderland`的文本，并尝试计算它包含多少个单词。我们把它放在当前程序目录中。
我用的文件放在了这里[alice.txt](https://github.com/wnz27/Cultivate__harvest/blob/master/codePractice/some_text_file/alice.txt)。

我们将使用方法`split()`，它根据一个字符串创建一个单词列表。
下面是对只包含童话名`"Alice in Wonderland"`的字符串调用方法`split()`的结果:
```
title = "Alice in Wonderland"
print (title.split())
输出：
['Alice', 'in', 'Wonderland']
```
方法`split()`以**空格为分隔符将**字符串分拆成多个部分，并将这些部分都存储到一个列表中。

结果是一个包含字符串中所有单词的列表，虽然有些单词可能包含标点。

为计算`Alice in Wonderland`包含多少个单词，我们将对整篇小说调用`split()`，再计算得到的列表包含多少个元素，从而确定整篇童话大致包含多少个单词：
```
file_name3 = "alice.txt"

try:
    with open(file_name3) as f_obj2:
        contents = f_obj2.read()
except FileNotFoundError:
        msg = "Sorry,the file " + file_name3 + " does not exist."
else:
        #计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The " + file_name3 + " has about " + str(num_words) + " words.")
```
我们把文件`alice.txt`移到了正确的目录中，让`try`代码块能够成功地执行。

我们对变量`contents`(它现在是一个长长的字符串，包含童话`alice.txt`的全部文本)调用方法`split()`，以生成一个列表，其中包含这部童话中的所有单词。

当我们使用`len()`来确定这个列表的长度时，就知道了原始字符串大致包含多少个单词。

我们打印一条消息，指出文件包含多少个单词。这些代码都放在`else`代码块中，因为仅当`try`代码块成功执行时才执行它们。

输出指出了文件alice.txt包含多少 个单词:
```
The alice.txt has about 17842 words.
```


<a id = "使用多个文件"></a>
#### 使用多个文件

下面多分析几本书。这样做之前，我们先将这个程序的大部分代码移到一个名为`count_words`的函数中，这样对多本书进行分析时将更容易:
```
def count_words(file_name):
    '''计算一个文件大致包含多少个单词'''
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry,the file " + file_name + " does not exist."
    else:
        #计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The " + file_name3 + " has about " + str(num_words) + " words.")
```
这些代码大都与原来一样，我们只是将它们移到了函数`count_words`中，并增加了缩进量。

修改程序的同时更新注释是个不错的习惯，因此我们将注释改成了文档字符串，并稍微调整了一下措辞。

现在可以编写一个简单的循环，计算要分析的任何文本包含多少个单词了。
为此，我们将要分析的文件的名称存储在一个列表中，然后对列表中的每个文件都调用`count_words()`。

我们将尝试计算[Alice in Aonderland](https://github.com/wnz27/Cultivate__harvest/blob/master/codePractice/some_text_file/alice.txt)、[Siddhartha](https://github.com/wnz27/Cultivate__harvest/blob/master/codePractice/some_text_file/siddhartha.txt)、[Moby Dick](https://github.com/wnz27/Cultivate__harvest/blob/master/codePractice/some_text_file/moby%20dick.txt)和[Little Women](https://github.com/wnz27/Cultivate__harvest/blob/master/codePractice/some_text_file/little%20women.txt)分别包含多少个单词，它们都不受版权限制。

我故意没有将siddhartha.txt放到当前程序所在的目录中，让你能够看到这个程序在文件不存在时处理得有多出色:
```
file_names = ["alice.txt","little women.txt","siddhartha.txt","moby dick.txt"]
for file_name in file_names:
    count_words(file_name)
```
文件siddhartha.txt不存在，但这丝毫不影响这个程序处理其他文件:
```
The alice.txt has about 17842 words.
The little women.txt has about 189079 words.
Sorry,the file siddhartha.txt does not exist.
The moby dick.txt has about 4594 words.
```
在这个示例中，使用`try--except`代码块提供了两个重要的优点:

1、避免让用户看到traceback。

2、让程序能够继续分析能够找到的其他文件。

如果不捕获因找不到`siddhartha.txt`而引发的`FileNotFoundError`异常，用户将看到完整的traceback，
而程序将在尝试分析`alice.txt`和`little women.txt`后停止运行——根本不分析`moby dick.txt`。


<a id = "失败时一声不吭"></a>
#### 失败时一声不吭

在前一个示例中，我们告诉用户有一个文件找不到。但并非每次捕获到异常时都需要告诉用户，有时候你希望程序在发生异常时一声不吭，
就像什么都没有发生一样继续运行。

要让程序在失败时一声不吭，可像通常那样编写`try`代码块，但在`except`代码块中明确地告诉Python什么都不要做。

Python有一个`pass`语句，可在代码块中使用它来让Python 什么都不要做:
```
def count_words(file_name):
    '''计算一个文件大致包含多少个单词'''
    try:
        省略
    except FileNotFoundError:
       pass
    else:
        #计算文件大致包含多少个单词
        省略
    
file_names = ["alice.txt","little women.txt","siddhartha.txt","moby dick.txt"]
for file_name in file_names:
    count_words(file_name)
```
相比于前一个程序，这个程序唯一不同的地方是`except`处的`pass`语句。

现在，出现`FileNotFoundError`异常时，将执行`except`代码块中的代码，但什么都不会发生。这种错误发生时，不会出现traceback，也没有任何输出。

用户将看到存在的每个文件包含多少个单词，但没有任何迹象表明有一个文件未找到:
```
The alice.txt has about 17842 words.
The little women.txt has about 189079 words.
The moby dick.txt has about 4594 words.
```
`pass`语句还充当了占位符，它提醒你在程序的某个地方什么都没有做，并且以后也许要在这里做些什么。

例如，在这个程序中，我们可能决定将找不到的文件的名称写入到文件`missing_files.txt`中。
用户看不到这个文件，但我们可以读取这个文件，进而处理所有文件找不到的问题。

**小技巧：**

你可以使用方法`count()`来确定特定的单词或短语在字符串中出现了多少次。例如，下面的代码计算`row`在一个字符串中出现了多少次:
```
test_count = "Row, row row your boat!"
print(test_count.count("row"))
print(test_count.lower().count("row"))
```
输出为：
```
2
3
```
请注意，这说明方法`count()`是区分大小写的，而通过使用方法`lower()`将字符串转换为小写，可捕捉要查找的单词出现的所有次数，而不管其大小写格式如何。


<a id = "决定报告哪些错误"></a>
#### 决定报告哪些错误

在什么情况下该向用户报告错误?在什么情况下又应该在失败时一声不吭呢?

如果用户知道要分析哪些文件，他们可能希望在有文件没有分析时出现一条消息，将其中的原因告诉他们。

如果用户只想看到结果，而并不知道要分析哪些文件，可能就无需在有些文件不存在时告知他们。向用户显示他不想看到的信息可能会降低程序的可用性。

Python的错误处理结构让你能够细致地控制与用户分享错误信息的程度，要分享多少信息由你决定。

编写得很好且经过详尽测试的代码不容易出现内部错误，如语法或逻辑错误，
但只要程序依赖于**外部因素**，如用户输入、存在指定的文件、有网络链接，就有可能出现异常。

凭借经验可判断该在程序的什么地方包含异常处理块，以及出现错误时该向用户提供多少相关的信息。


<a id = "存储数据"></a>
### 存储数据

很多程序都要求用户输入某种信息，如让用户存储游戏首选项或提供要可视化的数据。

不管专注的是什么，程序都把用户提供的信息存储在列表和字典等数据结构中。

用户关闭程序时，你几乎总是要保存他们提供的信息;一种简单的方式是使用模块json来存储数据。

模块`json`让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。你还可以使用`json`在Python程序之间分享数据。

更重要的是，JSON数据格式并非Python专用的，这让你能够将以JSON格式存储的数据与使用其他编程语言的人分享。这是一种轻便格式，很有用，也易于学习。 

注意：`JSON(JavaScript Object Notation)`格式最初是为JavaScript开发的，但随后成了一种常见格式，被包括Python在内的众多语言采用。


<a id = "使用json.dump()和json.load()"></a>
#### 使用`json.dump()`和`json.load()`

我们来编写一个存储一组数字的简短程序，再编写一个将这些数字读取到内存中的程序。
第一个程序将使用`json.dump()`来存储这组数字，而第二个程序将使用`json.load()`。

函数`json.dump()`接受两个实参：1、**要存储的数据**以及2、可用于存储数据的**文件对象**。

下面演示了如何使用`json.dump()`来存储数字列表:
```
import json #导入json模块

numbers = [2,3,5,7,11,13]

file_name = "numbers.json"
with open(file_name,"w") as f_obj:
    json.dump(numbers,f_obj) #把数字列表写入文件对象f_obj
```
我们先导入模块`json`，再创建一个数字列表。我们指定了要将该数字列表存储到其中的文件的名称。

通常使用文件扩展名`.json`来指出文件存储的数据为JSON格式。

我们以写入模式打开这个文件，让`json`能够将数据写入其中。我们使用函数`dump()`将数字列表存储到文件`numbers.json`中。

这个程序没有输出，但我们可以打开文件`numbers.json`，看看其内容。数据的存储格式与Python中一样:
```
[2, 3, 5, 7, 11, 13]
```
下面再编写另一个程序，使用`json.load()`将这个列表读取到内存中:
```
import json #导入json模块

file_name = "numbers.json"

with open(file_name) as f_obj: #只读模式建立文件对象
    numbers = json.load(f_obj) #把读取的数据放进变量numbers里

print(numbers) #输出变量numbers看看
```
我们先确保读取的是前面写入的文件。

这次我们以读取方式打开这个文件，因为Python只需读取这个文件。

我们使用函数`json.load()`加载存储在 `numbers.json`中的信息，并将其存储到变量`numbers`中。

最后，我们打印恢复的数字列表，看看它是否与上一个程序中创建的数字列表相同:
```
[2, 3, 5, 7, 11, 13]
```
这是一种在程序之间共享数据的简单方式。


<a id = "保存和读取用户生成的数据"></a>
#### 保存和读取用户生成的数据

对于用户生成的数据，使用`json`保存它们大有裨益，因为如果不以某种方式进行存储，等程序停止运行时用户的信息将丢失。

下面来看一个这样的例子：用户首次运行程序时被提示输入自己的名字，这样再次运行程序时就记住他了。

我们先来存储用户的名字:
```
import json #导入json模块

username = input("What's your name?") #提示用户输入用户名

file_username = "username.json" #指定存储用户名的文件名
with open(file_username,"w") as w_f_obj: #生成文件对象，作为写入用户名的文件
    json.dump(username,w_f_obj) #用json.dump()把用户名写入存放用户名的文件
    print("We'll remember you when you come back, " + username + "!") #告知用户
```
我们提示输入用户名，并将其存储在一个变量中。接下来，我们调用`json.dump()`，并将用户名和一个文件对象传递给它，从而将用户名存储到文件中。

然后，我们打印一条消息，指出我们存储了他输入的信息:
```
What's your name?abc
We'll remember you when you come back, abc!
```
现在再编写一个程序，向其名字被存储的用户发出问候:
```
file_username = "username.json" #指定存储用户名的文件名
# 读取用户名，问候用户
with open(file_username) as r_f_obj: # 生成文件对象用于读取里面的数据
    r_username = json.load(r_f_obj) # 把文件对象里存储的数据存放在变量r_username里
    print("Welcome back " + r_username + "!") #问候用户
```
我们使用`json.load()`将存储在`username.json`中的信息读取到变量`r_username`中。恢复用户名后，我们就可以欢迎用户回来了。
```
Welcome back abc!
```
我们需要将这两个程序合并到一个程序中。因为`username.json`这个文件已经存在，不好测试，所以我们换一个文件名，
当这个程序运行时，我们将尝试从文件`username1.json`中获取用户名，因此我们首先编写一个尝试读取用户名的`try`代码块。

如果这个文件不存在，我们就在`except`代码块中提示用户输入用户名，
并将其存储在`username1.json`中，以便程序再次运行时能够获取它:
```
import json #导入json模块

#如果以前存储了用户名，就加载它
#否则就提示用户输入用户名并存储它
file_name_test = "username1.json"
try: #尝从文件中读取用户名信息
    with open(file_name_test) as r_f_obj:
        username = json.load(r_f_obj)
except FileNotFoundError:  #当文件不存在时，提示用户设置用户名，并写入文件存储
    username = input("What is your name?")
    with open(file_name_test,"w") as w_f_obj:
        json.dump(username,w_f_obj)
        print("We'll remember you when you come back " + username + "!")
else:# 如果文件存在并且加载成功，则问候用户
    print("Welcome back " + username + "!")
```
无论执行的是`except`代码块还是`else`代码块，都将显示用户名和合适的问候语。如果这个程序是首次运行，输出将如下:
```
What is your name?qwe
We'll remember you when you come back qwe!
```
否则将输出如下：
```
Welcome back qwe!
```
这是程序之前至少运行了一次时的输出。


<a id = "重构"></a>
#### 重构

你经常会遇到这样的情况:代码能够正确地运行，但可做进一步的改进——将代码**划分为**一系列完成具体工作的**函数**。

这样的过程被称为**重构**。重构让代码更清晰、更易于理解、更容易扩展。

要重构刚才的程序，可将其大部分逻辑放到一个或多个函数中。
刚才写的程序的重点是问候用户，因此我们将其所有代码都放到一个名为`greet_user()`的函数中:
```
def greet_user():
    '''问候用户，并指出其名字'''
    #如果以前存储了用户名，就加载它
    #否则就提示用户输入用户名并存储它
    file_name_test = "username1.json"
    try: #尝从文件中读取用户名信息
        with open(file_name_test) as r_f_obj:
            username = json.load(r_f_obj)
    except FileNotFoundError:  #当文件不存在时，提示用户设置用户名，并写入文件存储
        username = input("What is your name?")
        with open(file_name_test,"w") as w_f_obj:
            json.dump(username,w_f_obj)
            print("We'll remember you when you come back " + username + "!")
    else:# 如果文件存在并且加载成功，则问候用户
        print("Welcome back " + username + "!")

greet_user()
```
考虑到现在使用了一个函数，我们使用一个文档字符串来指出程序是做什么。

这个程序更清晰些，但函数`greet_user()`所做的不仅仅是问候用户，还在存储了用户名时获取它，而在没有存储用户名时提示用户输入一个。

下面来重构`greet_user()`，让它不执行这么多任务。为此，我们首先将获取存储的用户名的代码移到另一个函数中:
```
import json #导入json模块

def get_stored_username():
    '''如果存储了用户名，得到它'''
    filename = "username1.json"
    try:
        with open(filename) as r_f_obj:
            username = json.load(r_f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    '''问候用户，并指出其名字'''
    username = get_stored_username()
    if username:
        print("Welcome back " + username + "!")
    else:
        username = input("What is your name?")
        filename = "username1.json"
        with open(filename,"w") as w_f_obj:
            json.dump(username,w_f_obj)
            print("We'll remember you when you come back " + username + "!")

greet_user()
```
新增的函数`get_stored_username()`目标明确，它的文档字符串指出了这一点。

如果存储了用户名，这个函数就获取并返回它;如果文件`username1.json`不存在，这个函数 就返回`None`。
这是一种不错的做法:函数要么返回预期的值，要么返回`None`;这让我们能够**使用函数的返回值做简单测试。**（更方便的当循环条件使用）

在`greet_user()`的if语句中，如果成功地获取了用户名，就打印一条欢迎用户回来的消息，否则就提示用户输入用户名。

我们还需将`greet_user()`中的另一个代码块提取出来:
将没有存储用户名时提示用户输入的代码放在一个独立的函数中:
```
import json #导入json模块

def get_stored_username():
    '''如果存储了用户名，得到它'''
    filename = "username1.json"
    try:
        with open(filename) as r_f_obj:
            username = json.load(r_f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    '''提示用户输入用户名'''
    username = input("What is your name?")
    filename = "username1.json"
    with open(filename,"w") as w_f_obj:
        json.dump(username,w_f_obj) #将用户名写入文件
    return username

def greet_user():
    '''问候用户，并指出其名字'''
    username = get_stored_username()
    if username:
        print("Welcome back " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back " + username + "!")

greet_user()
```
在这个最终版本中，每个函数都执行单一而清晰的任务。我们调用`greet_user()`，它打印一条合适的消息:要么欢迎老用户回来，要么问候新用户。

为此，它首先调用`get_stored_username()`，这个函数只负责获取存储的用户名(如果存储了的话)，
再在必要时调用`get_new_username()`，这个函数只负责获取并存储新用户的用户名。

要编写出清晰而易于维护和扩展的代码，这种划分工作必不可少。


<a id = "文件与异常小结"></a>
### 文件与异常小结

- 如何使用文件
- 如何一次性读取整个文件
- 如何以每次一行的方式读取文件的内容
- 如何在with语句外读取文件内容
- 如何写入文件
- 如何将文本附加到文件末尾
- 什么是异常
- 如何处理程序可能引发的异常
- 如何存储Python数据结构，以保存用户提供的信息，避免用户每次运行程序时都需要重新提供。



---
<a id = "测试代码"></a>
## 测试代码

- 你将学习高效的代码测试方式，这可帮助你确定代码正确无误，以及发现扩展现有程序时可能引入的bug。

- 编写函数或类时，还可为其编写测试。通过测试，可确定代码面对各种输入都能够按要求的那样工作。
测试让你信心满满，深信即便有更多的人使用你的程序，它也能正确地工作。

- 在程序中添加新代码时，你也可以对其进行测试，确认它们不会破坏程序既有的行为。
程序员都会犯错，因此每个程序员都必须经常测试其代码，在用户发现问题前找出它们。

- 在本章中，你将学习如何使用Python模块`unittest`中的工具来测试代码。

- 你将学习编写测试用例，核实一系列输入都将得到预期的输出。

- 你将看到测试通过了是什么样子，测试未通过又是什么样子，还将知道测试未通过如何有助于改进代码。

- 你将学习如何测试函数和类，并将知道该为项目编写多少个测试。


---
<a id = "测试函数"></a>
### 测试函数

要学习测试，得有要测试的代码。下面是一个简单的函数，它接受名和姓并返回整洁的姓名:
```
def get_formatted_name(first,last):
    '''生成简洁的全名'''
    full_name = first + " " + last
    return full_name.title()
```
函数`get_formatted_name()`将名和姓合并成姓名，在名和姓之间加上一个空格，并将它们的首字母都大写，再返回结果。

为核实`get_formatted_name()`像期望的那样 工作，我们来编写一个使用这个函数的程序。程序names.py让用户输入名和姓，并显示整洁的全名:
```
from test_prctice import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name:")
    if first == "q":
        break
    last = input("\nPlease give me a last name:")
    if last == "q":
        break
    fomatted_name = get_formatted_name(first,last)
    print("\tNeatly formatted name: " + fomatted_name + ".")
```
这个程序从test_practice.py中导入`get_formatted_name()`。用户可输入一系列的名和姓，并看到格式整洁的全名:
```
Enter 'q' at any time to quit.

Please give me a first name:f

Please give me a last name:zk
        Neatly formatted name: F Zk.

Please give me a first name:q
```
从上述输出可知，合并得到的姓名正确无误。现在假设我们要修改`get_formatted_name()`，使其还能够处理中间名。
这样做时，我们要确保不破坏这个函数处理只有名和姓的姓名的方式。

为此，我们可以在每次修改`get_formatted_name()`后都进行测试:运行程序names.py，并输入像`james jolin`这样的姓名，但这太烦琐了。

所幸 Python提供了一种**自动测试函数输出的高效方式**。倘若我们对`get_formatted_name()`进行自动测试，就能始终信心满满，
确信给这个函数提供我们测试过的姓名时，它都能正确地工作。


<a id = "单元测试和测试用例"></a>
#### 单元测试和测试用例

Python标准库中的模块`unittest`提供了代码测试工具。

**单元测试**用于核实函数的某个方面没有问题

**测试用例**是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求。
良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情形的测试。

**全覆盖式测试**用例包含一整套单元测试，涵盖了各种可能的函数使用方式。

对于大型项目，要实现全覆盖可能很难。通常，最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。


<a id = "可通过的测试"></a>
#### 可通过的测试

创建测试用例的语法需要一段时间才能习惯，但测试用例创建后，再添加针对函数的单元测试就很简单了。

要为函数编写测试用例，可先导入模块`unittest`以及要测试的函数，再创建一个继承`unittest.TestCase`的类，
并**编写一系列方法对函数行为的不同方面进行测试**。

下面是一个只包含一个方法的测试用例，它检查函数`get_formatted_name ()`在给定名和姓时能否正确地工作:
```
import unittest
from test_prctice import get_formatted_name

class NameTestCase(unittest.TestCase):
    '''测试test_practice.py'''
    def test_first_last_name(self):
        '''能够正确处理Janis Joplin这样的姓名吗？'''
        formatted_name = get_formatted_name("janis","joplin")
        self.assertEqual(formatted_name,"Janis Joplin")

unittest.main()
```
首先，我们导入了模块`unittest`和要测试的函数`get_formatted_name()`。

我们创建了一个名为`NameTestCase`的类，用于包含一系列针对`get_formatted_name()`的单元测试。
你可随便给这个类命名，但最好让它看起来与要测试的函数相关，并包含字样Test。

这个类**必须继承**`unittest.TestCase`类，这样Python才知道如何运行你编写的测试。

`NameTestCase`只包含一个方法，用于测试`get_formatted_name()`的一个方面。
我们将这个方法命名为`test_first_last_name()`，因为我们要核实的是只有名和姓的姓名能否被正确地格式化。

我们运行这个程序时，所有以`test`打头的方法都将**自动运行**。

在这个方法中，我们调用了要测试的函数，并存储了要测试的返回值。
在这个示例中，我们使用实参`janis`和`joplin`调用`get_formatted_name()`，并将结果存储到变量`formatted_name`中。

然后，我们使用了`unittest`类最有用的功能之一:一个**断言**方法。断言方法用来核实得到的结果是否与期望的结果一致。
在这里，我们知道`get_formatted_name()`应返回这样的姓名，即名和姓的首字母为大写，且它们之间有一个空格，
因此我们期望`formatted_name`的值为`Janis Joplin`。

为检查是否确实如此，我们调用`unittest`的方法`assertEqual()`，并向它传递`formatted_name`和`Janis Joplin`。
代码行`self.assertEqual(formatted_name,"Janis Joplin")`的意思是 说:“将`formatted_name`的值同字符串`Janis Joplin`进行比较，
如果它们相等，就万事大吉，如果它们不相等，跟我说一声!”

代码行`unittest.main()`让Python运行这个文件中的测试。运行`test_name_function.py`时，得到的输出如下:
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
第1行的句点表明有一个测试通过了。

接下来的一行指出Python运行了一个测试，消耗的时间不到0.001秒。

最后的`OK`表明该测试用例中的所有单元测试都通过了。 

上述输出表明，给定包含名和姓的姓名时，函数`get_formatted_name()`总是能正确地处理。

修改`get_formatted_name()`后，可再次运行这个测试用例。如果它通过了，我们就知道在给定`Janis Joplin`这样的姓名时，这个函数依然能够正确地处理。


<a id = "不能通过的测试"></a>
#### 不能通过的测试

测试未通过时结果是什么样的呢?

我们来修改`get_formatted_name()`，使其能够处理中间名，但这样做时，故意让这个函数无法正确地处理像Janis Joplin这样只有名和姓的姓名。

下面是函数`get_formatted_name()`的新版本，它要求通过一个实参指定中间名:

```
def get_formatted_name(first,middle,last):
    '''生成简洁的格式'''
    full_name = first + " " + middle + " " + last
    return full_name
```
这个版本应该能够正确地处理包含中间名的姓名，但对其进行测试时，我们发现它再也不能正确地处理只有名和姓的姓名。

这次运行程序`test_name_function.py`时，输出如下:
```
E
======================================================================
ERROR: test_first_last_name (__main__.NameTestCase)
能够正确处理Janis Joplin这样的姓名吗？
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/fzk27/fzk27/Practice_Python/test_name_function.py", line 8, in test_first_last_name
    formatted_name = get_formatted_name("janis","joplin")
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```
其中包含的信息很多，因为测试未通过时，需要让你知道的事情可能有很多。

第1行输出只有一个字母`E`，它指出测试用例中有一个单元测试导致了错误。

接下来，我们 看到`NameTestCase`中的`test_first_last_name()`导致了错误。测试用例包含众多单元测试时，知道哪个测试未通过至关重要。

我们看到了一个标准 的traceback，它指出函数调用`get_formatted_name("janis","joplin")`有问题，因为它缺少一个必不可少的位置实参。

我们还看到运行了一个单元测试(Ran 1 test in 0.000s)。

最后，还看到了一条消息，它指出整个测试用例都未通过，因为运行该测试用例时发生了一个错误(FAILED (errors=1))。
这条消息位于输出末尾，让你一眼就能看到——你可不希望为获悉有多少测试未通过而翻阅长长的输出。


<a id = "测试未通过时怎么办"></a>
#### 测试未通过时怎么办

测试未通过时怎么办呢?如果你检查的条件没错，测试通过了意味着函数的行为是对的，而测试未通过意味着你编写的新代码有错。

因此，测试未通过时，不要修改测试，而应修复导致测试不能通过的代码:检查刚才对函数所做的修改，找出导致函数行为不符合预期的修改。

在这个示例中，`get_formatted_name()`以前只需要两个实参——名和姓，但现在它要求提供名、中间名和姓。
新增的中间名参数是必不可少的，这导致`get_formatted_name()`的行为不符合预期。

就这里而言，最佳的选择是让中间名变为可选的。这样做后，使用类似于`Janis Joplin`的姓名进行测试时，测试就会通过了，同时这个函数还能接受中间名。

下面来修改`get_formatted_name()`，将中间名设置为可选的，然后再次运行这个测试用例。如果通过了，我们接着确认这个函数能够妥善地处理中间名。

要将中间名设置为可选的，可在函数定义中将形参`middle`移到形参列表末尾，并将其默认值指定为一个空字符串。
我们还要添加一个`if`测试，以便根据是否提供了中间名相应地创建姓名:
```
# 包含中间名的方法，中间名可选
def get_formatted_name(first,last,middle = ""):
    '''生成简洁的全名格式'''
    if middle:
        full_name = first + " " + middle + " " + last
        return full_name.title()
    else:
        full_name = first + " " + last
        return full_name.title()
```
在`get_formatted_name()`的这个新版本中，中间名是可选的。
如果向这个函数传递了中间名(`if middle:`)，姓名将包含名、中间名和姓，否则姓名将只包含名和姓。

现在，对于两种不同的姓名，这个函数都应该能够正确地处理。

为确定这个函数依然能够正确地处理像Janis Joplin这样的姓名，我们再次运行`test_name_function.py`:
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
现在，测试用例通过了。太好了，这意味着这个函数又能正确地处理像Janis Joplin这样的姓名了，而且我们无需手工测试这个函数。

这个函数很容易就修复了，因为未通过的测试让我们得知新代码破坏了函数原来的行为。(函数原本可以通过像Janis Joplin这样的姓名测试)



<a id = "添加新测试"></a>
#### 添加新测试

确定`get_formatted_name()`又能正确地处理简单的姓名后，我们再编写一个测试，用于测试包含中间名的姓名。

为此，我们在`NameTestCase`类中再添加一个方法:
```
import unittest
from test_prctice import get_formatted_name

class NameTestCase(unittest.TestCase):
    '''测试test_practice.py'''
    def test_first_last_name(self):
        '''能够正确处理像Janis Joplin这样的姓名吗？'''
        formatted_name = get_formatted_name("janis","joplin")
        self.assertEqual(formatted_name,"Janis Joplin")

    def test_first_last_middle_name(self):
        '''能够正确处理像Wolfgang Amadeus Mozart这样的姓名吗？'''
        formoatted_name = get_formatted_name("wolfgang","mozart","amadeus")
        self.assertEqual(formoatted_name,"Wolfgang Amadeus Mozart")

unittest.main()
```
我们将这个方法命名为`test_first_last_middle_name()`。方法名必须以`test`打头，这样它才会在我们运行`test_name_function.py`时自动运行。

这个方法名清楚地指出了它测试的是`get_formatted_name()`的哪个行为，这样，如果该测试未通过，我们就会马上知道受影响的是哪种类型的姓名。

在`NameTestCase`类中使用很长的方法名是可以的;这些方法的名称必须是描述性的，这才能让你明白测试未通过时的输出;
这些方法由Python自动调用，你根本不用编写调用它们的代码。

为测试函数`get_formatted_name()`，我们使用名、姓和中间名调用它，再使用`assertEqual()`检查返回的姓名是否与预期的姓名(名、中间名和姓)一致。

我们再次运行`test_name_function.py`时，两个测试都通过了:
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
现在我们知道，这个函数又能正确地处理像Janis Joplin这样的姓名了，我们还深信它也能够正确地处理像Wolfgang Amadeus Mozart这样的姓名。


<a id = "测试类"></a>
### 测试类

在本章前半部分，你编写了针对单个函数的测试，下面来编写针对类的测试。
很多程序中都会用到类，因此能够证明你的类能够正确地工作会大有裨益。

如果针对类的测试通过了，你就能确信对类所做的改进没有意外地破坏其原有的行为。


<a id = "各种断言方法"></a>
#### 各种断言方法

Python在`unittest.TestCase`类中提供了很多断言方法。

前面说过，断言方法检查你认为应该满足的条件是否确实满足。如果该条件确实满足，你对程序行为的假设就得到了确认，你就可以确信其中没有错误。
如果你认为应该满足的条件实际上并不满足，Python将引发异常。 

下面的表描述了6个常用的断言方法。使用这些方法可核实返回的值等于或不等于预期的值、返回的值为`True`或`False`、返回的值在列表中或不在列表中。

你只能在继承`unittest.TestCase`的类中使用这些方法，后面会试试如何在测试类时使用其中的一个。

`unittest Module`中的断言方法:

* 方法：`assertEqual(a,b)`               用途：`核实a == b`
* 方法：`assertNotEqual(a,b)`            用途：`核实a != b`
* 方法：`assertTrue(x)`                  用途：`核实x为True`
* 方法：`assertFalse(x)`                 用途：`核实x为False`
* 方法：`assertIn(item,list)`            用途：`核实item在list中`
* 方法：`assertNotIn(item,list)`         用途：`核实item不在list中`


<a id = "一个要测试的类"></a>
#### 一个要测试的类

类的测试与函数的测试相似——你所做的大部分工作都是测试类中方法的行为，但存在一些不同之处，下面来编写一个类进行测试。来看一个帮助管理匿名调查的类:

`survey.py`：

```
class AnonymousSurvey():
    '''收集匿名调查问卷的答案'''

    def __init__(self,question):
        '''存储一个问题，并为存储答案做准备！'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''显示调查问卷'''
        print(self.question)

    def store_response(self,new_response):
        '''存储单份调查答卷'''
        self.responses.append(new_response)

    def show_results(self):
        '''显示收集到的所有答卷'''
        print("Survey results:")
        for response in self.responses:
            print("- " + response)
```

这个类首先存储了一个你指定的调查问题(见第一个方法)，并创建了一个空列表，用于存储答案。

这个类包含打印调查问题的方法(见第二个方法)

在答案列表中添加新答案的方法(见第三个方法)

以及将存储在列表中的答案都打印出来的方法(见第四个方法)。

要创建这个类的实例，只需提供一个问题即可。

有了表示调查的实例后，就可使用`show_question()`来显示其中的问题，可使用`store_response()`来存储答案，并使用`show_results()`来显示调查结果。

为证明`AnonymousSurvey`类能够正确地工作，我们来编写一个使用它的程序:


`language_survey.py`

```
from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
qusetion = "What language did you first learn to speak? "
my_survey = AnonymousSurvey(qusetion)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit!")
while True:
    response = input("Language: ")
    if response == "q":
        break
    else:
        my_survey.store_response(response.title())
# 显示调查结果
print("Thank you to everyone who participated in the survey!")
my_survey.show_results()

```
这个程序定义了一个问题(`What language did you first learn to speak?`)，并使用这个问题创建了一个`AnonymousSurvey`对象。

接下来，这个程序调用`show_question()`来显示问题，并提示用户输入答案。

收到每个答案的同时将其存储起来。用户输入所有答案(输入q要求退出)后，调用`show_results()`来打印调查结果:
```
What language did you first learn to speak?
Enter 'q' at any time to quit!
Language: chinese
Language: english
Language: spanish
Language: q

Thank you to everyone who participated in the survey!
Survey results:
- Chinese
- English
- Spanish
```

`AnonymousSurvey`类可用于进行简单的匿名调查。

假设我们将它放在了模块`survey`中，并想进行改进:让每位用户都可输入多个答案
编写一个方法，它只列出不同的答案，并指出每个答案出现了多少次
再编写一个类，用于管理非匿名调查。

进行上述修改存在风险，可能会影响`AnonymousSurvey `类的当前行为。

例如，允许每位用户输入多个答案时，可能不小心修改了处理单个答案的方式。

要确认在开发这个模块时没有破坏既有行为，可以编写针对这个类的测试。


<a id = "测试AnonymousSurvey类"></a>
#### 测试AnonymousSurvey类

下面来编写一个测试，对`AnonymousSurvey`类的行为的一个方面进行验证:如果用户面对调查问题时只提供了一个答案，这个答案也能被妥善地存储。

为此，我们将在这个答案被存储后，使用方法`assertIn()`来核实它包含在答案列表中:

`test_survey.py`：
```
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''针对AnonymousSurvey类的测试'''
    def test_store_single_response(self):
        '''测试单个答案会被妥善保管'''
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")

        self.assertIn("English",my_survey.responses)

unittest.main()
```
我们首先导入了模块`unittest`以及要测试的类`AnonymousSurvey`。
我们将**测试用例**命名为`TestAnonymousSurvey`，它也继承了`unittest.TestCase`。

第一个测试方法验证调查问题的单个答案被存储后，会包含在调查结果列表中。

对于这个方法，一个不错的描述性名称是`test_store_single_response()`。
如果这个测试未通过，我们就能通过输出中的方法名得知，在存储单个调查答案方面存在问题。

要测试类的行为，需要创建其实例。
我们使用问题`What language did you first learn to speak?`创建了一个名为`my_survey`的实例，
然后使用方法`store_response()`存储了单个答案`English`。

接下来，我们检查`English`是否包含在列表`my_survey.responses`中，以核实这个答案是否被妥善地存储了。

当我们运行`test_survey.py`时，测试通过了:
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
这很好，但只能收集一个答案的调查用途不大。下面来核实用户提供三个答案时，它们也将被妥善地存储。

为此，我们在`TestAnonymousSurvey`中再添加一个方法:
```
def test_store_three_response(self):
        '''测试三个答案会被妥善保管'''
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ["Chinese","English","Spanish"]
        for response in responses: # 遍历列表存入对象
            my_survey.store_response(response)
        for response in responses: # 检查列表里三个答案是否都存入了对象
            self.assertIn(response,my_survey.responses)
```
我们将这个方法命名为`test_store_three_response()`，并像`test_store_single_response`一样，在其中创建一个调查对象。

我们定义了一个包含三个不同答案的列表，再对其中每个答案都调用`store_response()`。
存储这些答案后，我们使用一个循环来确认每个答案都包含在`my_survey.responses`中。 

我们再次运行`test_survey.py`时，两个测试(针对单个答案的测试和针对三个答案的测试)都通过了:
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
前述做法的效果很好，但这些测试有些重复的地方。下面使用`unittest`的另一项功能来提高它们的效率。


<a id = "方法setUp()"></a>
#### 方法setUp()

在前面的`test_survey.py`中，我们在每个测试方法中都创建了一个`AnonymousSurvey`实例，并在每个方法中都创建了答案。

`unittest.TestCase`类包含方法`setUp()`，让我们只需创建这些对象一次，并在每个测试方法中使用它们。

如果你在`TestCase`类中包含了方法`setUp()`，Python将**先运行它**，**再运行各个以`test`打头的方法**。

这样，在你编写的每个测试方法中都可使用在方法`setUp()`中创建的对象了。

下面使用`setUp()`来创建一个调查对象和一组答案，供方法`test_store_single_response`和`test_store_three_response()`使用:
```
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''针对AnonymousSurvey类的测试'''

    def setUp(self):
        '''创建一个调查对象和一组答案，供使用的测试方法使用'''
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["Chinese","English","Spanish"]

    def test_store_single_response(self):
        '''测试单个答案会被妥善保管'''
         self.my_survey.store_response(self.responses[0]) #把self.responses中第一个答案存入对象
        self.assertIn(self.responses[0],self.my_survey.responses) #查看self.responses中第一个答案是否存在在对象的答案中

    def test_store_three_response(self):
        '''测试三个答案会被妥善保管'''
        for response in self.responses: # 遍历列表存入对象
            self.my_survey.store_response(response)
        for response in self.responses: # 检查列表里三个答案是否都存入了对象
            self.assertIn(response,self.my_survey.responses)

unittest.main()
```
方法`setUp()`做了两件事情:创建一个调查对象;创建一个答案列表。

存储这两样东西的变量名包含前缀`self`(即存储在属性中)，因此可在这个类的任何地方使用。这让两个测试方法都更简单，因为它们都不用创建调查对象和答案。

方法`test_store_single_response()`核实`self.responses`中的第一个答案 ——`self.responses[0]`——被妥善地存储，
而方法`test_store_three_response()`核实`self.responses`中的全部三个答案都被妥善地存储。

再次运行`test_survey.py`时，这两个测试也都通过了:
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
如果要扩展`AnonymousSurvey`，使其允许每位用户输入多个答案，这些测试将很有用。
修改代码以接受多个答案后，可运行这些测试，确认存储单个答案或一系列答案的行为未受影响。

测试自己编写的类时，方法`setUp()`让测试方法编写起来更容易:可在`setUp()`方法中创建一系列实例并设置它们的属性，再在测试方法中直接使用这些实例。
相比于在每个测试方法中都创建实例并设置其属性，这要容易得多。

注意：运行测试用例时，每完成一个单元测试，Python都打印一个字符:

- 测试通过时打印一个句点

- 测试引发错误时打印一个`E`

- 测试导致断言失败时打印一个`F`。 

这就是你运行测试用例时，在输出的第一行中看到的句点和字符数量各不相同的原因。
如果测试用例包含很多单元测试，需要运行很长时间，就可通过观察这些结果来获悉有多少个测试通过了。


<a id = "测试代码小结"></a>
### 测试代码小结

如何使用模块`unittest`中的工具来为函数和类编写测试

如何编写继承`unittest.TestCase`的类

如何编写测试方法，以核实函数和类的行为符合预期

如何使用方法`setUp()`来根据类高效地创建实例并设置其属性，以便在类的所有测试方法中都可使用它们。 

测试是很多初学者都不熟悉的主题。作为初学者，并非必须为你尝试的所有项目编写测试。

但参与工作量较大的项目时，你应对自己编写的函数和类的重要行为进行测试。
这样你就能够更加确定自己所做的工作不会破坏项目的其他部分，你就能够随心所欲地改进既有代码了。
如果不小心破坏了原来的功能，你马上就会知道，从而能够轻松地修复问题。
相比于等到不满意的用户报告bug后再采取措施，在测试未通过时采取措施要容易得多。 

如果你在项目中包含了初步测试，其他程序员将更敬佩你，他们将能够更得心应手地尝试使用你编写的代码，也更愿意与你合作开发项目。
如果你要跟其他程序员开发的项目共享代码，就必须证明你编写的代码通过了既有测试，通常还需要为你添加的新行为编写测试。

请通过多开展测试来熟悉代码测试过程。对于自己编写的函数和类，请编写针对其重要行为的测试，
但在项目早期，不要试图去编写全覆盖的测试用例，除非有充分的理由这样做。

---

基础部分结束

---


<a id = "项目篇"></a>
## 项目篇


<a id = "在OSX系统中安装Pygame"></a>
### 在`OS X`系统中安装`Pygame`

要安装`Pygame`依赖的有些包，需要`Homebrew`。

为安装Pygame依赖的库，请执行下面的命令:
```
$ brew install hg sdl sdl_image sdl_ttf
```
这将安装运行游戏《外星人入侵》所需的库。每安装一个库后，输出都会向上滚动。

如果你还想启用较高级的功能，如在游戏中包含声音，可安装下面两个额外的库:
```
$ brew install sdl_mixer portmidi
```
使用下面的命令来安装Pygame(如果你运行的是Python 2.7，请将`pip3`替换为`pip`):
```
$ pip3 install --user hg+http://bitbucket.org/pygame/pygame
```
启动一个Python终端会话，并导入Pygame以检查安装是否成功(如果你运行的是Python 2.7，请将`python3`替换为`python`):
```
$ python3
>>> import pygame
>>> 
```



