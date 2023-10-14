import React, { useRef, useState, useEffect } from 'react';
import { apply } from 'ol-mapbox-style';
import Map from 'ol/Map';
import View from 'ol/View';
import './Map.css';
import {
	addHatcheriesToMap,
	getHatcheryConfig,
	getHatcheryLayer,
} from './utils';
import Zoom from 'ol/control/Zoom.js';
import ContentPane from '../UiComponents/ContentPane';
import { useAppDispatch } from '../redux/hooks';
import {
	setHatcheries,
	setHatcheryFromMap,
	fetchHatcheryData,
} from '../redux/hatcherySlice';

const key = 'F59yA6jVyqJDnIgNn4tK';

const HatcheryMap = () => {
	const mapRef = useRef();
	const [map, setMap] = useState();
	const dispatch = useAppDispatch();

	const mapClickCallback = async (e, map) => {
		const hatcheryLayer = getHatcheryLayer(map);
		const pixel = map.getEventPixel(e.originalEvent);
		const features = await hatcheryLayer.getFeatures(pixel);
		if (features[0].values_) {
			const { geometry, ...hatcheryFeatures } = features[0].values_;
			console.log(hatcheryFeatures);
			dispatch(setHatcheryFromMap(hatcheryFeatures));
			dispatch(fetchHatcheryData(hatcheryFeatures.Facility));
		}
	};

	useEffect(() => {
		// Initialize map
		const mapObject = new Map({
			view: new View({
				center: [-13442414.623521939, 5965064.045686038],
				zoom: 8,
			}),
			target: mapRef.current,
			controls: [new Zoom({})],
		});
		getHatcheryConfig().then((res) => {
			addHatcheriesToMap(mapObject, res.data);
			dispatch(setHatcheries(res.data.features));
		});

		// Add base map
		apply(
			mapObject,
			`https://api.maptiler.com/maps/9ce45627-a3fc-4a9e-998d-59bbca39cd11/style.json?key=${key}`
		);

		// Set map to state and cause render
		setMap(mapObject);

		return () => {
			mapObject.un(mapClickCallback);
			setMap(undefined);
			mapRef.current = undefined;
		};
	}, []);

	// Register map events after map has been initialized
	useEffect(() => {
		if (map === undefined) return;
		// Add events
		map.on('pointermove', (e) => {
			if (e.dragging) return;
			const hatcheryLayer = getHatcheryLayer(map);
			if (!hatcheryLayer) return;
			const pixel = map.getEventPixel(e.originalEvent);
			hatcheryLayer.getFeatures(pixel).then((f) => {
				const feature = f.length ? f[0] : undefined;
				if (feature !== undefined) {
					document.body.style.cursor = 'pointer';
				} else {
					document.body.style.cursor = 'default';
				}
			});
		});

		map.on('click', (e) => mapClickCallback(e, map));
	}, [map]);

	return (
		<>
			<div className='wrapper'>
				<div ref={mapRef} className='map' />
				<ContentPane />
			</div>
		</>
	);
};

export default HatcheryMap;
