/************************************************************************
PURPOSE: (Print the final lander state.)
*************************************************************************/
#include <stdio.h>
#include "../include/lander.h"
#include "trick/exec_proto.h"

int cannon_shutdown( LANDER* C) {
    double t = exec_get_sim_time();
    printf( "========================================\n");
    printf( "      Lander State at Shutdown     \n");
    printf( "t = %g\n", t);
    printf( "pos = [%.9f, %.9f]\n", C->pos[0], C->pos[1]);
    printf( "vel = [%.9f, %.9f]\n", C->vel[0], C->vel[1]);
    printf( "DID YOU SURVIVE?", survive);
	if (survive)
	{
		printf( "DID YOU LAND OPTIMALLY?", good_land);	
	}
    printf( "========================================\n");
    return 0 ;
}

