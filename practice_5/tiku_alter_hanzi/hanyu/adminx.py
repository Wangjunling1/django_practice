# from django.contrib import admin
from hanyu.models import Word,Phrase,Idiom,SchoolOverview
import xadmin
# Register your models here.
from xadmin import views

class WordAdmin(object):
    list_display=['word_name','pinyin','duyin',]
    search_fields=['word_name','pinyin','duyin',]
    list_filter=['word_name','pinyin','duyin',]

class PhraseAdmin(object):
    list_display=['phrase_name','pinyin','duyin','tag']
    search_fields=['phrase_name','pinyin','duyin','tag']
    list_filter=['phrase_name','pinyin','duyin','tag']

class IdiomAdmin(object):
    list_display=['idiom_name','pinyin','duyin','tag']
    search_fields=['idiom_name','pinyin','duyin','tag']
    list_filter=['idiom_name','pinyin','duyin','tag']

class SchoolOverviewAdmin(object):
    list_display=['key']
    search_fields=['key']
    list_filter=['key']

class GlobalSetting(object):
    site_title = u'阿凡题'
    site_footer = u'海南云江科技'
    site_header = u'阿凡题'
    menu_style = 'accordion'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(Word, WordAdmin)
xadmin.site.register(Phrase, PhraseAdmin)
xadmin.site.register(Idiom, IdiomAdmin)
xadmin.site.register(SchoolOverview, SchoolOverviewAdmin)