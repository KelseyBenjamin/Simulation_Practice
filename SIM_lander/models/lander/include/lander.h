/*************************************************************************
PURPOSE: (Represent the state and initial conditions of a lander)
**************************************************************************/
#ifndef _lander_hh_
#define _lander_hh_
#include "trick/regula_falsi.h"

class Lander {
public:
   

	double pos[2];
	double vel[2];
	double acc[2];
	double angle;
	double angleDot;
	double angleDDot;
	double thrust;

	double throttle;
	int rcs_command;


	double thrust_max;
	double rcs_torque;
	double mass;
	double moment_of_inertia;
	double g;

	int manual_throttle_change_command;
	int manual_rcs_command;
	int Auto_1;
	int Auto_2;

	bool survive;
	bool good_land;

	/*int impact;
	double impactTime;
	REGULA_FALSI rf;
	*/
	


	int lander_default_data();
	int lander_init();
	int lander_controls();
	int lander_deriv();
	int lander_integ();
	int lander_post_integ();
	int lander_shutdown();
	//double lander_impact();

};
#endif

