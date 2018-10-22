from django.db import models

class Schedule(models.Model):

    # 開始日
    start_date = models.DateField()

    # 終了日
    end_date = models.DateField()

    # 内容
    content = models.CharField(max_length=10)


class MenuItemHeader(models.Model):
    class Meta:
        verbose_name = '付箋(大分類)'
        verbose_name_plural = '付箋(大分類)s'
        ordering = ['order_number']

    # ラベル
    label = models.CharField(max_length=10)

    # 属性
    attributes = models.CharField(max_length=255,blank=True)

    # サムネイル
    thumbnail = models.CharField(max_length=255,blank=True)

    # 並び順
    order_number = models.IntegerField()

    def __str__(self):
        return self.label

class MenuItem(models.Model):
    class Meta:
        verbose_name = '付箋(小分類)'
        verbose_name_plural = '付箋(小分類)s'
        ordering = ['order_number']


    # 付箋種別
    item_type = models.CharField(max_length=10)

    # URL
    url = models.CharField(max_length=255)

    # sub URL(右ページ)
    url_sub = models.CharField(max_length=255,blank=True)

    # ラベル
    label = models.CharField(max_length=10)

    # 属性
    attributes = models.CharField(max_length=255,blank=True)

    # サムネイル
    thumbnail = models.CharField(max_length=255,blank=True)

    # 並び順
    order_number = models.IntegerField()

    def __str__(self):
        return self.label

class User(models.Model):
    # 名前
    name = models.CharField(max_length=50,blank=True)

    # パスワード
    password = models.CharField(max_length=50)


