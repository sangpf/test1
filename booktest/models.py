from django.db import models

# Create your models here.

'''自定义管理器'''
class BookInfoManager(models.Manager):
    # 情况二：修改管理器返回的原始查询集：重写get_queryset()
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)
    # 新增
    def create_book(self, title, pub_date):
        book = self.model()
        book.btitle = title
        book.bpub_date = pub_date
        book.bread=0
        book.bcommet=0
        book.isDelete = False
        return book

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    # 自定义管理器
    books = BookInfoManager()


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')


