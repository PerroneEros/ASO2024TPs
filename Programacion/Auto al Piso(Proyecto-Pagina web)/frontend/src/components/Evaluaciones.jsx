import React, { useEffect, useState } from 'react';
import { getEvaluaciones } from '../api/evaluaciones';
import '../styles/galeria.css';
import Navbar from './Navbar';

export default function Evaluaciones() {
  const [evaluaciones, setEvaluaciones] = useState([]);
  const [mensaje, setMensaje] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getEvaluaciones()
      .then(data => {
        setEvaluaciones(data);
        setMensaje('');
      })
      .catch(err => {
        console.error('Error al obtener evaluaciones:', err);
        setMensaje('No se pudieron cargar las evaluaciones.');
      })
      .finally(() => setLoading(false));
  }, []);

  return (
    <>
    <Navbar />
    
    <section className="content galeria fade-in">
      <h2>Evaluaciones Recibidas</h2>

      {loading && <p>Cargando evaluaciones...</p>}
      {mensaje && <p style={{ color: 'red' }}>{mensaje}</p>}

      <div className="grid-layout">
        {evaluaciones.map((ev, index) => (
          <div className="caja" key={index}>
            <h3>{ev.patente}</h3>
            <p>{ev.estado} – {ev.kilometros} km</p>
            {ev.fotos?.map((foto, i) => (
              <img
                key={i}
                src={`${import.meta.env.VITE_API_URL.replace('/api', '')}/uploads/${foto}`}
                alt={`Foto ${i + 1}`}
                style={{ width: '100%', marginBottom: '8px' }}
              />
            ))}
          </div>
        ))}
      </div>
    </section>
  </>
  );
}
