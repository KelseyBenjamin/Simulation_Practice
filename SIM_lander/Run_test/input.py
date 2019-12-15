trick.stop(10)

#==================================
# Start the variable server client.
#==================================
varServerPort = trick.var_server_get_port();
LanderDisplay_path = os.environ['HOME'] + "/LanderDisplay_Rev2.py"
if (os.path.isfile(LanderDisplay_path)) :
    LanderDisplay_cmd = LanderDisplay_path + " " + str(varServerPort) + " &" ;
    print(LanderDisplay_cmd)
    os.system( LanderDisplay_cmd);
else :
    print('Oops! Can\'t find ' + CannonDisplay_path )
