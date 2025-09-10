import React from 'react';
import Navbar from './Navbar';
import '../styles/galeria.css';

export default function Galeria() {
  return (
    <>
      <Navbar />

      <section className="content galeria fade-in">
        <div className="grid-layout">
          {[1, 2, 3, 4, 5, 6, 7, 11, 8, 9, 10].map((num) => (
            <React.Fragment key={num}>
              <div className="caja">
                <img src={`/img/Auto${num}.jpg`} alt={`Auto ${num}`} />
                <a href={`#modal${num}`} className="Boton">
                  <i className="bi bi-search" style={{ marginRight: '8px' }}></i>
                  Ver más
                </a>
              </div>

              <div className="modal" id={`modal${num}`}>
                <div className="modal-content">
                  <div className="close-btn"><a href="#">X</a></div>
                  <div className="modal-img">
                    <img src={`/img/Auto${num}.jpg`} alt={`Auto ${num} ampliado`} />
                  </div>
                  <h3>Auto {num}</h3>
                  <p>Descripción del auto {num}, esto es una tarjeta.</p>
                  <a href="#" className="btn">Más información.</a>
                </div>
              </div>
            </React.Fragment>
          ))}
        </div>
      </section>

      <footer className="footer">
        <p>© 2025 Autos Al Piso. Todos los derechos reservados.</p>
        <div className="redes">
          <a href="#"><img src="/img/github-icono.jpg" alt="GitHub" width="24" /></a>
          <a href="#"><img src="/img/linkedin-icono.jpg" alt="LinkedIn" width="24" /></a>
        </div>
      </footer>
    </>
  );
}
