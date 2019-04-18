class EHost(object):

    def goodMorning(self,name):
        '''Say good morning to guests'''
        return 'good morning, %s' % name


# if __name__ == '__main__':
#     h = EHost()
#     hi = h.goodMorning('sdadasd')
#     print(hi)


from zope.interface import Interface
from zope.interface.declarations import implementer

class IHost(Interface):
    def goodMorning(self,name):
        '''Say good morning to host'''


@implementer(IHost)
class Host:
    def goodMorning(self,name):
        """Say good morning to guests"""
        return 'good morning2: %s!' % name


if __name__ == '__main__':
    o = Host()
    eqw = o.goodMorning('请问啊')
    print(eqw)

