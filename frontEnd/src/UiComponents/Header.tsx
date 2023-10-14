import React, { useState, useRef, useEffect } from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import { InputBase } from '@mui/material';

type Filter = {
	textFilter: string | undefined;
	inSeason: boolean;
	recentEscapement: boolean;
};

const Header = () => {
	const [searchFilter, setSearchFilter] = useState<Filter>({
		textFilter: undefined,
		inSeason: false,
		recentEscapement: false,
	});

	const handleSearchChange = (e: any) => {
		setSearchFilter({ ...searchFilter, textFilter: e.target.value });
	};
	return (
		<Box sx={{ flexGrow: 1, zIndex: 200 }}>
			<AppBar position='static' sx={{}}>
				<Toolbar>
					<Typography variant='h6' component='div' sx={{ flexGrow: 1 }}>
						Salmon Finder
					</Typography>
					<Box sx={{ flexGrow: 15 }}>
						<div className='search-bar-wrapper'>
							<div className='search-box'>
								<InputBase
									className='search-input'
									placeholder='Search Hatcheries'
									onChange={handleSearchChange}
								></InputBase>
							</div>
						</div>
					</Box>

					<Button color='inherit'>About</Button>
				</Toolbar>
			</AppBar>
		</Box>
	);
};

export default Header;
