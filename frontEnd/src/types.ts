export type BarGraphData = {
	species: string;
	run: string;
	origin: string;
	year_counts: YearCount[];
};

export type YearCount = {
	year: number;
	count: number;
};

export type RecentEscapementData = {
	species: string;
	run: string;
	origin: string;
	day_counts: DayCount[];
};

export type DayCount = {
	day: string;
	count: number;
};

export type AreaGraphData = {
	species: string;
	run: string;
	origin: string;
	day_counts: DensityData[];
};

export type DensityData = {
	day: number;
	count: number;
};

export type ApiHatcheryDataResponse = {
	bargraph: BarGraphData;
	density_estimation: AreaGraphData;
	recent_escapement: RecentEscapementData | [];
};

export type HatcheryFeature = {
	type: string;
	properties: HatcheryFeatureProperties;
	geometry: Geometry;
};

export type HatcheryFeatureProperties = {
	'Facility Name': string;
	Facility: string;
	WRIA: string;
	river_guage: string;
};

export type Geometry = {
	type: 'Point';
	coordinates: number[];
};

export type HatcheryGeoJson = {
	type: 'FeatureCollection';
	features: HatcheryFeature[];
};

export type site = HatcheryGeoJson;
export type hatchery = ApiHatcheryDataResponse;
