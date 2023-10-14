import React from 'react';
import { HatcheryFeature } from '../types';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import { getHatchery } from '../Map/utils';
import { setHatcheryData, setSelectedHatchery } from '../redux/hatcherySlice';
import { useAppDispatch } from '../redux/hooks';

const ContentCard = (hatcheryFeature: HatcheryFeature) => {
	const dispatch = useAppDispatch();

	const handleHatcheryClick = async (e: any) => {
		// Dispatch hatchery name first to open hatchery content
		dispatch(setSelectedHatchery(hatcheryFeature.properties));
		const hatchery = await getHatchery(hatcheryFeature.properties.Facility);
		const uniqueRuns = hatchery.historical_yearly_counts.map((h: any) => {
			const uniqueRun = { [h.species]: `${h.run} ${h.origin}` };
			return uniqueRun;
		});
		dispatch(
			setHatcheryData({
				hatcheryData: hatchery,
				uniqueRuns,
			})
		);
	};

	return (
		<Card className='content-card'>
			<CardContent>
				<div onClick={handleHatcheryClick} className='hatchery-title'>
					{parseName(hatcheryFeature.properties['Facility Name'])}
				</div>
			</CardContent>
		</Card>
	);
};

export default ContentCard;

const parseName = (name: string): string => {
	let newString = '';
	const words = name.split(' ');
	words.forEach((w) => {
		const newWord = w.charAt(0).toUpperCase() + w.slice(1).toLowerCase();
		newString = newString + ' ' + newWord;
	});
	return newString;
};
