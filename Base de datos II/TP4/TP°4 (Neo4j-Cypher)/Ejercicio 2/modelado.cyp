CREATE 
    // Usuarios
    (Juan:Usuario {nombre:"JuanDev"}),
    (Eros:Usuario {nombre:"ErosPro"}),
    (Lautaro:Usuario {nombre:"LautaroArt"}),
    (Franco:Usuario {nombre:"FrancoFit"}),

    // Relaciones
    (Juan)-[:CONOCE]->(Franco),
    (Franco)-[:CONOCE]->(Juan),
    (Juan)-[:CONOCE]->(Eros),
    (Eros)-[:CONOCE]->(Juan),
    (Juan)-[:CONOCE]->(Lautaro),
    (Lautaro)-[:CONOCE]->(Juan),
    (Eros)-[:CONOCE]->(Lautaro),
    (Lautaro)-[:CONOCE]->(Eros),

    // POsts
    (Juan)-[:POSTEA]->(p1:Post {descripcion: "Mi nuevo proyecto de app"}),
    (Eros)-[:POSTEA]->(p2:Post {descripcion: "Foto del la pile"}),
    (Lautaro)-[:POSTEA]->(p3:Post {descripcion: "Dibujo que hice"}),
    (Eros)-[:POSTEA]->(p4:Post {descripcion: "Receta de fideos de mi abuela"}),
    (Lautaro)-[:POSTEA]->(p5:Post {descripcion: "Mi setup de escritorio"}),

    // Habilidades
    (Juan)-[:TIENE]->(h1:Habilidad {nombre: "Javascript"}),
    (Juan)-[:TIENE]->(h2:Habilidad {nombre: "Frontend"}),
    (Eros)-[:TIENE]->(h3:Habilidad {nombre: "Cocina"}),
    (Eros)-[:TIENE]->(h4:Habilidad {nombre: "Fotografía"}),
    (Lautaro)-[:TIENE]->(h5:Habilidad {nombre: "Dibujo"}),
    (Lautaro)-[:TIENE]->(h6:Habilidad {nombre: "Photoshop"}),
    (Franco)-[:TIENE]->(h7:Habilidad {nombre: "Tennis"}),        
    (Franco)-[:TIENE]->(h8:Habilidad {nombre: "Entrenamiento"}),

    // Endosar
    (Juan)-[:ENDOSA]->(h8),
    (Eros)-[:ENDOSA]->(h2),
    (Lautaro)-[:ENDOSA]->(h2);
;
