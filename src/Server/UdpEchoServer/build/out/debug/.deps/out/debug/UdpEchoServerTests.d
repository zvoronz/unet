cmd_out/debug/UdpEchoServerTests := flock out/debug/linker.lock g++ /home/kolyunya/projects/gtest/build/gtest-all.o -lpthread  -o out/debug/UdpEchoServerTests -Wl,--start-group out/debug/obj.target/UdpEchoServerTests/../src/UdpEchoServer.o out/debug/obj.target/UdpEchoServerTests/../tests/src/UdpEchoServerTests.o out/debug/obj.target/../../UdpServer/build/libUdpServer.a out/debug/obj.target/libUdpEchoServer.a out/debug/obj.target/../../../Exception/Exception/build/libException.a out/debug/obj.target/../../SocketServer/build/libSocketServer.a out/debug/obj.target/../../../Address/Address/build/libAddress.a out/debug/obj.target/../../../Socket/UdpSocket/build/libUdpSocket.a out/debug/obj.target/../../../Socket/Socket/build/libSocket.a out/debug/obj.target/../../../File/File/build/libFile.a out/debug/obj.target/../../../Datagram/Datagram/build/libDatagram.a out/debug/obj.target/../../../Address/NullAddress/build/libNullAddress.a out/debug/obj.target/../../../Address/AddressFactory/build/libAddressFactory.a out/debug/obj.target/../../../Address/Ipv4Address/build/libIpv4Address.a out/debug/obj.target/../../../Address/Ipv6Address/build/libIpv6Address.a -Wl,--end-group 
