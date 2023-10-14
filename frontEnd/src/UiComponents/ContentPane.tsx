import { useState, useEffect } from 'react';
import { HatcheryFeature, HatcheryFeatureProperties } from '../types';
import ContentCard from './ContentCard';
import './Content.css';
import HatcheryContent from './HatcheryContent';
import { selectHatcheries, selectHatchery } from '../redux/hatcherySlice';
import { useAppSelector } from '../redux/hooks';
type resizeState = { active: boolean; startingPoint: undefined | number };

type Filter = {
	textFilter: string | undefined;
	inSeason: boolean;
	recentEscapement: boolean;
};

interface ContentProps {
	hatcheryFeatures: HatcheryFeature[] | undefined;
}

const ContentPane = () => {
	const selectedHatchery = useAppSelector(selectHatchery);
	const hatcheryFeatures = useAppSelector(selectHatcheries);

	const [divSize, setDivSize] = useState(500);
	const [resize, setResize] = useState<resizeState>({
		active: false,
		startingPoint: undefined,
	});

	useEffect(() => {
		const removeMouseListener = () => {
			if (resize.active === true) {
				resize.active = false;
				resize.startingPoint = undefined;
			}
		};
		const resizeDiv = (e: any) => {
			if (resize.active === true && resize.startingPoint !== undefined) {
				const moveDiv = resize.startingPoint - e.clientX;
				const newWidth = divSize + moveDiv;
				setDivSize(newWidth);
			}
		};
		document.body.addEventListener('mouseup', removeMouseListener);
		document.body.addEventListener('mousemove', resizeDiv);
		return () => {
			document.body.removeEventListener('onmouseup', removeMouseListener);
			document.body.removeEventListener('mousemove', resizeDiv);
		};
	}, [resize]);

	return (
		<div className='content-pane' style={{ width: `${divSize}px` }}>
			<button
				className='resize-button'
				onMouseDown={(e) => {
					setResize({ active: true, startingPoint: e.clientX });
				}}
			/>
			<div className='content'>
				<div className='feature-wrapper'>
					{/* This controls what displays on the content pane */}
					{selectedHatchery !== undefined ? (
						//
						// Display content for a hatchery
						<HatcheryContent />
					) : hatcheryFeatures ? (
						//
						// Display each hatchery
						<div className='features'>
							{hatcheryFeatures?.map((h: HatcheryFeature) => {
								return <ContentCard {...h} />;
							})}
						</div>
					) : (
						//
						// Content is loading
						<div>Make skellies</div>
					)}
					{/* Possible other content we would add ? */}
				</div>
			</div>
		</div>
	);
};

export default ContentPane;

const filterHatcheries = (
	h: HatcheryFeature,
	searchFilter: Filter
): boolean => {
	const { textFilter, recentEscapement, inSeason } = searchFilter;
	if (textFilter === undefined && !recentEscapement && !inSeason) {
		return true;
	}
	let pass = false;
	const testValues = Object.values(h.properties);
	testValues.forEach((v) => {
		if (
			typeof textFilter === 'string' &&
			v.toLowerCase().includes(textFilter.toLowerCase())
		) {
			pass = true;
		}
	});
	return pass;
};
