var botui = new BotUI( 'botContainer' );

var step = 0;

function addBotHtmlMessageBox( htmlData ) {
    botui.message.bot( {
        delay: 500,
        type: 'html',
        content: htmlData
    } );
}

function addHumanHtmlMessageBox( htmlData ) {
    botui.message.human( {
        delay: 500,
        type: 'html',
        content: htmlData
    } );
}

function sendRequest( ) {
    var http = new XMLHttpRequest( );
    var url = '/receive';
    var params = 'step=' + step++;
    http.open( 'POST', url, true );
    http.setRequestHeader( 'Content-type', 'application/x-www-form-urlencoded' );
    http.onreadystatechange = function ( ) {
        if ( http.readyState == 4 && http.status == 200 ) {
            var result = JSON.parse(http.responseText);
            if ( result[ 'type' ] == 'bot' )
                addBotHtmlMessageBox(result['htmlData']);
            else
                addHumanHtmlMessageBox(result['htmlData']);
        }
    }
    http.send( params );
}

function init( ) {
    botui.message.bot( {
        delay: 500,
        type: 'html',
        content: mess1( ),
    } ).then((index) => {
        botui.message.bot( {
            delay: 1500,
            content: 'Here is the location..'
        } );
    } ).then( ( index ) => {
        botui.message.update( 0, {
            delay: 1500,
            content: 'Here is the location..'
        } );
    } )
}

//init( );
