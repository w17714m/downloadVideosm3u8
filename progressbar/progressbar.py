from util.banner import fy, sb, fc


class ProgressBar(object):
    def __init__(self):
        self.iteration = 0
        self.total = 0

    def printProgressBar(self, iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s%s%s |%s| %s%% %s' % (fy, sb, prefix, bar, percent, suffix))
        if iteration == total:
            print("%s%s::::::::::Completado::::::::::" % (fc, sb))

