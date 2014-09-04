# Create your views here.
# -*- coding: utf-8 -*-
import hashlib
import urllib2
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext, Template
from django.utils.encoding import smart_str, smart_unicode
import hashlib
from django.shortcuts import render_to_response
from xml.etree import ElementTree as etree
@csrf_exempt

def weixin(request):
    if request.method == 'GET':
        response = HttpResponse(checkSignature(request))
        return response
    else:
       xmlstr = smart_str(request.body)
       xml = etree.fromstring(xmlstr)
       ToUserName = xml.find('ToUserName').text
       FromUserName = xml.find('FromUserName').text
       CreateTime = xml.find('CreateTime').text
       MsgType = xml.find('MsgType').text
      # Content = xml.find('Content').text
       # MsgId = xml.find('MsgId').text
       if  MsgType == "event":
           mscontent = xml.find("Event").text
           if mscontent == "subscribe":
               replayText = u"欢迎关注本微信，你们有什么好的文章也欢迎反馈给我,我会不定期的分享给大家。输入L获得帮助信息。"
               return render_to_response("text.xml", {'ToUserName': FromUserName, "FromUserName":ToUserName, "CreateTime":CreateTime, "Content":replayText})

       if  MsgType == "text":
           content = xml.find("Content").text
           if  content == 'hi':
               replayText = u"你好"
               return render_to_response("text.xml", {'ToUserName': FromUserName, "FromUserName":ToUserName, "CreateTime":CreateTime, "Content":replayText})
           if  content == 'L'or content=='?':
               replayText = u"回复\n1: 健康百科\n2: 健康资讯\n3: 健康微店"
               return render_to_response("text.xml", {'ToUserName': FromUserName, "FromUserName":ToUserName, "CreateTime":CreateTime, "Content":replayText})
           else:
                ArticleCount = 1
                Title = "每天健康，每天新鲜"
                Description = "关注健康管理吧，了解最新的健康管理资讯，普及全面的健康管理知识。"
                Url = "http://115.29.164.186"
                PicUrl = "http://www.yanzhouren.org/images/688/688/upload/page/39/d8/e1/8b/ori_d8e18b60.jpg"
           return render_to_response("news.xml", {'ToUserName': FromUserName, "FromUserName":ToUserName, "CreateTime":CreateTime, "ArticleCount":ArticleCount, "Title":Title, "Description":Description, "PicUrl":PicUrl, "Url":Url})
def xiaohuangji(ask):
    ask = ask.encode('UTF-8')
    enask = urllib2.quote(ask)
    baseurl = r'http://www.simsimi.com/func/req?msg='
    url = baseurl + enask + '&lc=ch&ft=0.0'
    resp = urllib2.urlopen(url)
    # reson = json.loads(resp.read())
    return  None


def checkSignature(request):
    signature = request.GET.get('signature', None)
    timestamp = request.GET.get('timestamp', None)
    nonce = request.GET.get('nonce', None)
    echostr = request.GET.get('echostr', None)
    # 这里的token我放在setting，可以根据自己需求修改
    token = "pxy"

    tmplist = [token, timestamp, nonce]
    tmplist.sort()
    tmpstr = "%s%s%s" % tuple(tmplist)
    tmpstr = hashlib.sha1(tmpstr).hexdigest()
    if tmpstr == signature:
        return echostr
    else:
        return None
