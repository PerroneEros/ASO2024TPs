import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/index.css';

export default function Navbar() {
  const toggleMenu = () => {
    const nav = document.querySelector('.Navbar ul');
    nav.classList.toggle('show');
  };

  const toggleDarkMode = () => {
    document.body.classList.toggle('dark-mode');
  };

  return (
    <header className="head">
      <div className="logo">
        <Link to="/">
          <img src="/img/WhatsApp%20Image%202025-04-09%20at%204.21.12%20PM.jpeg" alt="Logo" />
        </Link>
      </div>

      <button className="menu-toggle" onClick={toggleMenu}>☰</button>

      <nav className="Navbar">
        <ul>
          <li><Link to="/">Inicio</Link></li>
          <li><Link to="/galeria">Vehículos</Link></li>
          <li><Link to="/contacto">Contáctenos</Link></li>
          <li><Link to="/promociones">Promociones</Link></li>
          <li><Link to="/evaluaciones">Evaluaciones</Link></li>
          <li><Link to="/comparar">Comparador</Link></li>
          <li><Link to="/reserva">Reservar</Link></li>
          <li><Link to="/testdrive">Test Drive</Link></li>
          <li><Link to="/simulador">Simulador</Link></li>
          <li><i className="bi bi-brightness-high-fill" onClick={toggleDarkMode}></i></li>
        </ul>
      </nav>
    </header>
  );
}
