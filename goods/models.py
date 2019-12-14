from datetime import datetime
from django.db import models

class GoodsCategroy(models.Model):
    """
    商品类别
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别编码", help_text="类别编码")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE,null=True, blank=True, verbose_name="父类", related_name="sub_cat")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategroyBrand(models.Model):
    name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌名")
    desc = models.TextField(default="", verbose_name="品牌描述", help_text="品牌描述")
    image = models.ImageField(upload_to='brand/images/', max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    category = models.ForeignKey(GoodsCategroy,on_delete=models.CASCADE, null=True, blank=True, verbose_name="商品类目")
    goods_sn = models.CharField(max_length=50, default='', verbose_name="商品编码")
    name = models.CharField(max_length=300, verbose_name='商品名称')
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存量")
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    shop_price = models.FloatField(default=0, verbose_name="本店售价")
    goods_brief = models.TextField(max_length=500, verbose_name="商品描述")
    # goods_des=models.TextField(verbose_name="内容",default="")
    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")
    goods_front_image = models.ImageField(upload_to="goods/front/", null=True, blank=True, verbose_name="封面图")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品",
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE,verbose_name="商品", related_name="images")
    image = models.ImageField(upload_to="goods/images/", verbose_name="图片", null=True, blank=True)
    image_url = models.CharField(max_length=300, null=True, blank=True, verbose_name="图片地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE,verbose_name="商品")
    image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播图片")

    class Meta:
        verbose_name = "轮播商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
