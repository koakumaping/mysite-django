document.writeln("<style type=\"text/css\">");
document.writeln("body { margin-bottom:60px !important; }");
document.writeln("a, button, input { -webkit-tap-highlight-color:rgba(255, 0, 0, 0); }");
document.writeln("ul, li { list-style:none; margin:0; padding:0 }");
document.writeln(".top_bar { position: fixed; z-index: 900; bottom: 0; left: 0; right: 0; margin: auto; font-family: Helvetica, Tahoma, Arial, Microsoft YaHei, sans-serif; }");
document.writeln(".top_menu { display:-webkit-box; border-top: 1px solid #3D3D46; display: block; width: 100%; background: rgba(255, 255, 255, 0.7); height: 40px; display: -webkit-box; display: box; margin:0; padding:0; -webkit-box-orient: horizontal; background: -webkit-gradient(linear, 0 0, 0 100%, from(#697077), to(#3F434E), color-stop(60%, #464A53)); box-shadow: 0 1px 0 0 rgba(255, 255, 255, 0.3) inset; }");
document.writeln(".top_bar .top_menu>li { -webkit-box-flex:1; background: -webkit-gradient(linear, 0 0, 0 100%, from(rgba(0, 0, 0, 0.1)), color-stop(50%, rgba(0, 0, 0, 0.3)), to(rgba(0, 0, 0, 0.4))), -webkit-gradient(linear, 0 0, 0 100%, from(rgba(255, 255, 255, 0.1)), color-stop(50%, rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0.15))); ; -webkit-background-size:1px 100%, 1px 100%; background-size:1px 100%, 1px 100%; background-position: 1px center, 2px center; background-repeat: no-repeat; position:relative; text-align:center; }");
document.writeln(".top_menu li:first-child { background:none; }");
document.writeln(".top_bar .top_menu li a { line-height:40px; display:block; text-align:center; color:#FFF; text-decoration:none; text-shadow: 0 1px rgba(0, 0, 0, 0.3); -webkit-box-flex:1; }");
document.writeln(".top_bar .top_menu li a label { padding:3px 0 0 3px; font-size:12px; overflow:hidden; }");
document.writeln(".top_bar .top_menu>li>a img { display: inline-block; height: 20px; width: 20px; margin-top:-2px; color: #fff; line-height: 40px; vertical-align:middle; }");
document.writeln(".top_bar li:first-child a { display: block; }");
document.writeln(".menu_font { text-align:left; position:absolute; right:10px; z-index:500; background: -webkit-gradient(linear, 0 0, 0 100%, from(#697077), to(#3F434E), color-stop(60%, #464A53)); border-radius: 5px; width: 120px; margin-top: 10px; padding: 0; box-shadow: 0 1px 5px rgba(0, 0, 0, 0.3); }");
document.writeln(".menu_font.hidden { display:none; }");
document.writeln(".menu_font { top:inherit !important; bottom:55px; }");
document.writeln(".menu_font li a { text-align: left !important; }");
document.writeln(".top_menu li:last-of-type a { background: none; }");
document.writeln(".menu_font:after { top: inherit!important; bottom: -6px; border-color: #464A53 rgba(0, 0, 0, 0) rgba(0, 0, 0, 0); border-width: 6px 6px 0; position: absolute; content: \"\"; display: inline-block; width: 0; height: 0; border-style: solid; left: 70%; }");
document.writeln(".menu_font li { border-top: 1px solid rgba(255, 255, 255, 0.1); border-bottom: 1px solid rgba(0, 0, 0, 0.2); }");
document.writeln(".menu_font li:first-of-type { border-top: 0; }");
document.writeln(".menu_font li:last-of-type { border-bottom: 0; }");
document.writeln(".menu_font li a { height: 40px; line-height: 40px !important; position: relative; color: #fff; display: block; width: 100%; text-indent: 10px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; }");
document.writeln(".menu_font li a img { width: 20px; height:20px; display: inline-block; margin-top:-2px; color: #fff; line-height: 40px; vertical-align:middle; }");
document.writeln("#menu_list0 { right:0; left:10px; }");
document.writeln("#menu_list0:after { left: 20%; }");
document.writeln("#sharemcover { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.7); display: none; z-index: 20000; }");
document.writeln("#sharemcover img { position: fixed; right: 18px; top: 5px; width: 260px; height: 180px; z-index: 20001; border:0; }");
document.writeln(".top_bar .top_menu>li>a:hover, .top_bar .top_menu>li>a:active { background-color:#333; }");
document.writeln(".menu_font li a:hover, .menu_font li a:active { background-color:#333; }");
document.writeln(".menu_font li:first-of-type a { border-radius:5px 5px 0 0; }");
document.writeln(".menu_font li:last-of-type a { border-radius:0 0 5px 5px; }");
document.writeln("#plug-wrap { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0); z-index:800; }");
document.writeln("#cate18 .device {bottom: 40px;}");
document.writeln("#cate18 #indicator {bottom: 240px;}");
document.writeln("#cate19 .device {bottom: 40px;}");
document.writeln("#cate19 #indicator {bottom: 330px;}");
document.writeln("#cate19 .pagination {bottom: 60px;}");
document.writeln("#cate60 .device {bottom: 55px;}");
document.writeln("#cate61 .device {bottom: 55px;}");
document.writeln("#cate74 .device {bottom: 55px;}");
document.writeln("#cate75 .device {bottom: 55px;}");
document.writeln("#cate63 #indicator {bottom: 80px;}");
document.writeln("</style>");
document.writeln("<div id=\"sharemcover\" onClick=\"document.getElementById(\'sharemcover\').style.display=\'\';\" style=\" display:none\"><img src=\"http://img.ishangtong.com/images/MgnnofmleM.png\"></div>");
document.writeln("<div class=\"top_bar\" style=\"-webkit-transform:translate3d(0,0,0)\">");
document.writeln("  <nav>");
document.writeln("    <ul id=\"top_menu\"  class=\"top_menu\">");document.writeln("    	<li> <a   onClick=\"javascript:displayit(0)\" ><img src=\"http://img.ishangtong.com/baeimages/IbWvMcfJVC.png\"><label>商家入驻</label></a>");
document.writeln("        	<ul id=\"menu_list0\" class=\"menu_font\" style=\" display:none\">");document.writeln("                <li> <a href=\"http://www.dwz.cn/n83Us\"><img src=\"http://img.ishangtong.com/baeimages/L5Zn3q3mDm.png\" ><label>我们地址</label></a></li>");
document.writeln("                <li> <a href=\"tel:18657099251\"><img src=\"http://img.ishangtong.com/baeimages/GckUWhdhPS.png\" ><label>联系电话</label></a></li>");
document.writeln("                <li> <a href=\"http://comment.duapp.com/?openid=fromUsername&refex=mp.weixin.qq.com&amp;wxid=5c7c14f3e4478a9ac7adad88d16cb6fb\"><img src=\"http://img.ishangtong.com/baeimages/IIryNeigXS.png\" ><label>咨询留言</label></a></li>");
document.writeln("            </ul>");
document.writeln("        </li>");
document.writeln("    	<li> <a   onClick=\"javascript:displayit(1)\" ><img src=\"http://img.ishangtong.com/baeimages/k3PlSiKIPy.png\"><label>使用帮助</label></a>");
document.writeln("        	<ul id=\"menu_list1\" class=\"menu_font\" style=\" display:none\">");document.writeln("                <li> <a href=\"http://www.2studio.com/wx.php?ac=news1&amp;w=2&amp;tid=508963\"><img src=\"http://img.ishangtong.com/baeimages/9ujht5y43X.png\" ><label>抽奖详解</label></a></li>");
document.writeln("                <li> <a href=\"http://www.2studio.com/wx.php?ac=news1&amp;w=2&amp;tid=508965\"><img src=\"http://img.ishangtong.com/baeimages/mlbj1FG1dz.png\" ><label>特权说明</label></a></li>");
document.writeln("            </ul>");
document.writeln("        </li>");
document.writeln("    	<li> <a   onClick=\"javascript:displayit(2)\" ><img src=\"http://img.ishangtong.com/baeimages/pqjEGr5twQ.png\"><label>便民发布</label></a>");
document.writeln("        	<ul id=\"menu_list2\" class=\"menu_font\" style=\" display:none\">");document.writeln("                <li> <a href=\"http://mp.weixin.qq.com/s?__biz=MjM5NzAxNDE2MA==&amp;mid=200296323&amp;idx=2&amp;sn=fb313d5f3143592b63174502742fc26c#rd\"><img src=\"http://img.ishangtong.com/baeimages/EcTKRQdxRK.png\" ><label>客运查询</label></a></li>");
document.writeln("                <li> <a href=\"http://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5NzAxNDE2MA==&amp;appmsgid=10000762&amp;itemidx=1&amp;sign=99de27254e6d7c07e2106bbca79ad2f7#wechat_redirect\"><img src=\"http://img.ishangtong.com/baeimages/Muy2GdAgKY.png\" ><label>公共自行车</label></a></li>");
document.writeln("                <li> <a href=\"http://wx.wsq.qq.com/159428194?filterType=34402\"><img src=\"http://img.ishangtong.com/baeimages/2yFKO6TwKI.png\" ><label>二手信息</label></a></li>");
document.writeln("                <li> <a href=\"http://img.ishangtong.com/baeimages/tubiao_hong/jiaoyu/21.png\"><img src=\"http://img.ishangtong.com/baeimages/7rIznPyShS.png\" ><label>求职招聘</label></a></li>");
document.writeln("            </ul>");
document.writeln("        </li>");
document.writeln("    	<li> <a   href=\"http://www.2studio.com/wx.php?ac=news1&amp;w=2&amp;tid=508965\"  ><img src=\"http://img.ishangtong.com/baeimages/7rIznPyShS.png\"><label>乐活No.1</label></a>");
document.writeln("        	<ul id=\"menu_list3\" class=\"menu_font\" style=\" display:none\">");document.writeln("            </ul>");
document.writeln("        </li>");
document.writeln("    </ul>");
document.writeln("  </nav>");
document.writeln("</div>");
document.writeln("<div id=\"plug-wrap\" onClick=\"closeall()\" style=\"display: none;\"></div>");
document.writeln("<script>");
document.writeln("function displayit(n){");
document.writeln("	var count = document.getElementById(\"top_menu\").getElementsByTagName(\"ul\").length;	");
document.writeln("	for(i=0;i<count;i++){");
document.writeln("		if(i==n){");
document.writeln("		 if(document.getElementById(\"top_menu\").getElementsByTagName(\"ul\").item(n).style.display==\'none\'){");
document.writeln("			 document.getElementById(\"top_menu\").getElementsByTagName(\"ul\").item(n).style.display=\'\';");
document.writeln("			 document.getElementById(\"plug-wrap\").style.display=\'\';");
document.writeln("			}else{");
document.writeln("				 document.getElementById(\"top_menu\").getElementsByTagName(\"ul\").item(n).style.display=\'none\';");
document.writeln("				  document.getElementById(\"plug-wrap\").style.display=\'none\';");
document.writeln("			}");
document.writeln("		}else{");
document.writeln("			document.getElementById(\"top_menu\").getElementsByTagName(\"ul\").item(i).style.display=\'none\';");
document.writeln("		}");
document.writeln("	}");
document.writeln("}");
document.writeln("function closeall(){");
document.writeln("	var count = document.getElementById(\"top_menu\").getElementsByTagName(\"ul\").length;	");
document.writeln("	for(i=0;i<count;i++){");
document.writeln("		 document.getElementById(\"top_menu\").getElementsByTagName(\"ul\").item(i).style.display=\'none\';");
document.writeln("	}");
document.writeln("	 document.getElementById(\"plug-wrap\").style.display=\'none\';");
document.writeln("}");
document.writeln("");
document.writeln("");
document.writeln("document.addEventListener(\'WeixinJSBridgeReady\', function onBridgeReady() {");
document.writeln("WeixinJSBridge.call(\'hideToolbar\');");
document.writeln("});");
document.writeln("</script> ");