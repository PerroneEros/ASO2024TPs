import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from './Navbar';
import '../styles/index.css';

export default function Index() {
  return (
    <>
      <Navbar />

      <a className="ir-arriba" href="#" title="Volver arriba">
        <span className="fa-stack">
          <i className="fa fa-circle fa-stack-2x"></i>
          <i className="fa fa-arrow-up fa-stack-1x fa-inverse"></i>
        </span>
      </a>

      <div className="slider-container fade-in">
        <div className="slide">
          <ul>
            <li><img src="/img/slider-1.jpg" alt="Imagen 1" /></li>
            <li><img src="/img/slider-2.jpg" alt="Imagen 2" /></li>
            <li><img src="/img/slider-3.jpg" alt="Imagen 3" /></li>
            <li><img src="/img/slider-4.jpg" alt="Imagen 4" /></li>
          </ul>
        </div>
        <div className="slider-texto">
          <h2>Bienvenidos a Autos Al Piso</h2>
        </div>
      </div>

      <main className="content home fade-in" id="home">
        <h2 className="title">¿Quiénes somos?</h2>
        <p>
          En <strong>Autos Al Piso</strong>, si buscan naves que rocen el asfalto y tengan un look que rompe cuellos,
          llegaron al lugar indicado. En nuestra web encontrarán una selección de autos al piso que son verdaderas obras de arte sobre ruedas.
          ¡Elijan uno y cómprennos, NECESITAN un auto al piso y nosotros queremos tu plata!
        </p>

        <div className="botones">
          <Link to="/contacto">Conocer más</Link>
          <Link to="/galeria">Explorar vehículos</Link>
        </div>
      </main>

      <footer className="footer">
        <p>© 2025 Autos Al Piso. Todos los derechos reservados.</p>
        <div className="redes">
          <a href="#"><img src="/img/github-icono.webp" alt="GitHub" width="24" /></a>
          <a href="#"><img src="/img/linkedin-icono.webp" alt="LinkedIn" width="24" /></a>
        </div>
      </footer>
    </>
  );
}
