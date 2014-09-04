__author__ = 'lzn'

class BaseMsg():
    def __init__(self, xml):
        self.ToUserName = xml.find('ToUserName').text
        self.FromUserName = xml.find('FromUserName').text
        self.CreateTime = xml.find('CreateTime').text
        self.MsgType = xml.find('MsgType').text

class TextMsg(BaseMsg):
    def __init__(self, xml):
        BaseMsg.__init__(self, xml)
        self.Content = xml.find('Content').text

class MediaMsg(BaseMsg):
    def __init__(self, xml):
        BaseMsg.__init__(self, xml)
        self.MediaId = xml.find('MediaId').text

class ImageMsg(MediaMsg):
    def __init__(self, xml):
        MediaMsg.__init__(self, xml)
        self.PicUrl = xml.find('PicUrl').text

class VoiceMsg(MediaMsg)
    def __init__(self, xml):
        MediaMsg.__init__(self, xml)
        self.Format = xml.find('Format').text

class VideoMsg(MediaMsg):
    def __init__(self, xml):
        MediaMsg.__init__(self, xml)
        self.ThumbMediaId = xml.find('ThumbMediaId').text

class LocationMsg(BaseMsg):
    def __init__(self, xml):
        MediaMsg.__init__(self, xml)
        self.Location_X = xml.find('Location_X').text
        self.Location_Y = xml.find('Location_Y').text
        self.Scale = xml.find('Scale').text
        self.Label = xml.find('Label').text

class LinkMsg(BaseMsg):
    def __init__(self, xml):
        MediaMsg.__init__(self, xml)
        self.Title = xml.find('Title').text
        self.Description = xml.find('Description').text
        self.Url = xml.find('Url').text





