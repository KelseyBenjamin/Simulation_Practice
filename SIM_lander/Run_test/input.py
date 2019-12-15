execfile("Modified_Data/realtime.py")
execfile("Modified_Data/lander.dr")


trick.stop(10)


#==========================================
# Start the display VarServer Client
#==========================================
varServerPort = trick.var_server_get_port();
LanderDisplay_path = "models/graphics/dist/LanderDisplay.jar"

if (os.path.isfile(LanderDisplay_path)) :
    LanderDisplay_cmd = "java -jar " \
                   + LanderDisplay_path \
                   + " " + str(varServerPort) + " &" ;
    print(LanderDisplay_cmd)
    os.system( LanderDisplay_cmd);
else :
    print('==================================================================================')
    print('LanderDisplay needs to be built. Please \"cd\" into models/graphics and type \"make\".')
    print('==================================================================================')




