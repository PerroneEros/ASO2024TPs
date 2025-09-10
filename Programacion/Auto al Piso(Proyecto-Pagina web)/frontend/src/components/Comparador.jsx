import React, { useState, useEffect } from 'react';
import { getVehiculos } from '../api/vehiculos';
import Navbar from './Navbar';

export default function Comparador() {
  const [vehiculos, setVehiculos] = useState([]);
  const [seleccion, setSeleccion] = useState({ uno: '', dos: '' });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getVehiculos()
      .then(data => {
        if (Array.isArray(data)) {
          setVehiculos(data);
        } else {
          setError('La respuesta del servidor no es válida.');
        }
      })
      .catch(err => {
        console.error('Error al obtener vehículos:', err);
        setError('No se pudieron cargar los vehículos.');
      })
      .finally(() => setLoading(false));
  }, []);

  const v1 = vehiculos.find(v => v._id === seleccion.uno);
  const v2 = vehiculos.find(v => v._id === seleccion.dos);

  return (
    <>
      <Navbar />

      <section className="content fade-in">
        <h2>Comparador de Vehículos</h2>

        {loading && <p>Cargando vehículos...</p>}
        {error && <p style={{ color: 'red' }}>{error}</p>}

        {vehiculos.length > 0 && (
          <div style={{ display: 'flex', gap: '1rem', marginBottom: '1rem' }}>
            <select
              value={seleccion.uno}
              onChange={e => setSeleccion({ ...seleccion, uno: e.target.value })}
            >
              <option value="">— Selecciona primer vehículo —</option>
              {vehiculos.map(v => (
                <option key={v._id} value={v._id}>
                  {v.marca} {v.modelo}
                </option>
              ))}
            </select>

            <select
              value={seleccion.dos}
              onChange={e => setSeleccion({ ...seleccion, dos: e.target.value })}
            >
              <option value="">— Selecciona segundo vehículo —</option>
              {vehiculos.map(v => (
                <option key={v._id} value={v._id}>
                  {v.marca} {v.modelo}
                </option>
              ))}
            </select>
          </div>
        )}

        {v1 && v2 && (
          <table>
            <thead>
              <tr>
                <th>Atributo</th>
                <th>{v1.marca} {v1.modelo}</th>
                <th>{v2.marca} {v2.modelo}</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Año</td>
                <td>{v1.anio}</td>
                <td>{v2.anio}</td>
              </tr>
              <tr>
                <td>Precio</td>
                <td>${v1.precio}</td>
                <td>${v2.precio}</td>
              </tr>
              <tr>
                <td>Kilometraje</td>
                <td>{v1.kilometros} km</td>
                <td>{v2.kilometros} km</td>
              </tr>
              <tr>
                <td>Combustible</td>
                <td>{v1.combustible}</td>
                <td>{v2.combustible}</td>
              </tr>
              <tr>
                <td>Transmisión</td>
                <td>{v1.transmision}</td>
                <td>{v2.transmision}</td>
              </tr>
            </tbody>
          </table>
        )}
      </section>
    </>
  );
}
