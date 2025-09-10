import { useEffect, useState } from "react";
import axios from "axios";
import ListaTarjetas from "./ListaTarjetas";

const TraerPersonas = () => {
  const [personas, setPersonas] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:3000/personas")
      .then(res => setPersonas(res.data))
      .catch(err => console.error("Error al traer personas", err));
  }, []);

  return (
    <div>
      <h2>Personas</h2>
      <ListaTarjetas personas={personas} />
    </div>
  );
};

export default TraerPersonas;