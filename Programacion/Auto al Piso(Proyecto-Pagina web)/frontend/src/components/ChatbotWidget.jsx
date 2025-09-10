import React, { useState } from 'react';
import axios from 'axios';
import '../styles/chatbot.css';

export default function ChatbotWidget() {
  const [visible, setVisible] = useState(false);
  const [mensaje, setMensaje] = useState('');
  const [respuesta, setRespuesta] = useState('');
  const [loading, setLoading] = useState(false);

  const enviarMensaje = async () => {
    if (!mensaje.trim()) return;

    setLoading(true);
    try {
      const res = await axios.post('/api/chatbot', { mensaje });
      setRespuesta(res.data.respuesta);
    } catch (err) {
      setRespuesta('Error al contactar al chatbot.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chatbot-widget">
      <button className="chatbot-toggle" onClick={() => setVisible(!visible)}>
        <i className="bi bi-chat-dots-fill"></i>
      </button>

      <div className={`chatbot-box ${visible ? 'visible' : ''}`}>
        <div className="chatbot-header">
          <h4>Asistente Virtual</h4>
          <button onClick={() => setVisible(false)} className="close-btn">×</button>
        </div>

        <div className="chatbot-body">
          <input
            type="text"
            placeholder="¿En qué puedo ayudarte?"
            value={mensaje}
            onChange={(e) => setMensaje(e.target.value)}
          />
          <button onClick={enviarMensaje} disabled={loading}>
            {loading ? 'Consultando...' : 'Enviar'}
          </button>
          {respuesta && <div className="chatbot-respuesta">{respuesta}</div>}
        </div>
      </div>
    </div>
  );
}
