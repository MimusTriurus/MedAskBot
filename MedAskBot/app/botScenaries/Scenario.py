from datetime import datetime
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from time import gmtime, strftime

class Scenario( object ) :
    def __init__( self ) :
        self.BOT = 'bot'
        self.HUMAN = 'human'
        self.DEF_TEMPLATE = 'app/baseMessage.html'
        self.data = []
        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/baseMessage.html',
            'data'      : 'Здравствуйте <b>Александр Владимирович</b>'
                '<p>[Авиценнов Александр Владимирович. Врач-терапевт. п.н. 0184]</p>',
            'txt' : 'вита',
            'delay' : '1500'
        } )
        self.data.append( {
            'type'      : self.HUMAN,
            'template'  : 'app/baseMessage.html',
            'data'      : 'рассчитай <b><span class="ner">риск ишемического инсульта</span></b> '
                'для <b><span class="ner">Петрова Николая Владимировича 1989 года</span></b> рождения',
            'txt'       : 'рассчитай риск ишемического инсульта '
                'для петрова николая владимировича восемьдесят девятого года рождения',
            'delay' : '2000'
        } )
        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/baseMessage.html',
            'data'      : 'CHA<font size="2">2</font>DS<font size="2">2</font>-VASc <b>Петров Н.В. 10.02.1989</b>'
                '<p>Набрано: <b>6</b> баллов. Ожидаемая частота инсультов за год - <b>9.8%</b>.</p>'
                '<p><u>Рекомендуется прием витамина К (варфарин) с целевым МНО 2.5 (2.0-3.0)</u></p>',
            'txt' : '',
            'delay' : '3000'
        } )
        self.data.append( {
            'type'      : self.HUMAN,
            'template'  : 'app/baseMessage.html',
            'data'      : 'дай оценку <b><span class="ner">риска кровотечения</span></b>',
            'txt'       : 'дай оценку риска кровотечения',
            'delay' : '1000'
        } )
        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/baseMessage.html',
            'data'      : 'Шкала HAS-BLED <b>Петров Н.В. 10.02.1989</b>'
                '<p>Набрано: <b>3</b> балла. Риск: <b>5.8%</b></p>'
                '<p><u>Следует рассмотреть альтернативы антикоагулянтной терапии. Пациент имеет высокий риск кровотечения</u></p>',
            'txt' : '',
            'delay' : '2000'
        } )
        self.data.append( {
            'type'      : self.HUMAN,
            'template'  : 'app/baseMessage.html',
            'data'      : 'рассчитай <span class="ner"><b>скорость инфузии</b></span> '
               'для <span class="ner"><b>100 миллилитров</b></span> раствора '
               'время введения <span class="ner"><b>5 часов</b></span>',
            'txt'       : 'рассчитай скорость инфузии '
               'для ста миллилитров раствора '
               'время введения пять часов',
            'delay' : '2000'
        } )
        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/baseMessage.html',
            'data'      : '<span class="resVal"><b>16.7</b></span> капель в минуту'
                '<p><span class="resVal"><b>0.28</b></span> капель в секунду</p>',
            'txt' : '',
            'delay' : '2500'
        } )
        self.data.append( {
            'type'      : self.HUMAN,
            'template'  : 'app/baseMessage.html',
            'data'      : 'рассчитай <span class="ner"><b>СКФ</b></span> '
                'для <span class="ner"><b>мужчины 32 лет</b></span> '
                'с уровнем креатинина сыворотки <span class="ner"><b>82 мкмоль/л</b></span>',
            'txt'       : 'рассчитай скф '
                'для мужчины тридцати двух лет '
                'с уровнем креатинина сыворотки восемьдесят два микромоль на литр',
            'delay' : '2000'
        } )
        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/baseMessage.html',
            'data'      : '<b>СКФ</b> = <span class="resVal">94 мл/мин/1.73 м2</span>'
                '<p><b>Стадия ХБП:</b> <span class="resVal"><b>I</b></span></p>'
                '<p><u>при наличии факторов риска или повреждение почек с нормальной почечной функцией</u></p>',
            'txt' : '',
            'delay' : '3000'
        } )
        self.data.append( {
            'type'      : self.HUMAN,
            'template'  : 'app/baseMessage.html',
            'data'      : 'какие <span class="ner"><b>противопоказания</b></span> '
                'и <span class="ner"><b>особые указания</b></span> у'
                ' <span class="ner"><b>Изопринозина</b></span>',
            'txt' : 'какие противопоказания '
                'и особые указания у'
                ' изопринозина',
            'delay' : '2000'
        } )
        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/baseMessage.html',
            'data'      : '<b>Противопоказания:</b>'
                '<ul>'
                    '<li>мочекаменная болезнь;</li>'
                    '<li>подагра;</li>'
                    '<li>аритмии;</li>'
                    '<li>хроническая почечная недостаточность.</li>'
                '</ul>'
                '<p><b>Особые указания:</b></p>'
                '<ul>'
                    '<li>влияние на способность к вождению автотранспорта и управлению механизмами</li>'
                '</ul>',
            'txt' : '',
            'delay' : '3000'
        } )
        self.data.append( {
            'type'      : self.HUMAN,
            'template'  : 'app/baseMessage.html',
            'data'      : 'подготовь рецепт для <span class="ner"><b>Петрова Николая Владимировича</b></span> '
                '<span class="ner"><b>1989</b></span> года рождения '
                'назначь <span class="ner"><b>30 таблеток Изопринозина</b></span> '
                'по <span class="ner"><b>500 мг.</b></span> '
                'принимать <span class="ner"><b>внутрь по одной таблетке утром</b></span> '
                'рецепт действителен <span class="ner"><b>1 месяц</b></span>',
            'txt' : 'подготовь рецепт для петрова николая владимировича '
                'восемьдесят девятого года рождения '
                'назначь тридцать таблеток изопринозина '
                'по пятьсот миллиграмм '
                'принимать внутрь по одной таблетке утром '
                'рецепт действителен один месяц',
            'delay' : '3000'
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
            'txt'       : '',
            'delay'     : '4000'
        } )
        return

    def getHtmlData( self, step ) :
        i = int( step )
        if i >= len( self.data ) :
            return {}
        params = self.data[ i ]
        params[ 'date' ] = datetime.today().strftime("%H:%M %d.%m.%y")
        htmlData = {}
        htmlData[ 'type' ] = params.get( 'type', self.BOT )
        htmlData[ 'htmlData' ] = render_to_string( params.get( 'template', self.DEF_TEMPLATE ), params )
        htmlData[ 'txt' ] = params.get( 'txt', '' )
        htmlData[ 'delay' ] = params.get( 'delay', '2000' )

        return htmlData


