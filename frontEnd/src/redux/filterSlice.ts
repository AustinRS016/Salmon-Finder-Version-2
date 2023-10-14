import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { RootState } from './store';

type Filter = {
	textFilter: string | undefined;
	inSeason: boolean;
	recentEscapement: boolean;
};

const initialState: Filter = {
	textFilter: undefined,
	inSeason: false,
	recentEscapement: false,
};

export const filterSlice = createSlice({
	name: 'filter',
	initialState,
	reducers: {
		setTextFilter: (state, action: PayloadAction<string>) => {
			state.textFilter = action.payload;
		},
		toggleInSeason: (state) => {
			const prevValue = state.inSeason;
			state.inSeason = !prevValue;
		},
		toggleRecentEscapement: (state) => {
			const prevValue = state.recentEscapement;
			state.recentEscapement = !prevValue;
		},
	},
});

export const { setTextFilter, toggleInSeason, toggleRecentEscapement } =
	filterSlice.actions;
export const setFilter = (state: RootState) => state.filter;
export default filterSlice.reducer;
