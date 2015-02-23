$(document).ready(function() {

	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			function getCookie(name) {
				var cookieValue = null;
				if (document.cookie && document.cookie != '') {
					var cookies = document.cookie.split(';');
					for (var i = 0; i < cookies.length; i++) {
						var cookie = jQuery.trim(cookies[i]);
						// Does this cookie string begin with the name we want?
						if (cookie.substring(0, name.length + 1) == (name + '=')) {
							cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
							break;
						}
					}
				}
				return cookieValue;
			}
			if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
				// Only send the token to relative URLs i.e. locally.
				xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			}
		}
	});

	var entrada = $('#id_entrada');
	var boton = $('#validar');

	function validarEntrada(entrada) {
		entrada = parseFloat(entrada)

		if (isNaN(entrada)) {
			sweetAlert("Oops...", "Debe ingresar un numero entero mayor a '0' ...", "error");
			console.log("El dato debe ser numerico")
			return false;
		};

		if (!(entrada % 1 == 0)) {
			sweetAlert("Oops...", "Solo se permiten numeros enteros NO decimales...", "error");
			return false
		}



		if (entrada < 1) {
			sweetAlert("Oops...", "Solo se permiten numeros positivos...", "error");
			return false;
		};

		return true;


	}


	$("#form").submit(function(event) {
		if (validarEntrada(entrada.val())) {

			$.ajax({
					type: "POST",
					url: "validar/",
					data: {
						data: entrada.val()
					}
				})
				.done(function(msg) {
					if (msg.success) {
						swal("Buen Trabajo!", "El Numero ingresado es PRIMO CIRCULAR...", "success")
					} else {
						swal("Oops...", "El numero ingresado NO ES PRIMO CIRCULAR", "warning")
					}

				});
				event.preventDefault();
		}else{
			event.preventDefault();
		}
	});


});