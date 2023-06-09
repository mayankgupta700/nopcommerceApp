import logging
class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger



# from Utilities.CustomLogger import LogGen
# logger = LogGen.loggen()
# self.logger.info("**************** Test_001_login*******************")  # first things is always TC ID
        # self.logger.info("******************Verifying Homepage Title********************")
# self.logger.info("******************Homepage Title TC is Passed********************")
# self.logger.info("**********************Verifying Login Cedentials****************************")
# self.logger.error("******************Homepage Title TC is Failed********************")
# self.logger.info("***********************Login TC is Passed****************************")
# self.logger.error("***********************Login TC is Failed****************************")