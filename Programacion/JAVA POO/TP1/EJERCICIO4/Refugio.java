
public class Refugio{
 //atributos de clase
 private final static int capacidadAlmacenada = 20;
 private final static int cantidadCamas = 10;
 //atributos de instancia
 private int alimentos;
 private int bebidas;
 private int camas;
 //constructor
 public Refugio(int a,int b,int c){
     if ((a + b) > capacidadAlmacenada){
         alimentos = capacidadAlmacenada / 2;
         bebidas = capacidadAlmacenada / 2;
     }else{
         alimentos = a;
         bebidas = b;
     }
     if (c > cantidadCamas){
         camas = cantidadCamas;
     }else{
         camas = c;
     }
 }
 //comandos
 public void consumirAlimento(){
     alimentos--;
 }
 public void consumirBebida(){
     bebidas--;
 }
 public boolean ocuparCama(){
     boolean seOcupo;
     if (camas < cantidadCamas){
         camas++;
         seOcupo = true;
     }else{
         seOcupo = false;
     }
     return seOcupo;
 }
 public boolean desocuparCama(){
     boolean seDesocupo;
     if (camas > 0){
         camas--;
         seDesocupo = true;
     }else{
         seDesocupo = false;
     }
     return seDesocupo;
 }
 public boolean reponerAlimnetos(int n){
     boolean seRePuso;
     if((n > 0) && (((alimentos+ bebidas) + n) <= capacidadAlmacenada)){
         alimentos += n;
         seRePuso = true;
     }else{
         seRePuso = false;
     }
     return seRePuso;
 }
 public boolean reponerBebidas(int n){
     boolean seRePuso;
     if((n > 0) && (((alimentos+ bebidas) + n) <= capacidadAlmacenada)){
         bebidas += n;
         seRePuso = true;
     }else{
         seRePuso = false;
     }
     return seRePuso;
 }
 //consultas
 public int obtenerAlimentos(){
     return alimentos;
 }
 public int obtenerBebidas(){
     return bebidas;
 }
 public int obtenerCamas(){
     return camas;
 }
 public int obtenerCapacidadAlmacenada(){
     return capacidadAlmacenada;
 }
 public boolean esHabitable(){
     boolean sePuedeHabitar;
     if (((alimentos > 0) && (alimentos <= capacidadAlmacenada)) || ((bebidas > 0) && (bebidas <= capacidadAlmacenada)) || ((camas > 0) && (camas <= cantidadCamas))){
         sePuedeHabitar = true;
     }else{
         sePuedeHabitar = false;
     }
     
     return sePuedeHabitar;
 }
 public int disponibilidad(){
    return cantidadCamas - camas;
 }
 public int diasSupervivencia(){
     int menorValor;
     if (alimentos > bebidas){
         menorValor = bebidas;
     }else{
         menorValor = alimentos;
     }
     return menorValor;   
 }
 public boolean mayorAlimentos(Refugio r){
     boolean tieneMasAlimentos;
     if(r != null){
         alimentos > r.    
     }
     return  ; 
 }
 public boolean equals(Refugio r){
     return ;  
 }
 public Refugio clone(){
     return;   
 }
 public string toString(){
     return;   
 }
 
}

