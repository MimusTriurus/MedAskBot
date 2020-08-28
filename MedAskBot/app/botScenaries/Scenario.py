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
                '<p>[Авиценнов Александр Владимирович. Врач-терапевт. Н.Т. 000130]</p>',
            'txt' : 'вита',
            'delay' : '1500',
            'audioFile' : '',
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
            'data'      : 'CHA<font size="2">2</font>DS<font size="2">2</font>-VASc '
                '<p><b>Петров Н.В. 10.02.1989</b> 123-456-789 22</p> '
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
            'data'      : 'Шкала HAS-BLED '
                '<p><b>Петров Н.В. 10.02.1989</b> 123-456-789 22</p>'
                '<p>Набрано: <b>3</b> балла. Риск: <b>5.8%</b></p>'
                '<p><u>Следует рассмотреть альтернативы антикоагулянтной терапии. Пациент имеет высокий риск кровотечения</u></p>',
            'txt' : '',
            'delay' : '2000'
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
                'у'
                ' <span class="ner"><b>Пронорана</b></span>',
            'txt' : 'какие противопоказания '
                'у'
                ' пронорана',
            'delay' : '2000'
        } )
        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/baseMessage.html',
            'data'      : '<b>Противопоказания:</b>'
                '<ul>'
                    '<li>коллапс</li>'
                    '<li>острая стадия инфаркта миокарда</li>'
                    '<li>совместный прием с нейролептиками (кроме клозапина)</li>'
                    '<li>детский возраст до 18 лет</li>'
                '</ul>',
            'txt' : '',
            'delay' : '3000'
        } )

        self.data.append( {
            'type'      : self.HUMAN,
            'template'  : 'app/baseMessage.html',
            'data'      : 'проверь <span class="ner"><b>наличие препарата</b></span> '
                'в ближайших аптеках',
            'txt' : 'проверь наличие препарата в ближайших аптеках',
            'delay' : '1000'
        } )

        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/baseMessage.html',
            'data'      : '<ul>'
                        '<li><b>Более 20 упаковок</b> "Самсон-Фарма" ул. Грекова, 8, стр. 2.</li>'
                        '<li><b>Более 20 упаковок</b> "Аптека столицы" Широкая улица, 13к1. </li>'
                        '<li><b>Менее 10 упаковок</b> "Столички" ул. Грекова, 8. </li>'
                        '</ul>',
            'txt'       : '',
            'delay' : '4000'
        } )

        self.data.append( {
            'type'      : self.HUMAN,
            'template'  : 'app/baseMessage.html',
            #####################################
            'data'      : 'подготовь рецепт для <span class="ner"><b>Абакумова Игоря Семеновича</b></span> '
                '<span class="ner"><b>1937</b></span> года рождения '
                'диагноз <span class="ner"><b>болезнь Паркинсона</b></span> '
                'назначь <span class="ner"><b>30 таблеток Пронорана</b></span> '
                'по <span class="ner"><b>50 мг.</b></span> '
                'принимать <span class="ner"><b>по одной таблетке 3 раза в день</b></span> ',
            #####################################
            'txt' : 'подготовь рецепт для абакумова игоря семеновича '
                'тридцать седьмого года рождения '
                'диагноз болезнь паркинсона '
                'назначь тридцать таблеток пронорана '
                'по пятьдесят миллиграмм '
                'принимать внутрь по одной таблетке три раза в день',
            #####################################
            'delay' : '3000'
        } )
        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/recipe.html',
            'series:'   : '46',
            'number'    : '30500859495504224',
            'date'      : datetime.now( ).strftime( "%d.%m.%y" ),
            
            'patient'   : 'Абакумов Игорь Семенович',
            'category'  : '060',
            'birthdate' : '10.10.1937',         
            'snils'     : '133-224-422 09',
            'omsNum'    : '46-19 492888',
            'address'   : '140180, МОСКОВСКАЯ ОБЛ., Г. ЛУХОВИЦЫ',
            'diagnosis' : 'G20.',

            'doctor'    : 'Авиценнов Александр Владимирович',
            'docCode'   : '000130',

            'rp'        : 'Pronoranum',
            'dosen'     : '50 мг №30',
            'dtd'       : 'таблетки с контролируемым высвобождением покрытые оболочкой',
            'signa'     : 'по 1 таблетке 3 раза в день',

            'txt'       : '',
            'delay'     : '4000'
        } )
        
        self.data.append( {
            'type'      : 'controls',
            'template'  : 'app/baseMessage.html',
            'data'      : '',
            'txt'       : '',
            'delay'     : '1000'
        } )

        self.data.append( {
            'type'      : self.BOT,
            'template'  : 'app/imgViewMessage.html',
            'data'      : '',
            'txt'       : '',
            'delay'     : '3000'
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

'''
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
'''


