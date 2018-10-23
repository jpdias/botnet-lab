/* jshint strict: true */
/* globals console */

var sendchat = (function() {
	var connection = new WebSocket('ws://'+window.location.host+'/ircbridge');
	window.addEventListener("unload", connection.close);

	connection.onopen = function(){
		console.log("Connection opened!");
	};

	connection.onclose = function(){
		console.log("Connection closed");
	};

	connection.onerror = function() {
		console.log("Error detection");
	};

	connection.onmessage = function(e){
		if ( e !== undefined ) {
			var message = JSON.parse(e.data);
			switch ( message.type ){
				case "join":
					$("#chatbox")
						.append("<span class=\"chat_notice\">" + message.user + " has joined the room.</span><br />");
					$("#userlist")
						.append("<span id=\""+message.user+"_list\">"+message.user+"</span><br />");
					break;

				case "part":
					$("#chatbox")
						.append("<i><span class=\"chat_notice\">"+message
														.user+" has left the room.</span></i><br />");
					$("#userlist").remove("#"+message.user+"_list");
					break;

				case "chat":
					$("#chatbox")
						.append("<strong><span style=\"color: blue;\">"+message.
														user+":</strong></span> " + message
														.message + "<br />");
					break;

        case "notice":
          $("chatbox")
            .append("<strong><span style=\"color: red;\">"+message.message+"<br />");
          break;

        case "PMoutbound":
          $("chatbox")
            .append("&gt;"+message.user+"&lt; "+message.message+"<br />");
          break;

        case "PMinbound":
          $("chatbox")
            .append("&lt;"+message.user+"&gt; "+message.message+"<br />");
          break;


				default:
					console.log("Malformed message from server \""+message+"\"");
			}
			$("#chatbox").animate({scrollTop: $("#chatbox")[0].scrollHeight}, 200); //scroll down
		}
	};

	return connection.send.bind(connection);
}());
