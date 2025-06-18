function gritar() {
	// caixa de diálogo (popup)
	alert("Ahhhhhhhhhhhhhhhhhhhhhhhhh!");
}

function perguntar(){
	var nome; // variável local
	nome = prompt("Qual é o seu nome? "); // caixa de diálogo para entrada de dados
	alert("Olá " + nome);
}

function mudar_texto(){
	var h1 = document.getElementsByTagName("h1"); // obtém todos os elementos <h1> do documento

	// verifica se o primeiro <h1> contém o texto "Geek University"
	if(h1[0].innerText == "Geek University"){
		h1[0].innerText = "Evolua seu lado geek!";	
	}else{
		h1[0].innerText = "Geek University";
	}
}

function incrementar(){
	var id = document.getElementById("identificador"); // obtém o elemento <p> com id "p1"

	id.innerText = parseInt(id.innerText) + 1; // converte o texto para inteiro e incrementa em 1
}