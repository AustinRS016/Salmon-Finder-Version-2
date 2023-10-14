import axios from 'axios';
import { HatcheryFeature, HatcheryGeoJson } from '../types';
import { fromLonLat } from 'ol/proj';
import { Vector } from 'ol/layer';
import VectorSource from 'ol/source/Vector';
import GeoJSON from 'ol/format/GeoJSON.js';
import { hatcheryStyle } from './styles';

export const getProjectionsString = async () => {
	return `PROJCRS["NAD83 / Washington North (ftUS)",BASEGEOGCRS["NAD83",DATUM["North American Datum 1983",ELLIPSOID["GRS 1980",6378137,298.257222101,LENGTHUNIT["metre",1]]],PRIMEM["Greenwich",0,ANGLEUNIT["degree",0.0174532925199433]],ID["EPSG",4269]],CONVERSION["SPCS83 Washington North zone (US Survey feet)",METHOD["Lambert Conic Conformal (2SP)",ID["EPSG",9802]],PARAMETER["Latitude of false origin",47,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8821]],PARAMETER["Longitude of false origin",-120.833333333333,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8822]],PARAMETER["Latitude of 1st standard parallel",48.7333333333333,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8823]],PARAMETER["Latitude of 2nd standard parallel",47.5,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8824]],PARAMETER["Easting at false origin",1640416.667,LENGTHUNIT["US survey foot",0.304800609601219],ID["EPSG",8826]],PARAMETER["Northing at false origin",0,LENGTHUNIT["US survey foot",0.304800609601219],ID["EPSG",8827]]],CS[Cartesian,2],AXIS["easting (X)",east,ORDER[1],LENGTHUNIT["US survey foot",0.304800609601219]],AXIS["northing (Y)",north,ORDER[2],LENGTHUNIT["US survey foot",0.304800609601219]],USAGE[SCOPE["Engineering survey, topographic mapping."],AREA["United States (USA) - Washington - counties of Chelan; Clallam; Douglas; Ferry; Grant north of approximately 47°30'N; Island; Jefferson; King; Kitsap; Lincoln; Okanogan; Pend Oreille; San Juan; Skagit; Snohomish; Spokane; Stevens; Whatcom."],BBOX[47.08,-124.79,49.05,-117.02]],ID["EPSG",2285]]`;
};

export const getESPGIO = async () => {
	const res = await axios.get('https://epsg.io/2285.wkt2');
	return res.data;
};

export const getHatcheryConfig = async (): Promise<any> => {
	try {
		const res = await axios.get('http://127.0.0.1:5000/mapconfig');
		reprojectCoordinates(res.data);
		return res;
	} catch (error) {
		console.log(error);
	}
};

export const getHatchery = async (facilityName: String): Promise<any> => {
	try {
		const res = await axios.get(
			`http://127.0.0.1:5000/hatchery/${facilityName}`
		);
		return res.data;
	} catch (error) {
		console.error(error);
	}
};

export const addHatcheriesToMap = async (map: any, hatcheries: Object) => {
	const hatcheryLayer = new Vector({
		source: new VectorSource({
			features: new GeoJSON().readFeatures(hatcheries),
		}),
		properties: { id: 'hatcheries' },
		style: (feature) => {
			hatcheryStyle.getText().setText(feature.get('Facility Name'));
			return hatcheryStyle;
		},
	});
	hatcheryLayer.setZIndex(100);
	map.addLayer(hatcheryLayer);
};

export const getHatcheryLayer = (map: any) => {
	const layers = map.getLayers().getArray();
	const hatcheryLayer = layers.find((l: any) => l.values_.id === 'hatcheries');
	return hatcheryLayer;
};

const reprojectCoordinates = (geojson: HatcheryGeoJson) => {
	geojson.features.forEach((f: HatcheryFeature) => {
		const coordinates: number[] = f.geometry.coordinates;
		const reprojCoords: number[] = fromLonLat(coordinates);
		f.geometry.coordinates = reprojCoords;
	});
};
