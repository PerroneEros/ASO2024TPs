import React from 'react';
import Navbar from './Navbar';
import '../styles/contacto.css';

export default function Contacto() {
  return (
    <>
      <Navbar />

      <a className="ir-arriba" href="#" title="Volver arriba">
        <span className="fa-stack">
          <i className="fa fa-circle fa-stack-2x"></i>
          <i className="fa fa-arrow-up fa-stack-1x fa-inverse"></i>
        </span>
      </a>

      <section className="content contacto fade-in" id="contacto">
        <div className="form-mapa-container">
          {/* Formulario */}
          <form className="form-container">
            <h2 className="fade-in">Formulario de contacto</h2>

            <div className="form-group">
              <label htmlFor="nombre">Nombre:</label>
              <input type="text" id="nombre" name="nombre" placeholder="Ingrese su Nombre" />
            </div>

            <div className="contact-fields">
              <div className="form-group">
                <label htmlFor="email">Email:</label>
                <input type="email" id="email" name="email" placeholder="Ingrese su Email" />
              </div>

              <div className="form-group">
                <label htmlFor="telefono">Teléfono:</label>
                <input type="tel" id="telefono" name="telefono" placeholder="Ingrese su Teléfono" />
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="comentarios">Comentarios:</label>
              <textarea id="comentarios" name="comentarios" rows="4" placeholder="Ingrese su comentario"></textarea>
            </div>

            <div className="form-group">
              <label htmlFor="opciones">Selecciona una opción:</label>
              <select id="opciones" name="opciones">
                <option value="">-- Selecciona --</option>
                <option value="op1">Reunión con vendedor.</option>
                <option value="op2">Reunión con comprador.</option>
                <option value="op3">Reunión con administrador.</option>
              </select>
            </div>

            <div className="form-group">
              <label>Preferencia de contacto:</label>
              <div className="options">
                <label><input type="radio" name="preferencia" value="email" /> Email</label>
                <label><input type="radio" name="preferencia" value="telefono" /> Teléfono</label>
                <label><input type="checkbox" name="condiciones" /> Acepta términos y condiciones</label>
              </div>
            </div>

            <div className="buttons">
              <button type="submit">Enviar</button>
              <button type="reset">Reset</button>
            </div>
          </form>

          {/* Mapa */}
          <div className="mapa fade-in">
            <h3>Ubicación de la UTN Bahía Blanca</h3>
            <iframe
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3112.3533900901457!2d-62.25998102465611!3d-38.73265208711029!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95eda3323284dd19%3A0x659d42ca958223f1!2sUTN%20-%20Facultad%20Regional%20Bah%C3%ADa%20Blanca!5e0!3m2!1ses-419!2sar!4v1744759580988!5m2!1ses-419!2sar"
              width="100%"
              height="350"
              style={{ border: 0 }}
              allowFullScreen=""
              loading="lazy"
              title="UTN Bahía Blanca"
            ></iframe>
          </div>
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
