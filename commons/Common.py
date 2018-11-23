import logging
from utils.ReturnCode import ReturnCode


class Common:
    _log = logging.getLogger('Common')

    @staticmethod
    def response(statusCode=0, msg=None, data=None):
        """
                回傳代碼及代碼轉換後的對應訊息
                :param statusCode:
                :param msg:
                :param data:
                :return:
                """
        Common._log.info("Common response()")
        return ReturnCode.getResp(statusCode, msg, data)