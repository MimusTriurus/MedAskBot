var botui = new BotUI('botContainer');

var step = -1;
var BOT_AREA_ID = 'botArea';

function initSpeechKITT( styleFPath ) {
    SpeechKITT.setStartCommand(function () { recognition.start() });
    SpeechKITT.setAbortCommand(function () { recognition.abort() });
    //recognition.addEventListener('start', SpeechKITT.onStart);
    //recognition.addEventListener('end', SpeechKITT.onEnd);
    SpeechKITT.setStylesheet(styleFPath);
    SpeechKITT.vroom();
}

function addBotHtmlMessageBox( htmlData, d ) {  
    botui.message
        .bot({
            delay: d,
            type: 'html',
            content: htmlData
        })
        .then(function (index) {
            SpeechKITT.onEnd();
            var elem = document.getElementById(BOT_AREA_ID);
            elem.scrollTop = elem.scrollHeight;
        });
}

function addHumanHtmlMessageBox( htmlData, d ) {
    botui.message.human({
        delay: d,
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
            return step++;
    }
}

function sendRequest(keycode) {
    var http = new XMLHttpRequest( );
    var url = '/receive';
    makeStepByKeyCode(keycode);
    var params = 'step=' + step;
    http.open( 'POST', url, true );
    http.setRequestHeader( 'Content-type', 'application/x-www-form-urlencoded' );
    http.onreadystatechange = function ( ) {
        if (http.readyState == 4 && http.status == 200) {
            var result = JSON.parse(http.responseText);
            var delay = Number(result['delay']);
            var htmlData = result['htmlData'];
            console.log(delay);
            if (result['type'] == 'bot') {
                addBotHtmlMessageBox(htmlData, delay);
            }
            else {
                addHumanHtmlMessageBox(htmlData, delay);
                sendRequest(39);
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