/*Utilities file. It stores additional functions used by the application.*/

/*Sends a GET request to an specific url*/
function postData(url, data, callback){
		$.ajax({
	  	type: 'POST',
	  	url: url,
	  	data: data,
      	complete: callback,
	  	dataType: "json"
	});
}

/*Sends a GET request to an specific url*/
function getData(url, data, callback){
	$.ajax({
	  	type: 'GET',
	  	url: url,
	  	data: data,
      	complete: callback,
	  	dataType: "json"
	});
}

function loginHandler(response){
	if(response.status == 200){
		console.log(response.responseJSON['message']);
		localStorage.setItem('loggedIn', true);
		$(".only-investor").show();
		window.location.replace(baseAddress+"portfolio");
		isLoggedIn = true;			
	}else if(response.status == 400){
		alert(response.responseJSON['message']);
	}else if(response.status == 401){
		alert(response.responseJSON['message']);
	}else{
	}
}

function registerHandler(response){
	if(response.status == 201){
		console.log(response.responseJSON['message']);			
	}else if(response.status == 400){
		console.log(response.responseJSON['message']);
	}else if(response.status == 401){
		console.log(response.responseJSON['message']);
	}
}

function registerInvestorHandler(response){
	if(response.status == 201){
		console.log(response.responseJSON['message']);			
	}else if(response.status == 400){
		console.log(response.responseJSON['message']);
	}else if(response.status == 401){
		console.log(response.responseJSON['message']);
	}
}

function issuerHandler(response){
	if(response.status == 201){
		console.log(response.responseJSON['message']);			
	}else if(response.status == 400){
		console.log(response.responseJSON['message']);
	}else if(response.status == 401){
		console.log(response.responseJSON['message']);
	}
}

function executeHandler(response){
	if(response.status == 201){
		console.log(response.responseJSON['message']);			
	}else if(response.status == 400){
		console.log(response.responseJSON['message']);
	}else if(response.status == 401){
		console.log(response.responseJSON['message']);
	}
}

