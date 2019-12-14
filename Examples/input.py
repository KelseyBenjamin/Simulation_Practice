execfile("Modified_data/realtime.py")
execfile("Modified_data/cannon.dr")



#trick.trick_view_add_auto_load_file("TV_cannon.tv")
trick.stop(5.2)

#==================================
# Start the variable server client.
#==================================
varServerPort = trick.var_server_get_port();
CannonDisplay_path = os.environ['HOME'] + "/CannonDisplay_Rev2.py"
if (os.path.isfile(CannonDisplay_path)) :
    CannonDisplay_cmd = CannonDisplay_path + " " + str(varServerPort) + " &" ;
    print(CannonDisplay_cmd)
    os.system( CannonDisplay_cmd);
else :
    print('Oops! Can\'t find ' + CannonDisplay_path )

