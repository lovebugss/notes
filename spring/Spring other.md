####Spring mvc 请求与转发

请求重定向与转发的区别

重定向：以前requset中存放的变量全部失效，并进去一个新的requset请求中。

转发：以前requset中存放的变量不会失效，就像把两个页面拼到一起。

使用方法：

	return "forward:index.jsp"; //转发 

	
	return "forward:user.do?method=reg5"; //转发
	
	return new ModelAndView("/toList");//转发

	return "redirect:user.do?method=reg5"; //重定向

	return "redirect:http://www.baidu.com"; //重定向

	return new ModelAndView("redirect:/toList"); //重定向


####四大域对象

<table style="width: 965px;" align="left" border="5">
<tbody><tr><td>对象</td>
<td>生效时间</td><td>作用域</td><td>&nbsp;实现接口</td>
</tr>
<tr>
<td>request</td>
<td>HTTP请求开始到结束这段时间</td>
<td>在当前请求中有效</td>
<td>&nbsp;HttpServletRequest</td>
</tr>
<tr>
<td>session　</td>
<td>HTTP会话开始到结束这段时间</td>
<td>在当前会话中有效</td>
<td>&nbsp;HttpSession</td>
</tr>
<tr>
<td>application</td>
<td>服务器启动到停止这段时间</td>
<td>在所有应用程序中有效</td>
<td>&nbsp;ServletContext</td>
</tr>
</tbody>
</table>