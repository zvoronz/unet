//  Unix-network (unet) - Object-oriented high-level C++ Unix network framework.
//  Copyright (C) 2013 Oleynikov Nikolay
//
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
//  Author email: OleynikovNY@mail.ru

#include <iostream>
#include <Unet/Ipv4Address.hpp>
#include <Unet/UdpEchoServer.hpp>

int main ( int argc , char** argv )
{

    //  Check if server IP address and port command line parameters were provided
    if ( argc != 3 )
    {
        //  Show how the program is supposed to be launched
        std::cout << "Usage: UdpEchoServer_002 $(SERVER_IP) $(SERVER_PORT)" << std::endl;
        return -1;
    }

    //  Create an instance of IPv4 address on the heap wrapped by a smart pointer
    Unet::AddressUniPtr udpEchoServerAddressUniPtr(new Unet::Ipv4Address(argv[1],argv[2]));

    //  Create an instance of UDP echo server
    Unet::UdpEchoServer udpEchoServer;

    //  Set server address which it will listen to
    udpEchoServer.setAddress(std::move(udpEchoServerAddressUniPtr));

    //  Launch the server
    udpEchoServer.start();

    //  The server runs asynchronously in a separate thread thus this indefinite loop is used
    //  to prevent the program from finishing it's execution
    while ( true )
    {

    }

    return 0;

}