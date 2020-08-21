from datetime import datetime
from django.template.loader import render_to_string
from django.template.response import TemplateResponse

class Scenario(object):
    def __init__( self ) :
        self.BOT = 'bot'
        self.HUMAN = 'human'
        self.DEF_TEMPLATE = 'app/baseMessage.html'
        self.data = []
        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/baseMessage.html',
            'data'      : 'Здравствуйте <b>Александр Владимирович</b>'
                '<p>[Авиценнов Александр Владимирович. Врач-терапевт. п.н. 0184]</p>'
        } )
        self.data.append( {
            'type'      : self.HUMAN,
            'template'  : 'app/baseMessage.html',
            'data'      : 'рассчитай <b>риск ишемического инсульта</b> для <b>петрова николая владимировича восемьдесят девятого года</b> рождения'
        } )
        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/baseMessage.html',
            'data'      : 'CHA<font size="2">2</font>DS<font size="2">2</font>-VASc <b>Петров Н.В. 10.02.1989</b>'
                '<p>Набрано: <b>6</b> баллов. Ожидаемая частота инсультов за год - <b>9.8%</b>.</p>'
                '<p><u>Рекомендуется прием витамина К (варфарин) с целевым МНО 2.5 (2.0-3.0)</u></p>'
        } )
        self.data.append( {
            'type'      : self.HUMAN,
            'template'  : 'app/baseMessage.html',
            'data'      : 'дай оценку <b>риска кровотечения</b>'
        } )
        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/baseMessage.html',
            'data'      : 'Шкала HAS-BLED <b>Петров Н.В. 10.02.1989</b>'
                '<p>Набрано: <b>3</b> балла. Риск: <b>5.8%</b></p>'
                '<p><u>Следует рассмотреть альтернативы антикоагулянтной терапии. Пациент имеет высокий риск кровотечения</u></p>'
        } )
        self.data.append( {
            'type'      : self.HUMAN,
            'template'  : 'app/baseMessage.html',
            'data'      : 'рассчитай <font color="black"><b>скорость инфузии</b></font> '
               'для <font color="black"><b>100 миллилитров</b></font> раствора '
               'время введения <font color="black"><b>пять часов</b></font>'
        } )
        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/baseMessage.html',
            'data'      : '<p><font color="black"><b>16.7</b></font> капель в минуту</p>'
                '<p><font color="black"><b>0.28</b></font> капель в секунду</p>'
        } )
        self.data.append( {
            'type'      : self.HUMAN,
            'template'  : 'app/baseMessage.html',
            'data'      : 'рассчитай <font color="black"><b>скф</b></font> '
                'для <font color="black"><b>мужчины тридцати двух лет</b></font> '
                'с уровнем креатинина сыворотки <font color="black"><b>восемьдесят два микромоль на литр</b></font>'
        } )
        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/baseMessage.html',
            'data'      : '<p><b>СКФ</b> = <font color=blue>94 мл/мин/1.73 м2</font></p>'
                '<p><b>Стадия ХБП:</b> <font color="black"><b>I</b></font></p>'
                '<p><u>при наличии факторов риска или повреждение почек с нормальной почечной функцией</u></p>'
        } )
        self.data.append( {
            'type'      : self.HUMAN,
            'template'  : 'app/baseMessage.html',
            'data'      : 'Какие <font color="black"><b>противопоказания</b></font> '
                'и <font color="black"><b>особые указания</b></font> у'
                ' <font color="black"><b>изопринозина</b></font>?'
        } )
        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/baseMessage.html',
            'data'      : '<p><b>Противопоказания:</b></p>'
                '<ul>'
                    '<li>мочекаменная болезнь;</li>'
                    '<li>подагра;</li>'
                    '<li>аритмии;</li>'
                    '<li>хроническая почечная недостаточность.</li>'
                '</ul>'
                '<p><b>Особые указания:</b></p>'
                '<ul>'
                    '<li>влияние на способность к вождению автотранспорта и управлению механизмами</li>'
                '</ul>'
        } )
        self.data.append( {
            'type'      : self.HUMAN,
            'template'  : 'app/baseMessage.html',
            'data'      : 'подготовь рецепт для <font color="black"><b>петрова николая владимировича</b></font> '
                '<font color="black"><b>восемьдесят девятого</b></font> года рождения '
                'назначь <font color="black"><b>тридцать таблеток изопринозина</b></font> по <font color="black"><b>пятьсот миллиграмм</u></font> '
                'принимать <font color="black"><b>внутрь по одной таблетке утром</b></font> '
                'рецепт действителен <font color="black"><b>1 месяц</b></font>'
        } )
        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/recipe.html',
            'date'      : datetime.now( ).strftime( "%d.%m.%y" ),
            'patient'   : 'Петров Н.В.',
            'yearsOld'  : '31',
            'recipe'    : 'Isoprinosini 0,5 D.t.d. N 30 in tab.',
            'signa'     : 'Внутрь по 1 таблетке утром',
            'validity'  : '1 месяц',
        } )
        return

    def getHtmlData( self, step ) :
        i = int( step )
        if i >= len( self.data ) :
            return {}
        params = self.data[ i ]
        htmlData = {}
        htmlData[ 'type' ] = params.get( 'type', self.BOT )
        htmlData[ 'htmlData' ] = render_to_string( params.get( 'template', self.DEF_TEMPLATE ), params )
        return htmlData


