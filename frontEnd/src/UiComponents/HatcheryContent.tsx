import { useEffect, useState } from 'react';
import GraphContainer from '../Graphs/GraphContainer';
import { HatcheryFeatureProperties } from '../types';
import {
	selectHatchery,
	selectUniqueRuns,
	unSelectHatchery,
} from '../redux/hatcherySlice';
import { useAppSelector, useAppDispatch } from '../redux/hooks';
import { Box, FormControl, InputLabel, MenuItem, Select } from '@mui/material';
import { IoArrowBack } from 'react-icons/io5';
import './Content.css';

type UniqueRun = {
	[key: string]: string;
};

type SelectedPopulation = {
	specie: string;
	run: string;
};

const HatcheryContent = () => {
	const hatchery = useAppSelector(selectHatchery);
	const uniqueRuns = useAppSelector(selectUniqueRuns);
	const dispatch = useAppDispatch();

	const [species, setSpecies] = useState<string[] | undefined>(['']);
	const [runs, setRuns] = useState<string[] | undefined>(['']);
	const [selectedPopulation, setSelectedPopulation] =
		useState<SelectedPopulation>({ specie: '', run: '' });

	const handleUnselectHatchery = () => {
		dispatch(unSelectHatchery());
	};

	const handleSpecieChange = (e: any, newValue: any) => {
		const newSpecie = newValue.props.value;
		const newRuns = createRuns(uniqueRuns!, newSpecie);
		setRuns(newRuns);
		setSelectedPopulation({ specie: newSpecie, run: newRuns[0] });
	};

	const handleRunChange = (e: any, newValue: any) => {
		setSelectedPopulation({ ...selectedPopulation, run: newValue.props.value });
	};

	useEffect(() => {
		if (uniqueRuns === undefined) return;
		const species: string[] = [];
		uniqueRuns.forEach((r: UniqueRun) => {
			const specie = Object.keys(r)[0];
			if (!species.includes(specie)) {
				species.push(specie);
			}
		});
		setSpecies(species);
		setSelectedPopulation({ run: '', specie: species[0] });
		return () => {
			setSelectedPopulation({ specie: '', run: '' });
		};
	}, [uniqueRuns]);

	if (
		uniqueRuns !== undefined &&
		selectedPopulation.specie !== '' &&
		selectedPopulation.run === ''
	) {
		const runs = createRuns(uniqueRuns, selectedPopulation.specie);
		setRuns(runs);
		setSelectedPopulation({ ...selectedPopulation, run: runs[0] });
	}
	return hatchery !== undefined ? (
		<div className='selected-hatchery'>
			<IoArrowBack onClick={handleUnselectHatchery} className='back-button' />
			<div className='selected-hatchery-title'>{hatchery['Facility Name']}</div>
			<br />
			<div className='fish-dropdowns'>
				{/* Drop down for species selection */}
				<div className='fish-dropdown'>
					<FormControl
						disabled={selectedPopulation.specie === ''}
						sx={{ maxWidth: 200, minWidth: 80 }}
					>
						<InputLabel>Species</InputLabel>
						<Select
							value={selectedPopulation.specie}
							onChange={handleSpecieChange}
							label='Species'
						>
							{species
								? species.map((s) => {
										return <MenuItem value={s}>{s}</MenuItem>;
								  })
								: null}
						</Select>
					</FormControl>
				</div>
				{/* Drop down for run selection */}
				<div className='fish-dropdown'>
					<FormControl
						disabled={selectedPopulation.run === ''}
						sx={{ maxWidth: 200, minWidth: 80 }}
					>
						<InputLabel>Run</InputLabel>
						<Select
							value={selectedPopulation.run}
							onChange={handleRunChange}
							label='Run'
						>
							{runs
								? runs.map((r) => {
										return <MenuItem value={r}>{r}</MenuItem>;
								  })
								: null}
						</Select>
					</FormControl>
				</div>
			</div>
			<GraphContainer {...selectedPopulation} />
		</div>
	) : null;
};

export default HatcheryContent;

const createRuns = (uniqueRuns: UniqueRun[], specie: string): string[] => {
	return uniqueRuns
		.filter((r: UniqueRun) => Object.keys(r)[0] === specie)
		.map((r: UniqueRun) => Object.values(r)[0]);
};
