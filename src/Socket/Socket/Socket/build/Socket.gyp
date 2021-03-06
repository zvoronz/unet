{
    'includes'  :   [
                        './../../../../../system/gyp/includes/includes.gypi',
                    ],
    'variables' :   {
                        'UNIT_NAME'             :   'Socket',
                        'UNIT_NEEDS_BUILDING'   :   'true',
                        'UNIT_NEEDS_TESTSING'   :   'false',
                        'UNIT_SOURCES'          :   [
                                                        '<(UNIT_SOURCES_DIR)/<(UNIT_NAME).hpp',
                                                        '<(UNIT_SOURCES_DIR)/<(UNIT_NAME).tpp',
                                                        '<(UNIT_SOURCES_DIR)/<(UNIT_NAME).cpp',
                                                    ],
                        'UNIT_DEPENDENCIES'     :   [
                                                        './../../../../Address/Address/AddressFactory/build/AddressFactory.gyp:AddressFactory',
                                                        './../../../../Address/NullAddress/build/NullAddress.gyp:NullAddress',
                                                        './../../../../File/File/build/File.gyp:File',
                                                    ],
                        'UNIT_CFLAGS'           :   [
                                                    ],
                        'UNIT_LDFLAGS'          :   [
                                                    ],
                    },
}