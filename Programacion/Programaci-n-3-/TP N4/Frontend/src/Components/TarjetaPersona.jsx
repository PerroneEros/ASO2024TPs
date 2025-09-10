const TarjetaPersona = ({ persona }) => {
  return (
    <div style={{
      border: "1px solid #ccc",
      borderRadius: "10px",
      padding: "1rem",
      width: "200px",
      backgroundColor: "#f9f9f9",
      boxShadow: "2px 2px 8px rgba(0,0,0,0.1)",
      color: "#333"
    }}>
      <h3>{persona.nombre} {persona.apellido}</h3>
      <p>Edad: {persona.edad}</p>
      <p>Email: {persona.email}</p>
    </div>
  );
};

export default TarjetaPersona;