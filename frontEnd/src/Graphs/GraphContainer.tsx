import { useEffect, useState } from 'react';
import { Card, Skeleton } from '@mui/material';
import { AreaGraphData, BarGraphData, RecentEscapementData } from '../types';
import AreaGraph from './AreaGraph';
import BarGraph from './BarGraph';
import RecentEscapement from './RecentEscapement';
import { useAppSelector } from '../redux/hooks';
import './Graphs.css';
import { auto } from '@observablehq/plot';

type UniqueRun = {
	[key: string]: string;
};

type populationSpecificGraphData = {
	areaGraph: AreaGraphData;
	barGraph: BarGraphData;
	recentEscapement: RecentEscapementData;
};

type SelectedPopulation = {
	specie: string;
	run: string;
};

const GraphContainer = (selectedPopulation: SelectedPopulation) => {
	const uniqueRuns: UniqueRun[] = useAppSelector(
		(state) => state.hatchery.uniqueRuns
	)!;
	const hatcheryData: any = useAppSelector(
		(state) => state.hatchery.hatcheryData
	);

	const [graphData, setGraphData] = useState<
		undefined | populationSpecificGraphData
	>();

	useEffect(() => {
		if (!selectedPopulation.run || !selectedPopulation.specie) return;
		const specie = selectedPopulation.specie;
		const runOrigin = selectedPopulation.run.split(' ');
		const origin = runOrigin.pop() as string;
		const run = runOrigin.join(' ');
		console.log({ specie }, { run }, { origin });
		console.log(hatcheryData.historical_daily_average_counts);
		const areaGraph = hatcheryData.historical_daily_average_counts.find(
			(d: AreaGraphData) => filterUniqueRun(specie, run, origin, d)
		);
		const barGraph = hatcheryData.historical_yearly_counts.find(
			(d: BarGraphData) => filterUniqueRun(specie, run, origin, d)
		);
		const recentEscapement = hatcheryData.recent_daily_escapement_counts.find(
			(d: RecentEscapementData) => filterUniqueRun(specie, run, origin, d)
		);
		setGraphData({ areaGraph, barGraph, recentEscapement });
	}, [selectedPopulation.run, selectedPopulation.specie]);

	return (
		<div className='graph-container'>
			<Card className='graph-card'>
				<h3>Average Run Timing Distribution</h3>

				{graphData !== undefined ? (
					<AreaGraph {...graphData.areaGraph} />
				) : (
					<div>Loading...</div>
				)}
			</Card>
			<Card className='graph-card'>
				<h3>Yearly Escapement Total</h3>

				{graphData !== undefined ? (
					<BarGraph {...graphData.barGraph} />
				) : (
					<div>Loading...</div>
				)}
			</Card>
			<Card className='graph-card'>
				<h3>Past 2 Week Escapement</h3>

				{graphData !== undefined ? (
					graphData.recentEscapement ? (
						<RecentEscapement {...graphData.recentEscapement} />
					) : (
						<div>No Data</div>
					)
				) : (
					<div>Loading...</div>
				)}
			</Card>
		</div>
	);
};

export default GraphContainer;

const createRadioValues = (
	uniqueRuns: UniqueRun[],
	species: string[],
	tabValue: number
): string[] => {
	return uniqueRuns
		.filter((r: UniqueRun) => Object.keys(r)[0] === species[tabValue])
		.map((r: UniqueRun) => Object.values(r)[0]);
};

const filterUniqueRun = (
	specie: string,
	run: string,
	origin: string,
	data: AreaGraphData | BarGraphData | RecentEscapementData
): boolean => {
	return (
		data.species.toLowerCase() === specie.toLowerCase() &&
		data.run.toLowerCase() === run.toLowerCase() &&
		data.origin.toLowerCase() === origin.toLowerCase()
	);
};
