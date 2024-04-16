const header = document.querySelector(".header");

header.innerHTML = `
  <div class="navbar">
    <div class="logo">
        <a href="index.html"><img src="img/logo-turismo.png" alt="logo-viajes"></a>
    </div>            
        <ul class="navbar-links"> 
        <li><a href="index.html">Inicio</a></li>                
        <li><a href="#">Donde Ir</a></li> 
        <li><a href="sobre_nosotros.html">Sobre Nosotros</a></li> 
        <li><a href="contacto.html" class="nav-menu-link_active" >Contacto</a></li>   
        </ul>                     
        <a href="#" class="action_btn">Consultanos</a>
    <div class="toggle_btn">
        <i class="fa-solid fa-bars"></i>
    </div>
    <div class="icon-whatsapp">
        <i class="fa-brands fa-whatsapp"></i> 
        <i class="fa-brands fa-facebook"></i>
    <a href="#"></a>
    </div>
    </div> 
    <div class="dropdown_menu">
        <li><a href="index.html">Inicio</a></li>                
        <li><a href="#">Donde Ir</a></li> 
        <li><a href="sobre_nosotros.html">Sobre Nosotros</a></li> 
        <li><a href="contacto.html" class="nav-menu-link_active" >Contacto</a></li>
        <a href="#" class="action_btn">Consultanos</a>
    </div>
`;
