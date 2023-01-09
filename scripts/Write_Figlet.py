'''
NAME
    Write_Figlet.py


PURPOSE
    Integrates with a custom PowerShell module, Write-Figlet.psm1,\n
    in order to leverage the pyfiglet module to print the Text Input\n
    provided to the script as a Command Line Argument represented in the\n
    ASCII Typesetting Format which may also be optionally proivided as a\n
    Command Line Arguement. 


DESCRIPTION
    After importing the neccessary modules, the script checks the Command Line\n
    Arguments it was provided to determine whether it needs to either print out\n
    the List of Font Options in JSON format, or to convert the given Text String\n
    to the ASCII Typesetting which wasoptionally specified. 


PROCESS
    #1 Import the neccessary sys, json, and pyfiglet modules

    #2 Check if the 'show_font_options' flag has been provided

    #3 Print the data provided as a Command Line Argument using an optional typesetting Font     


INPUT
    Command Line Arguments:
        Write-Figlet.psm1 takes arguments corresponding to the Text to be generated,\n 
        and the Font to be used in producing the ASCII Typesetting.

        These inputs are then migrated to Write_Figlet.py using the following call:

            python  Write_Figlet.py  text_to_generate  font_selection


OUTPUT
    NONE,\n 
    but produces the following SIDE-EFFECTs:\n 
        if provided a single argument indicating to 'show_font_options':\n
            prints a JSON-converted list of Font Options
        othewise:
            prints the Command Line Argument provided Text string\n
            to the ASCII Typresetting specified by the\n
            optionally provided Font Command Line Argument


DEPENDENCIES
    Standard Library Modules:\n
        sys\n
        json

    Third Party Modules:\n
        pyfiglet
'''

# 1. Import the neccessary sys, json, and pyfiglet modules
##########################################################################################
import pyfiglet, sys, json   #   generate ASCII, interface with the CLI, convert to json  
##########################################################################################


# 2 Check if the 'show_font_options' flag has been provided
##########################################################################################
if sys.argv[1] == 'show_font_options':       #   If the first Command Line Argument 
                                             #   provided explicitly reads:                                     
    print(                                   #       'show_font_options'
        json.dumps(                          #   it is a flag passed by the caller
            pyfiglet.FigletFont.getFonts()   #   to indicate the desire to convert
        )                                    #   the Figlet Font Library List 
    )                                        #   to json and print the output to console
##########################################################################################


# 3 Print the Text provided as a Command Line Argument using an optional Font 
##########################################################################################
else:                                        #   Otherwise, no 'show_font_options'
                                             #   has been flag passed into the CLI.
    if(                                      #      If the Number of Args passed into the  
        len(sys.argv) == 3                   #      CLI is 2, then the user has specified 
        and                                  #      a Font selection. ADDITIONALLY, 
        len(sys.argv[2]) > 1                 #      If it can be verified that Font   
    ):                                       #      Selection provided in the CLI is not     
                                             #      just an empty string,     
        pyfiglet.print_figlet(               #       
            sys.argv[1],                     #      then generate ASCII Typesetting        
            sys.argv[2]                      #      using the Selected Font.       
        )                                    #      
                                             #
    elif(                                    #      If the Number of Args passed into the  
        len(sys.argv) == 4                   #      CLI is 3, then the user has specified 
        and                                  #      a Font selection. ADDITIONALLY, 
        len(sys.argv[2]) > 1                 #      If it can be verified that Font   
    ):                                       #      Selection provided in the CLI is not     
                                             #      just an empty string,     
        pyfiglet.print_figlet(               #       
            sys.argv[1],                     #      then generate ASCII Typesetting        
            sys.argv[2]                      #      using the Selected Font.       
        )                                    #      
                                             #      
    else:                                    #         otherwise,    
                                             #            
        pyfiglet.print_figlet(               #             just generate ASCII Typesetting                
            sys.argv[1]                      #             using the Default Font.      
        )                                    #   
#########################################################################################