/*************************************************************************
PURPOSE: ( lander Numeric Model )
**************************************************************************/

#ifndef LANDER_NUMERIC_H
#define LANDER_NUMERIC_H

#include "lander.h"

#ifdef __cplusplus
extern "C" {
#endif
int lander_integ(LANDER*) ;
int lander_deriv(LANDER*) ;

#ifdef __cplusplus
}
#endif
#endif

