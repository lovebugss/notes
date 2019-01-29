### Redux
>设计思想：  
>（1）Web 应用是一个状态机，视图与状态是一一对应的  
>（2）所有的状态，保存在一个对象里面。
####基本概念

#####1. Store 
Store就是保存数据的地方，可以看成一个容器，整个应用只能有一个Store。  
Redux 提供createStore这个函数，用来生成 Store。

		import { createStore } from 'redux';
		//createStore 接受一个函数(reducer)，并且返回一个新的Store对象
		const store = createStore(fn);

#####2. State

Store对象包含所有数据。如果想得到某个时点的数据，就要对 Store 生成快照。这种时点的数据集合，就叫做 State。  
当前时刻的 State，可以通过store.getState()拿到。

		import { createStore } from 'redux';
		const store = createStore(fn);

		const state = store.getState();
Redux 规定， 一个 State 对应一个 View。只要 State 相同，View 就相同。你知道 State，就知道 View 是什么样，反之亦然。

#####3. Action
State 的变化，会导致 View 的变化。但是，用户接触不到 State，只能接触到 View。所以，State 的变化必须是 View 导致的。Action 就是 View 发出的通知，表示 State 应该要发生变化了。

Action 是一个对象。其中的type属性是必须的，表示 Action 的名称。其他属性可以自由设置，社区有一个规范可以参考。


		const action = {
		  type: 'ADD_TODO',
		  payload: 'Learn Redux'
		};
上面代码中，Action 的名称是ADD_TODO，它携带的信息是字符串Learn Redux。

可以这样理解，Action 描述当前发生的事情。改变 State 的唯一办法，就是使用 Action。它会运送数据到 Store。
4. Action Creator
5. store.dispatch()
