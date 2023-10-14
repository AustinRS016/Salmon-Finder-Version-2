import { useEffect, useState, useRef } from 'react';
import * as d3 from 'd3';

const RecentEscapement = (graphData) => {
	useEffect(() => {
		console.log(graphData);

		if (graphData === undefined || Object.keys(graphData).length === 0) return;
		const data = [
			...graphData.date_counts.map((d) => {
				const date = new Date(d.date).toDateString().slice(0, -5);
				const date_count_obj = { ...d };
				date_count_obj.date = date;
				return date_count_obj;
			}),
		];

		const margin = { top: 50, right: 20, bottom: 10, left: 50 },
			width = 415 - margin.left - margin.right,
			height = 175 - margin.bottom - margin.top;
		const paddingTop = 30;

		// Initiate graph
		const svg = d3
			.select('#escapement-graph')
			.attr('width', width + margin.left + margin.right)
			.attr('height', height + margin.top + margin.bottom + paddingTop);

		// Remove previous bar graph
		svg.selectAll('*').remove();

		// Create X axis
		const x = d3
			.scaleBand()
			.range([margin.left, width + margin.left])
			.domain(data.map((d) => d.date));

		// Add x axis
		svg
			.append('g')
			//Add 5 to move 5px to right
			.attr('transform', `translate(0, ${height + margin.bottom})`)
			.call(d3.axisBottom(x).tickSizeOuter([0]))
			.style('font-size', '12px')
			.selectAll('text')
			.style('text-anchor', 'end')
			// Move and rotate ticks
			.attr('transform', 'translate(-10,2), rotate(-56)');

		// Create y axis
		const y = d3
			.scaleLinear()
			.range([height, 0])
			.domain([0, Math.max(...data.map((y) => y.count))]);

		// Add y axis
		svg
			.append('g')
			.attr('transform', `translate(${margin.left}, ${margin.bottom})`)
			.call(d3.axisLeft(y).tickSizeOuter([0]))
			.style('font-size', '12px');

		svg
			.append('g')
			.attr('fill', '#94bbff')
			.selectAll()
			.data(data)
			.join('rect')
			.attr('x', (d) => x(d.date) - 1)
			.attr('y', (d) => y(d.count) + margin.bottom)
			.attr('height', (d) => y(0) - y(d.count))
			.attr('width', x.bandwidth() - 1)
			.attr('stroke', '#0044ba')
			.attr('stroke-width', 1);
	}, [graphData]);

	return <svg id='escapement-graph' height={300} width={415}></svg>;
};

export default RecentEscapement;
