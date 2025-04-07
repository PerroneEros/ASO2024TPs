
public class Poliza{
//Atributos de Instancia
 private int nroPoliza;
 private float incendio;
 private float robo;
 private boolean activa;
//constructor
 public Poliza(int np){
        nroPoliza = np;
        incendio = 0;
        robo = 0;
        activa = true;
 }
 public Poliza(int np,float i,float r){
     nroPoliza = np;
     incendio = i;
     robo = r;
     activa = true;
 }
//comandos
 public void establecerIncendio(float m){
     incendio = m;
 }
 public void establecerRobo(float m){
    robo = m;
 }
 public void actualizarPorcentaje(int p){
    if (activa == true) {
        incendio = (incendio * p/100) + incendio;
        robo = (robo * p/100) + robo;
    }
 }
 public void activar(){
     activa = true;
 }
 
 public void desactivar(){
     activa = false;
 }
//cosnultas
 public int obtenerNroPoliza(){
     return nroPoliza;
 }
 public float obtenerIncendio(){
    return incendio;
 }
 public float obtenerRobo(){
    return robo;
 }
 public float obtenerCostoPoliza(){
    return robo + incendio;
 }
 public boolean estaActiva(){
    return activa;
 }
}
