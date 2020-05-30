// toggle hide/show filter panel on click of filter button
function displayfilters(){
	var filterpanel = document.getElementById("filterpanel");
	if (filterpanel.style.display === "none"){
		filterpanel.style.display = "block";
	}
	else{
		filterpanel.style.display = "none";
	}
}