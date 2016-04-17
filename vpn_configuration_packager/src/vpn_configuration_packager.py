#! -*- coding: UTF-8 -*-
'''
Created on Nov 24, 2014

@summary: A small tool to generate VPN configuration packages for various tools and services.
@author: Hakan Bayındır
@contact: hakan@bayindir.org
'''

import sys      # I use some stuff from here.

import argparse # We will use argument parser to parse our arguments.
import logging  # Use a proper logging library to give information

# Logging settings
# They may be moved to a configuration file later on.
LOG_FILE = None # Change to a string of full path to enable logging to file.
MINIMUM_LOG_LEVEL = logging.DEBUG # Possible values are {DEBUG, INFO, WARN, ERROR, CRITICAL}

if __name__ == '__main__':
    # Start the logger first.
        # First step is to make the logger run.
    try:
        logging.basicConfig(filename=LOG_FILE, level=MINIMUM_LOG_LEVEL,
                            format="[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S")

        # Get the local logger and start.
        local_logger = logging.getLogger("main")

        local_logger.debug("Logger setup completed.")
        local_logger.debug("%s is starting.", sys.argv[0])
    except IOError as exception:
        print "Something about disk I/O went bad: " + str(exception)
        sys.exit(1)
    
    # Let's create the argument parser
    argument_parser = argparse.ArgumentParser();
    
    # Then configure it a bit.
    argument_parser.description = "Create unified configuration files for OpenVPN."
    
    # We need arguments, don't we?
    # NOTE: The format may be improved later.
    #argument_parser.add_argument("configuration_type", metavar="T", choices=["viscosity", "tunnelblick", "unified-ovpn"], help="Type of the configuration package to generate.");
    #argument_parser.add_argument("open_vpn_key", metavar="K", type=file, help="OpenVPN private key file.")
    #argument_parser.add_argument("open_vpn_certificate", metavar="C", type=file, help="OpenVPN certificate file.")
    argument_parser.add_argument("open_vpn_configuration_file", metavar="input_file", type=file, help="OpenVPN client configuration file.")
    argument_parser.add_argument("configuartion_otuput_file", metavar="output_file", help="Name of the unified configuration package.")
    
    # Set, ready, parse!
    arguments = argument_parser.parse_args();

    logging.debug("Passed arguments are %s", arguments)
    
    # OK. We got our arguments, so we can start processing them.
    logging.debug("Chosen configuration type is %s", arguments.configuration_type)
