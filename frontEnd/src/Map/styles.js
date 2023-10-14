import { Fill, Style, Text, Stroke, Circle } from 'ol/style.js';

export const hatcheryStyle = new Style({
    text: new Text({
        font: '12px Calibri,sans-serif',
        overflow: true,
        fill: new Fill({
            color: 'black',
        }),
        stroke: new Stroke({
            color: 'white',
            width: 3,
        }),
        offsetY: -5
    }),

    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: "red"
        })
    })
});

export const fishTrapStyle = new Style({
    text: new Text({
        font: '12px Calibri,sans-serif',
        overflow: true,
        fill: new Fill({
            color: 'black',
        }),
        stroke: new Stroke({
            color: 'white',
            width: 3,
        }),
        offsetY: -5
    }),

    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: "blue"
        })
    })
});