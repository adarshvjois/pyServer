function xml_http_post(url,data,callback){
	var req = false;
	try{
		req = new XMLHttpRequest();
	}
	catch(e){
		try{
			req = ActiveXObject("Msxml2.XMLHTTP");
		}catch(e){
			try{
				req = new ActiveXObject("Microsoft.XMLHTTP");
			}
			catch(e){
				alert("Your Browser no Ajax. You is stoneage.");
				return false;
			}
		}
	}
	req.open("POST",url,true);

	req.onreadystatechange = function(){
		if(req.readyState == 4 && req.status==200){
			callback(req);
		}
	}
	req.send(data);
}

function keyup(searchText){
	xml_http_post("_python_method_=search_for_user",searchText,appendToHints);
}

function appendToHints(req){
    deleteTable();
	var hintsTable = document.getElementById("hintsTable")
    var rowCount = hintsTable.rows.length;
    var row = hintsTable.insertRow(rowCount)
    
    var cell = row.insertCell(0);
    cell.innerHTML = req.responseText
}

function deleteTable(){
    try{
        var table = document.getElementById("hintsTable");
        var rowCount = table.rows.length;
        for(var i = 0;i<rowCount;i++){
            table.deleteRow(i)
        }
    }catch(e){
        alert(e)
    }
}
