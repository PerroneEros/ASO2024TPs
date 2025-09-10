import React from 'react';
import { Routes, Route } from 'react-router-dom';

import ChatbotWidget from './components/ChatbotWidget';
import Index from './components/Index';
import Galeria from './components/Galeria';
import Contacto from './components/Contacto';
import EvaluacionForm from './components/EvaluacionForm';
import TestDriveForm from './components/TestDriveForm';
import ReservaForm from './components/ReservaForm';
import Simulador from './components/Simulador';
import Evaluaciones from './components/Evaluaciones';
import Promociones from './components/Promociones';
import Reservas from './components/Reservas';
import Comparador from './components/Comparador';

function App() {
  return (
    <>
    <ChatbotWidget />
    <Routes>
      <Route path="/" element={<Index />} />
      <Route path="/galeria" element={<Galeria />} />
      <Route path="/contacto" element={<Contacto />} />
      <Route path="/evaluacion" element={<EvaluacionForm />} />
      <Route path="/testdrive" element={<TestDriveForm />} />
      <Route path="/reserva" element={<ReservaForm />} />
      <Route path="/simulador" element={<Simulador/>} />
      <Route path="/evaluaciones" element={<Evaluaciones/>} />
      <Route path="/promociones" element={<Promociones/>} />
      <Route path="/reservas" element={<Reservas/>} />
      <Route path="/comparar" element={<Comparador />} />
    </Routes>
    </>
  );
}

export default App;