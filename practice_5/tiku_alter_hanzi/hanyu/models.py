from django.db import models

# Create your models here.
class Word(models.Model):
    word_id=models.CharField(primary_key=True,max_length=128,verbose_name='md5')
    word_name=models.CharField(max_length=128,verbose_name=u'字')
    jiaoyan = models.IntegerField(blank=True, null=True,verbose_name='与新华字典对标过为1')
    pinyin = models.CharField(max_length=128,verbose_name='拼音')
    pinyin_source = models.IntegerField(blank=True, null=True,verbose_name='拼音来源 0：阿凡题 1：新华字典 2：阿凡题人工 3：搜狗人工 4：百度汉语 5：百度百科')
    duyin = models.CharField(max_length=1024,verbose_name='读音')
    duyin_source = models.IntegerField(blank=True, null=True,verbose_name='读音来源')
    bushou = models.CharField(max_length=128,verbose_name='部首')
    bushou_source = models.IntegerField(blank=True, null=True,verbose_name='部首来源')
    bihua = models.IntegerField()
    bihua_source = models.IntegerField(blank=True, null=True)
    bishun = models.CharField(max_length=128)
    bishun_source = models.IntegerField(blank=True, null=True)
    wubi = models.CharField(max_length=128, blank=True, null=True)
    wubi_source = models.IntegerField(blank=True, null=True)
    shiyi = models.TextField(verbose_name='释义')
    shiyi_source = models.IntegerField(blank=True, null=True)
    detail_shiyi = models.TextField(verbose_name='详细释义')
    detail_shiyi_source = models.IntegerField(blank=True, null=True)
    relate_ciyu = models.TextField(verbose_name='涉及的词语')
    relate_ciyu_source = models.IntegerField(blank=True, null=True)
    jyc = models.CharField(max_length=128, blank=True, null=True,verbose_name='近义词')
    jyc_source = models.IntegerField(blank=True, null=True)
    fyc = models.CharField(max_length=128, blank=True, null=True,verbose_name='反义词')
    fyc_source = models.IntegerField(blank=True, null=True)
    jiegou = models.CharField(max_length=128)
    jiegou_source = models.IntegerField(blank=True, null=True)
    wuxing = models.CharField(max_length=128, blank=True, null=True)
    wuxing_source = models.IntegerField(blank=True, null=True)
    fanti = models.CharField(max_length=128, blank=True, null=True)
    fanti_source = models.IntegerField(blank=True, null=True)
    tupian = models.CharField(max_length=1024, blank=True, null=True)
    tupian_source = models.IntegerField(blank=True, null=True)
    gif = models.CharField(max_length=1024, blank=True, null=True,verbose_name='动图')
    num = models.CharField(max_length=100, blank=True, null=True)
    xjz = models.TextField(blank=True, null=True)
    xjz_source = models.IntegerField(blank=True, null=True)
    zitou = models.CharField(max_length=255, blank=True, null=True)
    jiayibi = models.TextField(blank=True, null=True)
    jianyibi = models.TextField(blank=True, null=True)
    duoyinzizuci = models.TextField(blank=True, null=True)
    chaifen = models.CharField(max_length=255, blank=True, null=True)
    pinyinjx = models.CharField(max_length=255, blank=True, null=True)
    jppdanzi = models.TextField(blank=True, null=True)
    jppzuci = models.TextField(blank=True, null=True)
    tydanzi = models.TextField(blank=True, null=True)
    duoyinshiyi = models.TextField(blank=True, null=True)
    duoyinshiyi_source = models.IntegerField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    rank = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.word_id

    class Meta:
        db_table = 'detailed_word'
        managed = 'False'
        verbose_name = '汉字'
        verbose_name_plural = verbose_name

