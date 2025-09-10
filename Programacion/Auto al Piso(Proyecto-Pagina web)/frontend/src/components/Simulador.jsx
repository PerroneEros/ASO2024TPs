import React, { useState } from 'react';
import { simularFinanciacion } from '../api/simulador';
import '../styles/contacto.css';
import Navbar from './Navbar';

export default function Simulador() {
  const [monto, setMonto] = useState('');
  const [cuotas, setCuotas] = useState('');
  const [tasa, setTasa] = useState(5);
  const [resultado, setResultado] = useState('');
  const [loading, setLoading] = useState(false);

  const calcularCuota = async (e) => {
    e.preventDefault();

    // Validación básica
    if (!monto || !cuotas || tasa <= 0) {
      setResultado('Por favor completa todos los campos correctamente.');
      return;
    }

    setLoading(true);
    setResultado('Calculando...');

    try {
      const res = await simularFinanciacion({ monto, cuotas, tasa });
      setResultado(`Cuota estimada: $${res.cuotaMensual.toFixed(2)} durante ${cuotas} meses.`);
    } catch (err) {
      console.error('Error en la simulación:', err);
      setResultado('Error al calcular la financiación.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
    <Navbar />

    <section className="content contacto fade-in">
      <form className="form-container" onSubmit={calcularCuota}>
        <h2>Simulador de Financiación</h2>

        <label>Monto del vehículo ($):</label>
        <input
          type="number"
          value={monto}
          onChange={(e) => setMonto(e.target.value)}
          required
        />

        <label>Número de cuotas:</label>
        <input
          type="number"
          value={cuotas}
          onChange={(e) => setCuotas(e.target.value)}
          required
        />

        <label>Tasa mensual (%):</label>
        <input
          type="number"
          step="0.1"
          value={tasa}
          onChange={(e) => setTasa(e.target.value)}
          required
        />

        <div className="buttons">
          <button type="submit" disabled={loading}>
            {loading ? 'Calculando...' : 'Calcular'}
          </button>
        </div>

        {resultado && <p style={{ marginTop: '10px' }}>{resultado}</p>}
      </form>
    </section>
    </>
  );
}
