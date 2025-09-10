import React, { useEffect, useState } from 'react';
import { getReservas } from '../api/reservas';
import '../styles/galeria.css';
import Navbar from './Navbar';

export default function Reservas() {
  const [reservas, setReservas] = useState([]);
  const [mensaje, setMensaje] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getReservas()
      .then(data => {
        setReservas(data);
        setMensaje('');
      })
      .catch(err => {
        console.error('Error al obtener reservas:', err);
        setMensaje('No se pudieron cargar las reservas.');
      })
      .finally(() => setLoading(false));
  }, []);

  return (
    <>
    <Navbar />

    <section className="content galeria fade-in">
      <h2>Reservas Recibidas</h2>

      {loading && <p>Cargando reservas...</p>}
      {mensaje && <p style={{ color: 'red' }}>{mensaje}</p>}

      <div className="grid-layout">
        {reservas.map((reserva, index) => (
          <div className="caja" key={index}>
            <h3>{reserva.nombre}</h3>
            <p><strong>Email:</strong> {reserva.email}</p>
            <p><strong>Teléfono:</strong> {reserva.telefono || 'No especificado'}</p>
            <p><strong>Modelo:</strong> {reserva.modelo}</p>
            <p><strong>Fecha de reserva:</strong> {reserva.fechaReserva ? new Date(reserva.fechaReserva).toLocaleDateString() : 'Sin fecha'}</p>
            <p><strong>Comentarios:</strong> {reserva.comentarios || 'Sin comentarios'}</p>
          </div>
        ))}
      </div>
    </section>
    </>
  );
}
