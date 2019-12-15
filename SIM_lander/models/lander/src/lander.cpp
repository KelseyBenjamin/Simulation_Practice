/********************************* TRICK HEADER *******************************
PURPOSE: ( Simulate a model lander. )
LIBRARY DEPENDENCY:
    ((lander.o))
*******************************************************************************/
#include "sim_services/Integrator/include/integrator_c_intf.h"
#include "../include/lander.h"
#include "trick/exec_proto.h"
#include <math.h>
#include <iostream>

int Lander::lander_default_data() {

	thrust_max = 15000;
	rcs_torque = 50;
	mass = 2000;
	moment_of_inertia = 2000;
	g = 1.62;
    	return (0);
}

int Lander::lander_init() {
    
	pos[0] = 0.0;
	pos[1] = 1.8;


	vel[0] = 0.0;
	vel[1] = 0.0;


	angle = 0.0;

	angleDot = 0.0;

    	return (0);
}

int Lander::lander_deriv() {

	thrust = (throttle / 100) * thrust_max;
	acc[0] = (thrust* -sin(angle)*thrust_max);
	acc[1] = (thrust * cos(angle) * thrust_max);
	angleDDot = rcs_command * rcs_torque / moment_of_inertia;

   return(0);
}

int Lander::lander_shutdown() {

	double t = exec_get_sim_time();
  	printf( "========================================\n");
   	printf( "     Lander  State at Shutdown     \n");
    	printf( "t = %g\n", t);
    	printf( "pos = [%.9f, %.9f]\n", C->pos[0], C->pos[1]);
    	printf( "vel = [%.9f, %.9f]\n", C->vel[0], C->vel[1]);
	//printf( "DID YOU SURVIVE\n %s",survive);
	//printf( "WAS IT A GOOD LAND\n %s", good_land);
    	printf( "========================================\n");
    return 0 ;	

}

int Lander::lander_integ() {

   int integration_step;

   load_state ( &pos[0], &pos[1], &vel[0], &vel[1], &angle, &angleDot, (double*)0);
   load_deriv ( &vel[0], &vel[1], &acc[0], &acc[1], &angleDot, &angleDDot, (double*)0);

   integration_step = integrate();
   unload_state ( &pos[0], &pos[1], &vel[0], &vel[1], &angle, &angleDot, (double*)0);

   return(integration_step);
}
