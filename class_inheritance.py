# Inheritance
class YG:
    def girl_group(self):
        print("Girl group")
    def boy_group(self):
        print("Boy group")

class BlackLabel(YG):
    def co_op(self):
        print("Co op group contain both boy and girls")
        
allday_project = BlackLabel()
allday_project.co_op()
blackpink = YG()
blackpink.girl_group()