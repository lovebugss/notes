

### 1、SpringIOC容器

#### IOC基本概念
IOC-inversion of Control 即控制反转。首先控制反转不是一项技术，而是一种思想。如何理IOC？理解好IOC关键是要明确谁控制谁？控制什么？为何是反转？哪些方面反转了？
	
1. **谁控制谁，控制什么？**在传统的javase中，我们在对象内部直接通过new来创建对象，是程序主动的创建依赖对象；而IOC有一个专门的容器来创建对象，即由IOC来控制对象的创建。谁控制谁？即IOC控制了对象，控制了什么？主要控制了外部资源的获取（对象、文件）。
2. **为何是反转？哪些方面反转了？**传统的应用程序是有我们自己在对象中主动控制去直接获取依赖对象，也就是正转。而反转就是通过IOC容器来帮我们创建及注入依赖对象。为何是反转？因为由容器帮我们查找及注入依赖对象，对象只能被动的接受依赖对象，所有是反转。哪些方面反转了？依赖对象的获取反转了。<br>
传统应用程序示意图<br>![](http://i.imgur.com/Vi0LJup.jpg)

有IOC/DI容器后结果示意图<br>![](http://i.imgur.com/pNnyMQC.jpg)

####IOC容器的优点
IOC不是一种技术，而是一种思想，一个重要的面向对象编程的法则，它指导我们如何设计出低耦合，更优良的程序。传统的用于程序是由我们直接在程序的内部主动创建依赖对象，从而导致类之间的耦合，难于测试。有了IOC容器后，把创建和查找依赖对象的权限交给了IOC容器，从而降低了程序的耦合度，这样也便于程序的测试，利于功能的复用使得程序的整个结构体系变得非常灵活。<br>
IOC带来的最大的改变不是从编码上，而是从思想上，发生了“主从换位”的变化。<br>
**IOC可以降低组件之间的耦合度，提升程序的扩展性和移植性。**

### 2、IOC容器的使用

1. 创建IOC容器对象
 			
		<!-- 向容器添加组件 -->
		<bean id="p1" class="com.xdl.bean.Person" scope="singleton" 
			init-method="myinit" destroy-method="myclose">
		</bean>
			
		<bean id="d1" class="java.util.Date">
		</bean>
			
		<!-- 使用静态方法创建组件对象Calendar.getInstance -->
		<bean id="c1" class="java.util.Calendar" factory-method="getInstance">
		</bean>
			
		<!-- 使用对象方法创建组件对象c1.getTime() -->
		<bean id="d2" factory-bean="c1" factory-method="getTime">
		</bean>
			
		<!-- 利用lazy属性将单例对象创建时机推迟到getBean方法 -->
		<bean id="dept" class="com.xdl.bean.Dept" 
			scope="singleton" lazy-init="true">
		</bean>
2. IOC使用过程
	
	1.添加Spring jar包；

	2.添加xml配置文件，追加<bean>定义，将组件交给容器；

	3.创建Spring容器对象ApplicationContext加载配置；

	4.获取对象使用；
####3、IOC和DI
**DI-Dependency** [dɪ'pend(ə)nsɪ] **Injection** [ɪn'dʒekʃ(ə)n] ,即依赖注入，Spring 是利用DI技术实现了IOC控制。理解DI的关键是：“谁依赖谁？为什么要依赖，谁注入了谁，为什么要注入？”


**谁依赖谁：**应用程序依赖IOC容器；

**为什么要依赖：**应用程序需要IOC容器来提供需要的外部资源；

**谁注入谁：**IOC容器注入了应用程序某个对象，应用程序依赖的对象；

**注入了什么：**注入某个对象需要的外部资源；

**DI注入方法**

1. set注入

		applicationContext.xml配置文件如下:
	 	<bean id="logic" class="com.spring.test.di.LogicImpl"/>
		<bean id="loginAction" class="com.spring.test.di.LoginAction">
 	 	<property name="logic" ref="logic"></property>
		</bean>

2. 构造器注入

		applicationContext.xml配置文件如下:
		<bean id="logic" class="com.spring.test.di.LogicImpl"/>
		<bean id="loginAction" class="com.spring.test.di.LoginAction">
		<constructor-arg index="0" ref="logic"></constructor-arg>
		</bean>
3. 接口注入


####bean作用域
如何使用spring的作用域：

	<bean id="role" class="spring.chapter2.maryGame.Role" scope="singleton"/>
	这里的scope就是用来配置spring bean的作用域，它标识bean的作用域。
在spring2.0之前bean只有2种作用域即：singleton(单例)、non-singleton（也称prototype）, Spring2.0以后，增加了session、request、global session三种专用于Web应用程序上下文的Bean。

Spring中支持一下五中作用域：

1. singleton：容器只会创建该Bean的唯一实例；
2. prototype：每次请求都创建一个实例；
3. request：每次HTTP请求都会产生一个新的bean。需要注意的是个，该作用域仅 在基于 Web 的Spring ApplicationContext 情形下有效，以下的 session 和 global Session也是如此；
4. session：每次会话创建一个实例；
5. globalsession：全局的HttpSession中,容器会返回该bean的同一个实例。
 



