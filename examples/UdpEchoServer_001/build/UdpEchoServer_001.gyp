{
    'includes'  :   [
                        './../../../system/gyp/includes/example_includes.gypi',
                    ],
    'variables' :   {
                        'UNIT_NAME'         :   'UdpEchoServer_001',
                        'UNIT_SOURCES'      :   [
                                                    '<(UNIT_SOURCES_DIR)/<(UNIT_NAME).cpp',
                                                ],
                        'UNIT_DEPENDENCIES' :   [
                                                    './../../../src/Socket/UdpSocket/UdpSocket/build/UdpSocket.gyp:UdpSocket',
                                                    './../../../src/Address/Ipv4Address/build/Ipv4Address.gyp:Ipv4Address',
                                                ],
                        'UNIT_CFLAGS'       :   [
                                                ],
                        'UNIT_LDFLAGS'      :   [
                                                ],
                    },
}