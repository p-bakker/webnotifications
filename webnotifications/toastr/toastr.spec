{
	"name": "webnotifications-toastr",
	"displayName": "Toastr notifications",
	"version": 1,
 	"definition": "webnotifications/toastr/toastr.js",
	"libraries": 
	[
		{
			"name": "toastr.min.css",
			"version": "1",
			"url": "webnotifications/toastr/lib/toastr.min.css",
			"mimetype": "text/css"
		},

		{
			"name": "toastr.min.js",
			"version": "1",
			"url": "webnotifications/toastr/lib/toastr.min.js",
			"mimetype": "text/javascript"
		}
	],

	"model": 
	{
		
	},

	"api": 
	{
		"info": 
		{
			"parameters": [
				{                                                                 
					"name":"message",
					"type":"string"
				},
				{                                                                 
					"name":"title",
					"type":"string",
					"optional":true
				},
				{                                                                 
					"name":"options",
					"type":"toastrOptions",
					"optional":true
				}              
			]
		},

		"warning": 
		{
			"parameters": [
				{                                                                 
					"name":"message",
					"type":"string"
				},
				{                                                                 
					"name":"title",
					"type":"string",
					"optional":true
				},
				{                                                                 
					"name":"options",
					"type":"toastrOptions",
					"optional":true
				}               
			]
		},

		"success": 
		{
			"parameters": [
				{                                                                 
					"name":"message",
					"type":"string"
				},
				{                                                                 
					"name":"title",
					"type":"string",
					"optional":true
				},
				{                                                                 
					"name":"options",
					"type":"toastrOptions",
					"optional":true
				}               
			]
		},

		"error": 
		{
			"parameters": [
				{                                                                 
					"name":"message",
					"type":"string"
				},
				{                                                                 
					"name":"title",
					"type":"string",
					"optional":true
				},
				{                                                                 
					"name":"options",
					"type":"toastrOptions",
					"optional":true
				}               
			]
		},

		"clear": 
		{
			
		}
	},

	"types": 
	{
		"toastrOptions": 
		{
			"showDuration": "int",
			"hideDuration": "int",
			"positionClass": "string",
			"onclick": "string",
			"onShown": "string",
			"onHidden": "string",
			"closeButton": "boolean",
			"closeHtml": "string",
			"newestOnTop": "boolean",
			"showEasing": "string",
			"hideEasing": "string",
			"showMethod": "string",
			"hideMethod": "string"
		}
	}
}