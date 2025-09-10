import respuestasFAQ from '../utils/respuestasFAQ.js';

export const responderChatbot = (req, res) => {
  const { mensaje } = req.body;

  if (!mensaje) return res.status(400).json({ respuesta: 'Mensaje vacío.' });

  const lower = mensaje.toLowerCase();

  const encontrada = respuestasFAQ.find(({ palabrasClave }) =>
    palabrasClave.some(palabra => lower.includes(palabra))
  );

  if (encontrada) {
    return res.json({ respuesta: encontrada.respuesta });
  } else {
    return res.json({
      respuesta: 'No tengo esa información. ¿Quieres hablar con un asesor? Puedes hacerlo por WhatsApp: https://wa.me/549XXXXXXXXX'
    });
  }
};
