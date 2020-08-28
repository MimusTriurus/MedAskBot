var botui = new BotUI('botContainer');

var step = 10;
var BOT_AREA_ID = 'botArea';

function initSpeechKITT( styleFPath ) {
    SpeechKITT.setStartCommand( function ( ) { recognition.start( ) } );
    SpeechKITT.setAbortCommand( function ( ) { recognition.abort( ) } );
    //recognition.addEventListener('start', SpeechKITT.onStart);
    //recognition.addEventListener('end', SpeechKITT.onEnd);
    SpeechKITT.setStylesheet( styleFPath );
    SpeechKITT.vroom( );
}

function addBotHtmlMessageBox( htmlData, d, audioFile ) {  
    botui.message
        .bot( {
            delay: d,
            loading: false,
            type: 'html',
            content: htmlData
        } )
        .then( function (index) {
            SpeechKITT.onEnd();
            var elem = document.getElementById(BOT_AREA_ID);
            elem.scrollTop = elem.scrollHeight;

            if (audioFile != '') {
                var player = document.getElementById("player");
                player.src = audioFile;
                player.load( );
                player.play( );
            }
            //player.onended = function () { console.log('!!!') };
        } );
}

function addBotButtonsControls() {
    botui.action.button( {
        delay: 100,
        action: [
            {
                text: 'Подтвердить',
                value: 'yes'
            },
            {
                text: 'Отклонить',
                value: 'no'
            }
        ]
    } );
}

function addHumanHtmlMessageBox( htmlData, d ) {
    botui.message.human({
        delay: d,
        loading: true,
        type: 'html',
        content: htmlData
    }).then(function () {
        SpeechKITT.onEnd();
        var elem = document.getElementById(BOT_AREA_ID);
        elem.scrollTop = elem.scrollHeight;
    });
}

function makeStepByKeyCode(keycode) {
    switch (keycode) {
        case 37:
            if (step > 0)
                return step--;
            break;
        case 39:
                return step++;
            break;
        default:
            return -1;
    }
}

function sendRequest(keycode) {
    var s = makeStepByKeyCode(keycode);
    if (s==-1)
        return;
    var http = new XMLHttpRequest( );
    var url = '/receive';
    var params = 'step=' + step;
    http.open( 'POST', url, true );
    http.setRequestHeader( 'Content-type', 'application/x-www-form-urlencoded' );
    http.onreadystatechange = function ( ) {
        if (http.readyState == 4 && http.status == 200) {
            var result = JSON.parse(http.responseText);
            var delay = Number(result['delay']);
            var htmlData = result['htmlData'];
            var audioFile = result[ 'audioFile' ];
            switch (result['type']) {
                case 'bot':
                    addBotHtmlMessageBox(htmlData, delay, audioFile);
                    break;
                case 'human':
                    addHumanHtmlMessageBox(htmlData, delay);
                    sendRequest(39);
                    break;
            }
            var txt = result['txt'];
            if (txt != '') {
                SpeechKITT.setInstructionsText(txt);
                SpeechKITT.onStart();
            }
        }
    }
    http.send( params );
}

function onPlayerEnd() {
    console.log('play end');
}