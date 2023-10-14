import { useEffect, useRef } from 'react';
import * as d3 from 'd3';

const AreaGraph = (graphData) => {
	useEffect(() => {
		console.log(graphData);
		if (graphData === undefined) return;
		if (graphData === undefined || Object.keys(graphData).length === 0) return;
		const margin = { top: 20, right: 40, bottom: 20, left: 20 },
			width = 440 - margin.left - margin.right,
			height = 175 - margin.bottom - margin.top;

		const svg = d3
			.select('#density-plot')
			.attr('width', width + margin.left + margin.right)
			.attr('height', height + margin.top + margin.bottom);

		svg.selectAll('*').remove();

		const x = d3.scaleLinear().domain([0, 365]).range([0, width]);
		const xAxisGenerator = d3.axisBottom(x);
		const tickLabels = [
			'Jan',
			'Feb',
			'Mar',
			'Apr',
			'May',
			'Jun',
			'Jul',
			'Aug',
			'Sep',
			'Oct',
			'Nov',
			'Dec',
		];
		xAxisGenerator.tickValues([
			0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334,
		]);

		xAxisGenerator.tickFormat((d, i) => tickLabels[i]);
		// xAxisGenerator.tickSize(-height);

		// Add bottom x axis to graph
		svg
			.append('g')
			.attr('transform', `translate(${margin.left}, ${height})`)
			.call(xAxisGenerator)
			.select('.domain');
		// .remove();

		// // Create Y axis
		//   // Create a Y scale for densities
		const countArr = graphData.day_counts.map((d) => d.count);
		const maxY = Math.max(...countArr);
		const y = d3.scaleLinear().domain([0, maxY]).range([height, 0]);

		// Add right y axis to graph
		// svg
		// 	.append('g')
		// 	.attr('transform', `translate(${width + margin.left}, 0)`)
		// 	.call(d3.axisRight(y));

		svg
			.append('path')
			.datum(graphData.day_counts)
			.attr('transform', `translate(${margin.left}, 0)`)
			.attr('stroke', '#0044ba')
			.attr('stroke-width', 1)
			.attr('fill', '#94bbff')
			.attr('stroke-linejoin', 'round')
			.attr(
				'd',
				d3
					.area()
					.curve(d3.curveBasis)
					.x((d) => x(d.day))
					.y1((d) => y(d.count))
					.y0(y(0))
			);
	}, [graphData]);
	return <svg id='density-plot' />;
};

export default AreaGraph;
