##Spring Web MVC

###Spring Web MVC 概念

Spring提供了一个基于MVC模式的框架，用于开发Web程序。
####MVC模式

MVC是一种使用MVC（Model View Controller 模型-视图-控制器）设计的应用程序的模式；

- Model(模型) 表示用于程序的核心，业务处理，
- View （视图） 显示数据
- Controller（控制器） 控制M和V协同工作


####Spring Web MVC 如何实现MVC结构
1. 主要组件
 	- **DispatcherServlet** 主要控制器<br>
		作用：接受浏览器请求，反洗请求调用Handlermapping处理；
	-  **Handlermapping** 映射处理器<br>
		作用：维护请求URl和Controller之间的映射关系';
	- **Controller** 业务控制器<br>
		作用：调用M模型组件进行业务处理;
2. 执行流程

	![](http://i.imgur.com/vmeCUhr.png)

	具体执行步骤如下：

	- 首先浏览器发起请求，请求进入 DispatcherServlet。
	- DispatcherServlet调用HandlerMapping，Handlermapping根据请求调用不同的Controller。
	- DispatcherServlet 调用Controller对象进行业务处理。Controller执行完毕后返回一个ModelAndView信息。
	- DispatcherServlet 调用ViewResolver解析Controller返回的ModelAndView。然后找到View视图的jsp组件，并将Model数据传递给jsp。
	- DispatcherServlet调用jsp生成响应页面信息输出给浏览器
	

####Spring Web MVC 使用方法
#####使用配置

 1.配置DispatcherServlet组件（web.xml）
 
	<servlet>
	  <servlet-name>springmvc</servlet-name>
	  <servlet-class>
	  	org.springframework.web.servlet.DispatcherServlet
	  </servlet-class>
	  <!-- 指定SpringMVC配置文件/IOC配置文件 -->
	  <init-param>
	  	<param-name>contextConfigLocation</param-name>
	  	<param-value>classpath:applicationContext.xml</param-value>
	  </init-param>
	</servlet>
	<servlet-mapping>
	  <servlet-name>springmvc</servlet-name>
	  <url-pattern>*.do</url-pattern>
	</servlet-mapping>
2.配置HandlerMapping组件（applicationContext.xml）

	<!-- 配置HanlderMapping -->
	<bean id="handlerMapping" class="org.springframework.web.servlet.handler.SimpleUrlHandlerMapping">
		<!-- 维护uri和controller对应关系 -->
		<property name="mappings">
			<props>
				<!-- key指定请求;value指定controller的id名 -->
				<prop key="hello.do">helloController</prop>
			</props>
		</property>
	</bean>
3.配置Controller组件（applicationContext.xml）

	<!-- 配置controller -->
	<bean id="helloController" class="com.xdl.controller.HelloController">
	</bean>
4.配置ViewResovler组件 （applicationContext.xml）

	<!-- 配置ViewResolver,解析Controller返回的ModelAndView -->
	<bean id="viewResolver" class="org.springframework.web.servlet.view.InternalResourceViewResolver">
		<!-- 前缀,指定视图组件所在路径 -->
		<property name="prefix" value="/WEB-INF/"></property>
		<!-- 后缀,指定视图组件扩展名 -->
		<property name="suffix" value=".jsp"></property>
	</bean>
#####使用注解

1.配置DispatcherServlet组件

	<servlet>
 		<servlet-name>springmvc</servlet-name>
 		<servlet-class>
 			org.springframework.web.servlet.DispatcherServlet
 		</servlet-class>
 		<init-param>
 			<param-name>contextConfigLocation</param-name>
 			<param-value>classpath:applicationContext.xml</param-value>
 		</init-param>
 		<load-on-startup>1</load-on-startup>
    </servlet>
    <servlet-mapping>
 		<servlet-name>springmvc</servlet-name>
 		<url-pattern>*.do</url-pattern>
    </servlet-mapping>
2.配置RequestMappingHandlerMapping

	<!-- handlerMapping -->
	<bean class="org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerMapping">
	</bean>
	<bean class="org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter">
	</bean>
	<!--简写 -->
	<mvc:annotation-driven />
3.配置Controller

	<!-- 配置Controller,用注解扫描 -->
	<!--base-package 指定包名-->
	<context:component-scan base-package="com.xdl"/>
在Controller类的方法前追加@RequestMapping("URL")

4.配置ViewResolver
	
	<!-- 配置视图解析器 -->
	<bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
		<property name="prefix" value="/WEB-INF/"></property>
		<property name="suffix" value=".jsp"></property>
	</bean>
