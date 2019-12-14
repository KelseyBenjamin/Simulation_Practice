/******************************* TRICK HEADER ****************************
PURPOSE: (Set the initial data values)
*************************************************************************/

/* Model Include files */
#include <math.h>
#include "../include/lander.h"


/* default data job */
	int lander_default_data( LANDER* L) {

   	thrust_max = 15000;
	rcs_torque - 50;
	mass = 2000;
	moment_of_inertia = 2000;
	g = 1.62;
  	

	return 0 ;
}





/* initialization job */
	int lander_init( LANDER* L) {
   
    	
	L->pos[0] = 0.0;
	L->pos[1] = 1.8;


	L->vel[0] = 0.0;
	L->vel[1] = 0.0;

	
	angle = 0.0;
	
	angleDot = 0.0;




	return 0 ; 
}

