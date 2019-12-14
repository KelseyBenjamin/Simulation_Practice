/*********************************************************************
  PURPOSE: ( Trick numeric )
*********************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <math.h>
#include "trick/integrator_c_intf.h"
#include "../include/lander_numeric.h"

int lander_deriv(LANDER* L) {

  	L->thrust = (L->throttle / 100) * L->thrust_max);
	L->acc[0] = (thrust* -sin(L->angle)*L->thrust_max);
	L->acc[1] = (thrust * cos(L->angle) * L->thrust_max);
	L->angleDDot = L->rcs_command * L->rcs_torque / L->moment_of_inertia;

    return(0);
}



int lander_integ(LANDER* L) {
    int ipass;

    load_state(
        &L->pos[0] ,
        &L->pos[1] ,
        &L->vel[0] ,
        &L->vel[1] ,
	&angle ,
	&angleDot ,
        NULL );

    load_deriv(
        &L->vel[0] ,
        &L->vel[1] ,
        &L->acc[0] ,
        &L->acc[1] ,
	&angleDot ,
	&angleDDot ,
        NULL);

    ipass = integrate();

    unload_state(
        &L->pos[0] ,
        &L->pos[1] ,
        &L->vel[0] ,
        &L->vel[1] ,
	&angle ,
	&angleDot ,
        NULL );

    return(ipass);
}

double lander_impact( LANDER* L ) {
    double tgo ; /* time-to-go */
    double now ; /* current integration time. */
    
    L->rf.error = L->pos[1] ;              /* Specify the event boundary. */
    now = get_integ_time() ;               /* Get the current integration time */
    tgo = regula_falsi( now, &(L->rf) ) ;  /* Estimate remaining integration time. */ 
    if (tgo == 0.0) {                      /* If we are at the event, it's action time! */
        now = get_integ_time() ;
        reset_regula_falsi( now, &(L->rf) ) ; 
        L->impact = 1 ;
        L->impactTime = now ;
        L->vel[0] = 0.0 ; L->vel[1] = 0.0 ;
        L->acc[0] = 0.0 ; L->acc[1] = 0.0 ;
        fprintf(stderr, "\n\nIMPACT: t = %.9f, pos[0] = %.9f\n\n", now, L->pos[0] ) ;
    }
    return (tgo) ;
}





