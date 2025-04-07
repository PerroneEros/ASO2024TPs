import IPOO.*;

public class TesterRefugio
{

    public static void main(String args[]){

     // ATENCION:
     //
     // Se asume que los métodos  
     //
     //      obtener...()
     //      toString()   
     //
     // FUNCIONAN CORRECTAMENTE

     // Declaración de variables

        Refugio r1, r2, r3, r4, r5, r;
        int a, b, c, alim, llenar, camas, a1, a2;

     //----------------------------
     //---TESTING DE CONSTRUCTOR---
     //----------------------------

     // Se crean objetos con valores en el limite de la capacidad del refugio, 
     // y tambien por encima de la capacidad del refugio, 
     // tanto de alimentos y bebidas como de camas. Lo hace con valores fijos establecidos en el codigo.
     //
     // Se anuncia mediante salida por consola qué operación se realizó, 
     // cual es el resultado esperado, y luego muestra el valor obtenido.


        System.out.println("Testeando constructor con valores previamente establecidos");    
    
        r1 = new Refugio(16,4,10);
            System.out.println("Primer refugio creado con 16,4,10: "+ r1.toString());
    
        r2 = new Refugio(17,5,3);
        System.out.println("Segundo refugio creado con 17,5,3 pero deberia quedar 10,10,3: "+ r2.toString());
    
        r3 = new Refugio(12,3,17);
        System.out.println("Tercer refugio creado con 12,3,17 pero deberia quedar 12,3,10: "+ r3.toString());


     // Testeando constructor con valores ingresados por consola
     //
     // Se crea un objeto con valores ingresados por el usuario 
     // que esten por debajo del limite de la capacidad del refugio, 
     // tanto de alimentos y bebidas como de camas.
     //
     // Se anuncia mediante salida por consola qué operación se realizo, 
     // cual es el resultado esperado, y luego muestra el valor obtenido.

        System.out.println("Testeando constructor... Ingrese 3 valores enteros:");
 
        do{
            System.out.println("Ingrese alimentos y bebidas de modo que el total sea a lo sumo 20:");
            a = ES.leerEntero();
            b = ES.leerEntero();

            System.out.println("Ingrese el número de camas, a lo sumo 10:");
            c = ES.leerEntero();
            
        } while((a + b > 20) || (c > 10));
        
        r = new Refugio(a, b, c);
        System.out.println();       

        System.out.println("Cuarto refugio creado con " +a+ ","+b+"," +c+ " : "+ r.toString());

        System.out.println("----------------------------------------------------------");
        

     //----------------------------
     //-----TESTING DE METODOS-----
     //----------------------------

     // El tester evalúa consumirAlimento()
     //
     // A traves de un condicional y del valor obtenido luego de la operación, puede indicar si el metodo
     // funciona correctamente x

        
        System.out.println("Testeando metodo consumirAlimento()...");

        alim = r.obtenerAlimentos();

        if (alim > 0)
          {
            r.consumirAlimento();
            if (r.obtenerAlimentos() != (alim - 1))
               {
                    System.out.println("ERROR: revisar metodo consumirAlimento()");
               }
            else
               {
                    System.out.println("Metodo consumirAlimento() funciona correctamente");
                }
          }
          
        System.out.println();
        System.out.println(r.toString());

        System.out.println("----------------------------------------------------------");


        
        
        
        
        //  verificar consumirBebida()   
     
        
        
        
        
        
        //------------------------------------------------------------------------------------------
        
        System.out.println("Testeando método reponerAlimentos()...");

        System.out.println("Testeando reponerAlimentos(valor negativo)...");

        if (r.reponerAlimentos(-3) != false )
            System.out.println("ERROR : revisar metodo reponerAlimentos() al ingresar valor negativo");            
        
        alim = r.obtenerAlimentos()+ r.obtenerBebidas();
        
        llenar = 20 - alim;
        
        System.out.println("Testeando reponerAlimentos(supera capacidad)...");
        if (r.reponerAlimentos(llenar+1)!=false)
            System.out.println("ERROR : revisar metodo reponerAlimento() al superar capacidad");

        System.out.println("Testeando reponerAlimento(valor correcto)...");
        if (r.reponerAlimentos(llenar))           
                    System.out.println("Método obtenerAlimento() funciona correctamente");
               else  
                    System.out.println("ERROR ");
                
        System.out.println();    
        System.out.println(r.toString());
        
        System.out.println("----------------------------------------------------------");
        




        //  verificar reponerBebidas()





        //------------------------------------------------------------------------------------------
        
       
        System.out.println("Testeando método desocuparCama()...");

        camas = r.obtenerCamas();        
        
        if (r.desocuparCama())
            {
             System.out.println(r.toString());
             if (r.obtenerCamas()== camas - 1)
                  System.out.println("Método desocuparCama() funciona correctamente");
             else
                  System.out.println("ERROR: revisar método desocuparCama()");
             }
        else
            {
            
            System.out.println(r.toString());
            if (camas == 0)
                        System.out.println("Método desocuparCama() funciona correctamente");
            else                
                        System.out.println("ERROR: revisar metodo desocuparCama()");
                                
            }

        System.out.println("----------------------------------------------------------");









        // verificar ocuparCama()



    





        
        //------------------------------------------------------------------------------------------
        System.out.println();

        System.out.println("Testeando metodo mayorAlimentos()...");

        r4  = null;
        if (r.mayorAlimentos(r4) != false)
            System.out.println("Método mayorAlimentos() no funciona correctamente para el caso de parametros no ligados.");

        a1 = r.obtenerAlimentos();

        r4 = new Refugio(1,1,1);
        a2 = r4.obtenerAlimentos();

        System.out.println("Refugio 1   "+r.toString());
        System.out.println("Refugio 2   "+r4.toString());

        if (a1 > a2) 
            if (r.mayorAlimentos(r4))
                 System.out.println("Metodo mayorAlimentos() funciona correctamente");
            else 
                System.out.println("ERROR: revisar metodo mayorAlimentos()");
        
        else
             if (r.mayorAlimentos(r4)==false)
                 System.out.println("Método mayorAlimentos() funciona correctamente");
             else 
                System.out.println("ERROR: revisar metodo mayorAlimentos()");
        
        System.out.println("----------------------------------------------------------");
        
        //-------------------------------------------------------------------

        System.out.println("Testeando método clone()...");

        r5 = r.clone();
        if (r.obtenerAlimentos() == r5.obtenerAlimentos() && r.obtenerBebidas() == r5.obtenerBebidas() && r.obtenerCamas() == r5.obtenerCamas()){
            System.out.println("Método clone() funciona correctamente");
        }
        else{
            System.out.println("ERROR");
        }

        //-------------------------------------------------------------------






        // verificar los métodos restantes   







        System.out.println("----------------------------------------------------------");
        System.out.println("FIN DEL TESTING");

    }




}
