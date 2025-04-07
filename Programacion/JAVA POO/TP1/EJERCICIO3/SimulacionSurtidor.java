import IPOO.*;
public class SimulacionSurtidor{
    public static void main(){
        Surtidor surtidor1;
        int n;
        int opcion;
        int litros;
        
        do{
            System.out.println("Seleccione una opción:");
            System.out.println("1: Leer litros a cargar y cargar Gasoil");
            System.out.println("2: Leer litros a cargar y cargar Super");
            System.out.println("3: Leer litros a cargar y cargar Premium");
            System.out.println("4: Llenar depósito Gasoil");
            System.out.println("5: Llenar depósito Super");
            System.out.println("6: Llenar depósito Premium");
            System.out.println("7: Salir");
        
            opcion = ES.leerEntero();
            surtidor1 = new Surtidor();
       
            switch(opcion){
                case 1:
                    System.out.println("ingrese los litros de gasoil que quiere cargar:"); 
                    litros= ES.leerEntero();
                    surtidor1.extraerGasoil(litros);
                    break;
                case 2:
                    System.out.println("ingrese los litros de super que quiere cargar:"); 
                    litros= ES.leerEntero();
                    surtidor1.extraerSuper(litros);
                    break;
                case 3:
                    System.out.println("ingrese los litros de premium que quiere cargar:"); 
                    litros= ES.leerEntero();
                    surtidor1.extraerPremium(litros);
                    break;
                case 4:
                    System.out.println("cargargando deposito de gasoil...");
                    surtidor1.llenarDepositoGasoil();
                    break;
                case 5:
                    System.out.println("cargargando deposito de super...");
                    surtidor1.llenarDepositoSuper();
                    break;
                case 6:
                    System.out.println("cargargando deposito de premium...");
                    surtidor1.llenarDepositoPremium();
                    break;
                case 7:
                    System.out.println("Saliendo...");
                    break;
            }
        }while(opcion > 0 && opcion < 7 );
    }
}
