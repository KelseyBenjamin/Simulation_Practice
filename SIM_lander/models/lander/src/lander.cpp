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
using namespace std;

int Lander::lander_default_data() {

	thrust_max = 15000;
	thrust = 0;
	throttle =0;
	rcs_command =0;
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


int Lander::lander_controls() {

	throttle += manual_throttle_change_command;
	rcs_command = manual_rcs_command;
	
	if (throttle > 100)
		throttle = 100;
	if (throttle < 0)
		throttle = 0;


	//Auto controls
	if (Auto_1 == 1) {
		// Do some automatic control stuff ... (e.g. altitude hold).
		//fuel sim
	}
	if (Auto_2 == 1) {
		// Do some automatic control stuff ... (up to you also).
		//lose left thruster at a certain angle
	}
		
   return(0);
}

int Lander::lander_post_integ() {

	if (pos[1]<1.8)
	{
		pos[0]=0;
		pos[1]=1.8;
		vel[0]=0.0;
		vel[1]=0.0;
		angle = 0.0;
		angleDot = 0.0;
	}
	
   return(0);
}

int Lander::lander_deriv() {


	thrust = (throttle / 100) * thrust_max;
	acc[0] = (thrust* -sin(angle)/mass);
	acc[1] = (thrust * cos(angle)/mass)-g;
	angleDDot = rcs_command * rcs_torque / moment_of_inertia;

   return(0);
}

int Lander::lander_shutdown() {

	double t = exec_get_sim_time();
  	cout <<"========================================"<< endl;
	cout << t<< endl;
   	cout <<"    Lander  State at Shutdown     "<< endl;
    	cout <<"pos =" <<pos[0]<<", "<<pos[1]<<endl;
    	cout <<"vel ="<<vel[0]<<", "<<vel[1]<<endl;
	//printf( "DID YOU SURVIVE\n %s",survive);
	//printf( "WAS IT A GOOD LAND\n %s", good_land);
    	cout <<"========================================"<< endl;
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
