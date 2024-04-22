   const a = document.querySelector("#validationNombre");
   const b = document.querySelector("#validationApellido");
   const c = document.querySelector("#validationEmail");
   const d = document.querySelector("#validationTel");
   const e = document.querySelector("#validationConsulta");
    var errorNodes = document.querySelectorAll(".error");

    function validateForm() {

        clearMessages();
        let errorFlag = false;

        if (a.value.length < 3) {
            errorNodes[0].innerText = "*Por Favor ingrese un nombre valido";
            a.classList.add("error-border");
            errorFlag = true;
        }

        if (b.value.length < 3) {
            errorNodes[1].innerText = "*Por Favor ingrese un Apellido valido";
            b.classList.add("error-border");
            errorFlag = true;
        }

        if (!emailIsValid(c.value)) {
            errorNodes[2].innerText = "*Por Favor ingrese un Email valido";
            c.classList.add("error-border");
            errorFlag = true;
        }

        if (isNaN(d.value) || d.value.length != 10) {
            errorNodes[3].innerText = "*Por Favor ingrese un Telefono valido";
            d.classList.add("error-border");
            errorFlag = true;
        }

        if (e.value.length < 25) {
            errorNodes[4].innerText = "*Minimo 25 caracteres";
            e.classList.add("error-border");
            errorFlag = true;
        }

        if(!errorFlag) {
            success.innerText = "Consulta enviada con exito!";
        }
    }

    function clearMessages() {
        for (let i = 0; i < errorNodes.length; i++) {
            errorNodes[i].innerText = "";
        }
        success.innerText = "";

        a.classList.remove("error-border");
        b.classList.remove("error-border");
        c.classList.remove("error-border");
        d.classList.remove("error-border");
        e.classList.remove("error-border");

    }

    function emailIsValid(c) {
        let pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return pattern.test(c);     
    }

 
 


