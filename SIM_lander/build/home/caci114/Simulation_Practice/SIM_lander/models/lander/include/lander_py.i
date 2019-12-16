%module m496ab9d9ae3d6a89daf6de4a1204eb3a

%include "trick/swig/trick_swig.i"


%insert("begin") %{
#include <Python.h>
#include <cstddef>
%}

%{
#include "/home/caci114/Simulation_Practice/SIM_lander/models/lander/include/lander.h"
%}

%trick_swig_class_typemap(Lander, Lander)



#ifndef _lander_hh_
#define _lander_hh_
%import(module="sim_services") "trick/regula_falsi.h"

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

	

	


	int lander_default_data();
	int lander_init();
	int lander_controls();
	int lander_deriv();
	int lander_integ();
	int lander_post_integ();
	int lander_shutdown();
	

};
#define TRICK_SWIG_DEFINED_Lander
#endif


#ifdef TRICK_SWIG_DEFINED_Lander
%trick_cast_as(Lander, Lander)
#endif
