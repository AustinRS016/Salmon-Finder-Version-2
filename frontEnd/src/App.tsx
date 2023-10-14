import './App.css';
import GraphContainer from './Graphs/GraphContainer';
import HatcheryMap from './Map/Map';
import Header from './UiComponents/Header';

function App() {
	return (
		<div className='App'>
			<header className='App-header'></header>
			{/* <GraphContainer /> */}
			<Header />
			<HatcheryMap />
		</div>
	);
}

export default App;
