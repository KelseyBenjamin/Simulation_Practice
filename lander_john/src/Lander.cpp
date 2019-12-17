/********************************* TRICK HEADER *******************************
PURPOSE: ( Simulate a satellite orbiting the Earth. )
LIBRARY DEPENDENCY:
    ((Lander.o))
*******************************************************************************/
#include "../include/Lander.hh"
#include "trick/integrator_c_intf.h"
#include <math.h>
#include <iostream>

#define RAD_PER_DEG (M_PI / 180.0)
#define DEG_PER_RAD (180.0/ M_PI )

int Lander::default_data() {

    pos[0] = 0.0;
    pos[1] = 1.8;
    vel[0] = 0.0;
    vel[1] = 0.0;
    angle = 0.0;
    angleDot = 0.0;
    angleDDot = 0.0;

    thrust_max = 15000;
    rcs_torque = 100;
    mass = 2000;
    moment_of_inertia = 2000;
    g = 1.62;                   // Gravitional acceleration on the moon.

    throttle = 0;
    rcs_command = 0;

    // Controls
    manual_throttle_change_command = 0;
    manual_rcs_command = 0;
    Auto_1 = 0;
    Auto_2 = 0;

    // Auto Control Parameters
    x_cmd = 40.0;
    y_cmd = 20.0;

    return (0);
}

int Lander::state_init() {
    return (0);
}

int Lander::control() {

    if (Auto_1 == 1) {
         y_cmd = 100;
         vy_cmd = 0.2 * (y_cmd - pos[1]);
         double vy_limit = 40.0;
         if (vy_cmd >  vy_limit) vy_cmd = vy_limit;
         if (vy_cmd < -vy_limit) vy_cmd = -vy_limit;
         ay_cmd = g + 0.6 * (vy_cmd - vel[1]);
         throttle = (ay_cmd * mass * 100) / thrust_max;
    }

    if (Auto_2 == 1) {
        x_cmd = 0;
        if (throttle >= 10 ) {
            vx_cmd = 0.05 * (x_cmd - pos[0]);
            // double vx_limit = 5.0;
            double vx_limit = 0.2 * pos[1];
            if (vx_cmd >  vx_limit) vx_cmd =  vx_limit;
            if (vx_cmd < -vx_limit) vx_cmd = -vx_limit;

            double thrust = (throttle / 100.0) * thrust_max;
            double a_max = thrust / mass;

            ax_cmd = 0.1 * (vx_cmd - vel[0]);
            if (ax_cmd >  0.5 * a_max ) ax_cmd =  0.5 * a_max ;
            if (ax_cmd < -0.5 * a_max ) ax_cmd = -0.5 * a_max ;

            double acc_ratio = ax_cmd / a_max ; // must be between 0..1
            angle_cmd = -asin( acc_ratio );

            if (angle_cmd >  30.0 * RAD_PER_DEG) angle_cmd =  30.0 * RAD_PER_DEG;
            if (angle_cmd < -30.0 * RAD_PER_DEG) angle_cmd = -30.0 * RAD_PER_DEG;

            angle_dot_cmd = 0.5 * (angle_cmd - angle);

            if (angle_dot_cmd >  5.0 * RAD_PER_DEG) angle_dot_cmd =  5.0 * RAD_PER_DEG;
            if (angle_dot_cmd < -5.0 * RAD_PER_DEG) angle_dot_cmd = -5.0 * RAD_PER_DEG;

            if ((angle_dot_cmd - angleDot) > 0.1 * RAD_PER_DEG) {
                rcs_command =  1;
            } else if ((angle_dot_cmd - angleDot) < -0.1 * RAD_PER_DEG) {
                rcs_command = -1;
            } else {
                rcs_command =  0;
            }
        }
    } else {
        rcs_command = manual_rcs_command;
    }

    throttle += manual_throttle_change_command;
    if (throttle > 100) throttle = 100;
    if (throttle <   0) throttle = 0;

    return (0);
}

int Lander::state_deriv() {

   double thrust = (throttle / 100.0) * thrust_max;

   acc[0] = (thrust * -sin(angle)) / mass;
   acc[1] = (thrust *  cos(angle)) / mass - g;

   angleDDot = rcs_command * rcs_torque / moment_of_inertia;

   return(0);
}

int Lander::state_integ() {

   int integration_step;

   load_state ( &pos[0], &pos[1], &vel[0], &vel[1], &angle, &angleDot, (double*)0);
   load_deriv ( &vel[0], &vel[1], &acc[0], &acc[1], &angleDot, &angleDDot, (double*)0);

   integration_step = integrate();

   unload_state( &pos[0], &pos[1], &vel[0], &vel[1], &angle, &angleDot, (double*)0);

   return(integration_step);
}

int Lander::check_ground_contact() {
    if (pos[1] < 1.8) {
        pos[1] = 1.8;
        vel[0] = 0.0;
        vel[1] = 0.0;
        angle = 0.0;
        angleDot = 0.0;
    }
    return(0);
}
