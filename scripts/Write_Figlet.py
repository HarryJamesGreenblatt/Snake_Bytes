import pyfiglet, sys, json

if sys.argv[1] == 'show_font_options':

    print( json.dumps( pyfiglet.FigletFont.getFonts() ) )

else:

    if len(sys.argv) > 2 and len(sys.argv[2]) > 1:

        pyfiglet.print_figlet(
            sys.argv[1],
            sys.argv[2] 
        )

    else:

        pyfiglet.print_figlet(
            sys.argv[1]
        )