#! -*- coding: UTF-8 -*-
'''
Created on Nov 24, 2014

@summary: A small tool to generate VPN configuration packages for various tools and services.
@author: Hakan Bayındır
@contact: hakan@bayindir.org
'''

import argparse # We will use argument parser to parse our arguments.



if __name__ == '__main__':
    # Let's create the argument parser
    argument_parser = argparse.ArgumentParser();
    
    # Then configure it a bit.
    argument_parser.description = "Create configuration packages for various OpenVPN tools."
    
    # We need arguments, don't we?
    # NOTE: The format may be improved later.
    argument_parser.add_argument("configuration_type", metavar="T", choices=["viscosity", "tunnelblick", "unified-ovpn"], help="Type of the configuration package to generate.");
    argument_parser.add_argument("open_vpn_key", metavar="K", type=file, help="OpenVPN private key file.")
    argument_parser.add_argument("open_vpn_certificate", metavar="C", type=file, help="OpenVPN certificate file.")
    argument_parser.add_argument("open_vpn_configuration_file", metavar="F", type=file, help="OpenVPN client configuration file.")
    argument_parser.add_argument("configuartion_otuput_file", metavar="O", help="Name of the resulting configuration package.")
    
    # Set, ready, parse!
    arguments = argument_parser.parse_args();
    
    print arguments
    
    # OK. We got our arguments, so we can start processing them.
    print "Some information:"
    print "Chosen configuration package type", arguments.type