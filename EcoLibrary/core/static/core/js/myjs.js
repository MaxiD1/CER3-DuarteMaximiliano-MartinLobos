function timer(fecha){
    // Fecha del evento
    var fin = fecha
    // Variables que convierten las unidades
    // de tiempo a milisegundos
    var segundos = 1000
    var minutos = segundos*60
    var horas = minutos*60
    var dias = horas*24
    // Reloj
    var tiempo
    // Fecha actual
    var ahora = new Date()
    //document.write(ahora)
    // El tiempo faltante
    var diferencia = fin - ahora
    // En caso de que el evento haya empezado
    if (diferencia <= 0){
        // 
        clearInterval(timer)
        document.write("El evento ya ha terminado")
        return
    }
    // Calculo del tiempo faltante
    // dia
    var d = Math.floor(diferencia/dias)
    // hora
    var h = Math.floor((diferencia%dias)/horas)
    // minutos
    var m = Math.floor((diferencia%horas)/minutos)
    // segundos
    var s = Math.floor((diferencia%minutos)/segundos)

    // Escribe el tiempo faltante en el html
    document.write(d + "days ")
    document.write(h + "hrs ")
    document.write(m + "mins ")
    document.write(s + "secs")
}

function mk_comentario(){
    event.preventDefault()

    var nombre = document.getElementById("nombre").value
    var comentario = document.getElementById("comentario").value
    
    window.alert(nombre)
    if (nombre.length == 0){
        window.alert("Debe escribir un nombre.")
        exit()
    }
    if (comentario.length == 0){
        window.alert("Debe escribir un comentario.")
        exit()
    }
    if (nombre.length >= 500){
        window.alert("Use un nombre más corto (menos de 500 caracteres).")
        exit()
    }
    if (comentario.length >= 500){
        window.alert("Debe escribir un comentario más corto (menos de 500 caracteres).")
        exit()
    }


    // Seccion de comentarios
    var seccion = document.getElementsByClassName("col")[0]

    var carta = document.createElement("div")
    carta.setAttribute("class", "card")

    // Crea el cuerpo de la carta
    var card_body = document.createElement("div")
    card_body.setAttribute("class", "card-body")

    // Crea la seccion donde irá el nombre
    var h5 = document.createElement("h5")
    h5.setAttribute("class", "card-title")
    h5.innerText = nombre

    // Crea la seccion donde se mostrara la fecha
    var p = document.createElement("p")
    p.setAttribute("class", "card-subtitle mb-2 text-body-secondary")
    // Pone la fechar en texto pequeño
    var small = document.createElement("small")
    small.innerText = new Date()
    // Añade el texto pequeño a la seccion con la fecha
    p.append(small)

    // Crea la seccion con el comentario en sí
    var p2 = document.createElement("p")
    p2.setAttribute("class", "card-text")
    p2.innerText = comentario

    // Junta todos los elementos
    card_body.append(h5)
    card_body.append(p)
    card_body.append(p2)

    carta.append(card_body)

    seccion.append(carta)

    document.getElementById("nombre").value = ""
    document.getElementById("comentario").value = ""
}