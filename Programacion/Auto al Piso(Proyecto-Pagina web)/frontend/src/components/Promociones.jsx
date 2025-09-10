import React, { useEffect, useState } from 'react';
import { getPromociones } from '../api/promociones';
import '../styles/galeria.css';
import Navbar from './Navbar';

export default function Promociones() {
  const [promos, setPromos] = useState([]);
  const [mensaje, setMensaje] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getPromociones()
      .then(data => {
        setPromos(data);
        setMensaje('');
      })
      .catch(err => {
        console.error('Error al obtener promociones:', err);
        setMensaje('No se pudieron cargar las promociones.');
      })
      .finally(() => setLoading(false));
  }, []);

  return (
    <>
    <Navbar />

    <section className="content galeria fade-in">
      <h2>Promociones Activas</h2>

      {loading && <p>Cargando promociones...</p>}
      {mensaje && <p style={{ color: 'red' }}>{mensaje}</p>}

      <div className="grid-layout">
        {promos.map((promo, index) => (
          <div className="caja" key={index}>
            {promo.imagen && (
              <img
                src={`${import.meta.env.VITE_API_URL.replace('/api', '')}/uploads/${promo.imagen}`}
                alt={promo.titulo}
                style={{ width: '100%', marginBottom: '8px' }}
              />
            )}
            <h3>{promo.titulo}</h3>
            <p>{promo.descripcion}</p>
            <p>
              <strong>Precio original:</strong> ${promo.vehiculo.precioOriginal}<br />
              <strong>Con descuento:</strong> ${promo.vehiculo.precioConDescuento}
            </p>
            <p>
              <strong>Válido desde:</strong> {new Date(promo.desde).toLocaleDateString()}<br />
              <strong>Hasta:</strong> {new Date(promo.hasta).toLocaleDateString()}
            </p>
            <a href="/reserva" className="btn">Reservar ahora</a>
          </div>
        ))}
      </div>
    </section>
    </>    
  );
}
