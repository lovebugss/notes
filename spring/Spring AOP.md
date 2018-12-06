##Spring AOP
###1.Spring AOP 概念
AOP（Aspect Oritened Programming） 即面向切面编程/面向方面编程，可以说是OOP（Obeject Oritened Programming，面向对象编程）编程的补充和完善。

AOP 优点：将共通的Service解耦，增强程序的灵活性。
IOC解决的是两个组件的问题，AOP解决的是共通业务和传统业务的解耦问题。

1.切面

	共通的位置执行的共通的处理（切面组件），然后让共通的处理独立封装成组件，然后通过AOP的配置作用到其他目标组件方法上。从而实现了共通业务和传统业务的解耦，增强了程序的灵活性。

2.切入点

- **方法限定表达式**

		格式：execution (修饰符？ 返回类型 方法名(参数列表) 抛出异常？)

		//匹配方法名以save开始的，返回类型和参数没有要求
	    execution(* save*(..))
		//匹配DeptService中所有方法
		execution(* com.xdl.service.DeptService.*(..))
		//匹配service包下所有类的所有方法（不包含子包）
		execution(* com.xdl.service.*.*(..))
		//匹配service包及子包所有类所有方法
		execution(* com.xdl.service..*.*(..))
- **类限定表达式**

		格式： within(类型)

		//匹配DeptService组件，它所有方法都会被追加切面组件处理
		within(com.xdl.service.DeptService)		
		//匹配service包下所有类的所有方法（不包含子包）
		within(com.xdl.service.*)
		//匹配service包及子包所有类所有方法
		within(com.xdl.service..*)
- **bean名称限定表达式**

		格式：bean(bean的id名)

		//匹配id=deptService的组件对象
		bean("deptService")
		//匹配所有id名已Service结尾的组件对象
		bean("*Service")
		

3.通知

- **前置通知（Before Advice）**:在切入点选择的连接点处的方法之前执行的通知，该通知不影响正常程序执行流程（除非该通知抛出异常，该异常将中断当前方法链的执行而返回）。
- **后置通知（After Advice）**:在切入点选择的连接点处的方法之后执行的通知，包括如下类型的后置通知：
- **后置返回通知（After returning Advice）**:在切入点选择的连接点处的方法正常执行完毕时执行的通知，必须是连接点处的方法没抛出任何异常正常返回时才调用后置通知。
- **后置异常通知（After throwing Advice）**: 在切入点选择的连接点处的方法抛出异常返回时执行的通知，必须是连接点处的方法抛出任何异常返回时才调用异常通知。
- **后置最终通知（After finally Advice）**: 在切入点选择的连接点处的方法返回时执行的通知，不管抛没抛出异常都执行，类似于Java中的finally块。
- **环绕通知（Around Advices）**：环绕着在切入点选择的连接点处的方法所执行的通知，环绕通知可以在方法调用之前和之后自定义任何行为，并且可以决定是否执行连接点处的方法、替换返回值、抛出异常等等。

####2.Spring AOP 使用方法

动态代理：可以根据原有组件类动态的生成一个新的组件类，并且将新的组件类方法进行重写，来代替原有组件供外界使用。

Spring中支持两种动态代理的技术：

1. CGLIB技术（适用于目标组件有接口和没接口）：

原理：动态的生成一个子类，子类重写了父类原有的方法。

2. JDK Proxy API技术（适用于目标组件有接口）:

原理：利用原组件接口生成一个新的组件类。

