/*************************************************************************
PURPOSE: (Represent the state and initial conditions of a lander)
**************************************************************************/
#ifndef LANDER_H
#define LANDER_H

struct
{
	//Navigation State
								
	double pos[2];		/*	(m)		xy-position */
	double	vel[2]	;	/*	(m/s)		xy-velocity */
	double	acc[2]	;	/*	(m/s2)		xy-acceleration	*/
	double	angle	;	/*	(rad)		CCW=positive, CW= negative*/
	double	angleDot;	/*	(rad/s)	*/
	double	angleDDot;	/*	(rad/s2) */

	//Vehicle Controls State
								
	int throttle;			/* Range 0...100(percent) */
	int rcs_command;		/* 1 = CCW, 0 = no torque, -1 = CW */
	
	//Vehicle Attributes
	double thrust_max;		/* (N) Maxthrust the main engine can produce. */
	double rcs_torque;		/* Magnitude of RCS torque. */
	double mass;			/* (kg) */	
	double moment_of_inertia; 	/* (kg/m2) */
	double g;			/*(m/s2)- acceleration of gravity. */

	//Controls from client
	int manual_throttle_change_command;	/*(percent) update to throttle. */
	int manual_rcs_command;			/* 1 = CCW, 0 = no torque, -1 = CW */
	int Auto_1;
	int Auto_2;

	//bools added for output
	bool survive;
	bool good_land;
} LANDER ;


#ifdef __cplusplus
extern "C" {
#endif
    int lander_default_data(LANDER*) ;
    int lander_init(LANDER*) ;
    bool survive(LANDER*) ;
    bool good_land(LANDER*);
    int lander_shutdown(LANDER*) ;
#ifdef __cplusplus
}
#endif

#endif

