# Adaptations 

## Application

This code contains viewers created with Xeokit-SDK and a code imports sensor data, match sensor infortion with IFC Model.

## Compiling Sensor Information with IFC Model

After importing sensor information with ./SensodataIfModelConfiguration/sources/main.py you can upload the model into viewer

## Running Viewer

viewer is located in ./xeokit-sdk/examples/BIMOffline_XKT_WestRiverSideHospital.html you can run on your local machine
if you run the model it will start with Duplex.xkt model

## Converting Ifc to Xkt

Important to convert IFC Models to XKT format, xeokit convertor is a proper tool for this https://hub.docker.com/r/bimspot/xeokit-converter also available on docker. Important to make sure the XKT Version is v8



# xeokit-sdk

[![This project is using Percy.io for visual regression testing.](https://percy.io/static/images/percy-badge.svg)](https://percy.io/73524691/xeokit-sdk)
[![npm version](https://badge.fury.io/js/%40xeokit%2Fxeokit-sdk.svg)](https://badge.fury.io/js/%40xeokit%2Fxeokit-sdk)
[![](https://data.jsdelivr.com/v1/package/npm/@xeokit/xeokit-sdk/badge)](https://www.jsdelivr.com/package/npm/@xeokit/xeokit-sdk)

[xeokit](http://xeokit.io) is a JavaScript software development kit from [xeolabs](http://xeolabs.com) for viewing
high-detail, full-precision 3D engineering and BIM models in the browser.

## Installing

````bash
npm i @xeokit/xeokit-sdk
````

## Usage

The xeokit SDK lets us develop our own browser-based BIM viewer, which we can fully customize and extend with
plugins. Let's create a [Viewer](https://xeokit.github.io/xeokit-sdk/docs/class/src/viewer/Viewer.js~Viewer.html) with
a [WebIFCLoaderPlugin](https://xeokit.github.io/xeokit-sdk/docs/class/src/plugins/WebIFCLoaderPlugin/WebIFCLoaderPlugin.js~WebIFCLoaderPlugin.html)
to view a IFC model in the browser, then view a sample IFC model from
the [Open IFC Model Database](http://openifcmodel.cs.auckland.ac.nz/Model/Details/274).

 * [Run this example](https://xeokit.github.io/xeokit-sdk/examples/#BIMOffline_WebIFCLoaderPlugin_Duplex)
 * [Read the full tutorial](https://www.notion.so/xeokit/Viewing-an-IFC-Model-with-WebIFCLoaderPlugin-9a572b801af949bf87a21c88968bd251)

![](https://xeokit.io/img/docs/WebIFCLoaderPlugin/WebIFCLoaderPluginBig.png)

````html
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>xeokit Example</title>
    <style>
        body {
            margin: 0;
            width: 100%;
            height: 100%;
            user-select: none;
        }

        #myCanvas {
            width: 100%;
            height: 100%;
            position: absolute;
            background: lightblue;
            background-image: linear-gradient(lightblue, white);
        }
    </style>
</head>
<body>
<canvas id="myCanvas"></canvas>
</body>
<script id="source" type="module">

    import {Viewer, WebIFCLoaderPlugin} from
                "https://cdn.jsdelivr.net/npm/@xeokit/xeokit-sdk/dist/xeokit-sdk.es.min.js";

    const viewer = new Viewer({
        canvasId: "myCanvas",
        transparent: true
    });

    viewer.camera.eye = [-3.933, 2.855, 27.018];
    viewer.camera.look = [4.400, 3.724, 8.899];
    viewer.camera.up = [-0.018, 0.999, 0.039];

    const webIFCLoader = new WebIFCLoaderPlugin(viewer, {
        wasmPath: "https://cdn.jsdelivr.net/npm/@xeokit/xeokit-sdk/dist/"
    });

    const model = webIFCLoader.load({
        src: "Duplex.ifc",
        edges: true
    });

</script>
</html>
````

## Resources

* [xeokit.io](https://xeokit.io/)
* [Examples](http://xeokit.github.io/xeokit-sdk/examples/)
* [Guides](https://www.notion.so/xeokit/xeokit-Documentation-4598591fcedb4889bf8896750651f74e)
* [API Docs](https://xeokit.github.io/xeokit-sdk/docs/)
* [Changelog](https://xeokit.github.io/xeokit-sdk/CHANGE_LOG)
* [Features](https://xeokit.io/index.html?foo=1#features)
* [FAQ](https://xeokit.io/index.html?foo=1#faq)
* [Blog](https://xeokit.io/blog.html)
* [License](https://xeokit.io/index.html#pricing)






