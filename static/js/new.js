var services = document.getElementById('services')

console.log(services.value)

services.addEventListener("change", ()=>{
	console.log(services.value)
	var target = document.getElementById('targetdiv');
	var stylelbl = document.getElementById('stylelbl')
	if(services.value === "fashion"){
		target.style.display = "none";
		stylelbl.innerHTML="Input Image: "
	}else{
		target.style.display = "block"
		stylelbl.innerHTML="Style Image: "
	}
})