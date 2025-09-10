import React, { useState } from 'react';
import { postEvaluacion } from '../api/evaluaciones';
import '../styles/contacto.css';
import Navbar from './Navbar';

export default function EvaluacionForm() {
  const [form, setForm] = useState({
    nombre: '',
    email: '',
    telefono: '',
    patente: '',
    marca: '',
    modelo: '',
    anio: '',
    kilometros: '',
    estado: '',
    fotos: [],
  });

  const [mensaje, setMensaje] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    if (name === 'fotos') {
      setForm({ ...form, fotos: files });
    } else {
      setForm({ ...form, [name]: value });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!form.nombre || !form.email || !form.patente || !form.estado) {
      setMensaje('Por favor completa los campos obligatorios.');
      return;
    }

    setLoading(true);
    setMensaje('Enviando evaluación...');

    const formData = new FormData();
    Object.entries(form).forEach(([key, value]) => {
      if (key === 'fotos') {
        for (let i = 0; i < value.length; i++) {
          formData.append('fotos', value[i]);
        }
      } else {
        formData.append(key, value);
      }
    });

    try {
      await postEvaluacion(formData);
      setMensaje('Evaluación enviada correctamente.');
      setForm({
        nombre: '',
        email: '',
        telefono: '',
        patente: '',
        marca: '',
        modelo: '',
        anio: '',
        kilometros: '',
        estado: '',
        fotos: [],
      });
    } catch (error) {
      console.error('Error al enviar evaluación:', error);
      setMensaje('Error al enviar la evaluación.');
    } finally {
      setLoading(false);
    }
  };

  return (
  <>
    <Navbar />
    <section className="content contacto fade-in">
      <form className="form-container" onSubmit={handleSubmit}>
        <h2>Evaluar tu vehículo usado</h2>

        <label>Nombre:</label>
        <input name="nombre" type="text" value={form.nombre} onChange={handleChange} required />

        <label>Email:</label>
        <input name="email" type="email" value={form.email} onChange={handleChange} required />

        <label>Teléfono:</label>
        <input name="telefono" type="tel" value={form.telefono} onChange={handleChange} />

        <label>Patente:</label>
        <input name="patente" type="text" value={form.patente} onChange={handleChange} required />

        <label>Marca:</label>
        <input name="marca" type="text" value={form.marca} onChange={handleChange} />

        <label>Modelo:</label>
        <input name="modelo" type="text" value={form.modelo} onChange={handleChange} />

        <label>Año:</label>
        <input name="anio" type="number" value={form.anio} onChange={handleChange} />

        <label>Kilómetros:</label>
        <input name="kilometros" type="number" value={form.kilometros} onChange={handleChange} />

        <label>Fotos:</label>
        <input
          type="file"
          name="fotos"
          multiple
          accept="image/*"
          onChange={handleChange}
        />

        <label>Estado general:</label>
        <select name="estado" value={form.estado} onChange={handleChange} required>
          <option value="">-- Selecciona --</option>
          <option value="excelente">Excelente</option>
          <option value="bueno">Bueno</option>
          <option value="regular">Regular</option>
        </select>

        <div className="buttons">
          <button type="submit" disabled={loading}>
            {loading ? 'Enviando...' : 'Enviar evaluación'}
          </button>
        </div>

        {mensaje && <p style={{ marginTop: '10px' }}>{mensaje}</p>}
      </form>
    </section>
  </>
  );
}