class Phrase(models.Model):
    id=models.CharField(primary_key=True,max_length=11)
    phrase_id=models.CharField(max_length=128,verbose_name='md5')
    phrase_name=models.CharField(max_length=128,verbose_name='词语')
    pinyin=models.CharField(max_length=128,verbose_name='拼音')
    duyin=models.TextField(max_length=128,verbose_name='读音')
    detail_shiyi = models.TextField(blank=True, null=True)
    shiyi = models.TextField(blank=True, null=True)
    chuchu = models.TextField(blank=True, null=True)
    jyc = models.CharField(max_length=1024, blank=True, null=True)
    fyc = models.CharField(max_length=1024, blank=True, null=True)
    liju = models.TextField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True,verbose_name='标签')
    flag = models.CharField(max_length=10, blank=True, null=True)
    xuqiu = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.phrase_id

    class Meta:
        db_table = 'detailed_phrase'
        managed = 'False'
        verbose_name = '词语'
        verbose_name_plural = verbose_name

class Idiom(models.Model):
    idiom_id = models.CharField(primary_key=True, max_length=128)
    idiom_name = models.CharField(unique=True, max_length=128,verbose_name='成语')
    pinyin = models.CharField(max_length=128, blank=True, null=True,
                              verbose_name='拼音')
    duyin = models.CharField(max_length=1024, blank=True,
                             null=True,verbose_name='读音')
    jyc = models.CharField(max_length=1024, blank=True, null=True)
    fyc = models.CharField(max_length=1024, blank=True, null=True)
    detail_shiyi = models.TextField(blank=True, null=True)
    shiyi = models.TextField(blank=True, null=True)
    chuchu = models.TextField(blank=True, null=True)
    liju = models.TextField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True,verbose_name='标签')
    protagonist = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.idiom_id

    class Meta:
        db_table = 'detailed_idiom'
        managed = 'False'
        verbose_name = '成语'
        verbose_name_plural = verbose_name


class SchoolOverview(models.Model):
    id = models.CharField(primary_key=True,max_length=11)
    key = models.CharField(max_length=128,verbose_name='校名')
    title = models.CharField(max_length=128,verbose_name='校名')
    url = models.CharField(max_length=128,verbose_name='对应的落地页')
    name = models.CharField(max_length=128,verbose_name='校名')
    summary = models.TextField(blank=True, null=True,verbose_name='简介')
    level = models.CharField(max_length=128,blank=True, null=True,
                             verbose_name='批次')
    type = models.CharField(max_length=128,blank=True, null=True,
                            verbose_name='类型')
    rank = models.CharField(max_length=128,blank=True, null=True,
                            verbose_name='排名')
    image = models.CharField(max_length=128,blank=True, null=True,
                             verbose_name='校徽')
    class_field = models.CharField(db_column='class', max_length=128,blank=True, null=True
                                   , verbose_name='学校类型')  # Field renamed
    # because it was a Python reserved word.
    fenshuxian1 = models.CharField(max_length=128,blank=True, null=True,
                                   verbose_name='文')
    fenshuxian2 = models.CharField(max_length=128,blank=True, null=True,
                                   verbose_name='理')
    website = models.CharField(max_length=128,blank=True, null=True ,
                               verbose_name='学校网站')
    student = models.CharField(max_length=128,blank=True, null=True ,
                               verbose_name='招生网')
    phone = models.CharField(max_length=128,blank=True, null=True)
    xiaoxun = models.CharField(max_length=128,blank=True, null=True ,
                               verbose_name='校训')
    province = models.CharField(max_length=128,blank=True, null=True ,
                                verbose_name='学校所在地')
    city = models.CharField(max_length=128,blank=True, null=True ,
                            verbose_name='所在地城市')
    morelink = models.CharField(max_length=128,blank=True,
                                null=True,verbose_name='阿凡题落地页')
    location = models.CharField(max_length=128,blank=True,
                                null=True,verbose_name='位置')
    def __str__(self):
        return self.key
    class Meta:
        managed = False
        db_table = 'school_overview'
        verbose_name = '学校'
        verbose_name_plural = verbose_name