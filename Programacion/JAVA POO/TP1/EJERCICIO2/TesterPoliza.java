import IPOO.*;
public class TesterPoliza{
    public static void main(){
        Poliza poliza1;
        Poliza poliza2;//poliza con valor fijo
        int numeroPoliza;
        float incendio;
        float robo;
        
        System.out.println("Ingrese su numero de poliza: ");
        numeroPoliza = ES.leerEntero();
        System.out.println("Ingrese el valor de incendio: ");
        incendio = ES.leerFloat();
        System.out.println("Ingrese el valor de robo: ");
        robo = ES.leerFloat();
    
        for(int i = 0;numeroPoliza <= 0 && incendio <= 0 && robo <= 0 ;i++){
            if(numeroPoliza <= 0 ){
                System.out.println("ingrese nuevamente el numero de poliza (mayor a 0): ");
                numeroPoliza = ES.leerEntero();
            }else if(incendio <= 0){
                System.out.println("Ingrese nuevamente el valor del incendio (mayor a 0): ");
                incendio = ES.leerFloat();
            }else{
                System.out.println("Ingrese nuevamente el valor de robo (mayor a 0): ");
                robo = ES.leerFloat();
            }    
        }
        poliza1 = new Poliza(numeroPoliza,incendio,robo);
        
        poliza1.actualizarPorcentaje(20);
        poliza1.desactivar();
        poliza1.actualizarPorcentaje(10);
        poliza1.activar();
        System.out.println("el numero de tu poliza es:" + poliza1.obtenerNroPoliza());
        System.out.println("el valor del incendio es de:" + poliza1.obtenerIncendio());
        System.out.println("el valor del robo es de:" + poliza1.obtenerRobo());
        System.out.println("el valor del costo es de:" + poliza1.obtenerCostoPoliza());
        if(poliza1.estaActiva()){
            System.out.println("Tu Poliza esta activa");
        }else{
            System.out.println("Tu Poliza esta activa");
        }
        
        poliza2 = new Poliza(111);
        poliza2.establecerRobo(1000);
        poliza2.establecerIncendio(1200);
        poliza2.actualizarPorcentaje(15); 
        System.out.println("el numero de tu poliza es:" + poliza2.obtenerNroPoliza());
        System.out.println("el valor del incendio es de:" + poliza2.obtenerIncendio());
        System.out.println("el valor del robo es de:" + poliza2.obtenerRobo());
        System.out.println("el valor del costo es de:" + poliza2.obtenerCostoPoliza());
        if(poliza2.estaActiva()){
            System.out.println("Tu Poliza esta activa");
        }else{
            System.out.println("Tu Poliza esta activa");
        }
        }
    }

