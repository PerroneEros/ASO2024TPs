#incluir <unistd.h>
#incluir <sys/tipos.h>
#incluir <stdio.h>
#incluir <sys/esperar.h>


entero principal( ){
   pid_t pid_del_niño;

   pid_del_niño = tenedor();//Crea un nuevo proceso hijo

   si(pid_del_niño < 0) {
      imprimirf("¡¡FALLÓ EL TENEDOR!!");

      devolver 1;
   }demás si(pid_del_niño == 0) {
      imprimirf("ME ACABAN DE CREAR, SOY UN PROCESO HIJO!, MI PROCESS ID ES = %d, Y EL DEL MI PADRE ES = %d\n",obtener pid(),obtener ppid( ));
   }demás{
      esperar(NULO);//Bloquea al padre hasta que todos los hijos finalicen

      imprimirf("¡SOY EL PROCESO PADRE!");
      imprimirf("MI PROCESS ID ES = %d, Y EL DE MI PADRE = %d, Y EL DEL HIJO RECIEN CREADO = %d\n",obtener pid( ),obtener ppid( ),pid_del_niño);
   }


dormir(10);

devolver 0;
}
