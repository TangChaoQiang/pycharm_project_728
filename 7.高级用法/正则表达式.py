data = '<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;' \
       'charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge>' '<meta content=always name=referrer>' \
       '<link rel=stylesheet type=text/css href=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css>' \
       '<title>百度一下，你就知道</title></head>' \
       ' <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> ' \
       '<div class=s_form> <div class=s_form_wrapper> <div id=lg> ' \
       '<img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> ' \
       '</div> <form id=form name=f action=//www.baidu.com/s class=fm>' \
       ' <input type=hidden name=bdorz_come value=1>' \
       ' <input type=hidden name=ie value=utf-8> ' \
       '<input type=hidden name=f value=8> ' \
       '<input type=hidden name=rsv_bp value=1> ' \
       '<input type=hidden name=rsv_idx value=1> ' \
       '<input type=hidden name=tn value=baidu>' \
       '<span class="bg s_ipt_wr">' \
       '<input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus>' \
       '</span><span class="bg s_btn_wr">' \
       '<input type=submit id=su value=百度一下 class="bg s_btn"></span> '

import re

result = re.search("<title>(.+?)</title></head>", data)
print(result.group())

try:
    print(re.search(".+.com$", "sina.com").group())
    print(re.search("sina|qq|163", "sina.com").group())
    print(re.search("sina|qq|163", "163.com").group())
    print(re.search("sina|qq|163", "qq.com").group())
    print(re.search("sina|qq|163", "swa.com").group())
except:
    print("匹配失败")