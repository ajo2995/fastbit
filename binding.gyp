{
  "targets": [
    {
      "target_name": "fb",
      "sources": [ "fb.cc" ],
	  "include_dirs": ["/usr/local/include"],
	  "libraries": ["-L/usr/local/lib",'-lfastbit'],
      "cflags!": [ '-fno-exceptions' ],
      "cflags_cc!": [ '-fno-exceptions' ],
	  "conditions": [
		  ['OS=="mac"', {
			  'xcode_settings': {
				  'OTHER_CPLUSPLUSFLAGS' : ['-mmacosx-version-min=10.7','-stdlib=libc++'],
                  'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
			  }
		  }]
	  ]
    }
  ]
}
