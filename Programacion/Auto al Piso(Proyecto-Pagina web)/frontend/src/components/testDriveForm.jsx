import React, { useState } from 'react';
import { postTestDrive } from '../api/testdrive';
import '../styles/contacto.css';
import Navbar from './Navbar';

export default function TestDriveForm() {
  const [form, setForm] = useState({
    nombre: '',
    email: '',
    telefono: '',
    modelo: '',
    fechaDeseada: '',
    comentarios: '',
  });

  const [mensaje, setMensaje] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!form.nombre || !form.email || !form.modelo || !form.fechaDeseada) {
      setMensaje('Por favor completa todos los campos obligatorios.');
      return;
    }

    setLoading(true);
    setMensaje('Enviando...');

    try {
      await postTestDrive(form);
      setMensaje('Solicitud de test drive enviada con éxito.');
      setForm({
        nombre: '',
        email: '',
        telefono: '',
        modelo: '',
        fechaDeseada: '',
        comentarios: '',
      });
    } catch (error) {
      console.error('Error al enviar solicitud:', error);
      setMensaje('Error al enviar la solicitud. Intenta de nuevo.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
    <Navbar />

    <section className="content contacto fade-in">
      <form className="form-container" onSubmit={handleSubmit}>
        <h2>Solicitar Test Drive</h2>

        <label>Nombre:</label>
        <input name="nombre" type="text" value={form.nombre} onChange={handleChange} required />

        <label>Email:</label>
        <input name="email" type="email" value={form.email} onChange={handleChange} required />

        <label>Teléfono:</label>
        <input name="telefono" type="tel" value={form.telefono} onChange={handleChange} />

        <label>Modelo deseado:</label>
        <input name="modelo" type="text" value={form.modelo} onChange={handleChange} required />

        <label>Fecha deseada:</label>
        <input name="fechaDeseada" type="date" value={form.fechaDeseada} onChange={handleChange} required />

        <label>Comentarios:</label>
        <textarea name="comentarios" rows="4" value={form.comentarios} onChange={handleChange} />

        <div className="buttons">
          <button type="submit" disabled={loading}>
            {loading ? 'Enviando...' : 'Enviar solicitud'}
          </button>
        </div>

        {mensaje && <p style={{ marginTop: '10px' }}>{mensaje}</p>}
      </form>
    </section>
    </>
  );
}
