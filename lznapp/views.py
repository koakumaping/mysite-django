# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext, Template
from django.utils.encoding import smart_str, smart_unicode
import hashlib
import urllib2

from xml.etree import ElementTree as etree
@csrf_exempt

def weixin(request):
    if request.method=='GET':
        response=HttpResponse(checkSignature(request))
        return response
    else:
       xmlstr = smart_str(request.body)
       xml = etree.fromstring(xmlstr)
       ToUserName = xml.find('ToUserName').text
       FromUserName = xml.find('FromUserName').text
       CreateTime = xml.find('CreateTime').text
       MsgType = xml.find('MsgType').text
      # Content = xml.find('Content').text
       #MsgId = xml.find('MsgId').text
       if  MsgType =="event":
           mscontent = xml.find("Event").text
           if mscontent == "subscribe":
               replayText = u"欢迎关注本微信，你们有什么好的文章也欢迎反馈给我,我会不定期的分享给大家。输入L获得帮助信息。"
               reply_xml = """<xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[%s]]></Content>
            </xml>"""%(FromUserName,ToUserName,CreateTime,replayText)
               return HttpResponse(reply_xml)

       if  MsgType =="text":
           content = xml.find("Content").text
           if  content =='hi':
               replayText = u"你好"
               reply_xml = """<xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[%s]]></Content>
            </xml>"""%(FromUserName,ToUserName,CreateTime,replayText)
               return HttpResponse(reply_xml)
           if  content =='L':
               replayText = u"回复\n1: 健康百科\n2: 健康资讯\n3: 健康微店"
               reply_xml = """<xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[%s]]></Content>
            </xml>"""%(FromUserName,ToUserName,CreateTime,replayText)
               return HttpResponse(reply_xml)
           else:
                articleCount = 1
                title = "每天健康，每天新鲜"
                des = "关注健康管理吧，了解最新的健康管理资讯，普及全面的健康管理知识。"
                Url = "http://www.baidu.com/"
                replay_xml= """<xml>
             <ToUserName><![CDATA[%s]]></ToUserName>
             <FromUserName><![CDATA[%s]]></FromUserName>
             <CreateTime>%s</CreateTime>
             <MsgType><![CDATA[news]]></MsgType>
             <ArticleCount><![CDATA[%s]]></ArticleCount>
             <Articles>
             <item>
             <Title><![CDATA[%s]]></Title>
             <Description><![CDATA[%s]]></Description>
             <PicUrl><![CDATA[http://d.hiphotos.baidu.com/news/pic/item/a5c27d1ed21b0ef49b8bfffadfc451da81cb3e36.jpg]]></PicUrl>
             <Url><![CDATA[%s]]></Url>
             </item>
             </Articles>
             </xml> """%(FromUserName,ToUserName,CreateTime,articleCount,title,des,Url)
                return HttpResponse(replay_xml)
def xiaohuangji(ask):
    ask = ask.encode('UTF-8')
    enask = urllib2.quote(ask)
    baseurl = r'http://www.simsimi.com/func/req?msg='
    url = baseurl+enask+'&lc=ch&ft=0.0'
    resp = urllib2.urlopen(url)
    #reson = json.loads(resp.read())
    return  None


def checkSignature(request):
    signature=request.GET.get('signature',None)
    timestamp=request.GET.get('timestamp',None)
    nonce=request.GET.get('nonce',None)
    echostr=request.GET.get('echostr',None)
    #这里的token我放在setting，可以根据自己需求修改
    token="pxy"

    tmplist=[token,timestamp,nonce]
    tmplist.sort()
    tmpstr="%s%s%s"%tuple(tmplist)
    tmpstr=hashlib.sha1(tmpstr).hexdigest()
    if tmpstr==signature:
        return echostr
    else:
        return None
