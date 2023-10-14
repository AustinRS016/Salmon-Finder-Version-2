import {
	createAsyncThunk,
	createSlice,
	current,
	PayloadAction,
} from '@reduxjs/toolkit';
import { HatcheryFeature, HatcheryFeatureProperties } from '../types';
import { RootState } from './store';
import { getHatchery } from '../Map/utils';

type UniqueRun = {
	[key: string]: string;
};

type SelectedHatchery = {
	hatcheries: any;
	hatchery: HatcheryFeatureProperties | undefined;
	hatcheryData: any | undefined;
	uniqueRuns: UniqueRun[] | undefined;
};

type SetHatcheryPayload = {
	hatcheryData: any;
	uniqueRuns: UniqueRun[];
};

export const setHatcheryFromMap = createAsyncThunk(
	'hatcherySelection/getFromMapClick',
	async (features: any) => {
		await features;
		return features;
	}
);

export const fetchHatcheryData = createAsyncThunk(
	'hatchery/fetchHatchery',
	async (facility: string) => {
		const res = await getHatchery(facility);
		return res;
	}
);

const initialState: SelectedHatchery = {
	hatcheries: undefined,
	hatchery: undefined,
	hatcheryData: undefined,
	uniqueRuns: undefined,
};

export const hatcherySlice = createSlice({
	name: 'hatcherySelection',
	initialState,
	reducers: {
		setHatcheries: (state, action: PayloadAction<HatcheryFeature[]>) => {
			state.hatcheries = action.payload;
		},
		setSelectedHatchery: (
			state,
			action: PayloadAction<HatcheryFeatureProperties>
		) => {
			state.hatchery = action.payload;
		},
		setHatcheryData: (state, action: PayloadAction<SetHatcheryPayload>) => {
			state.hatcheryData = action.payload.hatcheryData;
			state.uniqueRuns = action.payload.uniqueRuns;
		},
		unSelectHatchery: (state) => {
			state.hatchery = undefined;
			state.hatcheryData = undefined;
			state.uniqueRuns = undefined;
		},
	},
	extraReducers: (builder) => {
		builder.addCase(setHatcheryFromMap.fulfilled, (state, action) => {
			state.hatchery = action.payload;
		});
		builder.addCase(fetchHatcheryData.fulfilled, (state, action) => {
			console.log(action.payload);
			const hatchery = action.payload;
			const uniqueRuns = hatchery.historical_yearly_counts.map((h: any) => {
				const uniqueRun = { [h.species]: `${h.run} ${h.origin}` };
				return uniqueRun;
			});
			state.hatcheryData = hatchery;
			state.uniqueRuns = uniqueRuns;
		});
	},
});

export const {
	setHatcheries,
	setSelectedHatchery,
	setHatcheryData,
	unSelectHatchery,
} = hatcherySlice.actions;
export const selectHatchery = (state: RootState) => state.hatchery.hatchery;
export const selectHatcheryData = (state: RootState) =>
	state.hatchery.hatcheryData;
export const selectUniqueRuns = (state: RootState) => state.hatchery.uniqueRuns;
export const selectHatcheries = (state: RootState) => state.hatchery.hatcheries;

export default hatcherySlice.reducer;
