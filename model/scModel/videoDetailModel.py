from pages.basePage import Action
from element.sc_copyright.sc_home_element import SCHomePageElement

class VideoDetailModel(Action):
    # 在视频详情获取视频名称
    def get_video_name(self):
        try:
            video_name = self.getText(SCHomePageElement.video_name_xpath)
        except:
            video_name = ""
        return video_name
    # 在视频详情获取视频ID
    def get_video_id(self):
        try:
            video_id = self.getText(SCHomePageElement.video_id_xpath)
        except:
            video_id = ""
        return video_id
